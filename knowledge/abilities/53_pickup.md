---
id: 53
name: Pickup
status: reviewed
character_count: 139
---

# Pickup - Ability ID 53

## In-Game Description
"Removes all hazards on entry. Not immune to hazards."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Clears all entry hazards from your side of the field when entering battle. The Pokemon is still susceptible to hazards while clearing them.

## Detailed Mechanical Explanation
*For Discord/reference use*

**PICKUP** is a hazard-clearing ability that removes all entry hazards from the user's side of the field upon switch-in, though it does not provide immunity to the hazards themselves.

### Activation Mechanics:
- **Trigger**: Immediately upon entering battle (onEntry hook)
- **Timing**: Activates after taking hazard damage (no immunity)
- **Scope**: Clears all hazards on user's side only
- **Script**: Displays "{Pokemon} removed hazards on its field side!"

### Hazards Cleared:
1. **Standard Hazards**:
   - Spikes (all layers, 1-3 stacks)
   - Toxic Spikes (all layers, 1-2 stacks)
   - Stealth Rock (single layer)
   - Sticky Web (single layer)

2. **Elite Redux Custom Hazards**:
   - Hot Coals (burns entering Pokemon)
   - Caltrops (damages entering Pokemon)

### Important Limitations:
- **No Immunity**: Pickup does NOT prevent hazard damage on entry
- **Takes Damage First**: The Pokemon suffers full hazard effects before clearing them
- **Side-Specific**: Only clears hazards on the user's side of the field
- **No Protection**: Does not prevent future hazard setting

### Technical Implementation:
```c
constexpr Ability Pickup = {
    .onEntry = +[](ON_ENTRY) -> int {
        int side = GetBattlerSide(battler);
        CHECK(gSideStatuses[side] & SIDE_STATUS_HAZARDS_ANY || gSideTimers[side].hotCoals || gSideTimers[side].caltrops)

        gSideStatuses[side] &= ~(SIDE_STATUS_STEALTH_ROCK | SIDE_STATUS_TOXIC_SPIKES | SIDE_STATUS_SPIKES | SIDE_STATUS_STICKY_WEB);
        gSideTimers[side].spikesAmount = 0;
        gSideTimers[side].toxicSpikesAmount = 0;
        gSideTimers[side].hotCoals = FALSE;
        gSideTimers[side].caltrops = FALSE;
        BattleScriptPushCursorAndCallback(BattleScript_PickUpActivate);
        return TRUE;
    },
};
```

### Hazard Damage Sequence:
1. Pokemon enters battle
2. Takes damage from all active hazards (Spikes, Stealth Rock, etc.)
3. Pickup ability activates
4. All hazards on user's side are cleared
5. Message displays: "{Pokemon} removed hazards on its field side!"

### Strategic Implications:
- **Hazard Control**: Excellent for teams vulnerable to hazard stacking
- **Entry Support**: Useful for frail sweepers that need clean entry
- **Limited Value**: Less useful against single-use hazards like Stealth Rock
- **Suicidal Risk**: May KO itself to hazards before clearing them

### Competitive Usage:
- **Hazard-Weak Teams**: Essential for teams with multiple hazard-weak Pokemon
- **Pivot Role**: Can be used to clear hazards before bringing in key team members
- **Risk Management**: Must consider if the Pokemon can survive initial hazard damage
- **Limited Scope**: Doesn't help against opponent's hazards or provide ongoing protection

### Synergies:
- **Heavy-Duty Boots**: Prevents hazard damage while still clearing them
- **Focus Sash**: Ensures survival to clear hazards even with chip damage
- **Healing Moves**: Can recover from hazard damage after clearing

### Counters:
- **Immediate Re-hazarding**: Opponents can immediately reset hazards after Pickup activation
- **Multi-hazard Stacking**: Heavy hazard damage may KO before clearing
- **Priority Moves**: Can finish off weakened Pickup users

### Version History:
- Elite Redux: Expanded to include custom hazards (Hot Coals, Caltrops)
- Original: Cleared standard entry hazards only
- Note: This is a complete rework from the original Pickup ability which collected items