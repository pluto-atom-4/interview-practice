# PyCharm Configuration for Black and isort

This guide will help you configure PyCharm to automatically run black and isort on save and through file watchers.

## Prerequisites

1. Make sure black and isort are installed in your Python environment:
   ```bash
   pip install black isort
   ```

2. Verify the tools work:
   ```bash
   python -m black --version
   python -m isort --version
   ```

## Method 1: File Watchers (Recommended)

### Step 1: Enable File Watchers Plugin
1. Go to `File` → `Settings` (or `PyCharm` → `Preferences` on macOS)
2. Navigate to `Plugins`
3. Search for "File Watchers" and ensure it's enabled
4. Click `OK`

### Step 2: Configure Black File Watcher
1. Go to `File` → `Settings` → `Tools` → `File Watchers`
2. Click the `+` button and select `Custom`
3. Configure as follows:
   - **Name**: `Black Formatter`
   - **File type**: `Python`
   - **Scope**: `Project Files`
   - **Program**: Path to your Python executable (e.g., `python` or full path like `C:\Python\python.exe`)
   - **Arguments**: `-m black $FilePath$`
   - **Output paths to refresh**: `$FilePath$`
   - **Working directory**: `$ProjectFileDir$`
   - **Environment variables**: (leave empty)
   - **Advanced Options**:
     - ✅ Auto-save edited files to trigger the watcher
     - ✅ Trigger the watcher on external changes
     - ❌ Trigger the watcher regardless of syntax errors
     - ✅ Create output file from stdout
     - ❌ Show console

### Step 3: Configure isort File Watcher
1. In the same File Watchers dialog, click `+` → `Custom`
2. Configure as follows:
   - **Name**: `isort Import Sorter`
   - **File type**: `Python`
   - **Scope**: `Project Files`
   - **Program**: Path to your Python executable
   - **Arguments**: `-m isort $FilePath$`
   - **Output paths to refresh**: `$FilePath$`
   - **Working directory**: `$ProjectFileDir$`
   - **Advanced Options**: Same as Black above

## Method 2: Actions on Save

### Step 1: Configure Actions on Save
1. Go to `File` → `Settings` → `Tools` → `Actions on Save`
2. Enable the following:
   - ✅ **Reformat code** (this will use the configured Python formatter)
   - ✅ **Optimize imports** (this will use the configured import organizer)

### Step 2: Configure External Tools (Alternative)
1. Go to `File` → `Settings` → `Tools` → `External Tools`
2. Click `+` to add a new tool for Black:
   - **Name**: `Black`
   - **Description**: `Format Python code with Black`
   - **Program**: Path to your Python executable
   - **Arguments**: `-m black $FilePath$`
   - **Working directory**: `$ProjectFileDir$`
   - **Advanced Options**:
     - ✅ Synchronize files after execution
     - ✅ Open console for tool output

3. Add another tool for isort:
   - **Name**: `isort`
   - **Description**: `Sort imports with isort`
   - **Program**: Path to your Python executable
   - **Arguments**: `-m isort $FilePath$`
   - **Working directory**: `$ProjectFileDir$`
   - **Advanced Options**: Same as Black

## Method 3: Code Style Configuration

### Configure Black as Default Formatter
1. Go to `File` → `Settings` → `Editor` → `Code Style` → `Python`
2. Click the gear icon ⚙️ next to the scheme dropdown
3. Select `Import Scheme` → `Black`
4. If that option isn't available, manually configure:
   - **Tabs and Indents**: Set to 4 spaces
   - **Line length**: 88 characters
   - **Continuation indent**: 4

### Configure Import Organization
1. Go to `File` → `Settings` → `Editor` → `Code Style` → `Python` → `Imports`
2. Configure to match isort settings:
   - **Structure**: Enable "From __future__ imports", "Standard library imports", "Related third party imports", "Local application imports"
   - **Sorting**: Enable "Sort imports"

## Testing the Configuration

1. Open any Python file in your project
2. Make some formatting changes (add extra spaces, mess up imports)
3. Save the file (`Ctrl+S`)
4. The file should automatically be formatted

## Troubleshooting

### If file watchers don't work:
1. Check that the Python path is correct
2. Verify that black and isort are installed in the correct environment
3. Check the PyCharm event log for errors

### If tools can't find your packages:
1. Make sure PyCharm is using the correct Python interpreter
2. Go to `File` → `Settings` → `Project` → `Python Interpreter`
3. Select the interpreter where black and isort are installed

### If formatting doesn't match pre-commit:
1. Ensure both PyCharm and pre-commit use the same configuration files (`pyproject.toml`)
2. Test both tools from command line to ensure they produce the same output

## Keyboard Shortcuts (Optional)

Add keyboard shortcuts for manual formatting:
1. Go to `File` → `Settings` → `Keymap`
2. Search for "External Tools"
3. Assign shortcuts to your Black and isort tools
   - Suggested: `Ctrl+Alt+L` for Black, `Ctrl+Alt+I` for isort

## Integration with Pre-commit

With this setup, your files will be automatically formatted in PyCharm, preventing pre-commit hook failures. The configuration in `pyproject.toml` ensures consistency between PyCharm formatting and pre-commit checks.
