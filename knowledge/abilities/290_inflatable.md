---
id: 290
name: Inflatable
status: reviewed
character_count: 171
---

# Inflatable - Ability ID 290

## In-Game Description
"Ups Def and Sp. Def by one stage if hit by Flying or Fire moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by any Fire or Flying moves, boost Defense and Special Defense by one stage each. Activates on each hit of a multihit move. The boost applies after the hit lands.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger**: Activates when the Pokemon is hit by any Fire-type or Flying-type move
- **Effect**: Raises both Defense and Special Defense by +1 stage each
- **Timing**: Activates after damage calculation but before the move's secondary effects

### Activation Conditions
- Must be hit by a Fire-type or Flying-type move
- The move must successfully hit (doesn't activate on miss)
- At least one of Defense or Special Defense must be below maximum (+6 stages)
- Uses `ShouldApplyOnHitAffect()` check (blocked by Substitute, etc.)

### Technical Implementation
```cpp
constexpr Ability Inflatable = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(CanRaiseStat(battler, STAT_DEF) || CanRaiseStat(battler, STAT_SPDEF))
        CHECK(moveType == TYPE_FIRE || moveType == TYPE_FLYING);
        BattleScriptCall(BattleScript_InflatableActivates);
        gBattleScripting.battler = battler;
        return TRUE;
    },
};
```

### Battle Script Behavior
- Attempts to raise Defense first, then Special Defense
- Each stat raise is independent - if Defense is at max, Special Defense can still be raised
- Uses standard stat change animations and messages
- Priority: Defense boost processed first, then Special Defense

### Affected Move Types
**Fire-type moves**: All Fire-type attacks trigger the ability
- Flamethrower, Fire Blast, Overheat, Will-O-Wisp, etc.
- Status moves like Will-O-Wisp also trigger the ability

**Flying-type moves**: All Flying-type attacks trigger the ability  
- Wing Attack, Hurricane, Air Slash, Roost, etc.
- Status moves like Roost also trigger the ability

### Interactions with Other Abilities/Mechanics
- **Substitute**: Blocked by Substitute (uses `ShouldApplyOnHitAffect`)
- **Magic Bounce**: Cannot be triggered by bounced moves
- **Stat Stage Limits**: Each stat can only be raised if below +6 stages
- **Mold Breaker**: Not affected by Mold Breaker (defensive ability)
- **Multi-hit moves**: Activates only once per turn, not per hit

### Strategic Implications
- **Defensive Pivoting**: Excellent for bulky Pokemon that can switch into Fire/Flying attacks
- **Setup Opportunities**: Creates immediate defensive bulk for further setup
- **Counter Strategy**: Works well against common offensive types
- **Momentum Shifts**: Can turn predicted Fire/Flying attacks into advantageous situations

### Example Damage Calculations
Before Inflatable activation:
- 252+ Atk Talonflame Flare Blitz vs 252 HP / 0 Def Munchlax Redux: ~45-55%

After Inflatable activation (+1 Def):
- Same attack: ~30-40% (significant reduction)

### Common Users
- **Bounsweet Redux**: Psychic/Fairy type with Magic Guard synergy
- **Tsareena Redux**: Psychic/Fairy type with balanced offensive stats
- **Tsareena Redux Mega**: Enhanced stats with Loud Bang combo ability
- **Munchlax Redux**: Water-type tank with Soundproof alternative

### Competitive Usage Notes
- **Best on**: Bulky Pokemon that can survive the initial hit and capitalize on boosts
- **Synergizes with**: Recovery moves, Stored Power, other stat-boosting abilities
- **Timing**: Most effective when opponent is locked into Fire/Flying moves
- **Prediction**: Rewards good prediction and switching skills

### Counters
- **Non-Fire/Flying attacks**: Ability doesn't activate against other types
- **Status moves**: Toxic, Thunder Wave, etc. don't trigger the ability
- **Taunt**: Prevents setup after the defensive boosts
- **Haze/Clear Smog**: Removes the stat boosts immediately

### Synergies
- **Stored Power**: Benefits from the defensive stat boosts
- **Body Press**: Defense boosts increase offensive power
- **Recovery moves**: Defensive bulk helps with healing strategies
- **Eviolite**: Stacks with natural defensive boosts on NFE Pokemon

### Version History
- Introduced in Elite Redux as a defensive reaction ability
- Designed to provide counterplay against common offensive types
- Part of the expanded ability system with unique battle interactions