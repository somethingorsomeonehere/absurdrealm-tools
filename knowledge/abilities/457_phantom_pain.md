---
id: 457
name: Phantom Pain
status: reviewed
character_count: 134
---

# Phantom Pain - Ability ID 457

## In-Game Description
"Ghost-type moves deal normal damage to Normal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Phantom Pain removes Normal-type immunity to Ghost-type moves, allowing Ghost attacks to hit Normal-type Pokemon for 1x effectiveness. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Phantom Pain is a unique type-modifying ability that removes the natural immunity Normal-type Pokemon have to Ghost-type moves. Instead of dealing 0x damage (no effect), Ghost-type moves deal 1x damage (normal effectiveness) to Normal-type Pokemon when the attacking Pokemon has Phantom Pain.

### Activation Conditions
- **Move requirement**: Only affects Ghost-type moves
- **Target requirement**: Only affects moves targeting Normal-type Pokemon
- **Timing**: Activates during type effectiveness calculation
- **Scope**: Works on all Ghost-type moves regardless of power or category

### Technical Implementation
```c
constexpr Ability PhantomPain = {
    .onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
        CHECK(moveType == TYPE_GHOST)        // Must be Ghost-type move
        CHECK(defType == TYPE_NORMAL)        // Must target Normal-type
        CHECK_NOT(*mod)                      // Only if no modifier set
        *mod = UQ_4_12(1.0);                // Set to 1.0x effectiveness
        return TRUE;
    },
};
```

### Type Effectiveness Override
- **Normal interaction**: Ghost vs Normal = 0x damage (no effect)
- **With Phantom Pain**: Ghost vs Normal = 1x damage (normal effectiveness)
- **Fixed-point math**: Uses UQ_4_12(1.0) which represents 1.0x multiplier
- **Priority**: Only applies if no other type effectiveness modifier is active

### Important Interactions
- **Dual typing**: Affects Normal-type portion of dual-type Pokemon
- **Multi-hit moves**: Each hit benefits from the effectiveness change
- **STAB bonus**: Ghost-type moves still get STAB if attacker is Ghost-type
- **Critical hits**: Can still critical hit with modified effectiveness
- **Type-boosting items**: Works with items like Spell Tag or Ghost Gem

### Move Coverage
Phantom Pain affects all Ghost-type moves including:
- **Physical moves**: Shadow Punch, Shadow Claw, Phantom Force
- **Special moves**: Shadow Ball, Ominous Wind, Hex
- **Status moves**: Confuse Ray, Spite (if they deal damage)
- **Signature moves**: Shadow Storm, Astral Barrage
- **Z-moves**: Never-Ending Nightmare and Ghost-type Z-moves

### Ability Interactions
- **Mold Breaker**: Cannot bypass Phantom Pain as it's offensive ability
- **Scrappy**: Redundant with Phantom Pain for Ghost vs Normal
- **Normalize**: Doesn't conflict - affects move type before Phantom Pain
- **Ability suppression**: Gastro Acid, Neutralizing Gas disable Phantom Pain

### Strategic Implications
- **Coverage expansion**: Allows Ghost-types to hit Normal-types for neutral damage
- **Anti-Normal**: Excellent against Normal-type walls and tanks
- **STAB utilization**: Ghost-types can use their STAB moves more freely
- **Niche utility**: Situational but powerful against Normal-heavy teams
- **Prediction reward**: Rewards predicting Normal-type switches

### Common Users
- Ghost-type Pokemon seeking better coverage
- Mixed attackers with Ghost-type moves
- Pokemon that struggle against Normal-type walls
- Competitive Ghost-types in formats with many Normal-types

### Competitive Usage Notes
- **Meta dependent**: More valuable in Normal-type heavy metagames
- **Coverage tool**: Provides reliable neutral coverage option
- **Switch punishment**: Discourages Normal-type pivots
- **Team support**: Benefits entire team's Ghost-type move users
- **Niche but impactful**: Situational ability with high impact when relevant

### Counters
- **Type immunity**: Steel types still immune to Poison moves
- **Resist berries**: Berries still reduce super-effective damage
- **Ability suppression**: Gastro Acid, Simple Beam, Neutralizing Gas
- **Non-Ghost moves**: Ability only affects Ghost-type moves
- **Protect variants**: King's Shield, Spiky Shield still work

### Synergies
- **Ghost-type STAB**: Maximizes Ghost-type move utility
- **Choice items**: Allows Ghost-type Choice item users more flexibility
- **Hex setup**: Makes Hex more reliable after status infliction
- **Shadow Ball**: Special Ghost move becomes universally neutral
- **Will-O-Wisp combo**: Burn + Hex combo works on all types

### Unique Characteristics
- **Type chart modifier**: One of few abilities that directly changes type effectiveness
- **Offensive utility**: Purely offensive benefit with no defensive component
- **Universal effect**: Benefits any Ghost-type move user on the team
- **Meta shifting**: Can change viability of Ghost-type Pokemon significantly

### Version History
- Elite Redux exclusive ability
- Part of the expanded ability roster for enhanced competitive depth
- Designed to address Ghost-type coverage limitations
- Provides unique type interaction manipulation