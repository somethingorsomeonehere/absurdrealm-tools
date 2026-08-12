---
id: 63
name: Marvel Scale
status: reviewed
character_count: 91
---

# Marvel Scale - Ability ID 63

## In-Game Description
"Ups Def and Sp. Def by 1.5x when statused."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases base Defense and Special Defense by 50% when afflicted with any status condition. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**MARVEL SCALE** is a defensive ability that converts status conditions into massive defensive boosts.

### Core Mechanics:
- **Defense Boost**: 1.5x Defense and Special Defense when statused
- **Status Requirement**: Any primary status condition activates the boost
- **Implementation**: Direct stat multiplication during calculation phase
- **Breakable**: Can be suppressed by Mold Breaker abilities

### Technical Implementation:
```c
constexpr Ability MarvelScale = {
    .onStat =
        +[](ON_STAT) {
            if ((statId == STAT_DEF || statId == STAT_SPDEF) && HasAnyStatusOrAbility(battler)) *stat *= 1.5;
        },
    .breakable = TRUE,
};
```

### Activation Conditions:
The `HasAnyStatusOrAbility(battler)` function checks for:
- **Primary Status**: Sleep, Poison, Burn, Paralysis, Freeze
- **Elite Redux Status**: Frostbite, Bleed
- **Special Cases**: Comatose ability, Blood Stain effect

### Status Synergies:
- **Burn**: Good - no defensive penalty, decent damage over time
- **Poison**: Excellent - consistent damage, no stat penalties
- **Paralysis**: Good - Speed reduction but massive defensive boost
- **Sleep**: Temporary - only while asleep
- **Freeze/Frostbite**: Situational - depends on thaw mechanics
- **Bleed**: Elite Redux - permanent bleeding for consistent activation

### Strategic Applications:
- **Toxic Orb Sets**: Self-inflict poison for guaranteed 1.5x defenses
- **Flame Orb Sets**: Alternative with burn damage
- **Status Absorber**: Turn opponent's status moves into advantages
- **Defensive Core**: Essential component of stall teams

### Elite Redux Enhancements:
- **Frostbite Status**: New freeze replacement that activates Marvel Scale
- **Bleed Status**: Prevents healing but triggers the defensive boost
- **Blood Stain Ability**: Creates permanent "bleeding" condition for non-Ghost/Rock types
- **Comatose Compatibility**: Works with ability-induced "sleep" states

### Common Users:
- **Dragonite**: Has both Multiscale and Marvel Scale as innate abilities
- **Milotic**: Combines with Prism Scales for type-based defensive stacking
- **Dratini/Dragonair**: Natural progression with Multiscale synergy

### Damage Calculations:
- **Defensive Stats**: Effectively 1.5x Defense and Special Defense
- **Example**: 100 Base Defense becomes 150 effective Defense
- **Stacking**: Multiplies with other defensive boosts like screens
- **Coverage**: Both physical and special defensive improvement

### Competitive Usage:
- **Defensive Wall**: Primary role with status orb
- **Stall Teams**: Essential for long-term defensive strategies
- **Pivot Pokemon**: Enhanced bulk for safe switching
- **Anti-Status**: Turns status moves into setup opportunities

### Item Synergies:
- **Toxic Orb**: Most reliable - escalating damage but consistent boost
- **Flame Orb**: Predictable burn activation
- **Leftovers**: Recovery to offset status damage
- **Multiscale Combo**: Dragonite gets both for incredible bulk

### Interactions:
- **Multiscale**: Stacks multiplicatively for extreme bulk at high HP
- **Guts**: Same status triggers both abilities (offense + defense)
- **Wonder Guard**: Marvel Scale boost still applies to allowed damage
- **Magic Guard**: Protects from status damage while keeping boost

### Counters:
- **Status Removal**: Aromatherapy, Heal Bell remove beneficial status
- **Mold Breaker**: Bypasses Marvel Scale completely
- **Critical Hits**: Ignore defensive boosts
- **Status Prevention**: Safeguard prevents beneficial status application

### AI Behavior:
The AI recognizes Marvel Scale and may:
- Avoid inflicting status on Marvel Scale users
- Prioritize status removal when possible
- Use critical hit moves to bypass defensive boosts
- Target with coverage moves rather than status

### Version History:
- Elite Redux maintains core 1.5x defensive boost
- Enhanced with new status conditions (Frostbite, Bleed)
- Expanded compatibility with ability-induced statuses
- Integrated with 4-ability system for powerful defensive combinations