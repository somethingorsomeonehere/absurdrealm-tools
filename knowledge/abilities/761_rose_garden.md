---
id: 761
name: Rose Garden
status: reviewed
character_count: 152
---

# Rose Garden - Ability ID 761

## In-Game Description
"Spreads two layers of Toxic Spikes on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Spreads two layers of Toxic Spikes on the opponent's side on entry. Any non-Poison or Steel-type grounded enemy that switches in will be badly poisoned.

## Detailed Mechanical Explanation
*For Discord/reference use*

Rose Garden is an entry hazard ability that automatically sets two layers of Toxic Spikes on the opponent's side of the field when the Pokemon with this ability enters battle.

### Core Mechanics
```cpp
constexpr Ability RoseGarden = {
    .onEntry = +[](ON_ENTRY) -> int {
        u8 targetSide = GetOppositeSide(battler);
        CHECK(gSideTimers[targetSide].toxicSpikesAmount < 2)

        gSideTimers[targetSide].toxicSpikesAmount = 2;
        gSideStatuses[targetSide] |= SIDE_STATUS_TOXIC_SPIKES;
        gBattlerTarget = targetSide;
        BattleScriptPushCursorAndCallback(BattleScript_RoseGarden);
        return TRUE;
    },
};
```

### Activation Conditions
- Triggers on switch-in (including initial battle entry)
- Only activates if the opponent's side has fewer than 2 layers of Toxic Spikes
- If the opponent already has 2 layers, the ability does nothing

### Toxic Spikes Layer Effects
Based on the battle system implementation:
- **1 layer**: Incoming Pokemon are inflicted with regular poison (STATUS1_POISON)
- **2 layers**: Incoming Pokemon are inflicted with badly poisoned/toxic poison (STATUS1_TOXIC_POISON)
- Rose Garden immediately sets 2 layers, ensuring maximum poison effect

### Technical Implementation
```cpp
// Entry hazard check logic
if (gSideTimers[GetBattlerSide(gActiveBattler)].toxicSpikesAmount >= 2)
    gBattleMons[gActiveBattler].status1 |= STATUS1_TOXIC_POISON;
else
    gBattleMons[gActiveBattler].status1 |= STATUS1_POISON;
```

### Affected Pokemon
- **Grounded Pokemon**: Take badly poisoned status when switching in
- **Flying types**: Immune to Toxic Spikes (not grounded)
- **Levitate users**: Immune to Toxic Spikes (not grounded)
- **Poison types**: Absorb the Toxic Spikes, removing them from the field
- **Steel types**: Immune to poison status, unaffected

### Interactions with Other Abilities/Mechanics
- **Magic Guard**: Prevents Toxic Spikes damage but still applies the status
- **Poison Heal**: Heals instead of taking damage from the poison status
- **Rapid Spin/Defog**: Can remove the Toxic Spikes from the field
- **Heavy-Duty Boots**: Prevents the Toxic Spikes effect entirely

### Strategic Implications
- **Immediate field control**: Sets maximum hazard pressure instantly on switch-in
- **Passive damage**: Forces opponent to take increasing damage over time
- **Switch punishment**: Discourages opponent switching
- **Team support**: Benefits from Poison-type teammates who can absorb hazards safely

### Damage Calculations
**Badly Poisoned (Toxic) Damage per turn:**
- Turn 1: 1/16 of max HP
- Turn 2: 2/16 of max HP  
- Turn 3: 3/16 of max HP
- And so on, increasing each turn

### Common Users
- **Roserade (Elite Redux form)**: Primary user with Grass/Poison typing
  - Synergizes with Poison typing (immune to own Toxic Spikes)
  - High Speed (125) allows quick hazard setting
  - Mixed offensive stats (145 Atk/SpAtk) for immediate pressure

### Competitive Usage Notes
- **Lead potential**: Excellent for setting immediate hazard pressure
- **Defensive pivoting**: Forces switches while setting hazards
- **Anti-setup**: Prevents opponent setup sweepers with passive damage
- **Wallbreaking support**: Gradual damage helps break through defensive cores

### Counters
- **Heavy-Duty Boots**: Complete immunity to entry hazards
- **Rapid Spin users**: Cloyster, Donphan, Forretress can remove hazards
- **Defog users**: Flying types that can clear the field
- **Magic Bounce**: Reflects the hazard back to the user's side
- **Poison types**: Absorb and remove the Toxic Spikes

### Synergies
- **Spikes/Stealth Rock setters**: Stack multiple hazard types
- **Pursuit users**: Trap Pokemon trying to escape poison damage
- **Healing support**: Keep Rose Garden user healthy for multiple entries
- **U-turn/Volt Switch**: Maintain momentum while setting hazards

### Version History
- Introduced in Elite Redux as a unique entry hazard ability
- Part of the expanded ability system for signature Pokemon effects