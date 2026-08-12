---
id: 550
name: Wind Power
status: reviewed
character_count: 152
---

# Wind Power - Ability ID 550

## In-Game Description
"Charges up when hit by wind moves or Tailwind starts."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gain Charged status when hit by wind-based moves or entering in during Tailwind. The Charged status doubles the power of Electric-type moves until used.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Activation Condition**: When hit by any move with the `airBased` property OR when Tailwind is set up on the field
- **Effect**: Grants the STATUS3_CHARGED_UP status condition
- **Single Use**: Can only activate once per battle unless the charged status is consumed by using an Electric-type move
- **Damage Boost**: While charged, Electric-type moves deal 2x damage (200% power multiplier)

### Technical Implementation
```c
constexpr Ability WindPower = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(gBattleMoves[move].airBased)
        CHECK_NOT(gStatuses3[battler] & STATUS3_CHARGED_UP)

        gStatuses3[battler] |= STATUS3_CHARGED_UP;
        BattleScriptCall(BattleScript_ElectromorphosisActivates);
        return TRUE;
    },
};
```

### Status3 Charged Up Effect
```c
// In battle_util.c - damage calculation
if (gStatuses3[battlerAtk] & STATUS3_CHARGED_UP && moveType == TYPE_ELECTRIC) 
    MulModifier(&modifier, UQ_4_12(2.0));
```

### Complete List of Wind-Based Moves
**Primary Wind Moves:**
- Gust, Razor Wind, Wing Attack, Whirlwind
- Aeroblast, Twister, Air Slash, Hurricane
- Tailwind (also activates from status setup)

**Weather-Based Wind Moves:**
- Blizzard, Icy Wind, Powder Snow
- Any move with the `airBased` flag

**Special Interactions:**
- **Tailwind Setup**: Activates when Tailwind status is applied to the field, not just when hit by the move
- **Air Blower Ability**: Pokemon with this ability automatically set Tailwind on entry, potentially triggering Wind Power on allies

### Strategic Implications
- **Electric Sweeper Setup**: Perfect for Electric/Flying types like Wattrel and Kilowattrel
- **Prediction Play**: Opponents may avoid using wind moves against Wind Power users
- **Team Synergy**: Combines excellently with Tailwind support for both speed and power
- **One-Time Nuke**: Creates a powerful one-time Electric attack opportunity

### Common Users
- **Wattrel** (Pre-evolution): Has Wind Power as a regular ability option
- **Kilowattrel** (Evolution): Has Wind Power as an innate ability, combining with other abilities

### Competitive Usage Notes
- **Priority Target**: Wind Power users become high-priority targets when charged
- **Electric Terrain Synergy**: Pairs well with Electric Terrain for additional Electric move power
- **Prediction Gameplay**: Creates mind games around wind move usage
- **Setup Sweeper Role**: Ideal for late-game cleanup after getting charged

### Counters
- **Avoid Wind Moves**: Don't use Gust, Tailwind, or other airBased moves against Wind Power users
- **Priority Moves**: KO before they can use their charged Electric attack
- **Status Conditions**: Sleep, paralysis, or other disabling effects prevent setup
- **Taunt**: Prevents setup moves but doesn't remove existing charge

### Synergies
- **Tailwind Teams**: Natural fit with speed-based team compositions
- **Electric Terrain**: Stacks with terrain boost for massive Electric move power
- **Flying-type STAB**: Most Wind Power users are Electric/Flying for dual STAB benefits
- **Choice Items**: Locks into powerful charged Electric moves for consistent damage

### Version History
- **Elite Redux**: Introduced as part of Generation 9 ability additions
- **Interaction Update**: May have interactions with new wind-based moves as they're added
- **Balance Consideration**: Single-use nature prevents excessive power accumulation

### Damage Calculation Examples
**Base Thunderbolt (90 BP):**
- Normal: 90 BP
- With Wind Power (Charged): 180 BP
- With Electric Terrain + Charged: ~234 BP (1.3x terrain boost)
- With STAB + Charged: 270 BP (1.5x STAB)

**Hurricane Setup Example:**
1. Opponent uses Hurricane (wind move) to Wind Power activates
2. User becomes charged (STATUS3_CHARGED_UP)
3. User's next Electric move deals double damage
4. Status is consumed after use, requiring another wind move to reactivate