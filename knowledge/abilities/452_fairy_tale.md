---
id: 452
name: Fairy Tale
status: reviewed
character_count: 149
---

# Fairy Tale - Ability ID 452

## In-Game Description
"Adds Fairy type to itself."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Fairy to the user's current typing. Retains Fairy typing even upon losing the ability, going away only when switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fairy Tale is a unique type-adding ability that grants the Pokemon an additional Fairy type upon switching into battle. This creates a triple-type Pokemon for the duration of their time on the field.

### Activation Conditions
- **Trigger**: Automatically activates when the Pokemon enters battle
- **Type addition**: Adds Fairy as a third type (stored in type3 slot)
- **Duration**: Persists until the Pokemon switches out or faints
- **Reactivation**: Triggers again on each switch-in

### Technical Implementation
```c
constexpr Ability FairyTale = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_FAIRY); },
};

static int AddBattlerType(int battler, int type) {
    CHECK_NOT(IS_BATTLER_OF_TYPE(battler, type))
    gBattleMons[battler].type3 = type;
    PREPARE_TYPE_BUFFER(gBattleTextBuff2, gBattleMons[battler].type3);
    BattleScriptPushCursorAndCallback(BattleScript_BattlerAddedTheType);
    return TRUE;
}
```

### Type Interactions
When Fairy type is added, the Pokemon gains all Fairy-type interactions:

**Resistances (0.5x damage):**
- Fighting-type moves
- Bug-type moves  
- Dark-type moves

**Immunity (0x damage):**
- Dragon-type moves

**Weaknesses (2x damage):**
- Poison-type moves
- Steel-type moves

### Important Interactions
- **No effect on existing types**: Original types remain unchanged
- **Type checking**: All type-based effects now consider Fairy type
- **Move effectiveness**: Damage calculations include the new Fairy typing
- **Ability interactions**: Other abilities that check types now see Fairy
- **Status conditions**: No inherent status immunities from Fairy typing

### Strategic Applications
- **Defensive utility**: Provides key resistances and Dragon immunity
- **Coverage enhancement**: Allows non-Fairy Pokemon to benefit from Fairy typing
- **Team synergy**: Can help cover team weaknesses to Dragon/Fighting/Bug
- **Flexibility**: Works on any Pokemon regardless of original typing

### Similar Abilities
- **Turboblaze**: Adds Fire type on entry
- **Teravolt**: Adds Electric type on entry
- **Grounded**: Adds Ground type on entry
- **IceAge**: Adds Ice type on entry
- **HalfDrake**: Adds Dragon type on entry
- **Aquatic**: Adds Water type on entry
- **Metallic**: Adds Steel type on entry
- **Phantom**: Adds Ghost type on entry

### Limitations
- **Poison weakness**: Makes Pokemon vulnerable to Poison moves
- **Steel weakness**: Makes Pokemon vulnerable to Steel moves
- **Temporary effect**: Lost when switching out
- **No offensive benefit**: Doesn't change the Pokemon's move types
- **Already Fairy-types**: Has no effect on Pokemon that are already Fairy-type

### Competitive Usage
- **Defensive pivots**: Excellent on bulky Pokemon that can utilize the resistances
- **Dragon immunity**: Provides safe switch-ins against Dragon-type attackers
- **Type coverage**: Helps round out team defensive profiles
- **Flexible application**: Works well on various Pokemon archetypes

### Counters
- **Poison-type moves**: Exploits the newly gained weakness
- **Steel-type moves**: Exploits the newly gained weakness
- **Mold Breaker**: Ignores the ability entirely
- **Neutralizing Gas**: Suppresses the ability
- **Role Swap/Skill Swap**: Can transfer the ability away

### Synergies
- **Assault Vest**: Enhanced special bulk to take advantage of resistances
- **Leftovers**: Passive recovery to maintain longevity
- **Rocky Helmet**: Punishes contact moves that now deal reduced damage
- **Fairy-type moves**: Though the Pokemon doesn't gain STAB, can still utilize coverage
- **Bulk Up/Calm Mind**: Stat boosts pair well with improved resistances

### Design Philosophy
Fairy Tale represents the concept of transformation and adaptation, allowing Pokemon to temporarily embrace Fairy-type characteristics. This ability enables creative team building by providing Fairy-type benefits to non-Fairy Pokemon, opening up new strategic possibilities while maintaining the temporary nature that requires careful positioning.

### Version History
- Custom ability introduced in Elite Redux
- Part of the type-adding ability family
- Designed to provide flexibility in team building and defensive strategies