---
id: 48
name: Early Bird
status: reviewed
character_count: 100
---

# Early Bird - Ability ID 48

## In-Game Description
"Awakens twice as fast from sleep."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Allows the user to wake up from sleep twice as fast. Subtract 2 sleep turns every turn instead of 1. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**EARLY_BIRD** is a status condition protection ability that reduces the duration of sleep by making the Pokemon wake up twice as fast.

### Sleep Mechanics Overview:
- **Sleep Status**: Uses first 3 bits of status1 (STATUS1_SLEEP = bits 0-2)
- **Sleep Counter**: Stored as turns remaining (1-7 possible values)
- **Initial Duration**: Sleep moves typically set 1-3 turns randomly
- **Wake-up Check**: Occurs at start of each turn before move selection

### Early Bird Activation:
- **Trigger**: Every turn while the Pokemon has sleep status
- **Effect**: Subtracts 2 from sleep counter instead of 1
- **Location**: Implemented in both `battle_util.c` and `battle_util2.c`
- **No Message**: No special text displayed when Early Bird activates

### Technical Implementation:
**In battle_util.c (move usage context):**
```c
u8 toSub;
if (BATTLER_HAS_ABILITY(gBattlerAttacker, ABILITY_EARLY_BIRD))
    toSub = 2;
else
    toSub = 1;

if ((gBattleMons[gBattlerAttacker].status1 & STATUS1_SLEEP) < toSub)
    gBattleMons[gBattlerAttacker].status1 &= ~(STATUS1_SLEEP);
else
    gBattleMons[gBattlerAttacker].status1 -= toSub;
```

**In battle_util2.c (end-of-turn context):**
```c
u32 toSub;
if (BattlerHasAbility(battlerId, ABILITY_EARLY_BIRD, FALSE))
    toSub = 2;
else
    toSub = 1;
```

### Sleep Duration Examples:
1. **Normal Pokemon**:
   - Turn 1: Sleep 3 to Sleep 2 (can't act)
   - Turn 2: Sleep 2 to Sleep 1 (can't act)  
   - Turn 3: Sleep 1 to Awake (can act)
   - **Total**: 2 turns asleep

2. **Early Bird Pokemon**:
   - Turn 1: Sleep 3 to Sleep 1 (can't act)
   - Turn 2: Sleep 1 to Awake (can act)
   - **Total**: 1 turn asleep

3. **Edge Cases**:
   - Sleep 1 to Always wakes up immediately (both normal and Early Bird)
   - Sleep 2 to Normal: 1 turn asleep, Early Bird: wakes immediately

### Interaction Rules:
- **Works Against**: All sleep-inducing moves (Sleep Powder, Spore, Hypnosis, etc.)
- **Works Against**: Sleep from abilities (Effect Spore when it triggers sleep)
- **Works Against**: Sleep from items or other effects
- **Does NOT Work**: Against Pokemon already asleep when switching in (doesn't cure existing sleep faster)
- **Stackable**: If sleep counter is set to maximum (7), still reduces by 2 per turn

### Move Interactions:
- **Sleep Talk/Snore**: Still usable while asleep, but Early Bird will wake up faster
- **Rest**: Duration halved from 2 turns to 1 turn of sleep
- **Dream Eater**: Opponent wakes up faster, reducing Dream Eater opportunities

### Competitive Analysis:
**Strengths:**
- Hard counter to sleep-based strategies
- Reduces Rest downtime significantly  
- Maintains momentum against sleep moves
- No drawbacks or negative effects

**Weaknesses:**
- Very situational - only useful when sleep is a factor
- No benefit against most common status conditions
- AI rates it only 4/10 in utility value
- Cannot prevent initial sleep, only reduces duration

**Synergies:**
- Rest users (particularly bulky Pokemon)
- Pokemon vulnerable to sleep moves in their meta
- Sleep Talk users (wake up to use regular moves sooner)

**Counters:**
- Status moves other than sleep (burn, poison, paralysis)
- Direct damage strategies that don't rely on sleep
- Moves with secondary effects rather than sleep focus

### Notable Users:
Early Bird is naturally found on several Normal-type and bird Pokemon species, making it thematically appropriate for early-rising creatures.

### Version History:
- Consistent behavior since Gen 3
- Elite Redux: No changes to core mechanic, maintains standard "subtract 2 instead of 1" functionality