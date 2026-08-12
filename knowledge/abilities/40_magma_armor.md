---
id: 40
name: Magma Armor
status: reviewed
character_count: 137
---

# Magma Armor - Ability ID 40

## In-Game Description
"Frostbite-immune. Takes 30% less dmg from Water/Ice-type moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to frostbite. Reduces damage received from Water and Ice-type moves by 30%. Multiplicative with other sources of damage reduction. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**MAGMA ARMOR** is a defensive ability that provides both status immunity and type-based damage reduction.

### Defensive Mechanics:
- **Type Resistance**: Reduces damage from Water and Ice-type moves by 30% (0.7x multiplier)
- **Activation**: Applied during damage calculation via onDefensiveMultiplier hook
- **Stacking**: Does not stack with other resistances; calculated as part of overall damage formula

### Status Immunity:
- **Frostbite Immunity**: Complete immunity to frostbite status condition
- **Removal**: Automatically removes frostbite if inflicted while ability is active (removesStatusOnImmunity = TRUE)
- **Breakable**: Ability can be suppressed by Mold Breaker, Neutralizing Gas, etc.

### Frostbite Status Effects (What Magma Armor Prevents):
1. **Turn Damage**: 1/16 max HP per turn (Gen 7+ mechanics)
2. **Special Attack Reduction**: Halves Special Attack stat when using special moves
3. **Duration**: Permanent until cured (unlike burn, no self-recovery)
4. **Healing**: Cured by Fire-type moves with FLAG_THAW_USER, status healing items/moves

### Interaction Rules:
- **vs Mold Breaker**: Magma Armor is suppressed; Pokemon can be frostbitten and takes full damage
- **vs Trace/Role Play**: Can be copied by other Pokemon
- **vs Skill Swap**: Can be swapped with other abilities
- **vs Gastro Acid**: Ability is suppressed temporarily

### Technical Implementation:
```c
constexpr Ability MagmaArmor = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_WATER || moveType == TYPE_ICE) RESISTANCE(.7);
        },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_FROSTBITE)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Damage Calculation:
- **RESISTANCE(.7)** macro applies 0.7x multiplier to both resistance and modifier values
- Applied during damage calculation after type effectiveness but before other modifiers
- Stacks multiplicatively with other damage reductions

### Competitive Analysis:
**Strengths:**
- Hard counter to frostbite-based strategies
- Reliable damage reduction against common offensive types
- Passive ability requiring no setup or activation

**Weaknesses:**
- Limited to only two types (Water/Ice)
- Provides no offensive benefit
- Can be bypassed by ability-suppressing moves/abilities
- 30% reduction is moderate compared to some other defensive abilities

**Synergies:**
- Excellent on Pokemon weak to Water/Ice moves
- Pairs well with Fire-types who naturally resist Ice but may be weak to Water
- Valuable in metas with prevalent Water/Ice attackers

### Pokemon That Benefit Most:
- Fire-types with Water weakness (Magma Armor negates the weakness partially)
- Pokemon in lower speed tiers that need to tank hits
- Defensive walls that can afford a passive ability slot

### Version History:
- Gen 3-4: Only prevented freezing (not frostbite, which didn't exist)
- Gen 5+: Continued freeze immunity
- Elite Redux: Enhanced with frostbite immunity and Water/Ice resistance

### Related Abilities:
- **Water Veil**: Burn immunity (opposite status condition)
- **Limber**: Paralysis immunity 
- **Immunity**: Poison immunity
- **Insomnia**: Sleep immunity
- **Own Tempo**: Confusion immunity