## Data Pipeline for Manufacturing Log Monitoring using AWS S3 and Lambda

## Table of Contents

- [Problem Statement](#problem-statement)
- [Multi-Stage Architectural Design](#1-multi-stage-architectural-design)
- [Standardized Message Model](#2-standardized-message-model)
- [Logic Implementation](#3-logic-implementation-python-313)
- [CI/CD Pipeline & Monitoring Integration](#4-cicd-pipeline--monitoring-integration)

### Problem Statement:

#### Objective
Design a **scalable, event-driven data pipeline** for real-time manufacturing log monitoring and automated incident response using AWS cloud services.

#### Business Requirements
Manufacturing facilities generate continuous streams of logs containing production status updates, performance metrics, and error alerts. The system must:

- **Ingest & Parse**: Capture manufacturing logs from multiple production lines and standardize them into a common message format
- **Route & Evaluate**: Intelligently route standardized messages to specialized handlers based on content attributes (status, errors, metrics)
- **Process & Act**: Execute domain-specific logic independently for:
  - Database updates (production status tracking)
  - Alert notifications (error/warning handling)
  - Analytics & metrics aggregation
- **Scale & Observe**: Support real-time processing across multiple production lines with full traceability and monitoring

#### Architecture Approach
This solution integrates **Amazon S3** (for durable log storage) with **AWS Lambda** (for serverless event processing) and **EventBridge** (for intelligent message routing) to create a decoupled, scalable architecture where logs are automatically processed as they arrive, enabling real-time operational insights and incident response.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MANUFACTURING LOG PIPELINE                          │
└─────────────────────────────────────────────────────────────────────────────┘

    Production Lines (Multi-Source)
              │
              ▼
    ┌─────────────────┐
    │   Amazon S3     │  ◄── Ingest & Store Manufacturing Logs
    │  (Log Bucket)   │
    └────────┬────────┘
             │
             │ S3:ObjectCreated Event
             ▼
    ┌─────────────────────────────────────┐
    │  Lambda: Parser & Dispatcher        │  ◄── Stage 1: Parse & Standardize
    │  (S3 Trigger)                       │
    └────────┬────────────────────────────┘
             │
             │ Standardized Message (JSON)
             ▼
    ┌─────────────────────────────────────┐
    │  Amazon EventBridge                 │  ◄── Stage 2: Intelligent Router
    │  (Event Bus with Rules)             │
    └────┬──────────┬──────────┬──────────┘
         │          │          │
         │ Routes   │ Routes   │ Routes
         ▼          ▼          ▼
    ┌─────────┐ ┌─────────┐ ┌─────────────┐
    │ Lambda  │ │ Lambda  │ │ Lambda      │
    │ Status  │ │ Alert   │ │ Analytics   │
    │Handler  │ │Handler  │ │ Handler     │
    └────┬────┘ └────┬────┘ └────┬────────┘
         │           │           │
         │ Updates   │ Notifies  │ Aggregates
         ▼           ▼           ▼
    ┌─────────┐ ┌─────────┐ ┌──────────────┐
    │DynamoDB │ │ SNS     │ │CloudWatch    │
    │(Status) │ │(Alerts) │ │(Metrics)     │
    └─────────┘ └─────────┘ └──────────────┘

    ▲
    │ AWS X-Ray Tracing (End-to-End Observability)
    │
```

### 1. Multi-Stage Architectural Design

1. Stage 1: Ingest & Parse: Lambda A extracts S3 data and publishes a "Standardized Message" to an Event Bus.
2. Stage 2: Router/Evaluator: EventBridge rules evaluate the message attributes (Status, Error, Metric) and route them to specific handlers.
3. Stage 3-5: Specialized Workers:
   * Status Worker: Updates the production database (e.g., DynamoDB).
   * Alert Worker: Processes errors/warnings and sends notifications.
   * Analytics Worker: Calculates team contributions and sends metrics to monitoring tools like AWS CloudWatch or Datadog.

### 2. Standardized Message Model

The Parser transforms raw logs into a structured JSON message used by all downstream stages:

```json
{
  "metadata": { "line_id": "L-01", "timestamp": "2026-01-13T12:00:00Z", "log_type": "PRODUCTION_UPDATE" },
  "payload": {
    "status": "OPERATIONAL",
    "output_count": 150,
    "team_id": "ALPHA-SHIFT",
    "warnings": ["TEMP_HIGH_THRESHOLD"],
    "errors": []
  }
}

```

### 3. Logic Implementation (Python 3.13)

#### Stage 1: The Parser & Dispatcher

This function acts as the entry point from S3.


#### Stage 2-5: The Specialized Handlers (Logic Examples)

These functions are triggered independently by the Event Bus based on the message content.

##### **Stage 2: EventBridge Rules & Routing Configuration**

EventBridge is the intelligent router that evaluates standardized messages and directs them to appropriate handlers. Minimum configuration requires three EventBridge Rules:

**Rule 1: Status Handler Rule**
```json
{
  "Name": "route-to-status-handler",
  "EventBusName": "manufacturing-log-bus",
  "EventPattern": {
    "source": ["manufacturing.parser"],
    "detail-type": ["PRODUCTION_UPDATE"],
    "detail": {
      "status": ["OPERATIONAL", "MAINTENANCE", "SHUTDOWN"]
    }
  },
  "State": "ENABLED",
  "Targets": [
    {
      "Arn": "arn:aws:lambda:us-east-1:123456789012:function:status-handler",
      "Id": "status-handler-target"
    }
  ]
}
```

**Rule 2: Alert Handler Rule**
```json
{
  "Name": "route-to-alert-handler",
  "EventBusName": "manufacturing-log-bus",
  "EventPattern": {
    "source": ["manufacturing.parser"],
    "detail-type": ["PRODUCTION_UPDATE"],
    "detail": {
      "warnings": [{"exists": true}]
    }
  },
  "State": "ENABLED",
  "Targets": [
    {
      "Arn": "arn:aws:lambda:us-east-1:123456789012:function:alert-handler",
      "Id": "alert-handler-target"
    }
  ]
}
```

**Rule 3: Analytics Handler Rule**
```json
{
  "Name": "route-to-analytics-handler",
  "EventBusName": "manufacturing-log-bus",
  "EventPattern": {
    "source": ["manufacturing.parser"],
    "detail-type": ["PRODUCTION_UPDATE"],
    "detail": {
      "output_count": [{"numeric": [">", 0]}]
    }
  },
  "State": "ENABLED",
  "Targets": [
    {
      "Arn": "arn:aws:lambda:us-east-1:123456789012:function:analytics-handler",
      "Id": "analytics-handler-target"
    }
  ]
}
```

**Key Routing Concepts:**
- **Event Pattern Matching**: Each rule filters events based on JSON path expressions
- **Content-Based Routing**: Messages are routed to handlers based on payload attributes (status, warnings, metrics)
- **Multiple Target Support**: A single rule can invoke multiple handlers if needed
- **Dead-Letter Queue (DLQ)**: Configure DLQ targets to capture failed events for debugging

##### **Stage 3: Manufacturing Status & Metrics Handler**:

```python
import cloudwatch_metrics_lib # Hypothetical 2026 optimized lib

def status_handler(event, context):
      data = event['detail']
      # Update Manufacturing Status in DynamoDB
      update_db_status(data['line_id'], data['status'])

      # Send Metrics to Monitoring Tool
      cloudwatch.put_metric_data(
        MetricName='UnitsProduced',
        Value=data['contribution'],
        Dimensions=[{'Name': 'Team', 'Value': data['team_id']}]
      )
```

##### **Stage 4: Error & Warning Processor**:

```python
def error_handler(event, context):
    errors = event['detail']['alerts']
    if errors:
        for error in errors:
            # Logic for automated ticket creation or machine shutdown
            trigger_incident_response(error)
```


##### **Stage 5: Team Contribution Processor**:
```python
def contribution_handler(event, context):
    # Aggregate logic for shift performance
   calculate_shift_efficiency(event['detail']['team_id'], event['detail']['contribution'])
```

### 4. CI/CD Pipeline & Monitoring Integration
To manage these multiple stages in 2026:
- **Infrastructure as Code (IaC)**: Use the AWS Cloud Development Kit (CDK) to define the EventBridge rules and the five Lambda functions in a single "Stack."
- **Observability**: Integrate AWS X-Ray to trace the message as it moves from S3 → Parser → EventBridge → Specialized Workers. This allows you to visualize bottlenecks in the manufacturing data flow.
- **Automated Testing**: The pipeline should include "Contract Testing" to ensure that if the Parser (Stage 1) changes the message format, the Downstream Workers (Stages 3-5) are alerted before deployment.
