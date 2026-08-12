---
id: 490
name: Peaceful Slumber
status: reviewed
character_count: 238
---

# Peaceful Slumber - Ability ID 490

## In-Game Description
"Sweet Dreams + Self Sufficient."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sweet Dreams restores 1/8 of maximum HP at the end of each turn when the user is asleep or has the Comatose ability. Additionally, it grants immunity to Bad Dreams damage. Restores 1/16 of the Pokemon's maximum HP at the end of each turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Peaceful Slumber is a hybrid healing ability that provides consistent recovery whether the Pokemon is asleep or awake, combining the effects of Sweet Dreams and Self Sufficient in an optimized way.

### Healing Mechanisms

#### When Asleep (Sweet Dreams Priority)
- **Base healing**: Sweet Dreams attempts to heal 1/8 max HP
- **Adjustment**: Code reduces this by 1/16 max HP
- **Net result**: 1/16 max HP healing when asleep
- **Advantage**: No first-turn restriction when sleeping

#### When Awake (Self Sufficient Fallback)
- **Standard healing**: 1/16 max HP at end of turn
- **First turn exception**: No healing on the first turn after switch-in
- **Consistency**: Reliable backup when not asleep

### Technical Implementation
```c
constexpr Ability PeacefulSlumber = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        if (SweetDreams.onEndTurn(DELEGATE_END_TURN)) {
            // Sweet Dreams activated, reduce healing by 1/16
            gBattleMoveDamage -= GetMaxHP(battler) / 16;
            return TRUE;
        }
        // Fall back to Self Sufficient if Sweet Dreams didn't activate
        return SelfSufficient.onEndTurn(DELEGATE_END_TURN);
    },
};
```

### Activation Conditions
- **Sleep healing**: Triggers when Pokemon has sleep status or Comatose ability
- **Wake healing**: Triggers when not asleep and not on first turn
- **Priority system**: Sweet Dreams is attempted first, Self Sufficient as backup
- **HP requirement**: Only heals if current HP < maximum HP

### Strategic Applications
- **Consistent recovery**: Provides healing in all battle states
- **Sleep synergy**: Works excellently with Rest users
- **Stall potential**: Reliable passive healing for defensive strategies
- **Status immunity**: Pairs well with sleep-inducing strategies
- **Tank support**: Sustains bulky Pokemon through prolonged battles

### Rest Synergy
- **Turn 1 (using Rest)**: Falls asleep, no healing yet
- **Turn 2 (asleep)**: Heals 1/16 max HP from Peaceful Slumber
- **Turn 3 (asleep)**: Heals 1/16 max HP from Peaceful Slumber
- **Turn 4 (wakes up)**: Full HP from Rest + continuous healing benefit

### Comparison to Component Abilities
- **vs Sweet Dreams**: More consistent, works when awake
- **vs Self Sufficient**: Works immediately when asleep, no first-turn wait
- **vs Regenerator**: Less healing per switch but continuous recovery
- **vs Leftovers**: Same 1/16 healing rate but as an ability

### Limitations
- **Healing amount**: Only 1/16 max HP, relatively modest
- **No stacking**: Doesn't stack with items like Leftovers
- **Full HP limit**: No healing when at maximum health
- **Ability dependence**: Lost if ability is suppressed

### Counters
- **Heal Block**: Prevents all healing from the ability
- **Ability suppression**: Mold Breaker family disables healing
- **Taunt**: Prevents Rest use for sleep synergy
- **Status moves**: Poison/burn can offset the healing

### Competitive Viability
- **Defensive tanks**: Excellent on bulky Pokemon for sustained presence
- **Rest users**: Perfect synergy with Rest strategies
- **Stall teams**: Provides passive recovery for stall archetypes
- **Status absorbers**: Can afford to take status with continuous healing
- **Longevity**: Increases overall battle endurance significantly

### Version History
- Elite Redux custom ability combining two healing effects
- Designed to provide reliable, consistent recovery
- Part of the expanded ability system for enhanced strategic options
- Optimized healing rate for balanced gameplay