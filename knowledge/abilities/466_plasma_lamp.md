---
id: 466
name: Plasma Lamp
status: reviewed
character_count: 87
---

# Plasma Lamp - Ability ID 466

## In-Game Description
"Boost accuracy & power of Fire & Electric type moves by 1.2x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Plasma Lamp boosts both power and accuracy of Fire and Electric-type moves by 20% each. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Plasma Lamp is an offensive ability that provides dual benefits to Fire and Electric-type moves: a 20% power boost and a 20% accuracy boost. Both effects apply simultaneously to qualifying moves.

### Activation Conditions
- **Move type requirement**: Only affects Fire-type and Electric-type moves
- **Dual effect**: Both power and accuracy bonuses apply to the same move
- **Always active**: No weather, health, or turn-based conditions required
- **Stacks multiplicatively**: Combines with other power/accuracy modifiers

### Technical Implementation
```c
constexpr Ability PlasmaLamp = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE || moveType == TYPE_ELECTRIC) MUL(1.2);
        },
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(moveType == TYPE_FIRE || moveType == TYPE_ELECTRIC)
        *accuracy *= 1.2;
        return ACCURACY_MULTIPLICATIVE;
    },
};
```

### Power Boost Mechanics
- **Multiplier**: 1.2x (20% increase) to base power
- **Calculation**: Applied during damage calculation phase
- **Stacking**: Multiplicative with other power boosts (STAB, items, etc.)
- **Affected moves**: All Fire and Electric moves, including:
  - Physical moves (Flare Blitz, Wild Charge)
  - Special moves (Flamethrower, Thunderbolt)
  - Status moves that deal damage (Thunder Wave doesn't get power boost)

### Accuracy Boost Mechanics
- **Multiplier**: 1.2x (20% increase) to base accuracy
- **Calculation**: Applied during accuracy check phase
- **Priority**: ACCURACY_MULTIPLICATIVE (standard timing)
- **Affected moves**: All Fire and Electric moves, including status moves
- **Examples**:
  - Thunder (70% accuracy to 84% accuracy)
  - Fire Blast (85% accuracy to 102% accuracy, capped at 100%)
  - Will-O-Wisp (85% accuracy to 102% accuracy, capped at 100%)

### Move Type Coverage
**Fire-type moves affected:**
- Flamethrower, Fire Blast, Overheat, Heat Wave
- Flare Blitz, Fire Punch, Flame Wheel
- Will-O-Wisp, Sunny Day (accuracy only)
- Sacred Fire, Blue Flare, V-create

**Electric-type moves affected:**
- Thunderbolt, Thunder, Discharge, Volt Switch
- Wild Charge, Thunder Punch, Spark
- Thunder Wave, Thunder Shock
- Zap Cannon, Bolt Strike, Fusion Bolt

### Strategic Implications
- **Mixed attacker synergy**: Benefits both physical and special Fire/Electric moves
- **Reliability boost**: Makes less accurate moves more consistent
- **Coverage enhancement**: Improves two common offensive types
- **No drawbacks**: Pure beneficial effect with no negative trade-offs
- **Type specialization**: Rewards mono-type or dual-type offensive sets

### Competitive Usage
- **Ideal users**: Pokemon with strong Fire/Electric movesets
- **Mixed sets**: Pokemon that run both physical and special Fire/Electric moves
- **Accuracy-dependent moves**: Makes Thunder and Fire Blast more reliable
- **STAB synergy**: Combines excellently with Fire/Electric dual-types
- **Choice item synergy**: Boosts locked-in Fire/Electric moves

### Damage Calculations
With STAB and Plasma Lamp on a Fire-type:
- Base move power x 1.5 (STAB) x 1.2 (Plasma Lamp) = 1.8x total multiplier
- Example: Flamethrower (90 BP) to 90 x 1.8 = 162 effective base power

### Accuracy Calculations
Examples of accuracy improvements:
- Thunder: 70% to 84%
- Fire Blast: 85% to 100% (capped)
- Zap Cannon: 50% to 60%
- Will-O-Wisp: 85% to 100% (capped)

### Synergistic Abilities
- **Flash Fire**: Absorb Fire moves to boost power further
- **Motor Drive/Volt Absorb**: Immunity to Electric moves for switching
- **Solar Power**: Additional Fire move boost in sun
- **Dry Skin**: Takes damage from Fire moves but ability still works

### Item Synergies
- **Choice items**: Boost locked-in Fire/Electric moves
- **Life Orb**: Stacks multiplicatively with Plasma Lamp
- **Expert Belt**: Super effective Fire/Electric moves get both boosts
- **Magnet/Charcoal**: Type-boosting items stack with ability
- **Wide Lens**: Additional accuracy boost for ultra-reliable moves

### Counters and Limitations
- **Type limitation**: Only affects two types, leaving other moves unboostered
- **Flash Fire**: Opponents can absorb Fire moves for their own boost
- **Ground immunity**: Electric moves don't affect Ground-types regardless
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Type-changing moves**: Moves that change type lose the boost

### Common Pokemon Synergies
**Ideal candidates:**
- Fire/Electric dual-types (Rotom-Heat forms)
- Mixed attackers with both Fire and Electric moves
- Pokemon with diverse Fire/Electric movesets
- Bulky attackers that benefit from accuracy boosts

**Move combinations:**
- Flamethrower + Thunderbolt (special mixed)
- Fire Punch + Thunder Punch (physical mixed)
- Overheat + Volt Switch (momentum + power)
- Will-O-Wisp + Thunder Wave (status utility)

### Version History
- Elite Redux custom ability (ID 466)
- Designed for Fire/Electric type specialization
- Part of the expanded ability roster for diverse team building
- Provides simple but effective dual-type offensive boost