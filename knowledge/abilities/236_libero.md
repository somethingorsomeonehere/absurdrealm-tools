---
id: 236
name: Libero
status: reviewed
character_count: 115
---

# Libero - Ability ID 236

## In-Game Description
"Before using a move, changes its type to the move's type."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Libero overrides the user's type to match the move being used before it attacks. Cannot activate on Struggle moves. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Libero is functionally identical to Protean, providing a powerful type-changing mechanic with the following properties:

### Core Mechanics
- **Activation Timing**: Triggers before the move is used during the `onBeforeAttack` phase
- **Once Per Turn**: Uses `CheckAndSetOncePerTurnAbility()` to prevent multiple activations per turn
- **Type Change**: Uses `SET_BATTLER_TYPE()` macro which sets both type1 and type2 to the move's type, and type3 to TYPE_MYSTERY
- **STAB Bonus**: Since the user's type matches the move type after transformation, all attacks receive Same Type Attack Bonus (1.5x damage)

### Activation Conditions
1. The ability must not have already triggered this turn
2. The user must not already be of the move's type (prevents redundant activation)
3. The move cannot be Struggle (hardcoded exception)
4. Standard ability activation requirements (not suppressed, etc.)

### Strategic Applications
- **Offensive Coverage**: Every move effectively gets STAB, significantly boosting damage output
- **Defensive Adaptation**: Type changes affect incoming move effectiveness immediately
- **Unpredictability**: Opponents cannot easily predict defensive typings
- **Multi-hit Protection**: Once-per-turn limitation prevents exploitation with multi-hit moves

### Technical Implementation
```cpp
constexpr Ability Libero = {
    .onBeforeAttack = Protean.onBeforeAttack,
};
```

Libero directly references Protean's implementation, making them mechanically identical. The Protean code checks for turn-based activation, verifies the user isn't already the move's type, excludes Struggle, then changes the battler's typing and displays the activation message.

### Elite Redux Context
In Elite Redux, Libero appears as both a regular ability choice and as an innate ability on certain Pokemon (notably the Scorbunny line), making it accessible in the game's 4-ability system. This provides consistent access to the powerful type-changing effect while maintaining other ability options.

### Comparison to Similar Abilities
- **Protean**: Mechanically identical - both share the same implementation
- **Color Change**: Activates when hit by a move rather than when using a move
- **Multitype/RKS System**: Permanent type changes based on held items rather than per-move adaptation

The once-per-turn limitation prevents potential abuse while still providing significant strategic value, making Libero a highly sought-after ability for offensive Pokemon seeking maximum type coverage and damage output.