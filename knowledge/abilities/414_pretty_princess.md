---
id: 414
name: Pretty Princess
status: reviewed
character_count: 96
---

# Pretty Princess - Ability ID 414

## In-Game Description
"Does 50% more damage if the target has any lowered stat."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Pretty Princess increases the user's damage by 50% against targets with any negative stat stage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Pretty Princess is an offensive ability that provides a significant damage boost against statistically weakened opponents. The ability increases damage output by 50% whenever the target has any stat stage below the default value of 6.

### Activation Conditions
- **Stat requirement**: Target must have at least one stat stage below 6 (default)
- **Stat types checked**: All battle stats (Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, Evasion)
- **Attack types**: Works with all physical and special moves
- **Timing**: Calculated during damage calculation phase

### Technical Implementation
```c
constexpr Ability PrettyPrincess = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (!IsUnaware(battler) && HasAnyLoweredStat(target)) MUL(1.5);
        },
};

// HasAnyLoweredStat checks all battle stats
bool8 HasAnyLoweredStat(u8 battler) {
    u8 i;
    for (i = STAT_ATK; i < NUM_BATTLE_STATS; i++) {
        if (CompareStat(battler, i, DEFAULT_STAT_STAGE, CMP_LESS_THAN)) return TRUE;
    }
    return FALSE;
}
```

### Stat Stage System
- **Default stage**: 6 (no modifier)
- **Lowered stages**: 0-5 (negative modifiers)
- **Raised stages**: 7-12 (positive modifiers)
- **Pretty Princess triggers**: When any stat is at stage 0-5

### Damage Calculation
- **Base multiplier**: 1.5x (50% increase)
- **Stacking**: Multiplies with other offensive modifiers
- **Type effectiveness**: Applied after type effectiveness calculation
- **Critical hits**: Works normally with critical hit damage

### Common Trigger Sources
**Opponent moves that lower stats:**
- Intimidate (lowers Attack)
- Growl, Leer, Scary Face
- Stat-lowering attacks (Charm, Sweet Scent, etc.)
- Overheat, Draco Meteor (self-lowering)

**Self-inflicted stat drops:**
- Close Combat (lowers Defense/Special Defense)
- Superpower (lowers Attack/Defense)
- V-create (lowers Defense/Special Defense/Speed)

### Important Interactions
- **Unaware immunity**: Doesn't work if the user has Unaware ability
- **Contrary**: Works against Contrary users who lower their own stats
- **Moody**: Triggers if Moody lowers any stat
- **White Smoke/Clear Body**: Prevents stat lowering, preventing activation
- **Defiant/Competitive**: These abilities raise stats when lowered, but Pretty Princess still triggers

### Strategic Applications
- **Anti-Intimidate**: Punishes Intimidate users by doing extra damage
- **Setup counter**: Effective against mixed setup sweepers who lower some stats
- **Pivot punishment**: Hits hard against U-turn/Volt Switch users who got Intimidated
- **End-game closer**: Strong against weakened late-game opponents

### Stat Drop Examples That Trigger
**Attack stage examples:**
- Stage 6 (default): No bonus
- Stage 5 (-1): Pretty Princess activates
- Stage 0 (-6): Pretty Princess activates
- Stage 7 (+1): No bonus

### Competitive Viability
- **Niche but powerful**: Very situational but provides significant damage boost
- **Meta dependent**: More valuable in metas with common stat-lowering moves
- **Prediction required**: Best used when expecting stat drops
- **Anti-meta tool**: Counters defensive strategies that rely on stat manipulation

### Counters and Limitations
- **Stat immunity**: Clear Body, White Smoke, Hyper Cutter prevent triggering
- **Unaware users**: Cannot benefit if user has Unaware
- **Clean targets**: Ineffective against unbuffed/undebuffed opponents  
- **One-time use**: Opponent may avoid stat drops after seeing the ability

### Synergies
- **Choice items**: Provides even more power when locked into moves
- **Life Orb**: Stacks with Life Orb for massive damage
- **STAB moves**: Combines with Same Type Attack Bonus for huge damage
- **Super effective moves**: Multiplicative with type effectiveness

### Team Building Considerations
- **Intimidate support**: Team with Intimidate users to guarantee triggers
- **Pivot synergy**: Works well with slow pivots that get Intimidated
- **Late-game sweeper**: Excellent on revenge killers and cleanup sweepers
- **Anti-setup role**: Put on Pokemon that check setup sweepers

### Version History
- Elite Redux exclusive ability
- Part of the expanded ability roster for enhanced competitive depth
- Designed to counter stat-manipulation strategies