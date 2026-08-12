---
id: 510
name: Mycelium Might
status: reviewed
character_count: 122
---

# Mycelium Might - Ability ID 510

## In-Game Description
"Status moves ignore immunities but go last."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Allows status moves to bypass all immunities and type resistances, but forces them to move last in their priority bracket.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Mycelium Might is a unique ability that trades move priority for immunity bypassing power. It fundamentally changes how status moves interact with defensive mechanics.

### Activation Conditions
- **Move type requirement**: Only affects status moves (non-damaging moves)
- **Target requirement**: Only affects moves targeting opponents (gBattleMoves[move].target != MOVE_TARGET_USER)
- **Self-targeting exception**: Moves like Swords Dance, Rest, etc. are unaffected
- **Priority modification**: Status moves always go last in their priority bracket

### Technical Implementation
```c
// Macro definition for affected moves
#define MYCELIUM_MIGHT_AFFECTED(battler, move) \
    (BATTLER_HAS_ABILITY(battler, ABILITY_MYCELIUM_MIGHT) && IS_MOVE_STATUS(move) && gBattleMoves[move].target != MOVE_TARGET_USER)

// Sets hitmarker when ability is active
if (BattlerHasAbility(gBattlerAttacker, ABILITY_MYCELIUM_MIGHT, FALSE)) 
    gHitMarker |= HITMARKER_MYCELIUM_MIGHT;

// Speed calculation modification
speedValue.goesLastNegation += MYCELIUM_MIGHT_AFFECTED(battler, GetChosenMove(battler));
```

### Immunity Bypassing Effects
The ability bypasses numerous defensive mechanics:

**Status Condition Immunities:**
- Type immunities (Electric-types vs paralysis, Fire-types vs burn, etc.)
- Ability-based immunities (Limber, Water Veil, Insomnia, etc.)
- Terrain protection (Misty Terrain preventing status)
- Safeguard protection
- Hold item immunities (Pecha Berry auto-cure, etc.)

**Status Move Specific Bypasses:**
- Powder moves hit Grass-types and Overcoat users
- Sleep moves work on Electric Terrain and Insomnia users
- Paralysis moves affect Electric-types and Limber users
- Burn moves affect Fire-types and Water Veil users
- Poison moves hit Poison/Steel types and immunity abilities

### Priority Mechanics
- **Speed modification**: Affected moves are forced to go last within their priority bracket
- **Priority preservation**: Base move priority is maintained, but speed is set to go last
- **Lagging Tail effect**: Functions similarly to Lagging Tail held item
- **Quash interaction**: Quash timer takes precedence over Mycelium Might
- **Trick Room**: Still goes last even in Trick Room conditions

### Important Interactions

**Status Move Examples Affected:**
- Thunder Wave (bypasses Ground-type immunity and Limber)
- Sleep Powder (bypasses Insomnia and Electric Terrain)
- Will-O-Wisp (bypasses Fire-type immunity and Water Veil)
- Toxic (bypasses Poison/Steel immunity and Immunity ability)
- Spore (bypasses all sleep immunities)

**Moves NOT Affected:**
- Self-targeting status moves (Swords Dance, Calm Mind, etc.)
- Healing moves targeting self (Recover, Rest, etc.)
- Damaging moves (never affected regardless of secondary effects)
- Status moves with MOVE_TARGET_USER flag

### Strategic Implications

**Advantages:**
- **Guaranteed status application**: Can status any opponent regardless of type/ability
- **Utility maximizer**: Makes status moves incredibly reliable
- **Team support**: Enables consistent status spreading for team support
- **Meta breaking**: Bypasses common status immunities that define the meta

**Disadvantages:**
- **Speed penalty**: Always moves last, making user vulnerable to KO before acting
- **Priority loss**: Loses first-move advantage that status moves often rely on
- **Predictable timing**: Opponents know when status moves will hit
- **Setup window**: Gives opponents time to set up or switch out

### Competitive Usage Notes

**Ideal Pokemon Types:**
- Bulky support Pokemon who can survive hits before moving
- Pokemon with natural bulk to tank attacks while setting up status
- Pokemon with recovery moves to maintain longevity
- Slow Pokemon who already move last anyway

**Team Compositions:**
- Stall teams benefiting from guaranteed status application
- Support builds focusing on status spreading
- Teams countering specific immunity-based strategies
- Builds utilizing Trick Room to potentially move first despite the penalty

### Counters

**Direct Counters:**
- **Priority moves**: Attack before status moves can be used
- **Taunt**: Prevents status move usage entirely
- **Magic Bounce/Magic Guard**: Reflects or prevents status effects
- **Substitute**: Blocks most status effects
- **Fast attackers**: KO before status moves can be executed

**Ability Interactions:**
- **Mold Breaker**: Ironically, Mold Breaker ignores Mycelium Might
- **Neutralizing Gas**: Suppresses the ability entirely
- **Simple Beam/Worry Seed**: Can replace the ability
- **Skill Swap**: Can transfer the ability away

### Synergies

**Supportive Strategies:**
- **Trick Room**: Potentially allows moving first despite the penalty
- **Follow Me/Rage Powder**: Protects user while they prepare status moves
- **Screens/Aurora Veil**: Reduces damage taken while moving last
- **Protect/Detect**: Can scout opponent's move before committing to status

**Move Synergies:**
- **Thunder Wave**: Guaranteed paralysis on any target
- **Toxic**: Reliable badly poisoned status on any opponent
- **Sleep moves**: Consistent sleep application regardless of type
- **Burn moves**: Universal burn application for physical attackers

### Pokemon Distribution
Based on the code analysis, Mycelium Might appears on:
- Fungal/mushroom-themed Pokemon (thematically appropriate)
- Pokemon with Infiltrator as another ability option
- Pokemon with Adaptability in some configurations
- Some Pokemon have it as an innate ability alongside other effects

### Unique Properties
- One of the few abilities that trades speed for reliability
- Creates a risk/reward dynamic unique in Pokemon battles
- Fundamentally changes the timing and reliability of status warfare
- Represents a design philosophy of powerful effect with meaningful drawback

### Version History
- Introduced in Elite Redux as ability ID 510
- Part of the expanded ability roster beyond Generation VIII
- Designed to create new strategic options for status-based gameplay
- Balances powerful effect (immunity bypass) with significant cost (speed penalty)