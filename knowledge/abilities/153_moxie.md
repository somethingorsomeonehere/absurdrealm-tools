---
id: 153
name: Moxie
status: reviewed
character_count: 91
---

# Moxie - Ability ID 153

## In-Game Description
"Dealing a KO raises Attack by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's Attack by one stage whenever it knocks out an opponent with a direct hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

Moxie is an ability that provides an immediate Attack stat boost upon knocking out an opposing Pokemon, making it a powerful ability for sweeping teams and maintaining offensive momentum.

### Core Mechanics
- **Activation Trigger**: Triggers when the Pokemon with Moxie deals the final blow that causes an opponent to faint
- **Stat Boost**: Raises Attack by one stage (equivalent to 50% increase) immediately after the knockout
- **Stack Limit**: Can stack up to +6 stages maximum, following standard stat boost rules
- **Duration**: The Attack boost persists until the Pokemon switches out, faints, or has its stats reset

### Technical Implementation
```cpp
constexpr Ability Moxie = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int { 
        return MoxieClone(battler, STAT_ATK); 
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};

static int MoxieClone(int battler, int stat) {
    CHECK(HasAttackerFaintedTarget())
    CHECK(ChangeStatBuffs(battler, 1, stat, MOVE_EFFECT_AFFECTS_USER | STAT_BUFF_DONT_SET_BUFFERS, NULL))
    BattleScriptCall(BattleScript_RaiseStatOnFaintingTarget);
    return TRUE;
}
```

### Activation Conditions
- **Direct Damage**: Works with any move that deals direct damage and causes a knockout
- **Indirect Damage**: Does NOT trigger from poison, burn, weather damage, or other indirect sources that cause fainting
- **Multi-hit Moves**: Triggers only once per knockout, regardless of how many hits the move has
- **Substitute**: Can trigger when breaking a Substitute if it causes the Pokemon to faint
- **Critical Hits**: Works normally with critical hits

### Interactions with Other Abilities/Mechanics
- **Mold Breaker Effects**: Cannot be suppressed by Mold Breaker, Turboblaze, or Teravolt
- **Ability Suppression**: Can be temporarily disabled by Gastro Acid or similar effects
- **Stat Reset**: Attack boosts are lost when the Pokemon switches out or uses moves like Haze
- **Contrary**: If the user has Contrary, Moxie would lower Attack instead of raising it
- **Simple**: If the user has Simple, each Moxie activation would provide +2 Attack stages instead of +1

### Strategic Applications
**Sweeping Potential**:
- Ideal for late-game sweeps when multiple weakened opponents can be knocked out in succession
- Each knockout makes subsequent knockouts easier to achieve
- Best used with high-speed attackers that can outspeed and knockout multiple targets

**Team Building Synergy**:
- Pairs well with entry hazards that weaken opponents
- Benefits from teammates that can weaken but not knockout key targets
- Excellent with Choice items for consistent power and speed

**Move Selection**:
- Favors reliable, high-power moves that can secure knockouts
- Multi-target moves like Earthquake can potentially trigger multiple times in doubles
- Priority moves help secure knockouts on faster, weakened opponents

### Example Damage Calculations
With a base 100 Attack Pokemon at level 50:
- **No Moxie boosts**: 152 Attack stat
- **+1 Moxie boost**: 228 Attack stat (50% increase)
- **+2 Moxie boosts**: 304 Attack stat (100% increase)
- **+3 Moxie boosts**: 380 Attack stat (150% increase)

### Common Users in Elite Redux
Notable Pokemon with Moxie include:
- **Mankey/Primeape**: Early-game sweepers with good Attack stats
- **Mightyena/Poochyena**: Dark-type attackers with decent speed
- **Heracross**: Powerful physical attacker with excellent movepool
- **Gyarados**: High Attack and Speed make it an excellent Moxie user
- **Salamence**: Pseudo-legendary with incredible sweeping potential
- **Krookodile**: Ground/Dark typing with solid offensive stats

### Competitive Usage Notes
**Advantages**:
- Snowball effect can single-handedly win games
- Provides consistent offensive pressure
- Rewards aggressive play and prediction
- Excellent for cleaning up weakened teams

**Counters and Weaknesses**:
- **Defensive Walls**: Pokemon with extremely high Defense can stop Moxie sweeps
- **Priority Moves**: Faster priority attacks can revenge kill before additional knockouts
- **Status Conditions**: Paralysis can prevent follow-up attacks, burn reduces Attack effectiveness
- **Switching**: Opponent switching forces the Moxie user to potentially waste turns

**Synergistic Strategies**:
- **Life Orb**: Increased damage helps secure crucial knockouts
- **Choice Scarf**: Ensures speed advantage for consistent knockouts
- **Focus Sash**: Allows a frail attacker to survive and potentially get multiple Moxie boosts

### Related Abilities
- **Beast Boost**: Similar mechanic but boosts the highest stat instead of Attack
- **Chilling Neigh**: Ice-type variant that also boosts Attack on knockout (shares same code)
- **Grim Neigh**: Boosts Special Attack instead of Attack on knockout
- **Adrenaline Rush**: Elite Redux custom ability that boosts Speed on knockout

### Version History
Moxie was introduced in Generation V and has remained mechanically consistent across all games, including Elite Redux. The implementation uses the shared `MoxieClone` helper function, which is also used by similar abilities like Beast Boost and the Neigh abilities.

This ability represents one of the most straightforward yet powerful momentum-based abilities in the game, rewarding successful knockouts with immediate offensive improvements that can lead to devastating sweeps when used effectively.