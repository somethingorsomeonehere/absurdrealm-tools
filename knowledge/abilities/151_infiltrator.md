---
id: 151
name: Infiltrator
status: reviewed
character_count: 79
---

# Infiltrator - Ability ID 151

## In-Game Description
"Own moves bypass Substitutes and damage reduction screens."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Allows moves to bypass the effects of screens, Safeguard, Mist, and Substitute.

## Detailed Mechanical Explanation
*For Discord/reference use*

Infiltrator provides the ability to bypass several defensive mechanics in battle:

### Core Mechanics
- **Substitute Bypass**: All moves hit through Substitute dolls as if they weren't there
- **Screen Penetration**: Ignores damage reduction from Reflect (physical), Light Screen (special), and Aurora Veil (both)
- **Mist Penetration**: Stat-lowering moves bypass Mist protection

### Technical Implementation
```cpp
constexpr Ability Infiltrator = {
    .onInfiltrate = +[](ON_INFILTRATE) -> InfiltrateType { 
        return INFILTRATE_SCREENS | INFILTRATE_SUBSTITUTE; 
    },
};
```

### Activation Conditions
- **Always Active**: No setup required, works on all moves
- **Damage Calculation**: Screens provide 50% damage reduction (33% in doubles), which Infiltrator completely negates
- **Substitute Interaction**: Moves hit the real Pokemon instead of being blocked by the doll

### Affected Screens
1. **Reflect**: Halves physical damage (bypassed)
2. **Light Screen**: Halves special damage (bypassed) 
3. **Aurora Veil**: Halves both physical and special damage (bypassed)
4. **Mist**: Prevents stat reduction (bypassed for stat-lowering moves)

### Move Interactions
- **All offensive moves** benefit from screen bypass
- **Stat-lowering moves** bypass Mist protection
- **Critical hits** naturally bypass screens, so Infiltrator provides no additional benefit for crits
- **Sound moves** naturally bypass Substitute, so overlap exists there

### Strategic Applications
- **Wall Breaking**: Excellent against defensive teams relying on screens
- **Guaranteed Damage**: Ensures moves deal expected damage without defensive interference
- **Status Application**: Stat-lowering moves always work against Mist users

### Common Users in Elite Redux
Pokemon commonly found with Infiltrator include:
- Noctowl
- Crobat 
- Seviper
- Spiritomb

### Battle Impact
Infiltrator transforms matchups against defensive teams. A 100 base power move hitting through Light Screen deals the same damage as a 200 base power move hitting normally. This makes Infiltrator users particularly valuable for breaking through defensive cores and ensuring consistent damage output.