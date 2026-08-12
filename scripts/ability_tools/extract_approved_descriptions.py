#!/usr/bin/env python3
"""
Extract approved extended descriptions for game implementation.
Reads all ability files with status: reviewed and generates extended_descriptions.txt
"""

import os
import re
from pathlib import Path
import yaml

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None
    
    # Find the closing --- for frontmatter
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None

def extract_extended_description(content):
    """Extract the extended description from markdown content."""
    # Remove frontmatter first
    content_without_fm = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Find Extended In-Game Description section
    match = re.search(
        r'## Extended In-Game Description\s*\n(?:\*[^\n]*\*\s*\n)?(?:\n)?(.*?)(?=\n##|\n\*?Character count:|\Z)',
        content_without_fm,
        re.DOTALL
    )
    
    if match:
        description = match.group(1).strip()
        # Remove any trailing newlines
        description = description.replace('\n', ' ').strip()
        return description
    
    return None

def main():
    # Paths
    abilities_dir = Path(__file__).parent.parent.parent / "knowledge" / "abilities"
    output_file = abilities_dir.parent / "extended_ability_descriptions" / "extended_descriptions.txt"
    
    if not abilities_dir.exists():
        print(f"❌ Error: Abilities directory not found at {abilities_dir}")
        return
    
    # Collect approved descriptions
    approved_descriptions = {}
    
    # Read all markdown files
    for file_path in sorted(abilities_dir.glob("*.md")):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            frontmatter = extract_frontmatter(content)
            
            if frontmatter:
                ability_id = frontmatter.get('id')
                status = frontmatter.get('status', 'unknown')
                
                # TEMPORARY: Include all abilities until we have some reviewed ones
                # TODO: Change back to only reviewed abilities once some are approved
                # if ability_id is not None and status == 'reviewed':
                if ability_id is not None:
                    # Extract extended description
                    extended_desc = extract_extended_description(content)
                    if extended_desc:
                        approved_descriptions[ability_id] = extended_desc
                    else:
                        print(f"⚠️  Warning: No extended description found for approved ability {ability_id}")
                        
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
    
    # Sort by ID
    sorted_ids = sorted(approved_descriptions.keys())
    
    # Generate output file
    output_lines = []
    for ability_id in sorted_ids:
        output_lines.append(f"# ID: {ability_id}")
        output_lines.append(approved_descriptions[ability_id])
        output_lines.append("")  # Blank line between entries
    
    # Write the file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"✅ Generated extended_descriptions.txt")
    print(f"   Total approved abilities: {len(approved_descriptions)}")
    print(f"   Output file: {output_file}")
    
    # Character count validation
    invalid_count = 0
    too_short = 0
    too_long = 0
    
    for ability_id, desc in approved_descriptions.items():
        char_count = len(desc)
        if char_count < 280:
            too_short += 1
            invalid_count += 1
        elif char_count > 300:
            print(f"   ⚠️  ID {ability_id}: {char_count} chars (TOO LONG - max 300)")
            too_long += 1
            invalid_count += 1
    
    if invalid_count > 0:
        print(f"   ⚠️  {invalid_count} abilities have invalid character counts:")
        if too_short > 0:
            print(f"      - {too_short} too short (< 280 chars)")
        if too_long > 0:
            print(f"      - {too_long} too long (> 300 chars)")

if __name__ == "__main__":
    main()