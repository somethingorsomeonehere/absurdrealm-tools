#!/usr/bin/env python3
"""
Fix completion count by using actual files as source of truth
"""

import os
import glob
import re

def get_completed_abilities_from_files():
    """Get completed abilities based on actual files that exist"""
    abilities_dir = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities"
    
    # Get all ability files (excluding README)
    pattern = os.path.join(abilities_dir, "*_*.md")
    ability_files = glob.glob(pattern)
    
    completed_ids = set()
    
    for file_path in ability_files:
        filename = os.path.basename(file_path)
        
        # Skip non-ability files
        if filename == "README.md":
            continue
            
        # Extract ID from filename
        match = re.match(r'(\d+)_(.+)\.md$', filename)
        if match:
            ability_id = int(match.group(1))
            completed_ids.add(ability_id)
    
    return completed_ids

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

def format_ability_name(ability_name):
    """Convert ABILITY_NAME to Title Case"""
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

def generate_corrected_progress():
    """Generate progress.md with correct completion count"""
    completed_ids = get_completed_abilities_from_files()
    id_to_name = load_correct_mapping()
    
    print(f"Found {len(completed_ids)} completed abilities based on actual files")
    print(f"Total abilities in mapping: {len(id_to_name)}")
    
    # Generate header
    header = f"""# Extended Ability Descriptions Progress

Total Abilities: {len(id_to_name)}
Completed: {len(completed_ids)}
In Progress: 0

## Progress Tracking

| ID  | Ability Name               | Researched | Written | Reviewed | Character Count |
|-----|----------------------------|------------|---------|----------|-----------------|"""
    
    # Generate table rows
    rows = []
    
    for ability_id in sorted(id_to_name.keys()):
        ability_name = id_to_name[ability_id]
        formatted_name = format_ability_name(ability_name)
        
        # Check if this ability has a file (completed)
        if ability_id in completed_ids:
            researched = '✅'
            written = '✅'
            reviewed = '❌'  # Assume not reviewed unless specifically marked
            char_count = '~300'  # Placeholder, could be updated later
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
    print("Fixing completion count based on actual files...")
    
    # Show current state
    completed_ids = get_completed_abilities_from_files()
    print(f"\nActual completed abilities: {len(completed_ids)}")
    print("Sample completed IDs:", sorted(list(completed_ids))[:10])
    
    # Generate corrected content
    content = generate_corrected_progress()
    
    # Backup the original file
    progress_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/extended_ability_descriptions/progress.md"
    backup_path = progress_path + ".backup2"
    
    # Create backup
    with open(progress_path, 'r') as f:
        original_content = f.read()
    
    with open(backup_path, 'w') as f:
        f.write(original_content)
    
    print(f"Backup created: {backup_path}")
    
    # Write the corrected content
    with open(progress_path, 'w') as f:
        f.write(content)
    
    print(f"Fixed progress.md - now shows {len(completed_ids)} completed abilities")

if __name__ == "__main__":
    main()