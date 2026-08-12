# CLAUDE.md - Abilities Documentation

Rules and learnings for systematic quality improvement of Elite Redux ability documentation files.

## Current Task: Structure Standardization

Fixing 294 files to have EXACT structure compliance. No variations allowed.

### Required File Structure (EXACT ORDER)
1. **Frontmatter** (YAML header)
2. `# {Ability Name} - Ability ID {id}` 
3. `## In-Game Description` - Short game description
4. `## Extended In-Game Description` - UI description (280-300 chars)
5. `## Detailed Mechanical Explanation` - ALL other content goes here

### Required Frontmatter
```yaml
---
id: 6
name: Damp
status: ai-generated|human-reviewed|verified
character_count: 294
---
```

**CRITICAL**: `name` field = ability name ONLY (no "- Ability #93" suffix)

## Fixing Rules

### Content Preservation
- **NEVER remove useful content** - only move it to correct location
- **NEVER delete sections** - move wrong sections under "Detailed Mechanical Explanation"
- **NEVER delete the meta-comment line**: `*For use in Elite Redux extended ability UI (280-300 chars max)*` must be preserved
- All technical details, Pokemon lists, code examples, etc. must be preserved

### Wrong Section Names to Fix
Remove these and move content under "Detailed Mechanical Explanation":
- "Overview", "Basic Information", "Summary", "Short Description"
- "Current Description", "Mechanics", "Implementation"
- "Current Implementation", "Core Mechanics", "Analysis"

### Character Counting
- **ALWAYS count WITH spaces** - GBA renders spaces as tiles
- Extended descriptions: **280-300 characters INCLUDING spaces**
- Use `echo "text" | wc -c` for accurate count
- Update frontmatter `character_count` field to match actual count
- Remove duplicate `**Character count: XXX**` lines from content body

### Header Format Fixes
- Wrong: `# Ability Name (Ability ID: 123)` or `# Ability Name (Ability #123)`
- Correct: `# Ability Name - Ability ID 123`

### Elite Redux Context
- **NEVER assume vanilla Pokemon mechanics** - abilities are completely reworked
- Extended descriptions must be 100% accurate to Elite Redux implementation
- Weather/terrain durations are 8 turns (not vanilla's 5)

## Progress Tracking

**Current Status**: 26/294 files completed (9%)
**Files Fixed**: 100_stall, 101_technician, 117_snow_warning, 121_multitype, 122_flower_gift, 123_bad_dreams, 124_pickpocket, 127_unnerve, 128_defiant, 129_defeatist, 130_cursed_body, 147_wonder_skin, 161_zen_mode, 162_victory_star, 163_turboblaze, 164_teravolt, 165_aroma_veil, 166_flower_veil, 168_protean, 169_fur_coat, 170_magician, 178_mega_launcher, 183_gooey, 185_parental_bond, 186_dark_aura, 187_fairy_aura

**Remaining**: 267 files in `REVIEW_STRUCTURE.md`

## Quality Check Commands

```bash
# Count characters in extended description
echo "description text here" | wc -c

# Check current progress
grep -l "Ability ID" eliteredux-darky/knowledge/abilities/*.md | wc -l
```

## Reference Template

```markdown
---
id: 123
name: Ability Name
status: ai-generated
character_count: 285
---

# Ability Name - Ability ID 123

## In-Game Description
"Short description from game."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Extended description here (280-300 characters including spaces).

## Detailed Mechanical Explanation

All other content goes here - implementation details, Pokemon lists, code examples, strategic analysis, etc.
```