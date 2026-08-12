#!/usr/bin/env python3
"""Update ability progress tracking for completed abilities."""

import re

def update_progress():
    # Read the progress file
    with open('/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/extended_ability_descriptions/progress.md', 'r') as f:
        content = f.read()
    
    # List of completed ability IDs
    completed_ids = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    # Update each ability's row
    for ability_id in completed_ids:
        # Pattern to match the row for this ability ID
        pattern = rf'(\|\s*{ability_id}\s*\|[^|]+\|)\s*❌\s*\|\s*❌\s*\|\s*❌\s*\|([^|]+\|)'
        replacement = rf'\1 ✅          | ✅       | ❌        |\2'
        content = re.sub(pattern, replacement, content)
    
    # Update the completed count at the top
    # Count total completed
    completed_count = content.count('✅          | ✅')
    content = re.sub(r'Completed: \d+', f'Completed: {completed_count}', content)
    
    # Write back the updated content
    with open('/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/extended_ability_descriptions/progress.md', 'w') as f:
        f.write(content)
    
    print(f"Updated progress.md - marked {len(completed_ids)} abilities as completed")
    print(f"Total completed abilities: {completed_count}")

if __name__ == "__main__":
    update_progress()