---
id: 79
name: Rivalry
status: reviewed
character_count: 156
---

# Rivalry - Ability ID 79

## In-Game Description
"Deals 1.25x to same gender. Takes .75x from opposite gender."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's damage by 25% against same-gender Pokemon and reduces damage taken by 25% from opposite-gender Pokemon. No effect with genderless Pokemon. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**RIVALRY** is a gender-based damage modifier ability that affects both offensive and defensive calculations based on the gender matchup between battler and target.

### Activation Mechanics:
- **Trigger**: Every move used by or against the Pokemon
- **Gender Check**: Compares attacker and defender genders
- **Genderless Override**: No effect if either Pokemon is genderless

### Damage Calculations:

1. **Offensive Modifier** (when attacking):
   - Same gender: 1.25x damage multiplier
   - Opposite gender: No offensive modifier
   - Genderless target: No effect

2. **Defensive Modifier** (when defending):
   - Opposite gender attacker: 0.75x damage taken (25% reduction)
   - Same gender attacker: No defensive modifier
   - Genderless attacker: No effect

### Technical Implementation:
```c
constexpr Ability Rivalry = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            int genderAtk = GetGenderFromSpeciesAndPersonality(gBattleMons[battler].species, gBattleMons[battler].personality);
            if (genderAtk != MON_GENDERLESS && genderAtk == GetGenderFromSpeciesAndPersonality(gBattleMons[target].species, gBattleMons[target].personality))
                MUL(1.25);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            int genderAtk = GetGenderFromSpeciesAndPersonality(gBattleMons[attacker].species, gBattleMons[attacker].personality);
            if (genderAtk == MON_MALE)
                genderAtk = MON_FEMALE;
            else if (genderAtk == MON_FEMALE)
                genderAtk = MON_MALE;
            if (genderAtk != MON_GENDERLESS && genderAtk == GetGenderFromSpeciesAndPersonality(gBattleMons[battler].species, gBattleMons[battler].personality))
                MUL(.75);
        },
    .breakable = TRUE,
};
```

### Damage Examples:
- Male Nidoking vs Male Rufflet: Nidoking deals 1.25x damage, no defensive bonus
- Male Nidoking vs Female Tsareena: Normal damage dealt, takes 0.75x damage from Tsareena
- Female Nidoqueen vs Metagross (genderless): No effect either way

### Common Users:
**Regular Ability Users:**
- Nidoking line (Nidoran♂, Nidorino, Nidoking)
- Hippopotas line (Hippopotas, Hippowdon)
- Pidove evolution line (Pidove, Tranquill, Unfezant)
- Scraggy evolution line
- Ducklett evolution line
- Rufflet evolution line
- Fletchling
- Tsareena

**Innate Ability Users:**
- Nidoran♀ line (includes Nidorina, Nidoqueen)
- Various Elite Redux custom Pokemon

### Strategic Implications:
1. **Team Building**: Consider gender ratios when building teams
2. **Gender Prediction**: Useful for predicting damage ranges in competitive play
3. **Synergy**: Pairs well with other stat-boosting abilities
4. **Coverage**: Most effective in metas with diverse gender distributions

### Interactions:
- **Mold Breaker**: Ignores Rivalry entirely
- **Ability Shield**: Protects against Mold Breaker nullification
- **Transform/Imposter**: Copies gender along with species, affecting Rivalry calculations
- **Gender-changing moves**: Would affect future Rivalry calculations if such moves existed

### Counters:
- Genderless Pokemon (no effect either way)
- Mold Breaker users (ignore the ability entirely)
- Opposite-gender teams (reduce offensive power)

### Synergies:
- Life Orb/Choice items (stack with the damage boost)
- Same-gender team compositions (maximize offensive potential)
- Moves with high base power (25% boost is more valuable)

### Competitive Usage:
- **Niche Pick**: Rarely seen in competitive due to situational nature
- **Prediction Game**: Requires knowledge of opponent's team genders
- **Double Battles**: More complex interactions with multiple gender combinations
- **Breeding Strategy**: Some players breed for specific genders to optimize Rivalry

### Version History:
- Generation 4: Introduced with standard mechanics
- Elite Redux: Functions identically to mainline games
- **Breakable**: Can be suppressed by Mold Breaker and similar abilities