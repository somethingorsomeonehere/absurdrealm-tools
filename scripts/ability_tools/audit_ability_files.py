#!/usr/bin/env python3
"""
Audit all individual ability files for wrong IDs
Cross-references with correct mapping from AbilityEnum.proto
"""

import os
import re
import glob

def load_correct_mapping():
    """Load the correct ability mapping"""
    mapping_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/scripts/ability_tools/ability_id_mapping.txt"
    
    id_to_name = {}
    name_to_id = {}
    
    with open(mapping_path, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                parts = line.strip().split(' | ')
                if len(parts) == 2:
                    ability_id = int(parts[0].strip())
                    ability_name = parts[1].strip().replace('ABILITY_', '')
                    id_to_name[ability_id] = ability_name
                    name_to_id[ability_name] = ability_id
    
    return id_to_name, name_to_id

def audit_individual_files():
    """Audit all individual ability files"""
    abilities_dir = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities"
    
    # Get all ability files (excluding README)
    pattern = os.path.join(abilities_dir, "*_*.md")
    ability_files = glob.glob(pattern)
    
    id_to_name, name_to_id = load_correct_mapping()
    
    issues = []
    correct_files = []
    
    for file_path in ability_files:
        filename = os.path.basename(file_path)
        
        # Skip non-ability files
        if filename == "README.md":
            continue
            
        # Extract ID and name from filename
        match = re.match(r'(\d+)_(.+)\.md$', filename)
        if not match:
            issues.append({
                'file': filename,
                'type': 'filename_format',
                'issue': 'Filename does not match expected format: {id}_{name}.md'
            })
            continue
            
        file_id = int(match.group(1))
        file_name = match.group(2).upper()
        
        # Read file content to get the header ID
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Look for "Ability ID" in the content
            id_match = re.search(r'Ability ID[:\s]+(\d+)', content, re.IGNORECASE)
            content_id = int(id_match.group(1)) if id_match else None
            
        except Exception as e:
            issues.append({
                'file': filename,
                'type': 'read_error',
                'issue': f'Could not read file: {e}'
            })
            continue
        
        # Check if the ID in filename matches the correct mapping
        correct_id = name_to_id.get(file_name)
        
        if correct_id is None:
            issues.append({
                'file': filename,
                'type': 'unknown_ability',
                'issue': f'Ability name "{file_name}" not found in mapping'
            })
            continue
            
        # Check for mismatches
        has_issue = False
        
        if file_id != correct_id:
            issues.append({
                'file': filename,
                'type': 'wrong_filename_id',
                'issue': f'Filename ID {file_id} should be {correct_id}',
                'correct_filename': f'{correct_id}_{file_name.lower()}.md'
            })
            has_issue = True
            
        if content_id and content_id != correct_id:
            issues.append({
                'file': filename,
                'type': 'wrong_content_id',
                'issue': f'Content ID {content_id} should be {correct_id}'
            })
            has_issue = True
            
        if not has_issue:
            correct_files.append(filename)
    
    return issues, correct_files

def main():
    print("Auditing individual ability files...")
    
    issues, correct_files = audit_individual_files()
    
    print(f"\nAudit Results:")
    print(f"  Correct files: {len(correct_files)}")
    print(f"  Files with issues: {len(issues)}")
    
    if correct_files:
        print(f"\nCorrect files ({len(correct_files)}):")
        for filename in sorted(correct_files):
            print(f"  ✅ {filename}")
    
    if issues:
        print(f"\nIssues found ({len(issues)}):")
        for issue in issues:
            print(f"  ❌ {issue['file']}: {issue['issue']}")
            if 'correct_filename' in issue:
                print(f"     Should be: {issue['correct_filename']}")
    
    # Group issues by type
    issue_types = {}
    for issue in issues:
        issue_type = issue['type']
        if issue_type not in issue_types:
            issue_types[issue_type] = []
        issue_types[issue_type].append(issue)
    
    print(f"\nIssues by type:")
    for issue_type, type_issues in issue_types.items():
        print(f"  {issue_type}: {len(type_issues)} files")
    
    # Save detailed report
    report_path = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/scripts/ability_tools/audit_report.txt"
    with open(report_path, 'w') as f:
        f.write("# Ability Files Audit Report\n\n")
        f.write(f"Total files audited: {len(correct_files) + len(issues)}\n")
        f.write(f"Correct files: {len(correct_files)}\n")
        f.write(f"Files with issues: {len(issues)}\n\n")
        
        if issues:
            f.write("## Issues Found\n\n")
            for issue in issues:
                f.write(f"**{issue['file']}**\n")
                f.write(f"- Type: {issue['type']}\n")
                f.write(f"- Issue: {issue['issue']}\n")
                if 'correct_filename' in issue:
                    f.write(f"- Correct filename: {issue['correct_filename']}\n")
                f.write("\n")
        
        if correct_files:
            f.write("## Correct Files\n\n")
            for filename in sorted(correct_files):
                f.write(f"- {filename}\n")
    
    print(f"\nDetailed report saved to: {report_path}")
    
    return issues, correct_files

if __name__ == "__main__":
    main()