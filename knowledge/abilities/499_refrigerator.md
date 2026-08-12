---
id: 499
name: Refrigerator
status: reviewed
character_count: 194
---

# Refrigerator - Ability ID 499

## In-Game Description
"Filter + Illuminate."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super effective attacks by 35%. Multiplicative with other damage reduction sources. Boosts the user's accuracy by 1.2x. Removes Ghost-typing on target when landing an attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Refrigerator combines defensive damage reduction with offensive accuracy enhancement, representing a well-organized, methodical approach that both protects from weaknesses and ensures reliable attack execution.

### Dual Effect Components

#### Filter Component (Defensive)
- **Trigger**: When taking super-effective damage (2.0x or higher)
- **Effect**: Reduces damage to 65% of calculated amount
- **Calculation**: damage *= 0.65 (35% reduction)
- **Coverage**: Works against all super-effective moves
- **Suppression**: Breakable by Mold Breaker effects

#### Illuminate Component (Offensive)
- **Effect**: Multiplies accuracy of all user's moves by 1.2 (20% boost)
- **Coverage**: Affects every move used by the Pokemon
- **Calculation**: accuracy *= 1.2
- **Priority**: ACCURACY_MULTIPLICATIVE for proper order
- **Reliability**: Makes unreliable moves more consistent

### Technical Implementation
```c
constexpr Ability Refrigerator = {
    .onDefensiveMultiplier = Filter.onDefensiveMultiplier,
    .onAccuracy = Illuminate.onAccuracy,
    .breakable = TRUE,
};

// Filter component
.onDefensiveMultiplier = +[](ON_DEFENSIVE_MULTIPLIER) {
    if (typeEffectivenessModifier >= UQ_4_12(2.0)) MUL(0.65);
}

// Illuminate component  
.onAccuracy = +[](ON_ACCURACY) {
    MUL(1.2);
    return ACCURACY_MULTIPLICATIVE;
}
```

### Damage Reduction Examples
**2x super-effective attacks:**
- Original damage: 200 HP
- With Filter: 130 HP (65% of original)
- **Damage saved**: 70 HP (35% reduction)

**4x super-effective attacks:**
- Original damage: 400 HP
- With Filter: 260 HP (65% of original)  
- **Damage saved**: 140 HP (35% reduction)

### Accuracy Enhancement Examples
**Moves with perfect accuracy (100%):**
- Remains 100% (already perfect)
- No practical change but mathematically boosted

**Moves with 90% accuracy:**
- Boosted to 108% to capped at 100%
- **Benefit**: Perfect accuracy for near-perfect moves

**Moves with 80% accuracy:**
- Boosted to 96% accuracy
- **Benefit**: Much more reliable

**Moves with 70% accuracy:**
- Boosted to 84% accuracy
- **Benefit**: Significantly improved reliability

### Strategic Applications
- **Defensive tank**: Survives super-effective attacks better
- **Reliable offense**: More consistent move accuracy
- **Balanced utility**: Both defensive and offensive benefits
- **Type coverage**: Enhanced survival against weaknesses
- **Accuracy moves**: Makes powerful but inaccurate moves viable

### Move Synergy Examples
**High-power, low-accuracy moves:**
- Hydro Pump (110 BP, 80% acc) to 96% accuracy
- Fire Blast (110 BP, 85% acc) to 100% accuracy
- Thunder (110 BP, 70% acc) to 84% accuracy
- Blizzard (110 BP, 70% acc) to 84% accuracy

**Perfect accuracy moves:**
- All moves maintain 100% accuracy
- Mathematical boost doesn't exceed accuracy cap

### Competitive Usage
- **Bulky attacker**: Survives hits while dealing reliable damage
- **Type disadvantage fighter**: Handles super-effective coverage better
- **Accuracy abuser**: Uses normally unreliable powerful moves
- **Balanced role**: Neither purely defensive nor offensive
- **Consistent performer**: Reliable in both offense and defense

### Super-Effective Coverage
**Common super-effective types to resist:**
- Ice vs Grass/Flying/Dragon (common coverage)
- Fighting vs Normal/Steel (widespread moves)
- Rock vs Fire/Flying/Bug (entry hazards/attacks)
- Electric vs Water/Flying (common types)

### Item Synergies
**Defensive items:**
- Leftovers: Sustain while tanking reduced damage
- Sitrus Berry: Emergency healing after surviving hits
- Assault Vest: Stack special bulk with damage reduction

**Offensive items:**
- Life Orb: Amplify reliable attacks
- Choice items: Guaranteed accuracy with power boost
- Expert Belt: Boost super-effective moves you can now land

### Limitations
- **Ability suppression**: Breakable by Mold Breaker effects
- **Normal effectiveness**: No damage reduction vs neutral hits
- **Accuracy cap**: Can't exceed 100% accuracy
- **Passive ability**: No active components or triggers
- **Type immunity**: Super-effective reduction doesn't help vs immunities

### Counters
- **Mold Breaker family**: Suppresses both defensive and offensive benefits
- **Normal effectiveness moves**: Bypass damage reduction entirely
- **Status moves**: Accuracy boost doesn't help vs non-damaging moves
- **Multi-hit moves**: Each hit gets damage reduction but total adds up
- **Critical hits**: Can still bypass damage reduction

### Double Battle Applications
- **Reliable spread moves**: Accuracy boost helps multi-target attacks
- **Tank role**: Survives super-effective spread moves better
- **Support utility**: Consistent accuracy for team support moves
- **Field presence**: Balanced offensive and defensive utility

### Team Building
**Ideal team support:**
- Entry hazard setters: Accuracy boost helps hazard moves
- Status spreaders: Reliable status move accuracy
- Coverage users: Makes diverse movesets more reliable
- Defensive cores: Adds another layer of bulk

### Comparison to Component Abilities
**vs Pure Filter:**
- Adds offensive utility with accuracy boost
- More balanced than purely defensive
- Better overall battle impact

**vs Pure Illuminate:**
- Adds significant defensive utility
- Much more viable in competitive play
- Balanced risk-reward profile

### Version History
- Elite Redux custom ability combining utility effects
- Designed for balanced offensive-defensive gameplay
- Part of hybrid ability design philosophy
- Represents methodical, well-prepared battle approach

### Advanced Strategy
**Damage calculation awareness:**
- Learn common super-effective damage ranges
- Plan around 35% damage reduction
- Use accuracy boost for coverage moves

**Move selection optimization:**
- Prioritize powerful but inaccurate moves
- Use coverage moves more confidently
- Build movesets around reliability