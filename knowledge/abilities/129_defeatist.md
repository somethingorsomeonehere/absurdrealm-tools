---
id: 129
name: Defeatist
status: reviewed
character_count: 127
---

# Defeatist - Ability ID 129

## In-Game Description
"Halves Attack and Special Attack when HP drops below 33%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Halves both Attack and Special Attack stats when HP drops below 33% of maximum. Deactivates after healing above this threshold.

## Detailed Mechanical Explanation

### Activation Threshold
- Activates when HP <= 33.33% (1/3) of maximum HP
- The exact threshold is calculated as `hp <= maxHP / 3`
- Deactivates immediately when healed above the threshold

### Stat Reduction
- Attack stat is halved (divided by 2)
- Special Attack stat is halved (divided by 2)
- Other stats remain unaffected
- The reduction applies to the final calculated stat value

### Implementation Details
From `abilities.cc`:
```cpp
constexpr Ability Defeatist = {
    .onStat =
        +[](ON_STAT) {
            if (statId != STAT_ATK && statId != STAT_SPATK) return;
            if (gBattleMons[battler].hp <= gBattleMons[battler].maxHP / 3) *stat /= 2;
        },
};
```

## Pokemon with Defeatist

### Archen (Innate)
- **Stats**: 55 HP / 112 Atk / 45 Def / 74 SpA / 45 SpD / 70 Spe
- **Types**: Rock/Flying
- **Other Abilities**:
  - Changeable: Opportunist, Rock Head, Unburden
  - Innate: Defeatist, Grounded, Fossilized

### Archeops (Innate)
- **Stats**: 75 HP / 140 Atk / 65 Def / 112 SpA / 65 SpD / 110 Spe
- **Types**: Rock/Flying
- **Other Abilities**:
  - Changeable: Opportunist, Predator, Reckless
  - Innate: Defeatist, Fossilized, Rock Head

## Strategic Implications

### Drawbacks
1. **Severe Power Loss**: Both physical and special attacks become significantly weaker
2. **HP Management Pressure**: Must maintain HP above 33% to remain effective
3. **Vulnerability**: Becomes an easy target when weakened
4. **Mixed Attacker Penalty**: Affects both attack stats, limiting offensive options

### Counterplay Strategies
1. **Priority Moves**: Use priority attacks before falling below threshold
2. **Healing Items**: Sitrus Berry, recovery moves to stay above 33%
3. **Hit-and-Run**: U-turn/Volt Switch to preserve HP
4. **Substitute**: Prevent HP from dropping below threshold
5. **Focus Sash**: Ensure at least one strong hit

### Team Support
1. **Wish Support**: Pass Wishes to heal above threshold
2. **Healing Wish**: Full restoration when needed
3. **Screens**: Reduce damage to maintain HP
4. **Hazard Control**: Prevent chip damage
5. **Speed Control**: Tailwind support for Archeops

## Competitive Analysis

### Viability Issues
- Defeatist severely limits the viability of affected Pokemon
- Archeops has excellent 140 Attack and 110 Speed, but Defeatist makes it unreliable
- The ability essentially creates a timer on the Pokemon's effectiveness

### Niche Uses
1. **Lead Role**: Maximum impact early before taking damage
2. **Choice Scarf**: Outspeed and KO before taking hits
3. **Endeavor Sets**: Turn low HP into an advantage
4. **Acrobatics**: No item for maximum Flying STAB power

### Item Considerations
- **Sitrus Berry**: Automatic healing at 50% HP
- **Focus Sash**: Guarantee survival from full HP
- **Choice Items**: Maximize damage output while healthy
- **White Herb**: Restore stats if affected by drops

## Ability Interactions

### Ability Suppression
- Neutralizing Gas removes Defeatist's effect
- Skill Swap can transfer this burden to opponents
- Worry Seed/Simple Beam won't work (innate ability)

### Stat Modifications
- Defeatist's reduction stacks with other stat changes
- Swords Dance at low HP: +2 stages but still halved
- The halving occurs after all other modifications

## Historical Context
Defeatist represents Game Freak's attempt to balance potentially overpowered fossil Pokemon. Archeops's 140 Attack and 110 Speed would make it a top-tier threat without this limitation. The ability creates a high-risk, high-reward dynamic that defines these Pokemon's playstyle.

