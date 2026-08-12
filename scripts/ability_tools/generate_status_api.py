#!/usr/bin/env python3
"""
Generate JSON API data from progress.md for Codex Wiki status tracking.
This script parses the progress.md table and creates a JSON file
that the VitePress config can consume for enhanced status indicators.
"""

import json
import re
import os
from pathlib import Path

def parse_progress_md():
    """Parse the progress.md file and extract status data."""
    progress_file = Path(__file__).parent.parent.parent / "knowledge/extended_ability_descriptions/progress.md"
    
    if not progress_file.exists():
        print(f"❌ Progress file not found: {progress_file}")
        return {}
    
    abilities_data = {}
    
    with open(progress_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the table section
    table_pattern = r'\|.*ID.*\|.*Ability Name.*\|.*Written.*\|.*Reviewed.*\|'
    lines = content.split('\n')
    
    in_table = False
    for line in lines:
        if re.match(table_pattern, line):
            in_table = True
            continue
        elif in_table and line.startswith('|---'):
            continue
        elif in_table and line.startswith('|'):
            # Parse table row
            cells = [cell.strip() for cell in line.split('|')[1:-1]]  # Remove empty first/last
            if len(cells) >= 4:
                try:
                    ability_id = int(cells[0])
                    name = cells[1]
                    written = cells[2] == '✅'
                    reviewed = cells[3] == '✅'
                    
                    # Calculate overall status
                    if reviewed:
                        status = 'reviewed'
                    elif written:
                        status = 'written'
                    else:
                        status = 'pending'
                    
                    abilities_data[ability_id] = {
                        'id': ability_id,
                        'name': name,
                        'written': written,
                        'reviewed': reviewed,
                        'status': status
                    }
                except (ValueError, IndexError) as e:
                    print(f"❌ Error parsing line: {line} - {e}")
                    continue
        elif in_table and not line.strip():
            # End of table
            break
    
    return abilities_data

def generate_status_indicators(data):
    """Generate visual status indicators for each ability."""
    indicators = {}
    
    for ability_id, info in data.items():
        # Create status indicator
        if info['reviewed']:
            indicator = '✅'  # Green checkmark for fully reviewed
            badge_class = 'status-complete'
        elif info['written']:
            indicator = '🟠'  # Orange circle for written but needs review
            badge_class = 'status-needs-review'
        else:
            indicator = '⏳'  # Hourglass for pending
            badge_class = 'status-pending'
        
        # Create progress summary
        completed_count = sum([info['written'], info['reviewed']])
        progress_text = f"{completed_count}/2"
        
        indicators[ability_id] = {
            'indicator': indicator,
            'badge_class': badge_class,
            'progress_text': progress_text,
            'tooltip': f"Written: {'✅' if info['written'] else '❌'}, "
                      f"Reviewed: {'✅' if info['reviewed'] else '❌'}"
        }
    
    return indicators

def main():
    """Main function to generate the status API."""
    print("🔄 Generating status API from progress.md...")
    
    # Parse progress data
    abilities_data = parse_progress_md()
    if not abilities_data:
        print("❌ No data found in progress.md")
        return
    
    # Generate status indicators
    status_indicators = generate_status_indicators(abilities_data)
    
    # Create output data
    from datetime import datetime
    
    output_data = {
        'metadata': {
            'total_abilities': len(abilities_data),
            'completed': sum(1 for data in abilities_data.values() if data['reviewed']),
            'written': sum(1 for data in abilities_data.values() if data['written']),
            'pending': sum(1 for data in abilities_data.values() if not data['written']),
            'generated_at': datetime.utcnow().isoformat() + 'Z'  # ISO 8601 format with Z suffix
        },
        'abilities': abilities_data,
        'indicators': status_indicators
    }
    
    # Write to JSON file
    output_file = Path(__file__).parent.parent.parent / "codex/docs/.vitepress/ability-status.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Status API generated: {output_file}")
    print(f"📊 Total abilities: {len(abilities_data)}")
    print(f"📊 Completed: {output_data['metadata']['completed']}")
    print(f"📊 Written: {output_data['metadata']['written']}")
    print(f"📊 Pending: {output_data['metadata']['pending']}")

if __name__ == "__main__":
    main()