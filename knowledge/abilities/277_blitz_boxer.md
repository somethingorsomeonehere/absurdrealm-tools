---
id: 277
name: Blitz Boxer
status: reviewed
character_count: 69
---

# Blitz Boxer - Ability ID 277

## In-Game Description
"At full HP, gives +1 priority to this Pokemon's punching moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Blitz Boxer grants +1 priority to all punching moves when at full HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Priority Boost**: Adds +1 priority to all punching moves when the Pokemon is at full HP
- **HP Requirement**: Must be at exactly maximum HP (gBattleMons[battler].hp == gBattleMons[battler].maxHP)
- **Move Classification**: Uses the same move list as Iron Fist ability (FLAG_IRON_FIST_BOOST)

### Technical Implementation
```c
constexpr Ability BlitzBoxer = {
    .onPriority = +[](ON_PRIORITY) -> int {
        CHECK(IsIronFistBoosted(battler, move))
        CHECK(BATTLER_MAX_HP(battler));
        return 1;
    },
};
```

The ability checks two conditions:
1. `IsIronFistBoosted(battler, move)` - Confirms the move has FLAG_IRON_FIST_BOOST
2. `BATTLER_MAX_HP(battler)` - Confirms HP equals maximum HP

### Affected Moves
All moves with FLAG_IRON_FIST_BOOST, including:
- **Mach Punch** (already +1 priority, becomes +2)
- **Fire Punch** (75 BP Fire-type)
- **Ice Punch** (75 BP Ice-type) 
- **Thunder Punch** (75 BP Electric-type)
- **Mega Punch** (80 BP Normal-type)
- **Comet Punch** (18 BP multi-hit Normal-type)
- **Dizzy Punch** (70 BP Normal-type with confusion chance)
- **Dynamic Punch** (100 BP Fighting-type with guaranteed confusion)
- **Focus Punch** (150 BP Fighting-type charging move)
- **Shadow Punch** (60 BP Ghost-type, never misses)
- And other punching moves flagged for Iron Fist boost

### Priority Examples
- **Mach Punch**: +1 to +2 priority (extremely fast)
- **Most Punching Moves**: 0 to +1 priority (faster than normal moves)
- **Focus Punch**: -3 to -2 priority (still slow but faster than normal)

### Activation Conditions
- **Requirement**: Pokemon must be at exactly full HP
- **Timing**: Checked at move selection/priority calculation
- **Persistence**: No lingering effects - rechecked each turn

### Strategic Implications
- **Early Game Dominance**: Powerful in the opening turns when at full HP
- **Revenge Killing**: Excellent for picking off weakened opponents
- **HP Management**: Requires careful play to maintain full HP condition
- **Risk/Reward**: High power but strict activation requirement

### Interactions with Other Abilities/Mechanics
- **Prankster**: Doesn't stack with other priority-boosting abilities
- **Quick Claw**: Can potentially stack for even higher priority
- **Trick Room**: Nullifies the priority advantage
- **Iron Fist**: Can be paired for both priority and power boosts
- **Brawling Wyvern**: Dragon-type moves also count as punching moves

### Common Users
This is a custom Elite Redux ability, so users would be Pokemon specifically designed with this ability in the ROM hack.

### Competitive Usage Notes
- **Sweeper Role**: Perfect for fast sweeping when healthy
- **Lead Position**: Excellent as a lead Pokemon for immediate pressure
- **Coverage**: Access to multi-type punching moves provides good coverage
- **Setup Prevention**: Can interrupt setup attempts with priority moves

### Counters
- **Residual Damage**: Stealth Rock, sandstorm, poison, burn disable the ability
- **Multi-hit Moves**: Breaking Focus Sash/Sturdy removes the HP requirement
- **Trick Room**: Reverses speed advantage entirely
- **Priority Users**: Other priority moves can still outspeed +1 priority
- **Protect/Detect**: Can scout and potentially cause self-damage

### Synergies
- **Focus Sash**: Guarantees survival at 1 HP, but ability won't work afterwards
- **Leftovers**: Can potentially restore to full HP to reactivate ability
- **Sitrus Berry**: May restore to full HP if timed correctly
- **Iron Fist**: Stacks for 1.3x power boost on punching moves
- **Life Orb**: Recoil damage will disable the ability after first use

### Version History
- Added in Elite Redux as custom ability ID 277
- Uses existing Iron Fist move classification system
- Part of the expanded ability roster in the ROM hack