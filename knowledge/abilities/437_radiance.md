---
id: 437
name: Radiance
status: reviewed
character_count: 90
---

# Radiance - Ability ID 437

## In-Game Description
"+20% accuracy; Dark moves fail when user is present."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Radiance increases the user's accuracy by 20% for all moves and causes Dark moves to fail. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Radiance is a dual-purpose ability that provides both offensive and defensive benefits. It combines an accuracy boost with complete immunity to Dark-type moves, making it valuable for both offensive pressure and defensive utility.

### Activation Conditions
- **Accuracy boost**: Always active, applies to all moves used by the Pokemon
- **Dark-type immunity**: Always active when the Pokemon is on the field
- **No weather dependency**: Both effects work regardless of weather conditions
- **Field presence**: Dark immunity only works when the Pokemon is actively battling

### Technical Implementation
```c
// Radiance provides accuracy boost (same as Illuminate)
constexpr Ability Radiance = {
    .onImmune = +[](ON_IMMUNE) -> int {
        CHECK(moveType == TYPE_DARK);
        *immunityScript = BattleScript_RadianceProtected;
        return TRUE;
    },
    .onAccuracy = Illuminate.onAccuracy,  // 20% accuracy boost
    .onImmuneFor = APPLY_ON_ANY,
    .breakable = TRUE,
};

// Accuracy boost implementation (from Illuminate)
.onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
    *accuracy *= 1.2;  // 20% increase
    return ACCURACY_MULTIPLICATIVE;
}
```

### Accuracy Mechanics
- **Boost amount**: 20% multiplicative increase to accuracy
- **Application**: Applies to all moves, regardless of type or category
- **Stacking**: Multiplicative with other accuracy modifiers
- **Examples**: 
  - 100% accuracy moves become 120% (still can miss due to evasion)
  - 80% accuracy moves become 96%
  - 70% accuracy moves become 84%

### Dark-Type Immunity
- **Complete immunity**: All Dark-type moves fail entirely
- **No damage**: Protected moves deal 0 damage
- **Status moves**: Dark-type status moves also fail
- **Multi-hit moves**: Entire attack fails, not just individual hits
- **Message display**: Shows protection message via BattleScript_RadianceProtected

### Important Interactions
- **Ability suppression**: Both effects disabled if ability is suppressed
- **Mold Breaker**: Can bypass the Dark-type immunity
- **Neutralizing Gas**: Disables both accuracy boost and immunity
- **Wonder Guard**: Radiance immunity takes precedence over Wonder Guard
- **Type changes**: Immunity applies to moves that become Dark-type through effects

### Strategic Implications
- **Offensive utility**: Reliable accuracy for powerful but inaccurate moves
- **Defensive utility**: Complete safety from Dark-type attacks
- **Role compression**: Combines offensive and defensive benefits in one ability
- **Dark-type counter**: Hard counters Dark-type attackers and coverage moves
- **Prediction safety**: Can switch into predicted Dark moves safely

### Synergies
- **High-power moves**: Makes Thunder, Blizzard, and Focus Blast more reliable
- **Setup moves**: More reliable Hypnosis, Sleep Powder for setup
- **OHKO moves**: Improves already low accuracy of Fissure, Sheer Cold
- **Anti-Dark teams**: Excellent for teams weak to Dark coverage
- **Mixed attackers**: Benefits both physical and special accuracy

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Gastro Acid
- **Non-Dark attacks**: Doesn't protect against other types
- **Accuracy reduction**: Evasion boosts, Sand Attack still affect user
- **Priority moves**: Dark-type priority moves still fail but other priority works
- **Substitute**: Can be used to safely set up against Radiance users

### Common Users
- Pokemon that learn inaccurate but powerful moves
- Defensive Pokemon that struggle with Dark-type coverage
- Mixed attackers who benefit from consistent accuracy
- Pokemon with naturally high offensive stats but poor move accuracy

### Competitive Usage Notes
- **Tier placement**: Strong utility ability suitable for multiple formats
- **Team building**: Excellent for teams weak to common Dark moves
- **Movepool synergy**: Best on Pokemon with powerful but inaccurate moves
- **Meta consideration**: Effectiveness depends on Dark-type move prevalence
- **Ability slot value**: Competes with other powerful abilities for slot

### Version History
- New ability introduced in Elite Redux
- Combines offensive and defensive utility in unique way
- Part of the expanded ability roster for increased strategic diversity
- ID 437 in the ability enumeration system