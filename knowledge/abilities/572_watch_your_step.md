---
id: 572
name: Watch Your Step
status: reviewed
character_count: 181
---

# Watch Your Step - Ability ID 572

## In-Game Description
"Spreads two layers of Spikes on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon switching in, sets up two layers of Spikes on the opponent's field. Each layer damages switching grounded Pokemon by 12.5%, 16.7%, or 25% of max HP for 1-3 layers respectively.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Watch Your Step** is a switch-in ability that automatically spreads two layers of Spikes on the opponent's side of the field when the Pokemon enters battle.

### Core Mechanics
- **Activation**: Triggers automatically when the Pokemon switches into battle
- **Effect**: Adds 2 layers of Spikes to the opponent's side of the field
- **Maximum Layers**: Cannot exceed 3 total layers of Spikes
- **Stacking**: If opponent already has 1 layer, adds 1 more (capping at 3)
- **Blockable**: Does not activate if opponent already has 3 layers of Spikes

### Spikes Damage Formula
```c
u8 spikesDmg = (5 - spikesAmount) * 2;
damage = maxHP / spikesDmg;
```

**Damage per layer:**
- 1 layer: 1/8 HP damage (12.5%)
- 2 layers: 1/6 HP damage (~16.7%)
- 3 layers: 1/4 HP damage (25%)

### Technical Implementation
```c
constexpr Ability WatchYourStep = {
    .onEntry = +[](ON_ENTRY) -> int {
        u8 targetSide = GetOppositeSide(battler);
        CHECK(gSideTimers[targetSide].spikesAmount < 3)
        
        gSideTimers[targetSide].spikesAmount = min(gSideTimers[targetSide].spikesAmount + 2, 3);
        gSideStatuses[targetSide] |= SIDE_STATUS_SPIKES;
        BattleScriptPushCursorAndCallback(BattleScript_DoubleSpikesOnEntry);
        return TRUE;
    },
};
```

### Affected Conditions
- **Grounded Pokemon**: Only affects Pokemon that make contact with the ground
- **Immune**: Flying-types, Levitate users, Air Balloon holders, Magnet Rise users
- **Magic Guard**: Pokemon with Magic Guard are immune to Spikes damage
- **Removal**: Cleared by Defog, Rapid Spin, Court Change, or switching abilities like Pickup

### Interactions with Other Abilities/Mechanics
- **Multiple Layers**: Combines with existing Spikes layers up to maximum of 3
- **Entry Hazards**: Works alongside Stealth Rock, Toxic Spikes, and Sticky Web
- **Defog/Rapid Spin**: Can be cleared by these moves
- **Court Change**: Spikes can be swapped to the user's side
- **Magic Bounce**: Does not interact with Magic Bounce (not a targeted move)

### Strategic Implications
- **Immediate Pressure**: Forces opponent to take damage on every switch-in
- **Pivot Punishment**: Heavily punishes switching strategies
- **Hazard Stacking**: Excellent for hazard-heavy teams
- **Entry Control**: Discourages frequent switching by opponent

### Example Damage Calculations
For a 300 HP Pokemon:
- **After Watch Your Step**: 2 layers = 300 ÷ 6 = 50 HP damage per switch-in
- **With 1 existing layer**: 3 layers = 300 ÷ 4 = 75 HP damage per switch-in
- **No existing layers**: 2 layers = 300 ÷ 6 = 50 HP damage per switch-in

### Common Users
- **Mega Garbodor**: Has Watch Your Step as an innate ability
- **Iron Treads**: Can have Watch Your Step as a regular ability option
- **Defensive Pokemon**: Typically found on bulky Pokemon that can afford to set hazards

### Competitive Usage Notes
- **Lead Potential**: Excellent for lead Pokemon to establish immediate field control
- **Defensive Cores**: Fits well in defensive teams that focus on hazard stacking
- **Switchin Punishment**: Heavily punishes opponents who rely on frequent switching
- **Hazard Support**: Reduces need for manual Spikes setting

### Counters
- **Hazard Removal**: Defog, Rapid Spin, Tidy Up users
- **Flying Types**: Immune to Spikes damage
- **Levitate**: Immunity to ground-based hazards
- **Magic Guard**: Prevents indirect damage
- **Heavy-Duty Boots**: Item that prevents hazard damage

### Synergies
- **Stealth Rock**: Combines for massive switch-in pressure
- **Toxic Spikes**: Creates a hazard-heavy field
- **Trapping Abilities**: Shadow Tag, Arena Trap force opponents to take damage
- **Pursuit**: Punishes switching attempts further
- **Sticky Web**: Adds Speed reduction to the hazard stack

### Version History
- **Elite Redux**: Introduced as ID 572
- **Current Status**: Active ability in the current meta
- **Rarity**: Uncommon ability, found on select defensive Pokemon