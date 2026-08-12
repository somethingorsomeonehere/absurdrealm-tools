---
id: 54
name: Truant
status: reviewed
character_count: 147
---

# Truant - Ability ID 54

## In-Game Description
"Can't use attacking moves twice in a row."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents consecutive attacking moves. After using an attack, the user must loaf around next turn and cannot attack. Status moves remain unaffected. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**TRUANT** is a severely detrimental ability that enforces a mandatory rest period after using any attacking move.

### Activation Mechanics:
- **Trigger**: onEndTurn hook tracks move usage
- **State Tracking**: Uses ability state system to remember if Pokemon attacked last turn
- **Move Classification**: Only affects physical and special moves (not status moves)
- **Script**: Shows "Pokemon is loafing around!" message when forced to rest

### Core Mechanics:
1. **Move Restriction**:
   - After using any physical or special move, ability state is set to TRUE
   - On turns when ability state is TRUE, attacking moves are blocked
   - Status moves (SPLIT_STATUS) are never blocked and can be used freely
   
2. **State Management**:
   - Ability state resets to FALSE after a loafing turn
   - If no attacking move was used, state remains FALSE
   - State persists through switches and other effects

### Move Categories:
- **Blocked Moves**: All physical and special attacks
- **Allowed Moves**: Status moves (Protect, Toxic, Thunder Wave, etc.)
- **Special Cases**: Moves like Transform and Sketch follow normal status move rules

### Battle Flow:
1. **Turn 1**: Pokemon uses attacking move to Ability state set to TRUE
2. **Turn 2**: Pokemon tries to use attacking move to Blocked by Truant to Forced to loaf
3. **Turn 3**: Ability state reset to FALSE to Can use attacking moves again
4. **Repeat**: Cycle continues indefinitely

### Technical Implementation:
```c
constexpr Ability Truant = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        if (GetAbilityState(battler, ability))
            SetAbilityState(battler, ability, FALSE);
        else if (gChosenMoveByBattler[battler] && !IS_MOVE_STATUS(gChosenMoveByBattler[battler]))
            SetAbilityState(battler, ability, TRUE);
        return FALSE;
    },
};
```

### Battle System Integration:
- **Attack Cancellation**: Processed in CANCELLER_TRUANT phase
- **Message Display**: Uses B_MSG_LOAFING string ID
- **Move Result**: Treated as MOVE_RESULT_MISSED for battle flow
- **Multiturn Moves**: Cancelled when Truant activates

### Interaction Rules:
- **Skill Swap/Role Play**: Truant can be transferred to opponents as a strategy
- **Entrainment**: Truant is banned from Entrainment (cannot be forced onto others)
- **Simple Beam**: Truant is banned from Simple Beam replacement
- **Recharge Moves**: Truant users get penalized AI scoring for recharge moves like Hyper Beam

### AI Behavior:
- **Move Selection**: AI heavily penalizes attacking moves when Truant state is active (-20 score)
- **Skill Swap Usage**: AI will try to Skill Swap Truant onto opponents (+5 score)
- **Recharge Considerations**: AI avoids recharge moves more on Truant users
- **Status Strategy**: AI prioritizes status moves on predicted loafing turns

### Competitive Implications:
**Severe Drawbacks:**
- Cuts effective attacking frequency in half
- Provides opponent with guaranteed setup opportunities
- Makes sweeping impossible due to forced breaks
- Severely limits late-game pressure

**Niche Applications:**
- **Doubles Strategy**: Transfer via Skill Swap to cripple opponents
- **Stall Teams**: Use status moves during forced rest turns
- **Choice Item Synergy**: Somewhat mitigates Choice lock by forcing switches anyway

### Synergies and Counters:
**Synergistic Strategies:**
- Status moves (Toxic, Will-O-Wisp, Thunder Wave)
- Protect/Detect to waste opponent's turns
- Entrainment to spread to entire team (if not banned)

**Counters to Truant:**
- Taunt prevents status move usage during loafing
- Setup moves during guaranteed loafing turns
- Switching to maintain offensive pressure

### Version History:
- **Gen 3**: Introduced on Slakoth line
- **Elite Redux**: Mechanics unchanged from standard implementation
- **Competitive**: Considered one of the worst abilities in the game