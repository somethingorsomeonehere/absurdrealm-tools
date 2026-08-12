---
id: 293
name: Let's Roll
status: reviewed
character_count: 165
---

# Let's Roll - Ability ID 293

## In-Game Description
"Casts Defense Curl on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Let's Roll automatically raises Defense by one stage and applies the Defense Curl status upon entering battle, doubling the power of Rollout and other rolling moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Let's Roll is an entry ability that combines two distinct effects:
1. **Defense Boost**: Raises the user's Defense stat by one stage (+50% physical defense)
2. **Defense Curl Status**: Applies the STATUS2_DEFENSE_CURL flag to the Pokemon

### Activation Conditions
- Triggers automatically when the Pokemon enters battle (switching in, sent out at start of battle)
- Only activates if the Defense stat can be raised (not blocked by Clear Body, etc.)
- Does not activate if already at maximum Defense stages (+6)

### Technical Implementation
```cpp
constexpr Ability LetsRoll = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, STAT_DEF))

        SetStatChanger(STAT_DEF, 1);
        gBattleMons[battler].status2 = STATUS2_DEFENSE_CURL;
        BattleScriptPushCursorAndCallback(BattleScript_BattlerInnateStatRaiseOnSwitchIn);
        return TRUE;
    },
};
```

### Defense Curl Status Effects
The Defense Curl status provides:
- **Rollout Power Boost**: Doubles the base power of Rollout (30 to 60 BP for first hit)
- **Ice Ball Power Boost**: Doubles the base power of Ice Ball (30 to 60 BP for first hit)
- **Move Synergy**: These moves continue to increase power each consecutive turn when used

### Affected Moves
- **Rollout**: Base power increased from 30 to 60 on first use, then continues doubling each turn
- **Ice Ball**: Base power increased from 30 to 60 on first use, then continues doubling each turn

### Interactions with Other Mechanics
- **Stat Boost Blocking**: Abilities like Clear Body, White Smoke prevent the Defense boost but not the Defense Curl status
- **Stat Reset**: Haze, Clear Smog remove Defense boost but Defense Curl status remains
- **Baton Pass**: Defense boost can be passed, Defense Curl status cannot
- **Rollout Counter**: Defense Curl status increases Rollout's rollout counter by 1 initially

### Strategic Implications
**Immediate Value:**
- Provides instant physical bulk (+50% defense against physical attacks)
- Enables immediate use of powered-up rolling moves
- Great for pivot Pokemon that need to tank a hit on entry

**Rolling Move Strategy:**
- Makes Rollout/Ice Ball viable as primary attacking options
- First hit deals doubled damage (60 BP instead of 30)
- Subsequent hits follow normal doubling pattern (120, 240, 480, 960 BP)
- Creates powerful late-game sweeping potential

### Example Damage Calculations
**Rollout with Defense Curl (Level 50, 100 Attack, neutral nature):**
- Turn 1: 60 BP (doubled from 30)
- Turn 2: 120 BP 
- Turn 3: 240 BP
- Turn 4: 480 BP
- Turn 5: 960 BP

**Without Defense Curl:**
- Turn 1: 30 BP
- Turn 2: 60 BP
- Turn 3: 120 BP
- Turn 4: 240 BP
- Turn 5: 480 BP

### Common Users
Notable Pokemon with Let's Roll include:
- **Sandslash**: Physical tank with Rollout access
- **Mamoswine**: Bulky physical attacker with Ice Ball
- **Shuckle**: Extreme defensive utility
- **Golem**: Rock-type physical tank
- **Forretress**: Steel-type defensive pivot
- **Snorlax**: Physical wall with potential offense

### Competitive Usage Notes
**Strengths:**
- Immediate defensive presence upon entry
- Enables unique rolling move strategies
- Works well on defensive pivots
- No setup required - activates automatically

**Weaknesses:**
- Defense boost can be removed by stat-clearing moves
- Rolling moves lock the user into the attack
- Vulnerable to Ghost-types (Rollout/Ice Ball can't hit)
- Single-use activation per battle entry

### Counters
- **Stat Control**: Haze, Clear Smog remove Defense boost
- **Ghost Types**: Immune to Rollout/Ice Ball followup
- **Special Attackers**: Defense boost doesn't help against special moves
- **Status Moves**: Taunt prevents potential setup after entry
- **Forcing Switches**: Roar, Whirlwind reset rolling move chains

### Synergies
**Defensive Synergies:**
- **Leftovers**: Sustain after tanking hits
- **Rocky Helmet**: Punish contact moves while boosted
- **Stamina**: Stack Defense boosts from taking damage

**Offensive Synergies:**
- **Choice Band**: Massive power boost to rolling moves
- **Life Orb**: Additional damage boost
- **Metronome**: Stacks with rolling move power increases

### Version History
- Introduced in Elite Redux as a unique defensive/offensive hybrid ability
- Designed to make rolling moves more viable in competitive play
- Part of the expanded ability system providing more strategic options