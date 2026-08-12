#!/usr/bin/env python3
"""
Test script for the GitHub issue processor.
Demonstrates how to use the processor without a GitHub token.
"""

import sys
from pathlib import Path

# Add the parent directory to the path so we can import the processor
sys.path.insert(0, str(Path(__file__).parent))

from process_github_issues import AbilityReviewProcessor

def main():
    print("Testing GitHub Issue Processor")
    print("=" * 60)
    
    # Create processor without token (will use test data)
    processor = AbilityReviewProcessor()
    
    # Fetch test issues
    print("\n1. Fetching test issues...")
    issues = processor.fetch_issues()
    print(f"   Found {len(issues)} test issue(s)")
    
    # Display test issue details
    for issue in issues:
        print(f"\n2. Test Issue Details:")
        print(f"   - Number: #{issue['number']}")
        print(f"   - Title: {issue['title']}")
        print(f"   - User: {issue['user']}")
        
        # Parse the issue
        issue_data = processor.parse_issue_body(issue['body'])
        print(f"\n3. Parsed Data:")
        print(f"   - Ability: {issue_data['ability_name']} (ID: {issue_data['ability_id']})")
        print(f"   - Issue Types: {', '.join(issue_data['issue_types'])}")
        
        # Validate character count
        if issue_data['suggested_text']:
            is_valid, char_count = processor.validate_character_count(issue_data['suggested_text'])
            print(f"\n4. Character Count Validation:")
            print(f"   - Count: {char_count}")
            print(f"   - Valid: {'✅' if is_valid else '❌'} (must be 280-300)")
            
            # Show text preview
            print(f"\n5. Suggested Text Preview:")
            preview = issue_data['suggested_text'][:100] + "..." if len(issue_data['suggested_text']) > 100 else issue_data['suggested_text']
            print(f"   {preview}")
    
    print("\n" + "=" * 60)
    print("Test complete! This was a dry run - no files were modified.")
    print("\nTo process real issues:")
    print("1. Get a GitHub personal access token")
    print("2. Run: python process_github_issues.py --token YOUR_TOKEN")
    print("3. Review the changes before committing")


if __name__ == '__main__':
    main()