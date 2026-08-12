---
id: 787
name: Cryo Architect
status: reviewed
character_count: 236
---

# Cryo Architect - Ability ID 787

## In-Game Description
"Boosts Attack and Def when hit by Water or Ice."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by a Water-type attack, raises the user's Attack by one stage, and Defense by one stage on the turn after. If it's hit by an Ice-type attack, it will raise both in the first turn. each. Activates on each hit of a multihit move. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Cryo Architect is a sophisticated defensive ability that converts incoming Water and Ice-type damage into stat boosts, utilizing different timing mechanisms for each type:

### Water-Type Interactions
- **Immediate Effect**: Raises Attack by 1 stage when hit
- **Delayed Effect**: Sets an ability state flag that triggers Defense +1 at the end of the turn
- **Technical Implementation**: Uses bit manipulation in ability state to track the delayed boost

### Ice-Type Interactions  
- **Immediate Effect**: Raises both Attack and Defense by 1 stage when hit
- **No Delayed Effect**: All boosts happen immediately upon being hit

### Strategic Applications
1. **Defensive Pivot**: Transforms defensive Pokemon into offensive threats when opponents use Water/Ice moves
2. **Baiting Strategy**: Encourages opponents to use these common attacking types
3. **Type Synergy**: Particularly powerful on Ice-types that resist Ice moves, creating a safe activation condition
4. **Stall Disruption**: Forces opponents to reconsider using Water moves for chip damage

### Technical Details
- **Activation Condition**: Must be hit by a damaging Water or Ice-type move (checked via `ShouldApplyOnHitAffect`)
- **Stat Caps**: Respects maximum stat stage limits (+6), won't activate if already at cap
- **Timing**: Water moves trigger dual-phase boosts (immediate Attack, delayed Defense), Ice moves trigger immediate dual boosts
- **Battle Scripts**: Uses `BattleScript_TargetAbilityStatRaiseOnMoveEnd` for immediate boosts and `BattleScript_AttackerAbilityStatRaiseEnd3` for end-turn boosts

### Distribution Analysis
Based on code analysis, this ability appears on defensive Ice-types, creating an interesting risk-reward dynamic where using Ice or Water moves against these Pokemon strengthens them significantly. This makes Cryo Architect users particularly threatening in environments where Water and Ice moves are common.

The dual-timing mechanism (immediate vs end-turn) adds strategic depth, as the Water-type interaction creates a delayed threat that opponents must account for in their turn planning.