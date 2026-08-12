---
id: 240
name: Mirror Armor
status: reviewed
character_count: 123
---

# Mirror Armor - Ability ID 240

## In-Game Description
"Bounces back any stat drops inflicted by an enemy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mirror Armor reflects all stat-lowering effects aimed at the user back to the attacker. The reflection bypasses immunities.

## Detailed Mechanical Explanation
*For Discord/reference use*

Mirror Armor is a defensive ability that completely reverses stat-lowering effects against the user. When any move, ability, or entry hazard attempts to lower one or more of the Pokemon's stats, Mirror Armor activates and instead applies that stat reduction to the attacker.

### Key Mechanics:

1. **Complete Stat Drop Reflection**: Any stat-lowering effect is reflected back to the source
2. **Bypasses Immunities**: The reflected stat drop ignores the attacker's normal immunities (e.g., Clear Body, Hyper Cutter)
3. **Works Against All Sources**: Reflects stat drops from:
   - Direct moves (e.g., Growl, Leer, Charm)
   - Contact abilities (e.g., Intimidate on switch-in)
   - Entry hazards (e.g., Sticky Web)
   - Secondary effects of damaging moves

### Implementation Details:

The ability is implemented through the `StatLowerableOrMirrorArmor()` function in battle_util.c, which checks if a stat can be lowered normally OR if the target has Mirror Armor. When Mirror Armor is detected, the battle script system calls `BattleScript_MirrorArmorReflect` which:

1. Shows the Mirror Armor activation popup
2. Redirects the stat change to affect the attacker instead of the defender
3. Uses the `MOVE_EFFECT_AFFECTS_USER` flag to properly target the original attacker

### Special Interactions:

- **Self-Targeting Moves**: Does not reflect stat drops from moves that the Pokemon uses on itself
- **Multi-Target Moves**: In multi-battles, reflects each stat drop individually
- **Sticky Web**: Has special handling to properly redirect Sticky Web's Speed drop to the original user when Mirror Armor activates on switch-in
- **Breakable**: The ability can be suppressed by Mold Breaker and similar effects

### Battle Script Integration:

The ability integrates deeply with the battle system through multiple battle scripts:
- `BattleScript_MirrorArmorReflect`: Main reflection handler
- `BattleScript_MirrorArmorReflectStickyWeb`: Special case for Sticky Web
- Uses `STAT_BUFF_ALLOW_PTR` flag for proper stat change redirection

This makes Mirror Armor an extremely powerful defensive ability that not only prevents stat drops but punishes opponents for attempting them, effectively turning their debuff strategies against them.