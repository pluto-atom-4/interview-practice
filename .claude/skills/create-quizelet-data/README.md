# Create Quizlet Data Skill - Usage Guide

## Usage in Claude Code Agent

### Invoking the Skill

You can invoke this skill in two ways within Claude Code:

1. **Using the Skill Command:**
   ```
   /create-quizelet-data
   ```
   Claude Code will prompt for the source material (mock quiz, problem list, or file path) to convert into Quizlet format.

2. **Direct Skill Invocation:**
   ```
   skill: "create-quizelet-data", args: "path/to/source/material.md"
   ```
   This directly specifies which source material to process into a Quizlet dataset.

### Workflow Integration

**Step 1: Prepare Source Material**
- Ensure your source material contains problem statements with solutions
- Include complexity analysis (time and space)
- Provide algorithm/technique explanation
- Include real-world examples or context

**Step 2: Invoke the Skill**
- Run `/create-quizelet-data` in Claude Code
- Provide the source file or material reference when prompted
- Alternatively, specify the file in the skill arguments
- Indicate quiz number and topic area

**Step 3: Review Generated Dataset**
- Claude Code will generate a CSV file formatted for Quizlet import
- The dataset includes three question types per problem:
  - Big O complexity questions
  - Technique/approach questions
  - Real-world example questions
- File is saved to `generated/media/quizlet/quiz[N]_[topic]_multiple_choice.csv`

**Step 4: Import to Quizlet**
- Download or copy the generated CSV file
- Visit Quizlet.com
- Use "Import" → "CSV" feature
- Upload the file and create your study set
- Customize study settings as needed (optional)

### Example Usage Scenario

When creating quiz material from mock interview questions:

```bash
# Source file: mocked-quizes.md (contains "Quiz 1 – Algorithms & Data Structures")
# Contains: 13 problems with solutions, complexity, and examples

claude-code /create-quizelet-data
# When prompted, specify: mocked-quizes.md or Quiz 1
# Topic: Algorithms & Data Structures

# Result:
# - CSV file generated with 39 questions (3 per problem)
# - File saved: generated/media/quizlet/quiz1_algorithms_multiple_choice.csv
# - Questions cover Big O, techniques, and examples
# - Ready to import into Quizlet
```

### Tips for Best Results

- **Complete Problem Statements:** Ensure each problem includes time/space complexity and technique used
- **Real-World Context:** Provide examples that relate to your interview target or domain
- **Multiple Choice Balance:** The skill generates plausible distractors; review for fairness
- **Source Organization:** Clearly label problems with quiz number and sequence
- **Review Complexity:** Verify all Big O answers match your solution approach
- **Iterate:** Re-run the skill if you modify source material or want different emphasis

---

## Usage in Copilot CLI

### Invoking the Skill

Copilot CLI provides several ways to invoke this skill:

1. **Using the Direct Skill Command:**
   ```bash
   copilot create-quizelet-data path/to/source/material.md
   ```
   Directly specifies the source material to convert.

2. **Interactive Mode:**
   ```bash
   copilot
   > create-quizelet-data
   ```
   Enters interactive skill mode where you provide the source file when prompted.

3. **With Extended Arguments:**
   ```bash
   copilot create-quizelet-data --file path/to/source.md --quiz-num 1 --topic algorithms
   ```
   Provides additional options for customization and organization.

### Workflow Integration

**Step 1: Navigate to Project**
```bash
cd /path/to/interview-practice
copilot
```

**Step 2: Invoke the Skill**
```bash
> create-quizelet-data mocked-quizes.md
```
Copilot will analyze the file and generate a Quizlet dataset.

**Step 3: Review Generated CSV**
- The CSV file is created in `generated/media/quizlet/`
- Check file naming: `quiz[N]_[topic]_multiple_choice.csv`
- Verify all problems are included (N problems × 3 questions each)

**Step 4: Export and Import to Quizlet**
```bash
# CSV is ready at: generated/media/quizlet/quiz1_algorithms_multiple_choice.csv
# Upload to Quizlet.com via their import interface
```

### Example Usage Scenario

```bash
$ cd interview-practice
$ copilot
Copilot CLI v2.0
> create-quizelet-data mocked-quizes.md
✓ Analyzing mocked-quizes.md
✓ Extracting "Quiz 1 – Algorithms & Data Structures" section
✓ Identifying 13 problems
✓ Generating Big O complexity questions
✓ Generating technique/approach questions
✓ Generating real-world example questions
✓ Formatting for Quizlet CSV import
✓ Dataset generated: generated/media/quizlet/quiz1_algorithms_multiple_choice.csv
✓ Total questions: 39 (13 problems × 3 question types)
> exit
$ cat generated/media/quizlet/quiz1_algorithms_multiple_choice.csv
# CSV formatted with Term | Definition columns, ready for import
```

### Integration with Copilot Workflows

The skill works seamlessly with Copilot CLI's workflow features:

- **Chain with Other Skills:** Use together with python-header-note or visualization skills
- **Batch Processing:** Generate datasets for multiple quizzes in sequence
  ```bash
  > create-quizelet-data mocked-quizes.md --section "Quiz 1"
  > create-quizelet-data mocked-quizes.md --section "Quiz 2"
  ```
- **Custom Organization:** Specify output naming and topic categorization
  ```bash
  > create-quizelet-data --file source.md --quiz 3 --topic system-design
  ```
- **Version Control:** Generated files integrate with Git for tracking quiz evolution
  ```bash
  > git add generated/media/quizlet/
  > git commit -m "feat: Add Quiz 1 Quizlet dataset for algorithms"
  ```

