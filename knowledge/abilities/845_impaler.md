---
id: 845
name: Impaler
status: reviewed
character_count: 262
---

# Impaler - Ability ID 845

## In-Game Description
"Mighty Horn + 30% Bleed chance on horn moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of horn and drill-based attacks by 30% and they have a 30% chance to inflict Bleed on the target. Bleeding causes 1/16 max HP damage per turn, prevents healing, and negates the effects of stat stages. Rock and Ghost types are immune to bleeding. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Impaler is a compound ability that provides two powerful effects for horn-based moves:

1. **Mighty Horn Effect**: All horn-based moves receive a 1.3x (30%) damage multiplier
2. **Bleed Chance**: 30% chance to inflict Bleed status on successful horn move hits

### Technical Implementation
From `src/abilities.cc`:
```cpp
constexpr Ability Impaler = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBleed(target))
        CHECK(gBattleMoves[move].hornBased);
        CHECK(Random() % 100 < 30)
        
        return AbilityStatusEffect(MOVE_EFFECT_BLEED);
    },
    .onOffensiveMultiplier = MightyHorn.onOffensiveMultiplier,
};
```

The Mighty Horn multiplier implementation:
```cpp
constexpr Ability MightyHorn = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].hornBased) MUL(1.3);
        },
};
```

### Activation Conditions
- Move must have the `hornBased` flag set to TRUE
- For bleed effect: Target must be able to bleed (not immune to status)
- Bleed chance is checked after hit confirmation

### Complete List of Horn-Based Moves
The following moves are boosted by Impaler and can trigger bleed:
- **MOVE_HORN_ATTACK**: Basic horn attack
- **MOVE_FURY_ATTACK**: Multi-hit horn strikes
- **MOVE_HORN_DRILL**: OHKO horn move
- **MOVE_PECK**: Flying-type pecking attack
- **MOVE_DRILL_PECK**: High-crit flying drill
- **MOVE_MEGAHORN**: Bug-type horn attack (120 BP → 156 BP with Impaler)
- **MOVE_POISON_JAB**: Poison-type jabbing move
- **MOVE_PSYCHO_CUT**: Psychic-type slashing
- **MOVE_DRILL_RUN**: Ground-type drilling charge
- **MOVE_HORN_LEECH**: HP-draining horn attack
- **MOVE_SMART_STRIKE**: Steel-type never-miss horn strike
- **MOVE_SHOCKING_JAB**: Electric-type horn jab
- **MOVE_AQUA_BASH**: Water-type horn bash
- **MOVE_JAGGED_HORNS**: Rock-type horn attack
- **MOVE_PSYBLADE**: Psychic-type blade strike
- **MOVE_HYPER_DRILL**: Normal-type powerful drill
- **MOVE_PSYSHIELD_BASH**: Psychic-type defensive bash
- **MOVE_SMOLDER_BASH**: Fire-type horn bash
- **MOVE_DRAGON_JAB**: Dragon-type horn jab
- **MOVE_ICICLE_IMPALE**: Ice-type impaling attack
- **MOVE_FIRE_GLAIVE**: Fire-type glaive strike
- **MOVE_BERSERKER_HORN**: Fighting-type rage horn

### Bleed Status Effect
- Bleed causes damage over time at the end of each turn
- Bleed damage bypasses substitutes
- Can stack with other status conditions
- Duration and damage amount depend on game implementation

### Damage Calculations
Example with Megahorn (120 BP):
- Base: 120 BP
- With Impaler: 120 x 1.3 = 156 BP
- Plus 30% chance to inflict additional bleed damage

### Strategic Implications
- Transforms horn moves into premier offensive options
- Bleed chance provides residual damage even if opponent switches
- Synergizes with high-BP horn moves like Megahorn
- Makes previously mediocre moves like Horn Attack viable

### Common Users
- **Gardevoir Redux Mega**: Water/Dark type with Impaler as innate ability
  - Also has Phantom and Tag as other innates
  - Can choose between Swift Swim, Marine Apex, or Ambush
  - High 150 Attack stat makes excellent use of physical horn moves

### Competitive Usage Notes
- Pairs excellently with coverage horn moves
- Bleed chance discourages switching
- 30% damage boost makes even weak horn moves threatening
- Consider pairing with Choice Band for maximum damage
- Smart Strike provides never-miss option with boost

### Counters
- Steel-types immune to bleed
- Poison-types may resist bleed (implementation dependent)
- High Defense walls can tank boosted hits
- Priority moves can revenge kill before bleed damage
- Protect stalling can maximize bleed damage taken

### Synergies
- **Choice Band**: Stacks multiplicatively for massive damage
- **Speed control**: Ensures horn moves connect before taking damage
- **Entry hazards**: Combined with bleed for chip damage
- **Pursuit trappers**: Punish switches forced by bleed

### Version History
- Introduced as a combination of Mighty Horn and bleed mechanics
- Provides unique offensive pressure through dual effects
- One of the few abilities that both boosts damage and adds status