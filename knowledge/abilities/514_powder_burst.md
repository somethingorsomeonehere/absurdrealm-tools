---
id: 514
name: Powder Burst
status: reviewed
character_count: 203
---

# Powder Burst - Ability ID 514

## In-Game Description
"Casts Powder on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Powder on entry, coating the target with explosive powder for the remainder of the turn. If the target uses any Fire-type move while coated, they lose 25% of their max HP and the powder is consumed. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Powder Burst is an entry ability that automatically applies the Powder status condition to an opponent when the Pokemon enters the battlefield. The Powder status creates a dangerous trap that punishes Fire-type move usage.

### Activation Conditions
- **Entry trigger**: Activates automatically when the Pokemon enters battle
- **Target selection**: Automatically targets an opponent (typically the active opponent)
- **No accuracy check**: Cannot miss since it's an ability effect
- **Bypasses immunity**: Applied as an ability effect, not a move

### Powder Status Effects
- **Status duration**: Lasts until end of turn (STATUS2_POWDER)
- **Fire move trigger**: Activates when the affected Pokemon uses any Fire-type move
- **Damage calculation**: Deals 25% of the target's max HP as damage
- **Magic Guard interaction**: Prevents damage if the target has Magic Guard
- **Move cancellation**: The Fire-type move still executes after taking damage

### Technical Implementation
```c
// Ability definition
constexpr Ability PowderBurst = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_POWDER, 0); 
    },
};

// Powder status check during attack
if (gBattleMons[gBattlerAttacker].status2 & STATUS2_POWDER) {
    u32 moveType;
    GET_MOVE_TYPE(gCurrentMove, moveType);
    if (moveType == TYPE_FIRE) {
        gBattleMoveDamage = BATTLER_HAS_MAGIC_GUARD(gBattlerAttacker) ? 0 : (gBattleMons[gBattlerAttacker].maxHP / 4);
        // Execute powder explosion
    }
}
```

### Important Interactions
- **Move execution**: Fire moves still execute after powder explosion
- **Magic Guard**: Prevents the powder explosion damage
- **Baton Pass**: Powder status is preserved when Baton Passing
- **Turn end**: Powder status is automatically removed at end of turn
- **Overcoat immunity**: Overcoat prevents powder moves from affecting the user
- **Multiple applications**: Can be reapplied if the Pokemon switches out and back in

### Strategic Implications
- **Anti-Fire utility**: Deters Fire-type attackers and sweepers
- **Entry pressure**: Provides immediate battlefield control upon switching in
- **Suicide deterrent**: Discourages Fire-type Pokemon from staying in
- **Mindgames**: Forces opponents to consider their Fire-type moves carefully
- **Limited duration**: Only lasts one turn, requiring careful timing

### Common Users
**Larvesta** (Changeable)
- Bug/Fire type with access to Powder Burst
- Can deter opposing Fire-types despite sharing the type
- Synergizes with its defensive bulk

**Ribombee** (Changeable)
- Bug/Fairy type with high Speed
- Can apply Powder quickly before opponents act
- Pairs well with its supportive movepool

**Butterfree** (Innate)
- Multiple Butterfree evolution lines have this as an innate ability
- Provides utility alongside their other abilities
- Good synergy with Compound Eyes for accuracy

### Competitive Usage Notes
- Excellent against Fire-type sweepers and wallbreakers
- Provides immediate entry pressure without setup
- Can discourage Fire-type coverage moves
- Pairs well with other entry abilities for multiple effects
- Limited to one turn duration requires strategic timing

### Counters
- **Non-Fire attacks**: Powder only affects Fire-type moves
- **Magic Guard**: Completely negates the powder explosion damage
- **Overcoat**: Prevents powder moves from affecting the user
- **Switching**: Switching out removes the powder status
- **Waiting**: Powder expires at end of turn if not triggered

### Synergies
- **Compound Eyes**: Improves accuracy of follow-up moves
- **Levitate**: Protects from Ground-type moves commonly used by Fire-types
- **Shield Dust**: Provides immunity to other powder moves
- **Prankster**: Prioritizes status moves to capitalize on powder pressure
- **Tinted Lens**: Enhances damage against Fire-types that resist other moves

### Version History
- Elite Redux original ability
- Part of the extended ability system
- Provides unique anti-Fire utility not found in other games
- Commonly distributed among Bug-type Pokemon as thematic fit

### Damage Calculation Details
- **Base damage**: 25% of target's maximum HP
- **Rounding**: Rounded down (standard HP damage rounding)
- **Immunity**: Magic Guard completely prevents damage
- **No type effectiveness**: Powder explosion is typeless damage
- **Substitute**: Damages the Pokemon directly, not the substitute