### Tips for Best Results

- **Source Format:** Use markdown files with clear problem headers and explanations
- **Include Examples:** Add real-world context (manufacturing, space, finance) for better retention
- **Verify Complexity:** Double-check time/space complexity in generated Big O questions
- **Multiple Attempts:** If not satisfied, run again after refining source material
- **Organize Topics:** Use consistent naming for related quizzes
- **Track Updates:** Commit generated datasets to Git for version history
- **Leverage Metadata:** Tag questions with difficulty (easy/medium/hard) if available

---

## Question Types and Formats

### Big O Complexity Questions

Test understanding of time and space complexity analysis.

**Format (with blank lines):**
```
Q[N] - Complexity: What is the [time/space] complexity for [technique]?

A) O(...)
B) O(...)
C) O(...)
D) O(...)

✓ Correct: X) O(...)
```

**Example:**
```
Q1 - Complexity: What is the time complexity for finding duplicates using Index Marking?

A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

✓ Correct: A) O(n)
```

### Technique/Approach Questions

Test algorithm selection and pattern recognition.

**Format (with blank lines):**
```
Q[N] - Technique: Which [approach/structure] is used for [problem]?

A) [Alternative 1]
B) [Correct approach]
C) [Alternative 2]
D) [Alternative 3]

✓ Correct: B) [Correct approach]
```

**Example:**
```
Q2 - Technique: Which technique is used to find duplicates without extra space?

A) Hash Table approach
B) Index Marking (Array Indexing)
C) Sorting approach
D) Binary Search

✓ Correct: B) Index Marking (Array Indexing)
```

### Example/Application Questions

Test practical understanding and real-world scenarios.

**Format (with blank lines):**
```
Q[N] - Example: [Scenario from real-world context]?

A) [Outcome 1]
B) [Correct outcome]
C) [Outcome 2]
D) [Outcome 3]

✓ Correct: B) [Correct outcome]
```

**Example:**
```
Q3 - Example: In build processes, detecting cycles prevents what kind of problem?

A) Slow builds
B) Infinite loops in dependency chains
C) Compilation errors
D) Memory leaks

✓ Correct: B) Infinite loops in dependency chains
```

---

## Quizlet Import Guide

### Step-by-Step Import Process

1. **Download CSV File**
   - Located at: `generated/media/quizlet/quiz[N]_[topic]_multiple_choice.csv`
   - File contains Term | Definition format

2. **Go to Quizlet**
   - Visit https://quizlet.com
   - Log in or create account

3. **Create New Set**
   - Click "Create" button (top left)
   - Select "Import" option
   - Choose "Quizlet" or "CSV" format

4. **Upload File**
   - Click "Choose file"
   - Select your CSV file from `generated/media/quizlet/`
   - Click "Import"

5. **Review Set**
   - Quizlet will parse and display the questions
   - Verify all problems and questions appear
   - Check that answers are correctly marked

6. **Customize (Optional)**
   - Add subject tags: "Algorithms", "Data Structures", etc.
   - Set difficulty levels
   - Enable/disable study modes

7. **Start Studying**
   - Use Flashcard mode for review
   - Test mode for practice exams
   - Spaced repetition for retention

---

## CSV Format Reference

### File Structure (Enhanced with Blank Lines)

```csv
Term,Definition
"Problem Name (Complexity)","(Multiple Choice)
Q1 - Question text?

A) Option A
B) Option B
C) Option C
D) Option D

✓ Correct: A) Correct text"
"Problem Name (Technique)","(Multiple Choice)
Q2 - Question text?

A) Option A
B) Option B
C) Option C
D) Option D

✓ Correct: B) Correct text"
```

**Key Enhancement:** Blank lines are added:
- **After the question** (before options list) - separates question from choices
- **After the options** (before answer key) - separates answer explanations

This formatting improves:
- Readability in Quizlet's display
- Visual scanning of question structure
- Clarity when reviewing flashcards

### Formatting Rules

- **Term Column**: Problem name or identifier
- **Definition Column**: Multiple choice question content with blank lines
- **Question Marker**: Q1, Q2, Q3 for sequence
- **Options**: A through D (4 options per question)
- **Answer Key**: Include `✓ Correct: X) Text` at bottom
- **Blank Lines**: Critical for improved readability and Quizlet parsing
- **Escaping**: Use double quotes for CSV-embedded quotes

### Best Practices

- One problem = 3 questions (Big O, Technique, Example)
- Consistent formatting across all questions
- **Blank lines after question and after options** - improves Quizlet display
- Clear answer marking for Quizlet parsing
- Readable option text (concise but complete)
- Real-world context in example questions

---

## Organization and File Management

### Directory Structure

```
generated/media/quizlet/
├── quiz1_algorithms_multiple_choice.csv
├── quiz2_data_structures_multiple_choice.csv
├── quiz3_system_design_multiple_choice.csv
└── README.md (optional: index of datasets)
```

### Naming Convention

- **Format:** `quiz[N]_[topic]_[style].csv`
- **N**: Quiz number (1, 2, 3, etc.)
- **topic**: Subject area (algorithms, data_structures, system_design)
- **style**: Question format (multiple_choice, flashcard)

### Version Control

Track datasets in Git:
```bash
git add generated/media/quizlet/
git commit -m "feat: Add Quiz 1 Quizlet dataset for algorithms & data structures"
```

---

For complete documentation including skill structure, implementation details, and quality checklist, see [SKILL.md](SKILL.md).
