---
id: 403
name: Roundhouse
status: reviewed
character_count: 92
---

# Roundhouse - Ability ID 403

## In-Game Description
"Kicks always hit. Damages foes' weaker defenses."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Roundhouse makes all kicking moves never miss and target the opponent's weaker defense stat.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Roundhouse is an offensive ability that enhances all kicking moves by guaranteeing accuracy and optimizing damage output through intelligent stat targeting.

### Activation Conditions
- **Move requirement**: Only works with moves that have the `striker: true` flag
- **Kicking moves include**: All moves with FLAG_STRIKER_BOOST flag set
  - Double Kick, Mega Kick, Jump Kick, Rolling Kick
  - High Jump Kick, Triple Kick, Blaze Kick
  - Stomping Tantrum, Axe Kick, many others
- **Dual effect**: Provides both accuracy and defensive stat targeting

### Accuracy Enhancement
The ability grants perfect accuracy to all kicking moves through the `ACCURACY_HITS_IF_POSSIBLE` return value, which means:
- **Never miss**: All kick moves will hit regardless of original accuracy
- **Ignores evasion**: Bypasses evasion boosts and accuracy drops
- **No Guard equivalent**: Functions like No Guard but only for kicks
- **Move accuracy irrelevant**: 95% accuracy Jump Kick becomes 100% reliable

### Defensive Stat Targeting
Roundhouse calculates both Defense and Special Defense of the target and forces kicks to target the weaker stat:
- **Stat comparison**: Compares raw Defense vs Special Defense values
- **Automatic targeting**: No manual selection needed
- **Optimal damage**: Always chooses the stat that results in higher damage
- **Mixed attackers benefit**: Physical kicks can target Special Defense if lower

### Technical Implementation
```c
constexpr Ability Roundhouse = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(IsStrikerBoosted(battler, move))
        return ACCURACY_HITS_IF_POSSIBLE;
    },
    .onChooseDefensiveStat = +[](ON_CHOOSE_DEFENSIVE_STAT) -> int {
        CHECK(IsStrikerBoosted(battler, move))
        u32 def = CalculateStat(target, STAT_DEF, 0, move, FALSE, ignoreDefensiveStatBoosts, battlerUnaware, FALSE);
        u32 spDef = CalculateStat(target, STAT_SPDEF, 0, move, FALSE, ignoreDefensiveStatBoosts, battlerUnaware, FALSE);
        if (def < spDef)
            return STAT_DEF;
        else if (spDef < def)
            return STAT_SPDEF;
        else
            return 0;
    },
};
```

### Striker Boost Eligibility
Kicks are identified through the `IsStrikerBoosted` function which checks for:
- **FLAG_STRIKER_BOOST**: Primary identifier for kick moves
- **FLAG_IRON_FIST_BOOST**: Secondary condition with Junshi Sanda ability
- **Move examples**: Double Kick, Mega Kick, Jump Kick, Rolling Kick, High Jump Kick, Triple Kick, Blaze Kick, Low Kick, etc.

### Important Interactions
- **Stat calculation**: Uses full stat calculation including items and abilities
- **Stat stage awareness**: Accounts for stat boosts/drops in targeting decision
- **Equal stats**: Returns 0 (no change) when Defense equals Special Defense
- **Ability stacking**: Works with other accuracy-boosting abilities
- **Priority moves**: Rolling Kick's +1 priority maintained with perfect accuracy

### Damage Calculation Impact
- **Defensive targeting**: Can dramatically increase damage output
- **Type effectiveness**: Still applies normally after stat targeting
- **Critical hits**: Unaffected by ability, follow normal crit rules
- **STAB bonus**: Applies normally to Fighting-type users

### Strategic Implications
- **Reliability boost**: Makes high-power, low-accuracy kicks usable
- **Damage optimization**: Ensures kicks always hit optimal defense
- **Mixed attackers**: Physical kicks can exploit Special Defense
- **Movepool synergy**: Enhances Pokemon with diverse kicking movesets
- **Prediction removal**: Eliminates need to predict defensive investment

### Competitive Usage
- **Guaranteed damage**: Converts unreliable moves into consistent threats
- **Wall breaking**: Targets weaker defensive stat for maximum damage
- **Speed control**: Rolling Kick becomes priority move with perfect accuracy
- **Setup sweeping**: Reliable STAB moves for Fighting-type sweepers
- **Coverage expansion**: Makes niche kick moves competitively viable

### Coverage Analysis
Common kicking moves and their enhanced utility:
- **Jump Kick**: 100 power, 95% to 100% accuracy, stat-optimized
- **High Jump Kick**: 130 power, 90% to 100% accuracy, devastating
- **Mega Kick**: 120 power, 75% to 100% accuracy, now reliable
- **Rolling Kick**: Priority flinch chance with perfect accuracy
- **Triple Kick**: Multi-hit with guaranteed connection

### Counters and Limitations
- **Non-kick moves**: Ability provides no benefit to non-kicking attacks
- **Ghost types**: Immune to Fighting-type kicks regardless of ability
- **Contact punishers**: Rocky Helmet, Rough Skin still trigger on contact kicks
- **Protect/Detect**: Still blocks kicks despite perfect accuracy
- **Substitute**: Blocks stat targeting, forces normal damage calculation

### Synergies
- **Iron Fist**: Boosts power of punch moves (doesn't affect kicks directly)
- **Reckless**: Boosts recoil moves like Jump Kick and High Jump Kick
- **Choice items**: Locks into powerful, now-reliable kick moves
- **Life Orb**: Boosts all kick damage with perfect accuracy
- **Fighting-type STAB**: Maximizes damage on reliable kicks

### Team Building Considerations
- **Fighting-type specialists**: Natural fit for Fighting-type Pokemon
- **Mixed attackers**: Pokemon with both physical kicks and special moves
- **Speed control**: Rolling Kick provides priority option
- **Coverage users**: Pokemon learning diverse kick moves for coverage
- **Wallbreakers**: Stat-targeting makes defensive investments less effective

### Version History
- **Elite Redux exclusive**: Custom ability not found in official games
- **Striker system**: Part of Elite Redux's enhanced move categorization
- **Accuracy mechanic**: Uses advanced targeting system for optimal damage
- **Defensive stat selection**: Intelligent stat targeting for competitive play