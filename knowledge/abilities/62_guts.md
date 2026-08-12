---
id: 62
name: Guts
status: reviewed
character_count: 109
---

# Guts - Ability ID 62

## In-Game Description
"Ups Atk by 1.5x if suffering from a status condition."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Attack stat by 50% when suffering from any status condition. Negates the Attack drop from burn status.

## Detailed Mechanical Explanation
*For Discord/reference use*

**GUTS** is an offensive ability that converts status conditions into massive Attack boosts for physical moves.

### Core Mechanics:
- **Attack Boost**: 1.5x Attack multiplier when statused
- **Physical Only**: Boost applies exclusively to physical moves (`IS_MOVE_PHYSICAL`)
- **Status Requirement**: Any primary status condition activates the boost
- **Burn Immunity**: Negates burn's Attack reduction (`.negatesBurnAtkDrop = TRUE`)

### Technical Implementation:
```c
constexpr Ability Guts = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (HasAnyStatusOrAbility(battler) && IS_MOVE_PHYSICAL(move)) MUL(1.5);
        },
    .negatesBurnAtkDrop = TRUE,
};
```

### Activation Conditions:
The `HasAnyStatusOrAbility(battler)` function checks for:
- **Primary Status**: Sleep, Poison, Burn, Paralysis, Freeze
- **Elite Redux Status**: Frostbite, Bleed
- **Special Cases**: Comatose ability, Blood Stain effect

### Status Synergies:
- **Burn**: Ideal - no Attack penalty, but still takes damage
- **Poison**: Good - consistent damage, no stat penalties
- **Paralysis**: Risky - Speed reduction but massive Attack boost
- **Sleep**: Temporary - only while asleep
- **Freeze/Frostbite**: Situational - depends on thaw mechanics

### Strategic Applications:
- **Flame Orb Sets**: Self-inflict burn for guaranteed 1.5x Attack
- **Toxic Orb Sets**: Alternative with escalating damage
- **Status Absorber**: Turn opponent's status moves into advantages
- **Late-Game Sweeper**: Activates naturally through battle damage

### Damage Calculations:
- **Base Power**: Remains unchanged
- **Attack Stat**: Effectively 1.5x for physical moves
- **Example**: 100 Base Attack becomes 150 effective Attack
- **Stacking**: Multiplies with other offensive boosts

### Elite Redux Enhancements:
- **Bleed Status**: New permanent status that activates Guts
- **Blood Stain**: Spreads bleeding condition for consistent activation
- **Expanded Status**: More ways to trigger the ability

### Common Users:
- **Machamp**: Classic Guts user with No Guard
- **Hariyama**: Thick Fat + Guts for defensive setup
- **Ursaring**: High Attack stat amplified by Guts
- **Conkeldurr**: Slow but incredibly powerful with status

### Competitive Usage:
- **Physical Sweeper**: Primary role with status orb
- **Wallbreaker**: Breaks through physical walls
- **Revenge Killer**: Status naturally acquired through battle
- **Anti-Status**: Turns status moves into setup opportunities

### Item Synergies:
- **Flame Orb**: Most popular - predictable activation
- **Toxic Orb**: Higher damage over time
- **Life Orb**: Stacks multiplicatively for extreme power
- **Choice Band**: Combined with Guts for overwhelming force

### Interactions:
- **Wonder Guard**: Guts boost still applies to super-effective moves
- **Huge Power**: Multiplies with Guts for 3x total Attack
- **Choice Items**: Guts boost stacks with Choice Band/Scarf
- **Mold Breaker**: Cannot suppress Guts activation

### Counters:
- **Physical Walls**: High Defense stats resist boosted attacks
- **Intimidate**: Lowers Attack stat before Guts multiplier
- **Will-O-Wisp**: Burn activates Guts but provides chip damage
- **Status Healing**: Aromatherapy removes beneficial status

### AI Behavior:
The AI recognizes Guts and may:
- Avoid inflicting status on Guts users
- Prioritize healing status when possible
- Use Intimidate to offset the Attack boost
- Target with special attacks instead

### Version History:
- Elite Redux maintains core 1.5x boost functionality
- Enhanced with burn Attack drop negation
- Expanded status conditions provide more activation opportunities
- Integrated with 4-ability system for defensive/utility combinations