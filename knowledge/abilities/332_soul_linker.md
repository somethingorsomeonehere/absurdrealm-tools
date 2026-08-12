---
id: 332
name: Soul Linker
status: reviewed
character_count: 263
---

# Soul Linker - Ability ID 332

## In-Game Description
"Enemies take all the damage they deal, same for this Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user takes a direct hit, the opponent takes identical damage. When landing a direct hit, the user also takes the same damage it inflicts. Does not activate when either Pokemon is knocked out, taking damage from Pain Split, or against another Soul Linker.

## Detailed Mechanical Explanation

### Basic Information
- **Name**: Soul Linker
- **ID**: 332
- **Type**: Defensive/Retaliation ability
- **Category**: Damage Reflection

### Mechanics

### Core Functionality
- **Bidirectional Damage Reflection**: Unlike typical retaliation abilities, Soul Linker works in both directions:
  - When the Soul Linker user is attacked, the attacker takes the same damage
  - When the Soul Linker user attacks, it also takes the same damage it deals

### Technical Implementation
- **Trigger Condition**: Uses `ON_EITHER` macro, activating both as attacker and defender
- **Damage Type**: Applies passive damage that ignores Substitute and Disguise
- **HP Updates**: Properly updates health bars and data for both Pokemon
- **Fainting Logic**: Can cause either or both Pokemon to faint simultaneously

### Restrictions and Interactions
1. **Soul Linker Immunity**: Cannot affect other Pokemon with Soul Linker (prevents infinite loops)
2. **Pain Split Exception**: Does not trigger on Pain Split move
3. **Alive Check**: Only triggers if the Soul Linker user is still alive
4. **Hit Effect Requirements**: Must pass standard hit effect checks

### Strategic Applications
- **Mutual Assured Destruction**: Forces opponents to consider the cost of attacking
- **Sweeper Counter**: Particularly effective against high-damage sweepers
- **Focus Sash Synergy**: Works well with Focus Sash to guarantee retaliation
- **Defensive Wall Support**: Can deter physical attackers from targeting defensive Pokemon

## Pokemon With Soul Linker
- **Sableye**: Listed in trainer data as having Soul Linker as ability slot 2
  - Often paired with Focus Sash for defensive utility
  - Used as a defensive wall with Soul Linker

## Code Implementation

### Location
- **Definition**: `src/abilities.cc` (lines around SoulLinker implementation)
- **Battle Script**: `data/battle_scripts_1.s` (BattleScript_AttackerSoulLinker)
- **Header**: `include/generated/constants/abilities.h` (ABILITY_SOUL_LINKER = 332)

### Implementation Details
```cpp
ON_EITHER(SoulLinker) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(IsBattlerAlive(battler))
    CHECK_NOT(BATTLER_HAS_ABILITY(opponent, ABILITY_SOUL_LINKER))
    CHECK(move != MOVE_PAIN_SPLIT)

    BattleScriptCall(BattleScript_AttackerSoulLinker);
    return TRUE;
}
```

### Battle Script Behavior
The battle script performs:
1. Shows ability pop-up
2. Sets passive damage flags (ignores Substitute/Disguise)
3. Updates attacker's health bar and data
4. Checks for fainting
5. Returns control to battle flow

## Competitive Analysis

### Strengths
- **Universal Deterrent**: Works against all damage types and moves
- **No Cost Activation**: Triggers automatically without consuming turns
- **Guaranteed Retaliation**: Cannot be prevented by most abilities
- **Symmetric Effect**: Affects both offensive and defensive scenarios equally

### Weaknesses
- **Self-Damage**: User takes damage when attacking, limiting offensive potential
- **Status Vulnerability**: Provides no protection against status moves
- **Healing Disadvantage**: Opponent can heal while user cannot without risk
- **Priority Moves**: Can be overwhelmed by multiple weak priority moves

### Ideal Usage Scenarios
1. **Defensive Cores**: Paired with recovery moves and defensive stats
2. **Revenge Killing**: With Focus Sash to guarantee at least one retaliation
3. **Anti-Sweeper**: Deterring setup sweepers and glass cannons
4. **Stall Teams**: Discouraging direct attacks in favor of passive damage

## Related Abilities
- **Magic Guard**: Protects from indirect damage, making Soul Linker safer
- **Rough Skin/Iron Barbs**: Similar retaliation concept but only when attacked
- **Counter/Mirror Coat**: Move-based versions with similar effects

## Trivia
- One of the few abilities that affects both attacking and defending
- The name suggests a spiritual or mystical connection between battlers
- Unique among retaliation abilities for its perfect damage mirroring
- Implementation carefully prevents infinite loops between multiple Soul Linker users