---
id: 39
name: Inner Focus
status: reviewed
character_count: 69
---

# Inner Focus - Ability ID 39

## In-Game Description
"Blocks flinch, Intimidate, Scare. Focus Blast never misses."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Focus Blast never misses. Unaffected by flinch, Intimidate, or Scare.

## Detailed Mechanical Explanation
*For Discord/reference use*

**INNER FOCUS** is a defensive ability that provides immunity to certain status conditions and battlefield effects while enhancing Focus Blast accuracy.

### Primary Immunities:
- **Flinching**: Complete immunity to flinch status from moves and abilities
- **Intimidate Effects**: Immune to all Intimidate-clone abilities that lower stats:
  - Intimidate (lowers Attack)
  - Scare (lowers Special Attack)
  - Fearmonger (lowers Attack and Special Attack)
  - Yuki Onna (lowers Attack and Special Attack)
  - Terrify, Malicious, and other Intimidate variants
- **Taunt Effects**: Immune to Taunt status condition

### Special Move Interaction:
- **Focus Blast**: When the user attempts Focus Blast (normally 70% accuracy), Inner Focus grants perfect accuracy
- This makes Focus Blast effectively 100% accurate, significantly improving its viability

### Technical Implementation:
```c
constexpr Ability InnerFocus = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(move == MOVE_FOCUS_BLAST)
        return ACCURACY_ALWAYS_HITS;
    },
    .breakable = TRUE,
    .tauntImmune = TRUE,
};
```

### Intimidate Immunity Mechanics:
- Uses the `tauntImmune = TRUE` flag which is checked by `IsBattlerImmuneToLowerStatsFromIntimidateClone()`
- When an Intimidate-clone ability activates, Inner Focus users are completely unaffected
- No stat changes occur, and no battle message is displayed for the immune Pokemon

### Breakable Property:
- **Mold Breaker Effects**: Inner Focus can be bypassed by Mold Breaker, Teravolt, Turboblaze, and similar abilities
- When suppressed, the Pokemon loses all immunities and Focus Blast accuracy bonus
- This is the main counterplay to Inner Focus's defensive benefits

### Competitive Applications:
1. **Flinch Immunity**: Protects against flinch-heavy strategies (Serene Grace, Stench, King's Rock)
2. **Intimidate Cycling**: Prevents stat drops from repeated Intimidate switches
3. **Focus Blast Reliability**: Makes Focus Blast a consistent 100% accurate Fighting-type nuke
4. **Anti-Control**: Immunity to Taunt prevents status move lockdown

### Common Users:
- Primarily found on Psychic and Fighting-type Pokemon
- Often paired with Focus Blast users for maximum benefit
- Valuable on special attackers that rely on non-damaging moves

### Interaction Notes:
- Does not prevent stat drops from moves (only ability-based drops)
- Does not prevent sleep, paralysis, or other major status conditions
- Focus Blast accuracy bonus works regardless of other accuracy modifiers
- Stacks with other accuracy-boosting effects when using non-Focus Blast moves

### Version History:
- Gen 3-4: Only prevented flinching
- Gen 5+: Added Intimidate immunity
- Elite Redux: Added Taunt immunity and Focus Blast accuracy bonus