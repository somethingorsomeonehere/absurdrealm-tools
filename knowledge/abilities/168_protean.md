---
id: 168
name: Protean
status: reviewed
character_count: 101
---

# Protean - Ability ID 168

## In-Game Description
"Changes type to match the move being used, granting STAB to all moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Before each attack, the user overrides their type to match the move's type. 
Activates once per turn.

## Detailed Mechanical Explanation

Protean is a type-changing ability that allows the user to change their type to match the type of the move they are about to use, providing Same Type Attack Bonus (STAB) for all moves.

### Core Functionality
- **Trigger**: Before using any move (except Struggle)
- **Effect**: Changes the user's type to match the move's type
- **Restriction**: Only activates once per turn per ability instance
- **Condition**: Only activates if the user is not already the same type as the move

### Implementation Details
```cpp
// From abilities.cc lines 1854-1864
constexpr Ability Protean = {
    .onBeforeAttack = +[](ABILITY_ON_BEFORE_ATTACK) -> int {
        CHECK(CheckAndSetOncePerTurnAbility(battler, ability))
        CHECK_NOT(IS_BATTLER_OF_TYPE(battler, moveType))
        CHECK(move != MOVE_STRUGGLE)
        SET_BATTLER_TYPE(gBattlerAttacker, moveType);
        PREPARE_TYPE_BUFFER(gBattleTextBuff1, moveType);
        BattleScriptCall(BattleScript_ProteanActivates);
        return TRUE;
    },
};
```

### Battle Message
When Protean activates, the message displayed is:
**"[Pokemon name] transformed into the [type] type!"**

## Pokemon with Protean

### Kecleon (National Dex #352)
- **Ability Type**: Innate (always active)
- **Base Stats**: 60/90/70/60/120/40
- **Types**: Normal
- **Tier**: 4

### Greninja (National Dex #658)
- **Ability Type**: Changeable (can be selected)
- **Base Stats**: 72/100/67/103/71/122
- **Types**: Water/Dark
- **Other Changeable Abilities**: Fatal Precision, Speed Boost

## Strategic Applications

### Offensive Benefits
- **STAB Bonus**: All moves receive 1.5x damage multiplier
- **Type Coverage**: Allows for diverse movesets with consistent power
- **Unpredictability**: Opponents cannot predict the user's type

### Defensive Considerations
- **Type Vulnerability**: Changing type may introduce new weaknesses
- **Timing**: Type change occurs before the move, affecting incoming damage calculations
- **Once Per Turn**: Limited to one activation per turn, requiring strategic move selection

## Limitations

### Usage Restrictions
- **Once Per Turn**: Cannot activate multiple times in the same turn
- **Struggle Exception**: Does not activate when using Struggle
- **Same Type Check**: Will not activate if already the same type as the move

### Strategic Limitations
- **Defensive Exposure**: May change to a type weak to opponent's moves
- **Prediction**: Experienced players can anticipate type changes
- **Move Selection**: Must consider both offensive and defensive type implications

## Interactions

### Related Abilities
- **Color Change**: Changes type when hit by a move (defensive vs. offensive)
- **Libero**: Functionally identical to Protean (same effect, different name)

### Battle Mechanics
- **Priority**: Activates before the move executes
- **Multi-Hit Moves**: Only changes type once per turn, not per hit
- **Switch Out**: Type reverts to base type when switching out

## Competitive Analysis

### Strengths
- **Versatility**: Turns every move into a STAB move
- **Power Boost**: Consistent 1.5x damage multiplier
- **Type Coverage**: Enables diverse offensive strategies

### Weaknesses
- **Defensive Risk**: May expose to super-effective attacks
- **Predictability**: Experienced players can anticipate type changes
- **Limited Activation**: Once per turn restriction

### Optimal Usage
- **Mixed Attackers**: Benefits Pokemon with diverse movepools
- **Hit-and-Run**: Synergizes with fast Pokemon that can change types and switch out
- **Coverage Moves**: Makes normally weak coverage moves viable with STAB