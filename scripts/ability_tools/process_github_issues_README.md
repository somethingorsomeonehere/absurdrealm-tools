# Process GitHub Issues Script

This script automates the processing of GitHub issues from the Elite Redux Ability Codex feedback system.

## Overview

The script fetches ability review issues from GitHub, validates suggested changes, and automatically updates the necessary files:
- Individual ability documentation files
- Central extended descriptions file
- Progress tracking

## Requirements

```bash
pip install PyGithub requests pyyaml
```

## Usage

### Basic Usage (Test Mode)
```bash
python process_github_issues.py
```

### With GitHub Token
```bash
python process_github_issues.py --token YOUR_GITHUB_TOKEN
```

### Dry Run (Preview Changes)
```bash
python process_github_issues.py --token YOUR_GITHUB_TOKEN --dry-run
```

### Process Closed Issues
```bash
python process_github_issues.py --token YOUR_GITHUB_TOKEN --state closed
```

### Save Summary Report
```bash
python process_github_issues.py --token YOUR_GITHUB_TOKEN --output summary_report.md
```

## How It Works

1. **Fetch Issues**: Queries GitHub for issues with the "ability-review" label
2. **Parse Data**: Extracts ability ID, name, and suggested description changes
3. **Validate**: Ensures character count is within 280-300 (GBA hardware limit)
4. **Update Files**:
   - Individual ability file in `knowledge/abilities/{id}_{name}.md`
   - Central descriptions in `extended_descriptions.txt`
   - Progress tracking in `progress.md` (marks as reviewed ✅)
5. **Generate Reports**: Creates summary and PR body for review

## Character Count Validation

The script enforces strict character limits due to GBA hardware constraints:
- **Minimum**: 280 characters
- **Maximum**: 300 characters
- **Counting**: Includes all characters, spaces, and punctuation

## Issue Format

The script expects issues to follow the template format:

```yaml
Ability Name: Speed Boost
Ability ID: 3
Issue Type:
  - [X] Extended description character count issue
Suggested Changes:
  Current text: "..."
  Suggested text: "..."
```

## Output Files

- **Summary Report**: Detailed processing results
- **PR Body**: Generated pull request description
- **Updated Files**: All modified ability files

## Error Handling

The script handles various error cases:
- Missing required fields in issues
- Character count violations
- File not found errors
- Invalid ability IDs

Skipped issues are logged with reasons for debugging.

## Integration with Workflow

1. Community members report issues via the codex "Suggest Edit" button
2. Issues are created with the ability-review template
3. This script processes batches of issues
4. Changes are reviewed and merged via pull request
5. Codex automatically updates with new descriptions

## Example Command

Process all open ability review issues and save a summary:

```bash
python process_github_issues.py \
  --token ghp_YOUR_TOKEN_HERE \
  --output "processing_summary_$(date +%Y%m%d).md"
```

## Notes

- Always review generated changes before committing
- The script creates a PR body file for easy pull request creation
- Test mode uses sample data when no GitHub token is provided
- Character counts are critical - the GBA cannot display text outside the limits