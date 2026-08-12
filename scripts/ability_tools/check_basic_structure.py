#!/usr/bin/env python3
"""
List files that don't have the basic expected structure:
1. Frontmatter
2. # AbilityName - Ability ID XX  
3. ## In-Game Description
4. ## Extended In-Game Description
"""

import re
from pathlib import Path

def has_correct_basic_structure(file_path):
    """Check if file has correct structure until Extended Description."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find the main sections (lines starting with #)
    sections = []
    for i, line in enumerate(lines):
        if line.startswith('#') and not line.startswith('---'):
            sections.append(line.strip())
    
    if len(sections) < 3:
        return False
    
    # Check section 1: # AbilityName - Ability ID XX
    if not re.match(r'^# .+ - Ability ID \d+$', sections[0]):
        return False
    
    # Check section 2: ## In-Game Description
    if sections[1] != "## In-Game Description":
        return False
    
    # Check section 3: ## Extended In-Game Description
    if sections[2] != "## Extended In-Game Description":
        return False
    
    return True

def main():
    abilities_dir = Path(__file__).parent.parent.parent / "knowledge" / "abilities"
    ability_files = list(abilities_dir.glob("[0-9]*_*.md"))
    ability_files.sort()
    
    problem_files = []
    
    for file_path in ability_files:
        if not has_correct_basic_structure(file_path):
            problem_files.append(file_path.name)
    
    # Generate simple list
    output_file = abilities_dir / "REVIEW_STRUCTURE.md"
    with open(output_file, 'w') as f:
        f.write("# Files to Review - Wrong Basic Structure\n\n")
        f.write(f"**Total: {len(problem_files)} files**\n\n")
        f.write("Expected structure:\n")
        f.write("1. `# AbilityName - Ability ID XX`\n")
        f.write("2. `## In-Game Description`\n") 
        f.write("3. `## Extended In-Game Description`\n\n")
        f.write("## Files to Fix\n\n")
        
        for filename in problem_files:
            f.write(f"- [ ] {filename}\n")
    
    print(f"Generated: {output_file}")
    print(f"Found {len(problem_files)} files with wrong basic structure")

if __name__ == "__main__":
    main()