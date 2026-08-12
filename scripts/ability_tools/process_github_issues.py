#!/usr/bin/env python3
"""
Process GitHub issues from the Elite Redux Ability Codex feedback system.
Automatically updates ability descriptions based on community review issues.

Requirements:
    pip install PyGithub requests pyyaml
"""

import os
import re
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml

try:
    from github import Github
    HAS_PYGITHUB = True
except ImportError:
    HAS_PYGITHUB = False
    print("Warning: PyGithub not installed. Install with: pip install PyGithub")

# Configuration
REPO_NAME = "Elite-Redux/eliteredux-source"
ISSUE_LABEL = "ability-review"
BASE_PATH = Path("/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky")
ABILITIES_PATH = BASE_PATH / "knowledge" / "abilities"
EXTENDED_DESC_PATH = BASE_PATH / "knowledge" / "extended_ability_descriptions" / "extended_descriptions.txt"
PROGRESS_PATH = BASE_PATH / "knowledge" / "extended_ability_descriptions" / "progress.md"

# Character count limits (GBA hardware requirement)
MIN_CHAR_COUNT = 280
MAX_CHAR_COUNT = 300


class AbilityReviewProcessor:
    def __init__(self, github_token: Optional[str] = None):
        """Initialize the processor with optional GitHub token."""
        self.github_token = github_token
        self.github = None
        self.repo = None
        
        if HAS_PYGITHUB and github_token:
            self.github = Github(github_token)
            self.repo = self.github.get_repo(REPO_NAME)
        
        self.processed_issues = []
        self.skipped_issues = []
        self.errors = []
    
    def fetch_issues(self, state: str = "open") -> List[Dict]:
        """Fetch ability review issues from GitHub."""
        if not self.repo:
            print("GitHub connection not available. Using test data...")
            return self._get_test_issues()
        
        issues = []
        try:
            for issue in self.repo.get_issues(labels=[ISSUE_LABEL], state=state):
                issues.append({
                    'number': issue.number,
                    'title': issue.title,
                    'body': issue.body,
                    'url': issue.html_url,
                    'created_at': issue.created_at,
                    'user': issue.user.login
                })
        except Exception as e:
            print(f"Error fetching issues: {e}")
            return self._get_test_issues()
        
        return issues
    
    def _get_test_issues(self) -> List[Dict]:
        """Return test issues for development."""
        return [{
            'number': 999,
            'title': '[Ability Review] Speed Boost',
            'body': '''### Ability Name
Speed Boost

### Ability ID
3

### Source File
knowledge/abilities/3_speed_boost.md

### Issue Type
- [X] Extended description character count issue (MUST be 280-300 chars - GBA hardware limit)

### Issue Description
The current extended description is 287 characters, which is good, but could be optimized to provide more detail about the timing of activation.

### Suggested Changes
Current text: "Speed Boost generates increasing velocity through battle momentum, raising the user's Speed by one stage at the end of each turn they remain on the field. Does not activate on the turn of entry or when switching in. Continues until reaching maximum Speed (+6 stages). Creates powerful momentum in extended battles through continuous acceleration."

Suggested text: "Speed Boost raises Speed by one stage at the end of each turn. Does not activate on switch-in turn. Continues until reaching +6 stages. Creates powerful momentum through continuous acceleration, making fast Pokemon even faster over time. Essential for sweepers who need to outpace threats. Maximum benefit after 6 turns on field."
''',
            'url': 'https://github.com/Elite-Redux/eliteredux-source/issues/999',
            'created_at': datetime.now(),
            'user': 'test_user'
        }]
    
    def parse_issue_body(self, body: str) -> Dict:
        """Parse the issue body to extract relevant information."""
        data = {
            'ability_name': None,
            'ability_id': None,
            'source_file': None,
            'issue_types': [],
            'description': None,
            'suggested_text': None,
            'current_text': None
        }
        
        # Parse sections
        sections = body.split('###')
        for section in sections:
            lines = section.strip().split('\n')
            if not lines:
                continue
                
            header = lines[0].strip()
            content = '\n'.join(lines[1:]).strip()
            
            if header == 'Ability Name':
                data['ability_name'] = content
            elif header == 'Ability ID':
                data['ability_id'] = content
            elif header == 'Source File':
                data['source_file'] = content
            elif header == 'Issue Type':
                # Extract checked checkboxes
                for line in lines[1:]:
                    if '- [X]' in line or '- [x]' in line:
                        data['issue_types'].append(line.replace('- [X]', '').replace('- [x]', '').strip())
            elif header == 'Issue Description':
                data['description'] = content
            elif header == 'Suggested Changes':
                # Extract current and suggested text
                if 'Current text:' in content and 'Suggested text:' in content:
                    parts = content.split('Suggested text:')
                    current_part = parts[0].replace('Current text:', '').strip()
                    suggested_part = parts[1].strip()
                    
                    # Clean up quotes
                    data['current_text'] = current_part.strip('"')
                    data['suggested_text'] = suggested_part.strip('"')
        
        return data
    
    def validate_character_count(self, text: str) -> Tuple[bool, int]:
        """Validate character count is within GBA limits."""
        char_count = len(text)
        is_valid = MIN_CHAR_COUNT <= char_count <= MAX_CHAR_COUNT
        return is_valid, char_count
    
    def update_individual_file(self, ability_id: str, ability_name: str, new_description: str, char_count: int) -> bool:
        """Update the individual ability markdown file."""
        # Convert ability name to filename format
        filename = f"{ability_id}_{ability_name.lower().replace(' ', '_')}.md"
        filepath = ABILITIES_PATH / filename
        
        if not filepath.exists():
            self.errors.append(f"File not found: {filepath}")
            return False
        
        try:
            content = filepath.read_text()
            
            # Update the extended description section
            # Look for the pattern between "## Extended In-Game Description" and the character count line
            pattern = r'(## Extended In-Game Description.*?\n\n)(.*?)(\n\n\*Character count: )(\d+)'
            
            replacement = f'\\1{new_description}\\3{char_count}'
            updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
            if updated_content == content:
                self.errors.append(f"Failed to update extended description in {filename}")
                return False
            
            filepath.write_text(updated_content)
            return True
            
        except Exception as e:
            self.errors.append(f"Error updating {filename}: {str(e)}")
            return False
    
    def update_extended_descriptions(self, ability_id: str, ability_name: str, new_description: str) -> bool:
        """Update the central extended_descriptions.txt file."""
        try:
            content = EXTENDED_DESC_PATH.read_text()
            
            # Find the ability section
            ability_pattern = rf'# ID: {ability_id}\s*\nability \{{[^}}]+\}}'
            
            # Create the new ability block
            new_block = f'''# ID: {ability_id}
ability {{
  id: ABILITY_{ability_name.upper().replace(" ", "_")}
  extended_description: "{new_description}"
}}'''
            
            # Replace the existing block
            updated_content = re.sub(ability_pattern, new_block, content, flags=re.DOTALL)
            
            if updated_content == content:
                # Try to find by ability name if ID search failed
                name_pattern = rf'ability \{{\s*id: ABILITY_{ability_name.upper().replace(" ", "_")}\s*extended_description: "[^"]+"\s*\}}'
                if re.search(name_pattern, content, re.DOTALL):
                    updated_content = re.sub(name_pattern, new_block.split('\n', 1)[1], content, flags=re.DOTALL)
                else:
                    self.errors.append(f"Failed to find ability {ability_id} in extended_descriptions.txt")
                    return False
            
            EXTENDED_DESC_PATH.write_text(updated_content)
            return True
            
        except Exception as e:
            self.errors.append(f"Error updating extended_descriptions.txt: {str(e)}")
            return False
    
    def update_progress_tracking(self, ability_id: str, mark_reviewed: bool = True) -> bool:
        """Update the progress.md file to mark ability as reviewed."""
        try:
            content = PROGRESS_PATH.read_text()
            
            # Find the row for this ability
            pattern = rf'(\|\s*{ability_id}\s*\|[^|]+\|\s*✅\s*\|\s*✅\s*\|)\s*❌\s*(\|[^|]+\|)'
            
            if mark_reviewed:
                replacement = r'\1 ✅        \2'
            else:
                replacement = r'\1 🔄        \2'  # In progress marker
            
            updated_content = re.sub(pattern, replacement, content)
            
            if updated_content == content:
                self.errors.append(f"Failed to update progress for ability {ability_id}")
                return False
            
            PROGRESS_PATH.write_text(updated_content)
            return True
            
        except Exception as e:
            self.errors.append(f"Error updating progress.md: {str(e)}")
            return False
    
    def process_issue(self, issue: Dict) -> bool:
        """Process a single GitHub issue."""
        print(f"\nProcessing issue #{issue['number']}: {issue['title']}")
        
        # Parse issue data
        issue_data = self.parse_issue_body(issue['body'])
        
        # Validate required fields
        if not all([issue_data['ability_id'], issue_data['ability_name'], issue_data['suggested_text']]):
            self.skipped_issues.append({
                'issue': issue,
                'reason': 'Missing required fields (ID, name, or suggested text)'
            })
            return False
        
        # Validate character count
        is_valid, char_count = self.validate_character_count(issue_data['suggested_text'])
        
        if not is_valid:
            self.skipped_issues.append({
                'issue': issue,
                'reason': f'Character count {char_count} outside valid range ({MIN_CHAR_COUNT}-{MAX_CHAR_COUNT})'
            })
            return False
        
        # Process updates
        success = True
        
        # 1. Update individual ability file
        if not self.update_individual_file(
            issue_data['ability_id'],
            issue_data['ability_name'],
            issue_data['suggested_text'],
            char_count
        ):
            success = False
        
        # 2. Update extended descriptions
        if not self.update_extended_descriptions(
            issue_data['ability_id'],
            issue_data['ability_name'],
            issue_data['suggested_text']
        ):
            success = False
        
        # 3. Update progress tracking
        if not self.update_progress_tracking(issue_data['ability_id']):
            success = False
        
        if success:
            self.processed_issues.append({
                'issue': issue,
                'ability_id': issue_data['ability_id'],
                'ability_name': issue_data['ability_name'],
                'char_count': char_count,
                'changes': issue_data['suggested_text']
            })
        
        return success
    
    def generate_summary(self) -> str:
        """Generate a summary of processed issues."""
        summary = []
        summary.append(f"# GitHub Ability Review Processing Summary")
        summary.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        summary.append(f"## Statistics")
        summary.append(f"- Total issues processed: {len(self.processed_issues) + len(self.skipped_issues)}")
        summary.append(f"- Successfully updated: {len(self.processed_issues)}")
        summary.append(f"- Skipped: {len(self.skipped_issues)}")
        summary.append(f"- Errors encountered: {len(self.errors)}\n")
        
        if self.processed_issues:
            summary.append("## Successfully Processed Issues")
            for item in self.processed_issues:
                issue = item['issue']
                summary.append(f"\n### Issue #{issue['number']}: {issue['title']}")
                summary.append(f"- **Ability**: {item['ability_name']} (ID: {item['ability_id']})")
                summary.append(f"- **Character Count**: {item['char_count']}")
                summary.append(f"- **URL**: {issue['url']}")
                summary.append(f"- **Submitted by**: {issue['user']}")
                summary.append(f"- **New Description**: {item['changes'][:100]}...")
        
        if self.skipped_issues:
            summary.append("\n## Skipped Issues")
            for item in self.skipped_issues:
                issue = item['issue']
                summary.append(f"\n### Issue #{issue['number']}: {issue['title']}")
                summary.append(f"- **Reason**: {item['reason']}")
                summary.append(f"- **URL**: {issue['url']}")
        
        if self.errors:
            summary.append("\n## Errors Encountered")
            for error in self.errors:
                summary.append(f"- {error}")
        
        return '\n'.join(summary)
    
    def create_pull_request_body(self) -> str:
        """Generate a pull request body for the changes."""
        pr_body = []
        pr_body.append("## Ability Review Updates from Community Feedback\n")
        pr_body.append("This PR processes community feedback from the Elite Redux Ability Codex.\n")
        
        pr_body.append("### Changes Made")
        for item in self.processed_issues:
            pr_body.append(f"- **{item['ability_name']}** (#{item['issue']['number']}): Updated extended description ({item['char_count']} chars)")
        
        pr_body.append("\n### Files Modified")
        pr_body.append("- Individual ability files in `knowledge/abilities/`")
        pr_body.append("- `knowledge/extended_ability_descriptions/extended_descriptions.txt`")
        pr_body.append("- `knowledge/extended_ability_descriptions/progress.md`")
        
        pr_body.append("\n### Issues Resolved")
        for item in self.processed_issues:
            pr_body.append(f"- Closes #{item['issue']['number']}")
        
        return '\n'.join(pr_body)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Process GitHub ability review issues')
    parser.add_argument('--token', help='GitHub personal access token')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('--state', default='open', choices=['open', 'closed', 'all'], help='Issue state to process')
    parser.add_argument('--output', help='Output file for summary report')
    
    args = parser.parse_args()
    
    # Initialize processor
    processor = AbilityReviewProcessor(github_token=args.token)
    
    # Fetch and process issues
    print("Fetching ability review issues from GitHub...")
    issues = processor.fetch_issues(state=args.state)
    print(f"Found {len(issues)} issues to process")
    
    if args.dry_run:
        print("\n[DRY RUN MODE - No changes will be made]")
    
    # Process each issue
    for issue in issues:
        if not args.dry_run:
            processor.process_issue(issue)
        else:
            print(f"Would process issue #{issue['number']}: {issue['title']}")
    
    # Generate summary
    summary = processor.generate_summary()
    print("\n" + "="*60)
    print(summary)
    print("="*60)
    
    # Save summary if requested
    if args.output:
        Path(args.output).write_text(summary)
        print(f"\nSummary saved to: {args.output}")
    
    # Generate PR body if issues were processed
    if processor.processed_issues and not args.dry_run:
        pr_body_file = BASE_PATH / "scripts" / "ability_tools" / "pr_body.md"
        pr_body = processor.create_pull_request_body()
        pr_body_file.write_text(pr_body)
        print(f"\nPull request body saved to: {pr_body_file}")
        print("\nNext steps:")
        print("1. Review the changes with git diff")
        print("2. Commit the changes")
        print("3. Create a pull request using the generated PR body")


if __name__ == '__main__':
    main()