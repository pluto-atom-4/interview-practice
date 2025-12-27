# GitHub Copilot Instructions

**Purpose:** Define best practices for AI assistant interactions to suppress excessive file generation, maintain clean project structure, and ensure consistent Git Bash usage.

**Scope:** These instructions apply to all AI assistant interactions (GitHub Copilot, Claude, etc.) within this workspace.

---

## File & Documentation Generation

### Directory Rules (🔴 MUST ENFORCE)
- **Output directory for markdown files:** `generated/docs-copilot/` (auto-created)
- **All Copilot-generated markdown files (documentation, guides, summaries, etc.) MUST be saved in this directory by default.**
- **Do NOT save Copilot-generated markdown files in the project root or any other subdirectory unless the user explicitly requests it or a project structure change requires it.**
- **Other file types (scripts, code, etc.) may be saved in their relevant subdirectories unless the user requests otherwise.**
- **Example:**
    - If you generate a markdown document, save it as `[project root]/generated/docs-copilot/[filename].md`.
    - Do NOT save as `[project root]/[filename].md` or `[project root]/data_structures/trees/[filename].md` unless the user requests it.
- **Maximum files per session:** 1
- **Require explicit user request** before generating
- Exception: User can override if project structure changes require it

### Preserve in Root Only (🔴 MUST ENFORCE)
✅ `README.md`, `README-*.md`, `SETUP.md`, `CONTRIBUTING.md`, `LICENSE`

---

## Code Generation Rules (🟡 RECOMMENDED)

- Confirm before creating new files
- Prefer modifying existing files over creating new ones
- Keep changes focused and minimal
- Use tool calls (insert_edit_into_file/replace_string_in_file) instead of printing code blocks
- Always validate changes with get_errors after editing

---

## Manim Script Output (🔴 MUST ENFORCE)

### Media Output Directory
- **Output directory for manim media files:** `generated/media/` (auto-created)
- **All manim scripts MUST output media files (animations, rendered videos, images, etc.) to `[project root]/generated/media/` by default.**
- **Do NOT output manim media files to the project root or scattered across subdirectories.**
- **Configure manim scripts with:** `--media_dir generated/media/` or equivalent in manim configuration
- **Example:**
    - Render command: `manim -qh --media_dir generated/media/ script.py SceneName`
    - Output structure: `generated/media/videos/`, `generated/media/images/`, `generated/media/partial_movie_files/`
- **Subdirectories in `generated/media/`:** Auto-organized by manim (videos, images, etc.)

---

## Shell & Terminal Configuration

### Default Shell: bash.exe (Git Bash)

| Operation | Shell | Notes |
|-----------|-------|-------|
| ✅ Git operations | bash | POSIX paths: `/c/Users/...` |
| ✅ npm/node commands | bash | Auto-convert Windows paths |
| ✅ Python development | bash | |
| ✅ File/directory operations | bash | |
| ✅ Script execution | bash | |
| ❌ cmd.exe | | Avoid for grep, sed, awk, complex pipes |

### Git Configuration (🟡 RECOMMENDED)
- **Default branch:** main
- **Commit template:** `fix: {description}` for bugfixes, `feat: {description}` for features
- **Auto-stage:** disabled
- Always include context in commit messages
- Reference relevant files/tests when appropriate

### Python Development (🟡 RECOMMENDED)
- Always use virtual environment (ensure active before running tests)
- Check `pyproject.toml` for project configuration and dependencies
- Run tests via bash terminal: `python -m pytest tests/`
- Validate changes don't break existing tests
- Follow existing code style and naming conventions

---

## Key Principles

1. **Minimal generation** - Create only what's necessary
2. **Single source of truth** - `README.md` is primary documentation
3. **No redundant files** - One comprehensive document > many partial ones
4. **Git Bash always** - Use `bash.exe` for all terminal operations
5. **Keep root clean** - Generated content → `generated/docs-copilot/` for docs, `generated/media/` for manim media
6. **Centralized media** - All manim outputs → `generated/media/` directory

---

## Document Maintenance

- **Last reviewed:** December 27, 2025
- **Review frequency:** Quarterly or when project structure changes significantly
- **Update process:** Submit changes via pull request with clear justification
