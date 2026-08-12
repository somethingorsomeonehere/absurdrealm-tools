---
id: 494
name: Arcane Force
status: reviewed
character_count: 195
---

# Arcane Force - Ability ID 494

## In-Game Description
"Mystic Power + super-effective boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants the 1.5x STAB damage bonus to all moves regardless of type matching. Does not boost moves that already receive a STAB bonus. Additionally, boosts the power of super effective moves by 10%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Arcane Force is a powerful hybrid ability that combines universal STAB with super-effective move amplification, representing mastery over mystical energies that transcend normal type limitations.

### Universal STAB Component
- **Effect**: All moves receive STAB bonus regardless of type matching
- **Multiplier**: Standard 1.5x STAB damage boost
- **Coverage**: Every move gains the Same Type Attack Bonus
- **Versatility**: No type restrictions on STAB eligibility

### Super-Effective Boost Component
- **Trigger**: When attack type effectiveness ≥ 2.0x (super-effective)
- **Boost**: Additional 10% damage multiplier (1.1x)
- **Stacking**: Multiplies with existing super-effective damage
- **Result**: 2.0x becomes 2.2x, 4.0x becomes 4.4x

### Technical Implementation
```c
constexpr Ability ArcaneForce = {
    .onStab = MysticPower.onStab,  // Universal STAB
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
        if (gTypeEffectiveness >= UQ_4_12(2.0)) MUL(1.1);
    },
};
```

### Damage Calculation Examples
**Normal effectiveness (1.0x):**
- Base move: 100 damage
- With STAB: 150 damage (1.5x)
- No super-effective boost
- **Final: 150 damage**

**Super-effective (2.0x):**
- Base move: 100 damage  
- With type effectiveness: 200 damage (2.0x)
- With STAB: 300 damage (1.5x)
- With super-effective boost: 330 damage (1.1x)
- **Final: 330 damage**

**Double super-effective (4.0x):**
- Base move: 100 damage
- With type effectiveness: 400 damage (4.0x)
- With STAB: 600 damage (1.5x)
- With super-effective boost: 660 damage (1.1x)
- **Final: 660 damage**

### Strategic Applications
- **Universal coverage**: Every move becomes a STAB move
- **Type flexibility**: No need to match move types to Pokemon types
- **Super-effective punishment**: Extra damage against weaknesses
- **Coverage moves**: Status moves, Hidden Power, etc. all get STAB
- **Consistent power**: Reliable damage across all moves

### Move Synergies
**Excellent with:**
- Coverage moves (Thunderbolt on non-Electric types gets STAB)
- Hidden Power (Always STAB regardless of type)
- Status moves with damage (Knock Off, etc.)
- Multi-type movesets (Every move benefits equally)
- Super-effective coverage (Maximum damage potential)

### Competitive Applications
- **Mixed attackers**: Both physical and special moves get STAB
- **Coverage specialists**: Makes all coverage moves significantly stronger
- **Type-breaking**: Non-STAB moves become as strong as STAB moves
- **Super-effective sweepers**: Enhanced damage against weaknesses
- **Versatile attackers**: No move selection restrictions

### Limitations
- **No defensive benefits**: Purely offensive ability
- **Resistances still apply**: Doesn't overcome type resistances
- **Immunity unchanged**: Type immunities still block moves completely
- **Ability dependence**: Lost if ability is suppressed

### Counters
- **Mold Breaker family**: Suppresses the ability entirely
- **Type immunities**: Still block moves completely
- **Defensive walls**: High bulk can still tank boosted attacks
- **Priority moves**: Fast attacks can prevent setup

### Comparison to Component Abilities
- **vs Mystic Power**: Adds super-effective boost for extra damage
- **vs Neuroforce**: Universal STAB vs higher super-effective boost
- **vs Adaptability**: Universal coverage vs double STAB
- **vs type boosters**: Works on all moves vs single type

### Version History
- Elite Redux custom ability combining two powerful effects
- Designed for ultimate offensive versatility
- Part of the expanded ability system for enhanced strategic options
- Represents mastery of mystical energies beyond type limitations