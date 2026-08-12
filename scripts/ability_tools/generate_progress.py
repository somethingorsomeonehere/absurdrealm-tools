#!/usr/bin/env python3
"""
Generate progress.md from frontmatter in individual ability files.
This script reads all ability markdown files and builds the progress tracking table.
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
            data = yaml.safe_load(match.group(1))
            if data:
                # Normalize keys to handle variations
                normalized = {}
                
                # Handle id/ability_id
                if 'ability_id' in data:
                    normalized['id'] = data['ability_id']
                elif 'id' in data:
                    normalized['id'] = data['id']
                
                # Handle name/ability_name
                if 'ability_name' in data:
                    normalized['name'] = data['ability_name']
                elif 'name' in data:
                    normalized['name'] = data['name']
                
                # Copy other fields as-is
                for key in ['status']:
                    if key in data:
                        normalized[key] = data[key]
                
                return normalized
            return data
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return None
    return None

def main():
    # Paths
    abilities_dir = Path(__file__).parent.parent.parent / "knowledge" / "abilities"
    progress_file = abilities_dir.parent / "extended_ability_descriptions" / "progress.md"
    
    # Ensure abilities directory exists
    if not abilities_dir.exists():
        print(f"Error: Abilities directory not found at {abilities_dir}")
        return
    
    # Collect all ability data
    abilities = []
    
    # Read all markdown files in the abilities directory
    for file_path in sorted(abilities_dir.glob("*.md")):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            
            # Extract frontmatter
            frontmatter = extract_frontmatter(content)
            
            if frontmatter:
                abilities.append(frontmatter)
            else:
                # If no frontmatter, try to extract ID from filename
                match = re.match(r'^(\d+)_(.+)\.md$', file_path.name)
                if match:
                    ability_id = int(match.group(1))
                    ability_name = match.group(2).replace('_', ' ').title()
                    
                    abilities.append({
                        'id': ability_id,
                        'name': ability_name,
                        'status': 'ai-generated'  # Default for legacy files
                    })
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    # Sort by ID
    abilities.sort(key=lambda x: x.get('id', 999999))
    
    # Find the actual highest ability ID
    max_id = max((a.get('id', 0) for a in abilities), default=0)
    
    # Total abilities is from 0 to max_id inclusive
    total_abilities = max_id + 1  # This should be 876 (0-875)
    
    # Count statistics
    completed = len(abilities)
    reviewed = sum(1 for a in abilities if a.get('status') == 'reviewed')
    
    # Generate progress.md content
    content = ["# Extended Ability Descriptions Progress\n"]
    content.append(f"Total Abilities: {total_abilities}")
    content.append(f"Completed: {completed}")
    content.append(f"In Progress: 0")
    content.append("\n## Progress Tracking\n")
    content.append("| ID  | Ability Name               | Written | Reviewed |")
    content.append("|-----|----------------------------|---------|----------|")
    
    # Track which IDs we've seen
    seen_ids = set()
    
    # Add entries for all abilities from 0 to max_id
    for i in range(total_abilities):  # 0 to max_id inclusive
        ability_data = None
        
        # Find matching ability data
        for a in abilities:
            if a.get('id') == i:
                ability_data = a
                seen_ids.add(i)
                break
        
        if ability_data:
            # Ability has been analyzed
            name = ability_data.get('name', 'Unknown')
            status = ability_data.get('status', 'ai-generated')
            
            written = "✅"
            reviewed = "✅" if status == 'reviewed' else "❌"
        else:
            # Ability not yet analyzed
            # Try to get name from AbilityEnum or default to placeholder
            name = f"Ability {i}" if i > 0 else "None"
            written = "❌"
            reviewed = "❌"
        
        # Format the row
        row = f"| {i:3d} | {name:26s} | {written:7s} | {reviewed:8s} |"
        content.append(row)
    
    # Write the file
    with open(progress_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content) + '\n')
    
    print(f"✅ Generated progress.md")
    print(f"   Total abilities: {total_abilities}")
    print(f"   Completed: {completed}")
    print(f"   Reviewed: {reviewed}")
    print(f"   Remaining: {total_abilities - completed}")

if __name__ == "__main__":
    main()