---
id: 61
name: Shed Skin
status: reviewed
character_count: 103
---

# Shed Skin - Ability ID 61

## In-Game Description
"30% chance to heal its status condition at the end of a turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

At the end of each turn, there's a 30% chance for the user to cure status conditions afflicted on them.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shed Skin provides a 30% chance at the end of each turn to cure any status condition the Pokemon is currently suffering from. Unlike Natural Cure, this healing occurs without requiring the Pokemon to switch out, making it extremely valuable for staying power.

### Technical Implementation
From `/src/abilities.cc`:
```cpp
constexpr Ability ShedSkin = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK(Random() % 100 < 30)
        CHECK(AbilityHealMonStatus(battler, ability));
        return TRUE;
    },
};
```

The ability:
1. Triggers at the end of each turn
2. Rolls a 30% chance (Random() % 100 < 30)
3. Calls AbilityHealMonStatus if successful
4. Clears all status flags and shows cure notification

### AbilityHealMonStatus Function
From `/src/battle_util.c`:
- Checks if any STATUS1_ANY condition is present
- Sets appropriate cure message for each status type
- Clears all status1 flags and nightmare
- Triggers BattleScript_ShedSkinActivates
- Updates battle data and shows ability popup

### Status Conditions Cured
Shed Skin can cure all major status conditions:
- **Sleep** (including Rest-induced sleep)
- **Poison** (regular and toxic)
- **Burn**
- **Paralysis**
- **Freeze**
- **Frostbite** (Elite Redux status)
- **Bleed** (Elite Redux status)

### Activation Mechanics
**Timing:** End of turn phase
**Chance:** Exactly 30% per turn
**Requirement:** Must have at least one status condition
**Display:** Shows ability popup and cure message

The ability only activates if:
1. The Pokemon has a status condition
2. The 30% roll succeeds
3. The Pokemon is still alive

### AI Behavior
From `battle_ai_main.c`, the AI considers Shed Skin when evaluating status moves:
- AI recognizes the 30% cure chance
- Less likely to rely on status moves against Shed Skin users
- May factor in probability when calculating move effectiveness
- Still attempts status moves but with adjusted expectations

### Related Abilities
**Wonder Scale** (Ability ID varies):
```cpp
constexpr Ability WonderScale = {
    .onEndTurn = ShedSkin.onEndTurn,
    .fortKnox = TRUE,
};
```
Uses identical healing mechanics but adds Fort Knox property (immune to stat reductions).

### Pokemon with Shed Skin
Common users in Elite Redux include:
- **Pupitar** (ability 0)
- **Dratini line** (as innate ability)
- **Seviper** (as innate ability)
- Various snake and reptilian Pokemon

### Strategic Applications

**Bulky setup sweepers:**
- Can set up despite status pressure
- Natural cure chance allows extended setup time
- Reduces need for status-curing items

**Defensive walls:**
- Stay in against status moves
- 30% chance negates status strategies
- Provides passive status immunity over time

**RestTalk users:**
- Perfect synergy with Rest + Sleep Talk
- Can wake up naturally via Shed Skin
- Reduces sleep dependency

### Probability Analysis
**Single turn:** 30% cure chance
**Multiple turns:**
- 2 turns: 51% chance of at least one cure
- 3 turns: 65.7% chance of at least one cure
- 4 turns: 75.9% chance of at least one cure
- 5 turns: 83.2% chance of at least one cure

Formula: 1 - (0.7)^n where n = number of turns

### Synergies
- **Rest**: Can wake up early, reducing sleep vulnerability
- **Sleep Talk**: Insurance if Shed Skin fails to cure sleep
- **Leftovers/Black Sludge**: Passive healing stacks with status curing
- **Substitute**: Blocks status while Shed Skin handles existing conditions
- **Bulk Up/Coil**: Setup moves benefit from status immunity

### Advantages
- Passive activation (no switching required)
- No item slot needed
- Works on all status types
- Can't be disabled by most means
- Psychological pressure on status users
- Unlimited uses

### Limitations
- Only 30% chance per turn (unreliable)
- No protection from initial status infliction
- Doesn't prevent status, only cures it
- Can fail multiple turns in a row
- No effect on non-status conditions (confusion, etc.)

### Counters
- **Direct damage moves**: Bypass status reliance entirely
- **Multi-hit status moves**: Reapply status after cure
- **Taunt**: Prevents Rest usage for recovery
- **Knock Off**: Remove recovery items if carried
- **High offensive pressure**: Force out before cure chance matters

### Competitive Usage Notes
Shed Skin excels on Pokemon designed for longevity rather than speed. It's particularly valuable on setup sweepers and defensive walls that need to operate despite status pressure. The 30% chance creates uncertainty for opponents relying on status strategies.

### Team Building Considerations
- Best on naturally bulky Pokemon
- Reduces need for cleric support
- Enables aggressive status absorption
- Pairs well with setup moves and recovery
- Consider alongside RestTalk strategies

### Mathematical Expectations
Against persistent status damage:
- **Poison:** Reduces average damage over time
- **Burn:** Lessens attack reduction duration
- **Sleep:** Averages 2.3 turns instead of full sleep duration
- **Paralysis:** Reduces average speed reduction time

### Version History
Shed Skin has maintained its 30% cure rate since Generation 3. Elite Redux preserves the classic mechanics while expanding the status types it can cure to include frostbite and bleed, maintaining its relevance in the expanded status system.