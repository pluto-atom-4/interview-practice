"""
- Replace "your-subscription-id", "your-resource-group", and "your-workspace-name" with your actual Azure details.
- Ensure all components are registered in Azure ML.
- You can switch train_model to use BERT or LambdaMART depending on your component logic.
- Uncomment the schedule section to enable automated retraining.
"""

from azure.ai.ml import Input, MLClient, Output
from azure.ai.ml.dsl import pipeline
from azure.ai.ml.entities import JobSchedule, PipelineJob
from azure.identity import DefaultAzureCredential

# Connect to Azure ML workspace
ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="your-subscription-id",
    resource_group_name="your-resource-group",
    workspace_name="your-workspace-name"
)

# Load registered components
preprocess = ml_client.components.get(name="preprocess_component", version="latest")
feature_engineering = ml_client.components.get(name="feature_engineering_component", version="latest")
train_model = ml_client.components.get(name="train_ranking_model", version="latest")
evaluate_model = ml_client.components.get(name="evaluate_model_component", version="latest")
register_model = ml_client.components.get(name="register_model_component", version="latest")

# Define pipeline
@pipeline(default_compute="cpu-cluster")
def search_ranking_pipeline():
    step1 = preprocess(raw_data=Input(type="uri_file", path="azureml:search_logs_dataset@latest"))
    step2 = feature_engineering(processed_data=step1.outputs.processed_data)
    step3 = train_model(features=step2.outputs.features)
    step4 = evaluate_model(model=step3.outputs.model_output, test_data=Input(type="uri_file", path="azureml:test_dataset@latest"))
    step5 = register_model(model=step3.outputs.model_output, evaluation=step4.outputs.evaluation_report)

    return {
        "model_output": step3.outputs.model_output,
        "evaluation_report": step4.outputs.evaluation_report
    }

# Submit pipeline job
pipeline_job = search_ranking_pipeline()
pipeline_job = ml_client.jobs.create_or_update(pipeline_job)
print(f"Pipeline job submitted. ID: {pipeline_job.name}")

# Optionally schedule retraining
# schedule = JobSchedule(
#     name="search-ranking-retrain-schedule",
#     trigger={"type": "cron", "expression": "0 0 * * 0"},  # Weekly retraining
#     create_job=pipeline_job
# )
# ml_client.schedules.begin_create_or_update(schedule)
