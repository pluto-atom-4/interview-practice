# SKILL: Add Comprehensive Header Note to Python Scripts for Interview Preparation

## Overview
This skill provides a systematic approach to adding professional, interview-ready header notes to Python implementation files. The header serves as both documentation and a quick reference guide for technical interviews.

## Purpose
Transform a Python script into an interview-preparation asset by adding a structured header that:
- Clearly articulates the problem and solution approach
- Explains design decisions and key concepts
- Provides multiple explanation formats (technical, pitch, rapid-fire)
- Serves as a confidence booster and communication aid during interviews

---

## Header Structure Template

Use this standardized structure for all Python interview preparation files:

```python
"""
## Problem Statement

[1-2 sentence problem description with goal and context]

## Whiteboard Coding Challenge Notes

* For this problem, I'm using [approach/algorithm name]:

[Brief overview of why this approach is suitable]

* Key Concepts:

  - [Concept 1: Why/How?]
[Detailed explanation with implementation considerations]

  - [Concept 2: Why/How?]
[Detailed explanation with implementation considerations]

* Logic:

1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]
[Continue as needed]

* **30-Second Pitch**:

[Concise explanation suitable for quick verbal communication]

* **Rapid-Fire Version**:

- [Key point 1]
- [Key point 2]
- [Key point 3]

* **Ultra-Minimal One-Liner**:

- [Single sentence capturing the essence]

* **Complexity Analysis**:

- **Time Complexity:** [Expression with explanation]
- **Space Complexity:** [Expression with explanation]

* **Use Cases**:

[Where/when this solution is applicable]
"""

# Implementation code follows...
```

---

## Step-by-Step Implementation Guide

### 1. Problem Statement Section
**What to include:**
- Clear problem objective (1-2 sentences)
- Key constraint or goal (space, time, specific requirement)
- Context (why this matters in interviews)

**Example:**
```
Merge two sorted arrays in place without using extra space. 
The goal is to achieve this efficiently by minimizing comparisons and swaps. 
This tests understanding of in-place algorithms and optimization techniques.
```

### 2. Key Concepts Section
**What to include:**
- 2-3 critical design decisions
- For each: explain WHY (motivation) and HOW (implementation)
- Include code snippets if they clarify the concept

**Template for each concept:**
```
- [What is this concept?]
[Why is it important? What problem does it solve?]
[How is it implemented? Any trade-offs?]
```

**Example:**
```
- Why initialize gap as `n + m` and reduce using `(gap + 1) // 2`?
The GAP method initialization to combined length ensures far-apart elements 
are compared first, resolving large inversions early. The reduction formula 
`(gap + 1) // 2` ensures controlled gap decrease, eventually reaching 1 for 
full sort completion.
```

### 3. Logic Section
**What to include:**
- Numbered steps of the algorithm
- High-level description (not pseudo-code, not line-by-line)
- Flow and decision points

**Format:**
```
1. [Initialize variables with purpose]
2. [Define helper functions/structures with purpose]
3. [Main loop: what condition? what operations?]
4. [Termination: when and why does it stop?]
```

### 4. Interview Talking Points
**Create three formats:**

**30-Second Pitch:** 
- Natural speech pattern
- Suitable for verbal explanation
- Includes key algorithm name and main benefit

**Rapid-Fire Version**:
- Bullet points
- Key techniques and trade-offs
- "What would you say if interrupted?"

**Ultra-Minimal One-Liner:**
- Single sentence
- Captures essence for quick reference
- Includes algorithm name + complexity

---

## Key Concepts to Explain

For most interview problems, address these design decisions:

| Question | Why Explain | How to Address |
|----------|------------|-----------------|
| Why this algorithm? | Shows problem understanding | Justify vs alternatives |
| Why these data structures? | Tests design knowledge | Explain space/time trade-offs |
| Why this initialization? | Shows attention to edge cases | Explain boundary conditions |
| Why these helper functions? | Shows code quality thinking | Explain abstraction benefits |
| Why this formula/formula? | Shows mathematical reasoning | Explain derivation or inspiration |

---

## Common Pitfalls to Avoid

❌ **Too brief:** "Use gap reduction" → ✅ "Initialize gap to n+m for early inversion resolution, reduce via (gap+1)//2 for controlled decrease"

❌ **Implementation details:** Focus on WHY, not line-by-line HOW → ✅ Explain the concept, not every line of code

❌ **No complexity analysis:** Always include time and space → ✅ Provide both with clear explanation

❌ **Single explanation:** Redundant for interviews → ✅ Provide 3 formats (pitch, rapid-fire, one-liner)

❌ **Missing context:** Assumes interviewer knows the problem → ✅ Always include Problem Statement section

---

## Quality Checklist

Before finalizing a header note, verify:

- [ ] **Problem Statement** is clear and interview-contextualized
- [ ] **Key Concepts** explain WHY (motivation) not just HOW (implementation)
- [ ] **Logic** section describes algorithm flow at high level
- [ ] **30-Second Pitch** is natural and conversational
- [ ] **Rapid-Fire Version** uses clear bullet points
- [ ] **Ultra-Minimal One-Liner** captures essence in one sentence
- [ ] **Complexity Analysis** includes both time and space with explanation
- [ ] **Use Cases** section contextualizes real-world applicability
- [ ] No code implementation details in header (implementation follows below)
- [ ] Consistent formatting and markdown structure

---

## Integration with Solution Files

### File Organization
```
.claude/skills/interview-preparation/
├── SKILL.md                    (This file - template and guide)
├── README.md                   (Index of all skills)
└── [solution-name].md          (Individual solution guide)
```

### Python Script Format
```python
"""
[Comprehensive header from this skill]
"""

def solution_function(params):
    """Implementation with docstring."""
    # Code implementation
    pass

def helper_function():
    """Helper with docstring."""
    pass
```

---

## Usage in Claude Code Agent

### Reference in prompts:
```
@merge-sorted-arrays Add a comprehensive header note following @SKILL for interview preparation
```

### Skill tagging:
- `#interview` `#algorithm` `#header-note`
- `#[language]` (e.g., `#python`)
- `#[topic]` (e.g., `#array`, `#gap-method`)

---

## Real-World Application Examples

This skill applies to any interview coding problem:

### Covered Problem Types
- ✅ Array/String manipulation
- ✅ Graph/Tree traversal
- ✅ Dynamic programming
- ✅ Sorting/Searching
- ✅ Design patterns
- ✅ System design components
- ✅ Optimization problems

### Adaptable Sections
- Algorithm name changes
- Concept count varies (typically 2-3 key ones)
- Complexity analysis remains consistent
- Interview talking points universal

---

## Tags
`#interview-prep` `#documentation` `#header-note` `#skill` `#interview-coaching` `#algorithm-explanation` `#code-documentation`
