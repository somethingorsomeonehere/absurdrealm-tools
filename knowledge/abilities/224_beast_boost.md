---
id: 224
name: Beast Boost
status: reviewed
character_count: 199
---

# Beast Boost - Ability ID 224

## In-Game Description
"Dealing a KO raises highest calculated stat by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Beast Boost raises the user's highest calculated stat by one stage each time it KOs an opponent. The stat raised is determined by comparing the raw stat without current modifiers such as stat raises.

## Detailed Mechanical Explanation
*For Discord/reference use*

Beast Boost is an ability that provides stat boosts upon defeating opponents, making it excellent for momentum-based strategies and late-game sweeping.

### Core Mechanics
- **Activation Condition**: User must deal the final blow that causes an opponent to faint
- **Effect**: Raises the user's highest stat by one stage (+50% for offensive stats, +33% for defensive stats)
- **Stat Determination**: Uses base calculated stats WITHOUT current battle modifiers (stat stages, items, abilities)

### Technical Implementation
```cpp
constexpr Ability BeastBoost = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int { 
        return MoxieClone(battler, GetHighestStatId(battler, FALSE)); 
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

The ability uses `GetHighestStatId(battler, FALSE)` where `FALSE` means it doesn't include current stat stage modifications. The function compares:
- Attack
- Defense  
- Speed
- Special Attack
- Special Defense

HP is excluded from consideration. The stat with the highest raw value gets boosted by one stage.

### Stat Priority Examples
- **Physical Attacker**: If Attack is highest to Attack +1 stage
- **Fast Sweeper**: If Speed is highest to Speed +1 stage  
- **Mixed Attacker**: If Special Attack is highest to Special Attack +1 stage
- **Defensive Wall**: If Defense/Special Defense is highest to that defensive stat +1 stage

### Accumulation
- Multiple KOs = multiple boosts
- Each KO triggers separately
- Can boost different stats if stat distributions change due to previous boosts
- Stacks with other stat-boosting effects

### Common Users in Elite Redux
**Ultra Beasts** (signature ability):
- **Nihilego** - Typically boosts Special Attack or Special Defense
- **Buzzwole** - Usually boosts Attack or Defense
- **Stakataka** - Often boosts Defense or Attack

**Other Notable Users**:
- Some Elite Redux modified Pokemon with Beast Boost as hidden/innate ability
- Various legendary and pseudo-legendary Pokemon in trainer teams

### Strategic Applications
1. **Late-Game Sweeping**: Accumulate boosts by KOing weaker opponents first
2. **Momentum Building**: Each KO makes subsequent KOs easier
3. **Adaptive Boosting**: Different stat distributions create different boost patterns
4. **Multi-Battle Advantage**: Boosts persist until switching out

### Interactions
- **Works with**: All stat-boosting items and abilities
- **Doesn't stack with**: N/A (each activation is separate)
- **Blocked by**: Abilities that prevent stat changes (Clear Body, etc.)
- **Reset by**: Switching out, Haze, Clear Smog, etc.

### Competitive Usage
- **Tier**: High-value sweeping ability
- **Best suited for**: Mixed attackers and late-game sweepers
- **Team synergy**: Pairs well with setup moves and offensive pivots
- **Risk**: Requires KOs to activate, so setup may be needed initially

### Counters
1. **Priority moves** - Prevent accumulation by KOing before boosts stack
2. **Status effects** - Burn halves Attack boosts, paralysis reduces Speed
3. **Stat reset moves** - Haze, Clear Smog eliminate accumulated boosts
4. **Switching** - Force switches to reset boosts
5. **Defensive play** - Avoid giving KOs to prevent activation

### Version History
- Originally from Generation VII (Sun/Moon) as Ultra Beast signature ability
- Elite Redux implementation maintains core mechanics while expanding distribution
- Enhanced with 4-ability system compatibility as innate ability on some Pokemon

### Damage Calculation Examples
**Base Attack 130 Pokemon:**
- No boosts: 130 Attack
- +1 Beast Boost: 195 Attack (50% increase)  
- +2 Beast Boost: 260 Attack (100% increase)
- +3 Beast Boost: 325 Attack (150% increase)

**Base Speed 110 Pokemon:**
- No boosts: 110 Speed
- +1 Beast Boost: 165 Speed
- +2 Beast Boost: 220 Speed  
- Creates significant outspeeding potential

### Synergistic Abilities
Works excellently with:
- **Life Orb/Choice items** for immediate power
- **Speed control** abilities to secure initial KOs
- **Recovery moves** to maintain longevity for multiple KOs
- **Priority moves** as backup when outsped despite boosts