---
id: 126
name: Contrary
status: reviewed
character_count: 84
---

# Contrary - Ability ID 126

## In-Game Description
"Stat raises turn into stat drops for this Pokemon and vice versa."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reverses all stat changes affecting this Pokemon. Works with self-inflicted changes.

## Detailed Mechanical Explanation
*For Discord/reference use*

**CONTRARY** is a stat-manipulation ability that reverses the direction of all stat changes affecting the Pokemon.

### Core Mechanics:
- **Trigger**: All stat changes, regardless of source
- **Effect**: Multiplies the stat change value by -1 (`statValue *= -1`)
- **Scope**: Affects Attack, Defense, Speed, Special Attack, Special Defense, Accuracy, and Evasion
- **Limits**: Reversed stats still respect the standard -6 to +6 stage limits

### Technical Implementation:
```c
// In ChangeStatBuffs function (battle_script_commands.c:9616-9621)
if (BATTLER_HAS_ABILITY(battler, ABILITY_CONTRARY)) {
    statValue *= -1;
    if (updateMoveEffect) {
        gBattleScripting.moveEffect = ReverseStatChangeMoveEffect(gBattleScripting.moveEffect);
    }
}
```

The ability also reverses move effects through `ReverseStatChangeMoveEffect()`, which converts effects like:
- `MOVE_EFFECT_ATK_PLUS_1` to `MOVE_EFFECT_ATK_MINUS_1`
- `MOVE_EFFECT_DEF_MINUS_2` to `MOVE_EFFECT_DEF_PLUS_2`
- And all other stat change effects

### Interaction Order:
1. **Contrary check**: Stat value is reversed first
2. **Simple interaction**: If the Pokemon also has Simple, the reversed value is then doubled
3. **Other modifiers**: Subdue and similar effects apply after Contrary

```c
// Order of operations in ChangeStatBuffs:
if (BATTLER_HAS_ABILITY(battler, ABILITY_CONTRARY)) {
    statValue *= -1;  // Step 1: Reverse
}
if (BattlerHasAbility(battler, ABILITY_SIMPLE, FALSE)) {
    statValue *= 2;   // Step 2: Double if Simple
}
```

### Affected Sources:
1. **Self-inflicted moves**: Overheat (-2 SpA to +2 SpA), Close Combat (-1 Def/SpD to +1 Def/SpD), V-Create (-1 Def/SpD to +1 Def/SpD)
2. **Opponent moves**: Growl (-1 Atk to +1 Atk), Leer (-1 Def to +1 Def)
3. **Abilities**: Intimidate (-1 Atk to +1 Atk), Download effects
4. **Items**: Stat-boosting berries, White Herb (prevents stat drops, so Contrary makes them prevent stat rises)
5. **Battle effects**: Sticky Web (-1 Spe to +1 Spe), stat-changing Z-moves

### Battle Message Changes:
The ability also changes battle text through `BufferStatChange()`:
- "Attack fell!" becomes "Attack rose!" and vice versa
- Messages are swapped in real-time to match the actual effect

### Strategic Applications:
1. **Power moves with drawbacks**: Leaf Storm, Draco Meteor, Overheat become setup moves
2. **Intimidate immunity**: Turns Attack drops into Attack boosts
3. **Sticky Web weakness**: Entry hazards that lower Speed become Speed boosts
4. **Stat-drop moves**: King's Shield, Icy Wind become beneficial to the user

### Example Damage Calculations:
**Serperior with Contrary using Leaf Storm:**
- Leaf Storm: 130 BP, normally -2 SpA
- With Contrary: 130 BP, +2 SpA instead
- Next Leaf Storm: 130 BP x 1.5 (SpA boost) = 195 effective BP
- After 3 uses: +6 SpA, Leaf Storm hits with ~260 effective BP

### Common Users:
Notable Pokemon with Contrary in Elite Redux:
- **Serperior line** (Snivy evolution): Grass starter with access to Leaf Storm
- **Inkay/Malamar**: Dark/Psychic types with Topsy-Turvy synergy
- **Shuckle**: Defensive user that benefits from stat drop immunity
- **Various legendaries**: Including Houndoom-Redux and Enamorus forms

### Competitive Interactions:
- **Simple + Contrary**: Stat changes are reversed then doubled (e.g., -1 becomes +2)
- **Unaware opponents**: Cannot ignore Contrary-boosted stats
- **Haze/Clear Smog**: Still resets stats normally, ignoring Contrary
- **Topsy-Turvy**: Reverses stats again, effectively canceling Contrary for that turn

### Counters:
1. **Haze users**: Reset all stat changes
2. **Spectral Thief**: Steals stat boosts (treats Contrary boosts as normal boosts)
3. **Clear Smog**: Resets target's stats while dealing damage
4. **Status moves**: Paralysis, sleep, etc. bypass stat manipulation entirely
5. **Fixed damage**: Seismic Toss, Night Shade ignore stat changes

### Synergies:
1. **Self-debuffing moves**: V-Create, Close Combat, Superpower, Hammer Arm
2. **High-power special moves**: Overheat, Draco Meteor, Leaf Storm, Psycho Boost
3. **Entry hazard setup**: Benefits from opponent's Sticky Web
4. **Baton Pass**: Can pass reversed stat boosts to teammates

### Breakable Nature:
Contrary has `.breakable = TRUE`, meaning it can be suppressed by:
- Mold Breaker and variants
- Neutralizing Gas
- Other ability-suppressing effects

### Version History:
- **Generation 5**: Introduced with Snivy line and Inkay line
- **Elite Redux**: Expanded to more Pokemon as a balancing option for powerful moves with drawbacks