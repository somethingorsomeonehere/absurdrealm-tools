#!/usr/bin/env python3
"""
Check all ability files for extended descriptions that are outside the 280-300 character range.
Counts characters including spaces.
Can optionally update frontmatter with correct counts.
"""

import os
import re
import yaml
import sys
from pathlib import Path

def extract_extended_description(content):
    """Extract the extended description from the markdown content."""
    # Find the section after "## Extended In-Game Description"
    pattern = r'## Extended In-Game Description\s*\n\*For use in Elite Redux extended ability UI \(280-300 chars max\)\*\s*\n\s*\n(.+?)(?=\n\n##|\n\n#|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        # Get the description text and strip any trailing whitespace
        description = match.group(1).strip()
        return description
    return None

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if content.startswith('---'):
        try:
            # Find the closing ---
            end_idx = content.find('---', 3)
            if end_idx != -1:
                yaml_str = content[3:end_idx].strip()
                return yaml.safe_load(yaml_str)
        except:
            pass
    return None

def update_frontmatter_count(file_path, new_count):
    """Update the character_count in frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('---'):
        end_idx = content.find('---', 3)
        if end_idx != -1:
            frontmatter_str = content[3:end_idx].strip()
            rest_of_content = content[end_idx+3:]
            
            try:
                frontmatter = yaml.safe_load(frontmatter_str)
                frontmatter['character_count'] = new_count
                
                # Rebuild content
                new_frontmatter = yaml.dump(frontmatter, sort_keys=False, default_flow_style=False)
                new_content = f"---\n{new_frontmatter}---{rest_of_content}"
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
            except:
                pass
    return False

def main():
    # Check for --update flag
    update_mode = '--update' in sys.argv
    
    # Path to abilities directory
    abilities_dir = Path("/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities")
    
    # Lists to store results
    too_short = []
    too_long = []
    correct_length = []
    missing_description = []
    
    # Process all markdown files
    for file_path in sorted(abilities_dir.glob("*.md")):
        # Skip CLAUDE.md and other non-ability files
        if file_path.name in ["CLAUDE.md", "README.md"]:
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter = extract_frontmatter(content)
        if not frontmatter:
            print(f"Warning: No frontmatter found in {file_path.name}")
            continue
            
        ability_id = frontmatter.get('id', '?')
        ability_name = frontmatter.get('name', '?')
        stated_count = frontmatter.get('character_count', 0)
        
        # Extract extended description
        description = extract_extended_description(content)
        
        if description is None:
            missing_description.append({
                'file': file_path.name,
                'id': ability_id,
                'name': ability_name
            })
            continue
        
        # Count characters (including spaces)
        char_count = len(description)
        
        # Categorize based on character count
        entry = {
            'file': file_path.name,
            'id': ability_id,
            'name': ability_name,
            'count': char_count,
            'stated_count': stated_count,
            'description': description
        }
        
        if char_count < 280:
            too_short.append(entry)
        elif char_count > 300:
            too_long.append(entry)
        else:
            correct_length.append(entry)
    
    # Print results
    print("ABILITY CHARACTER COUNT CHECK RESULTS")
    print("=" * 80)
    
    print(f"\nTOO SHORT (< 280 chars): {len(too_short)} files")
    print("-" * 80)
    for entry in too_short:
        mismatch = " (MISMATCH!)" if entry['stated_count'] != entry['count'] else ""
        print(f"{entry['file']:30} | ID: {entry['id']:3} | {entry['name']:20} | {entry['count']:3} chars (stated: {entry['stated_count']}){mismatch}")
        print(f"   Description: {entry['description'][:60]}...")
    
    print(f"\nTOO LONG (> 300 chars): {len(too_long)} files")
    print("-" * 80)
    for entry in too_long:
        mismatch = " (MISMATCH!)" if entry['stated_count'] != entry['count'] else ""
        print(f"{entry['file']:30} | ID: {entry['id']:3} | {entry['name']:20} | {entry['count']:3} chars (stated: {entry['stated_count']}){mismatch}")
        print(f"   Description: {entry['description'][:60]}...")
    
    print(f"\nMISSING EXTENDED DESCRIPTION: {len(missing_description)} files")
    print("-" * 80)
    for entry in missing_description:
        print(f"{entry['file']:30} | ID: {entry['id']:3} | {entry['name']:20}")
    
    print(f"\nCORRECT LENGTH (280-300 chars): {len(correct_length)} files")
    print("-" * 80)
    mismatches = [e for e in correct_length if e['stated_count'] != e['count']]
    if mismatches:
        print("Files with correct length but mismatched frontmatter count:")
        for entry in mismatches:
            print(f"{entry['file']:30} | ID: {entry['id']:3} | {entry['name']:20} | {entry['count']:3} chars (stated: {entry['stated_count']})")
    else:
        print(f"All {len(correct_length)} files have correct character counts and matching frontmatter!")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    total_files = len(too_short) + len(too_long) + len(correct_length) + len(missing_description)
    print(f"Total ability files checked: {total_files}")
    print(f"Too short (<280): {len(too_short)}")
    print(f"Too long (>300): {len(too_long)}")
    print(f"Correct length (280-300): {len(correct_length)}")
    print(f"Missing extended description: {len(missing_description)}")
    
    # Check for frontmatter mismatches
    all_entries = too_short + too_long + correct_length
    mismatches = [e for e in all_entries if e['stated_count'] != e['count']]
    print(f"\nFrontmatter character_count mismatches: {len(mismatches)}")
    
    # Update mismatches if requested
    if update_mode and mismatches:
        print("\nUpdating frontmatter counts...")
        updated = 0
        for entry in mismatches:
            if update_frontmatter_count(abilities_dir / entry['file'], entry['count']):
                updated += 1
        print(f"Updated {updated} files with correct character counts")
    elif mismatches and not update_mode:
        print("Run with --update to fix frontmatter mismatches")

if __name__ == "__main__":
    main()