---
id: 259
name: Quick Draw
status: reviewed
character_count: 152
---

# Quick Draw - Ability ID 259

## In-Game Description
"30% chance to move first."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Quick Draw gives a 30% chance for the user to act first in their priority bracket. Stacks multiplicatively with Quick Claw for a 44% chance to activate.  

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Activation Rate**: Exactly 30% chance each turn
- **Priority System**: When activated, sets `quickDraw` flag in round structure
- **Turn Order Calculation**: Adds to `speedValue.goesFirst` along with Quick Claw effects
- **Battle Script**: Uses `BattleScript_QuickDrawActivation` with ability popup display

### Implementation Details
- **Random Check**: `(Random() % 100) < 30` - checked once per turn during `SetActionsAndBattlersTurnOrder()`
- **Priority Stacking**: Can stack with Quick Claw/Custap Berry effects (both flags contribute to `goesFirst`)
- **Turn Order**: Processed after regular priority but before Speed calculations
- **Activation Display**: Shows ability popup and battle message when triggered

### Interactions
- **Status Conditions**: Does not activate if the Pokemon is asleep or has no valid moves
- **Move Restrictions**: Works with any move the Pokemon can use
- **Turn Priority**: Independent of move priority - can make negative priority moves go first
- **Speed Stats**: Completely bypasses Speed comparison when activated

### Comparison to Similar Effects
- **Quick Claw**: Same priority level but item-based with different activation rates
- **Custap Berry**: Same priority system but consumable and requires low HP
- **Prankster**: Different - gives +1 priority to status moves only
- **Gale Wings**: Different - gives +1 priority to Flying-type moves only

### Strategic Usage
- Excellent for slow, powerful Pokemon that want to move first occasionally
- Particularly effective on Pokemon with strong but negative priority moves
- Provides unpredictable speed control that opponents cannot reliably counter
- Most valuable on Pokemon that would otherwise never outspeed opponents

### Notable Differences from Official Games
This implementation follows the standard Quick Draw mechanics from Generation VIII, maintaining the 30% activation rate and priority boost system exactly as intended.