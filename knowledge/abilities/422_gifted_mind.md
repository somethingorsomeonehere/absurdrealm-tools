---
id: 422
name: Gifted Mind
status: reviewed
character_count: 191
---

# Gifted Mind - Ability ID 422

## In-Game Description
"Nulls Psychic weakness; status moves always hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gifted Mind grants immunity to Dark, Ghost, and Bug-type moves while making all status moves used by this Pokemon never miss. This immunity ignores Inverse Room. 

*For Discord/reference use*

### Core Mechanics
Gifted Mind is a dual-function ability that provides both defensive immunity and offensive utility. It completely nullifies damage from Dark, Ghost, and Bug-type moves while ensuring perfect accuracy for all status moves used by the wielder.

### Defensive Component - Type Immunity
- **Immunity types**: Dark, Ghost, and Bug-type moves deal 0 damage
- **Coverage**: These three types cover the most common weaknesses of Psychic-type Pokemon
- **Interaction**: Works like type immunity - no damage, no secondary effects
- **Priority**: Applied during damage calculation phase

### Offensive Component - Status Move Accuracy
- **Accuracy boost**: All status moves have 100% accuracy regardless of base accuracy
- **Move types affected**: Any move classified as a status move
- **Overrides**: Bypasses accuracy checks, evasion boosts, and accuracy reductions
- **Limitations**: Does not affect damaging moves, only pure status moves

### Technical Implementation
```c
// Defensive immunity check in battle_util.c (line 7831-7832)
if ((moveType == TYPE_DARK || moveType == TYPE_GHOST || moveType == TYPE_BUG) && 
    (BATTLER_HAS_ABILITY(battlerDef, ABILITY_GIFTED_MIND)))
    modifier = UQ_4_12(0.0);  // Set damage to 0

// Status move accuracy in battle_ai_util.c (line 1174)
if (BattlerHasAbility(battlerAtk, ABILITY_GIFTED_MIND, FALSE) && IS_MOVE_STATUS(move)) 
    return TRUE;  // Always hits
```

### AI Considerations
The AI recognizes both aspects of this ability:
- **Defensive AI**: Will avoid using Dark, Ghost, or Bug-type moves against Gifted Mind users
- **Offensive AI**: Factors in guaranteed status move accuracy when predicting outcomes

### Important Interactions
- **Type immunity**: Functions like Wonder Guard but for specific types
- **Status moves**: Affects moves like Thunder Wave, Will-O-Wisp, Sleep Powder
- **Secondary effects**: Immunity prevents secondary effects from blocked moves
- **Multi-hit moves**: Each hit is blocked individually
- **Ability bypass**: Mold Breaker and similar abilities can overcome the immunity
- **Status immunity**: Does not grant immunity to status conditions themselves

### Strategic Applications
- **Psychic-type support**: Perfect for Psychic-types weak to Dark/Ghost/Bug
- **Utility Pokemon**: Excellent for support Pokemon that rely on status moves
- **Counter-meta**: Hard counters common offensive types
- **Team support**: Reliable status spreaders and support Pokemon

### Counters and Limitations
- **Other move types**: Still vulnerable to other types like Flying, Electric, etc.
- **Damaging moves**: Does not affect damaging move accuracy
- **Ability suppression**: Mold Breaker, Neutralizing Gas bypass immunity
- **Status immunity**: Targets with status immunity still aren't affected by status moves
- **Substitute/Magic Bounce**: Can still block status moves through other means

### Synergies
- **Status moves**: Thunder Wave, Will-O-Wisp, Sleep Powder, Toxic
- **Psychic-type pairing**: Natural fit for Psychic-types' defensive profile
- **Support movesets**: Works well with utility and support-focused strategies
- **Team cores**: Excellent on teams needing reliable status support

### Common Status Moves Enhanced
- **Thunder Wave**: Paralysis support with perfect accuracy
- **Will-O-Wisp**: Burn spreading with no miss chance
- **Sleep Powder**: Sleep inducement with 100% accuracy
- **Toxic**: Poison spreading without accuracy concerns
- **Hypnosis**: Sleep moves become perfectly reliable

### Version History
- Elite Redux exclusive ability
- ID 422 in the ability list
- Combines defensive immunity with offensive utility
- Designed to support Psychic-type viability and utility Pokemon

### Competitive Usage Notes
- Excellent on support Pokemon that need reliable status moves
- Provides defensive backbone for Psychic-types
- Creates interesting team-building decisions around type coverage
- Particularly strong in formats where Dark/Ghost/Bug moves are common
- Can enable unique strategies combining immunity with status support