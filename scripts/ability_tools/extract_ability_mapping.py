#!/usr/bin/env python3
"""
Extract complete ability mapping from proto/AbilityEnum.proto
Creates master mapping of ID -> Name for ability ID correction project
"""

import re
import os

def extract_abilities_from_proto():
    """Extract all ability mappings from AbilityEnum.proto"""
    proto_path = "/Users/joel/Github/eliteredux/eliteredux-source/proto/AbilityEnum.proto"
    
    abilities = {}
    
    with open(proto_path, 'r') as f:
        content = f.read()
    
    # Find all ability definitions using regex
    # Pattern: ABILITY_NAME = NUMBER;
    pattern = r'ABILITY_([A-Z_]+)\s*=\s*(\d+);'
    matches = re.findall(pattern, content)
    
    for ability_name, ability_id in matches:
        abilities[int(ability_id)] = ability_name
    
    return abilities

def save_mapping(abilities):
    """Save the mapping to a file for reference"""
    output_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/scripts/ability_tools/ability_id_mapping.txt"
    
    with open(output_path, 'w') as f:
        f.write("# Complete Ability ID Mapping from proto/AbilityEnum.proto\n")
        f.write(f"# Total abilities: {len(abilities)}\n\n")
        
        for ability_id in sorted(abilities.keys()):
            ability_name = abilities[ability_id]
            f.write(f"{ability_id:3d} | ABILITY_{ability_name}\n")
    
    return output_path

def main():
    print("Extracting ability mappings from proto/AbilityEnum.proto...")
    
    abilities = extract_abilities_from_proto()
    
    print(f"Found {len(abilities)} abilities")
    print(f"ID range: {min(abilities.keys())} to {max(abilities.keys())}")
    
    # Save to file
    output_path = save_mapping(abilities)
    print(f"Mapping saved to: {output_path}")
    
    # Show first few for verification
    print("\nFirst 10 abilities:")
    for ability_id in sorted(abilities.keys())[:10]:
        ability_name = abilities[ability_id]
        print(f"  {ability_id:3d} | ABILITY_{ability_name}")
    
    # Check specific problematic ones
    print("\nKey abilities to verify:")
    test_abilities = ['DRIZZLE', 'SPEED_BOOST', 'INTIMIDATE', 'INSOMNIA']
    for test_name in test_abilities:
        for ability_id, ability_name in abilities.items():
            if ability_name == test_name:
                print(f"  {ability_id:3d} | ABILITY_{ability_name}")
                break
    
    return abilities

if __name__ == "__main__":
    main()