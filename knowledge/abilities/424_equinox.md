---
id: 424
name: Equinox
status: reviewed
character_count: 214
---

# Equinox - Ability ID 424

## In-Game Description
"Boosts Atk or SpAtk to match the higher value."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Equinox chooses the higher offensive stat for each attack. If Attack is higher, physical and special moves use your Attack stat. If Special Attack is higher, physical and special moves use your Special Attack stat.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Equinox is a unique offensive ability that automatically selects the higher of the user's Attack or Special Attack stats for damage calculation on every move. This allows Pokemon to use their stronger offensive stat regardless of whether they're using physical or special moves.

### Activation Conditions
- **Trigger**: Activates before damage calculation for every offensive move
- **Stat comparison**: Compares current Attack vs Special Attack (including stat stages)
- **Move type independence**: Works for both physical and special moves
- **Timing**: Occurs during the `onChooseOffensiveStat` phase of battle

### Technical Implementation
```c
// Equinox ability implementation from abilities.cc
constexpr Ability Equinox = {
    .onChooseOffensiveStat =
        +[](ON_CHOOSE_OFFENSIVE_STAT) {
            // Calculate both offensive stats with current modifiers
            int atk = CalculateStat(battler, STAT_ATK, 0, move, TRUE, ignoreOffensiveStatDrops, targetUnaware, FALSE);
            int spAtk = CalculateStat(battler, STAT_SPATK, 0, move, TRUE, ignoreOffensiveStatDrops, targetUnaware, FALSE);
            
            // Choose the higher stat for damage calculation
            if (atk > spAtk)
                *atkStatToUse = STAT_ATK;
            else if (spAtk > atk)
                *atkStatToUse = STAT_SPATK;
            // If equal, use the move's natural offensive stat
        },
};
```

### Stat Calculation Details
- **Includes stat stages**: Accounts for boosts/drops from moves like Swords Dance
- **Includes all modifiers**: Nature, EVs, IVs, items, and temporary effects
- **Real-time calculation**: Recalculates for every move, adapting to changing stats
- **Tie behavior**: When stats are equal, uses the move's natural offensive stat

### Important Interactions
- **Mixed attackers**: Transforms any Pokemon into an effective mixed attacker
- **Stat boosts**: Swords Dance and Nasty Plot become equally valuable
- **Physical/Special split**: Makes the physical/special distinction less important
- **Choice items**: Works with Choice Band/Specs - will use whichever stat is higher
- **Burn interaction**: Burn halves Attack but doesn't affect Special Attack calculation

### Move Interactions
- **Physical moves**: Can use Special Attack if it's higher
- **Special moves**: Can use Attack if it's higher  
- **Status moves**: Not affected (no damage calculation)
- **Multi-hit moves**: Stat choice applies to all hits
- **Critical hits**: Uses the chosen stat for crit damage

### Strategic Implications
- **Flexible building**: Allows investment in both offensive stats
- **Move variety**: Can run both physical and special moves effectively
- **Stat boost flexibility**: Any offensive boost becomes valuable
- **Counters stat drops**: If one stat is lowered, can switch to the other
- **Surprise factor**: Opponents can't predict which stat will be used

### Optimal Usage
- **Mixed movesets**: Run 2-3 physical and 2-3 special moves
- **Balanced investment**: Invest EVs in both Attack and Special Attack
- **Stat boosting**: Use moves that boost both stats (like Growth)
- **Coverage moves**: Use whatever type provides best coverage regardless of category
- **Adaptability**: Adjust strategy based on opponent's defensive stats

### Common Applications
- **Wallbreakers**: Can break both physical and special walls
- **Setup sweepers**: Any offensive boost becomes immediately useful
- **Coverage users**: Access to both physical and special coverage moves
- **Anti-meta**: Adapts to defensive threats dynamically

### Counters
- **Defensive stat targeting**: Use moves that target the weaker defensive stat
- **Stat lowering**: Lower both offensive stats to reduce effectiveness
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Status conditions**: Burn still affects physical moves using Attack stat
- **Defensive walls**: High defense AND special defense still problematic

### Synergies
- **Work Up**: Boosts both stats equally, maximizing flexibility
- **Growth**: In sun, boosts both stats by 2 stages
- **Mixed coverage**: Earthquake + Thunderbolt type combinations
- **Choice items**: Maximizes the benefit of whatever stat is higher
- **Life Orb**: Boosts all moves regardless of which stat is used

### Competitive Considerations
- **Unpredictability**: Opponents can't easily predict damage output
- **Stat spread optimization**: Requires careful EV distribution
- **Move selection**: Favors Pokemon with diverse movepools
- **Team building**: Reduces need for specialized physical/special roles
- **Meta adaptation**: Automatically adjusts to opponent's defensive profile

### Unique Characteristics
- **First of its kind**: Only ability that dynamically switches offensive stats
- **Move-independent**: Works with any damaging move
- **Stat-agnostic**: Equally effective for physical and special attackers
- **Adaptive**: Responds to real-time battle conditions
- **Balanced**: Doesn't directly boost damage, just optimizes stat usage

### Version History
- **Elite Redux exclusive**: Custom ability created for Elite Redux
- **Innovative design**: Represents new approach to offensive abilities
- **Balanced implementation**: Provides flexibility without raw power increase
- **Meta impact**: Encourages more diverse team building and movesets