---
id: 566
name: Cud Chew
status: reviewed
character_count: 81
---

# Cud Chew - Ability ID 566

## In-Game Description
"Eats berries again at the end of the next turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When consuming a berry, the user re-consumes it at the end of the following turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

Cud Chew is a complex berry re-consumption ability that operates through a sophisticated state management system:

### Core Mechanics
- **Berry Storage**: When a Pokemon with Cud Chew consumes any berry naturally, the ability stores the berry's ID
- **Turn Delay**: The stored berry is re-consumed at the end of the **next** turn (not the same turn)
- **Single Berry Limit**: Only one berry can be stored at a time; consuming additional berries overwrites the stored one
- **Natural Consumption Only**: Only works with berries consumed through normal battle mechanics (HP triggers, status healing, etc.)

### Technical Implementation
The ability uses a `CudChewState` structure with three key fields:
```c
typedef struct {
    u16 itemId;           // Stores the berry ID to re-consume
    bool8 setThisTurn:1;  // Tracks if berry was consumed this turn
    bool8 activating:1;   // Tracks if ability is currently re-consuming
} CudChewState;
```

### Turn-Based State System
1. **Berry Consumption Turn**: When a berry is consumed, `SetCudChew()` is called:
   - Sets `itemId` to the consumed berry
   - Sets `setThisTurn = TRUE`

2. **End of Same Turn**: The `onEndTurn` handler processes `setThisTurn`:
   - Clears `setThisTurn` flag
   - Keeps `itemId` stored for next turn

3. **End of Next Turn**: The `onEndTurn` handler processes stored `itemId`:
   - Temporarily restores the berry to the Pokemon's item slot
   - Sets `activating = TRUE` to prevent infinite loops
   - Calls `BattleScript_CudChew` to trigger consumption
   - Uses `sBERRY_OVERRIDE = TRUE` to bypass normal berry requirements

### Berry Interaction Details
- **Pocket Verification**: Only works with items from `POCKET_BERRIES`
- **Ate Berry Tracking**: Uses `gBattleStruct->ateBerry` to verify natural consumption
- **Override System**: Uses `sBERRY_OVERRIDE` to force berry consumption regardless of current HP/status
- **Item Restoration**: Uses `gBattleStruct->changedItems` to restore original item state after consumption

### Competitive Applications
- **Pinch Berry Synergy**: Excellent with Sitrus Berry, Figy Berry family for repeated healing
- **Status Berry Utility**: Works with Lum Berry, Pecha Berry for repeated status cure
- **Damage Berry Stacking**: Can re-trigger Jaboca/Rowap Berries for additional damage
- **Setup Berry Support**: Re-consumes stat-boosting berries like Salac or Petaya Berry
- **Defensive Consistency**: Provides reliable secondary healing/utility one turn later

### Strategic Considerations
- **Timing Awareness**: One-turn delay means planning around opponent's moves
- **Berry Management**: Choose berries that provide maximum value when consumed twice
- **Team Synergy**: Works well with Harvest ability for potential three-time berry usage
- **Prediction Value**: Opponents must account for delayed berry effects in their planning