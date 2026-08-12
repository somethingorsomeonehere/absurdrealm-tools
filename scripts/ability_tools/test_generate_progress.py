#!/usr/bin/env python3
"""
Test script for generate_progress.py
Creates a test ability file with frontmatter and runs the generator
"""

import os
import tempfile
import shutil
from pathlib import Path

# Test frontmatter content
test_ability_content = """---
id: 999
name: Test Ability
status: reviewed
character_count: 295
reviewer: test_user
review_date: 2025-01-14
---

# Test Ability

**Ability ID**: 999
**Type**: Regular Ability

**In-Game Description**: "This is a test ability for testing frontmatter."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max INCLUDING spaces)*

Test ability that demonstrates frontmatter functionality. This extended description is exactly 295 characters long to test the character counting feature. It includes all the necessary information about how this fictional ability would work in the game, providing strategic value.

*Character count: 295*

## Detailed Mechanical Explanation
This is just a test file to verify frontmatter parsing works correctly.
"""

def main():
    # Get the abilities directory
    abilities_dir = Path(__file__).parent.parent.parent / "knowledge" / "abilities"
    test_file = abilities_dir / "999_test_ability.md"
    
    try:
        # Create test file
        print("Creating test ability file with frontmatter...")
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_ability_content)
        print(f"✅ Created: {test_file}")
        
        # Run generate_progress.py
        print("\nRunning generate_progress.py...")
        import subprocess
        result = subprocess.run(
            ['python3', 'generate_progress.py'],
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ generate_progress.py ran successfully!")
            print(result.stdout)
        else:
            print("❌ Error running generate_progress.py:")
            print(result.stderr)
        
        # Check if test ability appears in progress.md
        progress_file = abilities_dir.parent / "extended_ability_descriptions" / "progress.md"
        if progress_file.exists():
            with open(progress_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if "999" in content and "Test Ability" in content:
                    print("\n✅ Test ability found in progress.md!")
                    # Find and print the line
                    for line in content.split('\n'):
                        if "999" in line:
                            print(f"   {line}")
                else:
                    print("\n❌ Test ability not found in progress.md")
        
    finally:
        # Clean up test file
        if test_file.exists():
            os.remove(test_file)
            print(f"\n🧹 Cleaned up test file: {test_file}")

if __name__ == "__main__":
    main()