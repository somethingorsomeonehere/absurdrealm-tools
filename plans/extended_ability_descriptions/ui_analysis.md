# Extended Ability Description UI Analysis

Based on screenshots analyzed on [current date].

## UI Flow

1. **Main Ability Screen** - Shows Pokemon's 4 abilities with short descriptions
2. **Press A** - Header changes to "More Info (A)"  
3. **Press A Again** - Opens extended description popup

## Extended Description Display Constraints

### Text Area Dimensions
- **Total visible lines**: 14 (including blank lines)
- **Recommended blank lines**: 3 (for readability)
- **Usable text lines**: 11
- **Characters per line**: 30 (GBA UI physical limit)
- **Absolute character ceiling**: 330 (11 × 30)
- **Practical target**: 280-300 characters total (to account for word-wrap)

### Observed Examples

#### Drought (Short Extended)
```
Moves inflict burn 5x as often.
```
- Only 1 line used
- Plenty of empty space below

#### Blaze (Multi-line Extended)
```
Boosts Fire-type moves by 1.2x or
1.5x when under 1/3 HP. 50% is an
ability activated chance. Fire
type starter Pokemon like
charmander.
```
- 5 lines used
- Shows automatic text wrapping
- ~32-35 characters per line

## Key Findings

1. **Automatic text wrapping** - No manual line breaks needed
2. **Generous space** - Can fit detailed explanations (5+ lines)
3. **Same width as main screen** - Consistent with normal ability descriptions
4. **Clean presentation** - White text on gray background
5. **Navigation** - Can scroll between abilities while in extended view

## Recommendations for Extended Descriptions

- **Target length**: 280-300 characters total (INCLUDING spaces - GBA hardware requirement)
- **Line usage**: 9-11 lines of text (leaving 3 blank for readability)
- **Style**: Complete sentences, detailed mechanics, but more concise than originally planned
- **No manual formatting** - Let codegen handle wrapping
- **Key constraint**: Must fit within GBA UI's physical display limits (spaces count as tiles)
- **CRITICAL**: Character counting MUST include spaces - GBA renders each space as a fixed 8×8 tile

## Character Counting Requirements

### Why Spaces Must Be Counted
The Game Boy Advance renders text using a fixed 8×8 tile grid system:
- **Every character** (letter, number, punctuation, space) occupies one tile
- **Spaces are visible tiles** - they consume screen real estate
- **30 characters per line** means 30 tiles, regardless of content
- **Text overflow** occurs if too many tiles are used, not too many "letters"

### Historical Issue
Many existing ability files have incorrect character counts that exclude spaces:
- Example: Simple ability shows "Character count: 299" but is actually 324 with spaces
- This causes overflow on real GBA hardware
- **Solution**: Use the recount script to fix all existing files

### Validation Formula
```
safe_char_limit = (visible_lines - blank_lines) × max_cols
                = (14 - 3) × 30  
                = 330 tiles maximum (aim for ≤300)
```

## Notes
- The UI is already fully implemented and working
- Pressing A twice from ability screen opens extended descriptions
- Can navigate between abilities while viewing extended descriptions
- Title bar shows current ability name