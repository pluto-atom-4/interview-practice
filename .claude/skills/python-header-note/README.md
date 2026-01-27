# Python Header Note Skill - Usage Guide

## Usage in Claude Code Agent

### Invoking the Skill

You can invoke this skill in two ways within Claude Code:

1. **Using the Skill Command:**
   ```
   /python-header-note
   ```
   Claude Code will prompt for the Python file path or context to document.

2. **Direct Skill Invocation:**
   ```
   skill: "python-header-note", args: "path/to/your/file.py"
   ```
   This directly specifies which file to add header documentation to.

### Workflow Integration

**Step 1: File Preparation**
- Ensure your Python file contains the algorithm implementation
- The file should be ready for documentation (code doesn't need to be perfect yet)

**Step 2: Invoke the Skill**
- Run `/python-header-note` in Claude Code
- Provide the file path when prompted
- Alternatively, specify the file in the skill arguments

**Step 3: Review Generated Header**
- Claude Code will analyze your implementation
- A comprehensive header note will be added to the top of your file
- The header follows the structure outlined in [Header Structure](SKILL.md#header-structure)

**Step 4: Refinement (Optional)**
- Edit the generated header if you want to adjust explanations
- Re-run the skill if you significantly modify the algorithm implementation
- Ensure all complexity analysis matches your final code

### Example Usage Scenario

When documenting an interview preparation solution:

```bash
# File: drills/merge_sorted_arrays.py
# Contains: Implementation of merge two sorted arrays algorithm

claude-code /python-header-note
# When prompted, specify: drills/merge_sorted_arrays.py

# Result:
# - Header note added with Problem Statement
# - Algorithm explanation with Key Concepts
# - Multiple summary formats (30-second pitch, rapid-fire, one-liner)
# - Complexity analysis and use cases
```

### Tips for Best Results

- **Provide Context:** If your file has comments explaining the approach, Claude Code will use them to generate better headers
- **Finalize Code First:** Complete your implementation before generating the header for accurate explanations
- **Review Complexity Analysis:** Verify the time and space complexity match your implementation
- **Use Interview Context:** The skill is optimized for technical interview preparation, so explanations will emphasize interview-relevant aspects
- **Iterate:** If you refactor your solution, consider re-running the skill to keep documentation synchronized

---

## Usage in Copilot CLI

### Invoking the Skill

Copilot CLI provides several ways to invoke this skill:

1. **Using the Direct Skill Command:**
   ```bash
   copilot python-header-note path/to/your/file.py
   ```
   Directly specifies the Python file to document.

2. **Interactive Mode:**
   ```bash
   copilot
   > python-header-note
   ```
   Enters interactive skill mode where you provide the file path when prompted.

3. **With Extended Arguments:**
   ```bash
   copilot python-header-note --file path/to/file.py --verbose
   ```
   Provides additional options for customization.

### Workflow Integration

**Step 1: Navigate to Project**
```bash
cd /path/to/interview-practice
copilot
```

**Step 2: Invoke the Skill**
```bash
> python-header-note drills/merge_sorted_arrays.py
```
Copilot will analyze the file and generate a comprehensive header note.

**Step 3: Review Generated Header**
- The header note is added to the top of your Python file
- Check the Problem Statement, Algorithm Explanation, and Summary Variations
- Verify complexity analysis matches your implementation

**Step 4: Refinement**
- Edit the generated header directly in your editor if needed
- Re-run the skill after significant code changes
- Use Copilot's editing capabilities to refine explanations

### Example Usage Scenario

```bash
$ cd interview-practice
$ copilot
Copilot CLI v2.0
> python-header-note drills/find_duplicates.py
✓ Analyzing drills/find_duplicates.py
✓ Generating header note with problem statement
✓ Creating algorithm explanation
✓ Building summary variations
✓ Computing complexity analysis
✓ Header note successfully added to file

> exit
$ cat drills/find_duplicates.py
# Header note with comprehensive documentation now appears at the top
```

### Integration with Copilot Workflows

The skill works seamlessly with Copilot CLI's workflow features:

- **Chain with Other Skills:** Use together with refactoring or testing skills
- **Batch Processing:** Document multiple files in sequence
  ```bash
  > for file in drills/*.py; do python-header-note $file; done
  ```
- **Script Integration:** Automate documentation in development pipelines
- **Version Control:** Header notes integrate well with git workflows

### Tips for Best Results

- **Complete Your Code First:** Run the skill after finalizing your implementation
- **Include Comments:** Code comments help Copilot generate more accurate headers
- **Use Consistent Style:** Maintain alignment with existing code in your project
- **Validate Output:** Always review the generated header for accuracy
- **Keep Documentation Current:** Re-run the skill if you refactor your algorithm significantly
- **Leverage Copilot's Editor:** Use Copilot's built-in editor to fine-tune headers if needed

---

For complete documentation including header structure, implementation guide, and quality checklist, see [SKILL.md](SKILL.md).
