---
id: 703
name: Rage Point
status: reviewed
character_count: 231
---

# Rage Point - Ability ID 703

## In-Game Description
"Gets a 1.5x boost while statused. Raises offenses when crit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts offensive moves by 50% while the user has any status condition. When the Pokemon takes a critical hit, both Attack and Special Attack are raised by one stage. Also negates burn's Attack drop and freeze's Special Attack drop.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Rage Point is a dual-purpose ability that provides both offensive enhancement while statused and stat boosts when taking critical hits. It has three main components:
1. 1.5x offensive multiplier while having any status condition
2. +1 Attack and Special Attack when taking a critical hit
3. Negates Attack drop from burn and Special Attack drop from freeze

### Activation Conditions
- **Status boost**: Active whenever the Pokemon has any major status condition
- **Critical hit response**: Triggers when the Pokemon takes (not deals) a critical hit
- **Status drop negation**: Always active for burn and freeze penalties

### Status Conditions Recognized
The ability recognizes any of these status conditions via `HasAnyStatusOrAbility()`:
- Burn
- Freeze  
- Paralysis
- Poison (including badly poisoned)
- Sleep
- Comatose ability (counts as sleep status)
- Blood Stain status (custom Elite Redux status)

### Technical Implementation
```c
// Rage Point implementation from abilities.cc
constexpr Ability RagePoint = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(gIsCriticalHit)  // Only triggers on critical hits taken
        CHECK(CanRaiseStat(battler, STAT_ATK) || CanRaiseStat(battler, STAT_SPATK))
        
        BattleScriptCall(BattleScript_RagePointActivates);
        return TRUE;
    },
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
        if (HasAnyStatusOrAbility(battler)) MUL(1.5);  // 50% boost while statused
    },
    .negatesBurnAtkDrop = TRUE,    // Ignores burn's Attack penalty
    .negatesFrzSpatkDrop = TRUE,   // Ignores freeze's Special Attack penalty
};
```

### Critical Hit Stat Boost
When taking a critical hit, the battle script attempts to raise both stats:
1. First tries to raise Attack by +1 stage
2. Then tries to raise Special Attack by +1 stage  
3. Only shows stat change animation if at least one stat can be raised
4. Won't activate if both stats are already at maximum (+6)

### Offensive Multiplier Details
- **Multiplier**: Exactly 1.5x (50% increase)
- **Move types affected**: All offensive moves (physical, special, status moves that deal damage)
- **Stacking**: Multiplies with other damage modifiers
- **Timing**: Applied during damage calculation phase

### Important Interactions
- **Self-inflicted status**: Works with self-induced status like from Rest or Flame Orb
- **Ability-based status**: Comatose ability counts as having sleep status
- **Status immunity**: If immune to status effects, the boost won't apply
- **Critical hit immunity**: Abilities like Battle Armor prevent the stat boost trigger
- **Stat boost prevention**: Abilities like Clear Body can prevent the stat raises

### Strategic Applications
- **Status Orb synergy**: Flame Orb/Toxic Orb provide permanent status for consistent boost
- **Rest abuse**: Can use Rest for healing while maintaining offensive boost
- **Mixed attacker**: Benefits both physical and special moves equally
- **Revenge killer**: Stat boosts from critical hits help with revenge killing
- **Status absorber**: Can switch into status moves for the boost

### Burn and Freeze Negation
The ability provides additional utility by negating status penalties:
- **Burn normally**: Reduces Attack by 50%
- **With Rage Point**: Attack reduction is completely negated
- **Freeze normally**: Reduces Special Attack by 50% 
- **With Rage Point**: Special Attack reduction is completely negated

### Competitive Viability
**Strengths:**
- Consistent damage boost with status condition
- Defensive response to critical hits
- Negates major status penalties
- Works with both physical and special movesets

**Weaknesses:**
- Requires status condition for primary benefit
- Critical hit response is situational
- Status condition may still cause other negative effects
- Vulnerable to status condition removal

### Common Users
- Mixed attackers who benefit from both stat boosts
- Pokemon with access to status-inducing items
- Bulky offensive Pokemon that can survive critical hits
- Pokemon with naturally high critical hit rates (to trigger opponent crits)

### Synergies
- **Status Orbs**: Flame Orb, Toxic Orb for permanent status
- **Rest**: Maintains boost while sleeping
- **Guts**: Stacks multiplicatively for massive physical damage
- **Magic Guard**: Prevents status damage while keeping boost
- **Substitute**: Protects from status while maintaining boost effect

### Counters
- **Status prevention**: Safeguard, Misty Terrain, Taunt
- **Status clearing**: Aromatherapy, Heal Bell, cleric support
- **Critical hit prevention**: Lucky Chant, Battle Armor, Shell Armor
- **Stat reset**: Haze, Clear Smog, stat-resetting moves
- **Ability suppression**: Mold Breaker, Neutralizing Gas

### Version History
- New ability introduced in Elite Redux
- Combines offensive and defensive utility
- Part of the expanded ability roster for increased strategic depth