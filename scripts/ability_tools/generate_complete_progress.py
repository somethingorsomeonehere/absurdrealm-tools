#!/usr/bin/env python3
"""
Generate complete progress.md with all 869 abilities and correct IDs
"""

import re
import os

def load_correct_mapping():
    """Load the correct ability mapping"""
    mapping_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/scripts/ability_tools/ability_id_mapping.txt"
    
    id_to_name = {}
    
    with open(mapping_path, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                parts = line.strip().split(' | ')
                if len(parts) == 2:
                    ability_id = int(parts[0].strip())
                    ability_name = parts[1].strip().replace('ABILITY_', '')
                    id_to_name[ability_id] = ability_name
    
    return id_to_name

def load_existing_progress():
    """Load existing progress data to preserve completion status"""
    progress_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/extended_ability_descriptions/progress.md"
    
    completed_abilities = {}  # name -> {character_count, etc}
    
    with open(progress_path, 'r') as f:
        content = f.read()
    
    # Find all existing entries in the progress table
    # Format: | ID  | Ability Name      | Researched | Written | Reviewed | Character Count |
    table_pattern = r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'
    
    matches = re.findall(table_pattern, content)
    
    for match in matches:
        old_id, name, researched, written, reviewed, char_count = match
        name = name.strip()
        
        # Convert name to consistent format (Title Case)
        name_parts = name.replace('_', ' ').split()
        formatted_name = ' '.join(word.capitalize() for word in name_parts)
        
        completed_abilities[formatted_name] = {
            'researched': researched.strip(),
            'written': written.strip(), 
            'reviewed': reviewed.strip(),
            'character_count': char_count.strip()
        }
    
    return completed_abilities

def format_ability_name(ability_name):
    """Convert ABILITY_NAME to Title Case"""
    # Remove ABILITY_ prefix if present
    if ability_name.startswith('ABILITY_'):
        ability_name = ability_name[8:]
    
    # Convert to title case
    words = ability_name.split('_')
    formatted = ' '.join(word.capitalize() for word in words)
    
    # Handle special cases
    special_cases = {
        'Hp': 'HP',
        'Mp': 'MP',
        'Ai': 'AI',
        'Id': 'ID',
        'Iv': 'IV',
        'Ev': 'EV',
        'Ko': 'KO',
        'Pp': 'PP'
    }
    
    for old, new in special_cases.items():
        formatted = formatted.replace(old, new)
    
    return formatted

def generate_progress_md():
    """Generate the complete progress.md file"""
    id_to_name = load_correct_mapping()
    completed_abilities = load_existing_progress()
    
    # Count completed abilities
    completed_count = len([data for data in completed_abilities.values() if data['written'] == '✅'])
    
    # Generate header
    header = f"""# Extended Ability Descriptions Progress

Total Abilities: {len(id_to_name)}
Completed: {completed_count}
In Progress: 0

## Progress Tracking

| ID  | Ability Name               | Researched | Written | Reviewed | Character Count |
|-----|----------------------------|------------|---------|----------|-----------------|"""
    
    # Generate table rows
    rows = []
    
    for ability_id in sorted(id_to_name.keys()):
        ability_name = id_to_name[ability_id]
        formatted_name = format_ability_name(ability_name)
        
        # Check if this ability is already completed
        if formatted_name in completed_abilities:
            data = completed_abilities[formatted_name]
            researched = data['researched']
            written = data['written']
            reviewed = data['reviewed']
            char_count = data['character_count']
        else:
            # Not completed yet
            researched = '❌'
            written = '❌'
            reviewed = '❌'
            char_count = '-'
        
        row = f"| {ability_id:3d} | {formatted_name:<26} | {researched:<10} | {written:<7} | {reviewed:<8} | {char_count:<15} |"
        rows.append(row)
    
    # Read the existing file to preserve batch organization and notes
    progress_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/extended_ability_descriptions/progress.md"
    
    with open(progress_path, 'r') as f:
        existing_content = f.read()
    
    # Find where the batch organization starts
    batch_start = existing_content.find("## Batch Organization")
    
    if batch_start != -1:
        batch_section = existing_content[batch_start:]
    else:
        batch_section = """
## Batch Organization

### Batch 1: Weather Abilities (10 abilities)
- [x] ABILITY_DRIZZLE
- [x] ABILITY_DROUGHT
- [x] ABILITY_SAND_STREAM
- [x] ABILITY_SNOW_WARNING
- [x] ABILITY_PRIMORDIAL_SEA
- [x] ABILITY_DESOLATE_LAND
- [x] ABILITY_DELTA_STREAM
- [x] ABILITY_ELECTRIC_SURGE
- [x] ABILITY_GRASSY_SURGE
- [x] ABILITY_PSYCHIC_SURGE

## Notes
- Use `/project:analyze-ability` for researching mechanics
- Target 280-300 characters per description (GBA UI limit: 11 lines × 30 chars)
- Update `extended_descriptions.txt` as abilities are completed
- Mark phases: ❌ Not Started | 🔄 In Progress | ✅ Complete"""
    
    # Combine everything
    complete_content = header + "\n" + "\n".join(rows) + "\n" + batch_section
    
    return complete_content

def main():
    print("Generating complete progress.md with all abilities...")
    
    # Generate the content
    content = generate_progress_md()
    
    # Backup the original file
    progress_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/extended_ability_descriptions/progress.md"
    backup_path = progress_path + ".backup"
    
    # Create backup
    with open(progress_path, 'r') as f:
        original_content = f.read()
    
    with open(backup_path, 'w') as f:
        f.write(original_content)
    
    print(f"Backup created: {backup_path}")
    
    # Write the new content
    with open(progress_path, 'w') as f:
        f.write(content)
    
    print(f"Updated progress.md with all 869 abilities")
    print("Preserved completion status for existing abilities")
    
    # Count lines for verification
    lines = content.split('\n')
    table_lines = [line for line in lines if line.startswith('|') and '---' not in line and 'Ability Name' not in line]
    print(f"Total table rows: {len(table_lines)}")

if __name__ == "__main__":
    main()