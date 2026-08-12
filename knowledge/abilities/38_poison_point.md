---
id: 38
name: Poison Point
status: reviewed
character_count: 92
---

# Poison Point - Ability ID 38

## In-Game Description
"30% chance to poison on contact. Also works on offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Has a 30% chance to inflict poison on contact moves, both when attacking and being attacked.

## Detailed Mechanical Explanation
*For Discord/reference use*

**POISON POINT** is a dual-trigger contact ability that can inflict poison status on opponents during physical combat.

### Activation Mechanics:
- **Trigger**: Both onAttacker and onDefender hooks (ON_EITHER)
- **Chance**: 30% activation rate
- **Contact Requirement**: Move must make contact
- **Status Effect**: Regular poison (1/8 max HP damage per turn)
- **Bypass**: Ignores Safeguard protection when activated

### Activation Conditions:
1. **Contact Check**: `IsMoveMakingContact(move, gBattlerAttacker)` must return true
2. **Target Eligibility**: `ShouldApplyOnHitAffect(opponent)` must pass
3. **Poison Immunity**: `CanBePoisoned(battler, opponent, MOVE_NONE)` must return true
4. **Random Chance**: 30% probability check (`Random() % 100 < 30`)

### How It Works:
**Defensive Mode** (When receiving contact moves):
- Opponent uses contact move against Poison Point user
- 30% chance to poison the attacker
- Activates after damage calculation

**Offensive Mode** (When using contact moves):
- Poison Point user uses contact move
- 30% chance to poison the target
- Activates after damage calculation

### Status Effect Details:
- **Poison Type**: Regular poison (not badly poisoned)
- **Damage**: 1/8 of poisoned Pokemon's max HP per turn
- **Duration**: Until switched out, cured, or KO'd
- **Script**: Uses `AbilityStatusEffectSafe(MOVE_EFFECT_POISON, battler, opponent)`
- **Safeguard Override**: Sets `HITMARKER_IGNORE_SAFEGUARD` flag

### Immunities and Interactions:
- **Poison Types**: Cannot poison Poison-type Pokemon
- **Steel Types**: Cannot poison Steel-type Pokemon (unless affected by special conditions)
- **Already Poisoned**: Cannot poison already poisoned Pokemon
- **Substitutes**: Blocked by Substitute
- **Magic Guard**: Does not protect from the poison infliction itself

### Contact Moves That Trigger:
- Most physical moves (Tackle, Body Slam, etc.)
- Some special moves with contact flag (Grass Knot, etc.)
- **Non-Contact Moves**: Will NOT trigger (Earthquake, Surf, etc.)

### Technical Implementation:
```c
ON_EITHER(PoisonPoint) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(CanBePoisoned(battler, opponent, MOVE_NONE))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))
    CHECK(Random() % 100 < 30)

    AbilityStatusEffectSafe(MOVE_EFFECT_POISON, battler, opponent);
    return TRUE;
}
constexpr Ability PoisonPoint = {
    ON_EITHER_ABILITY(PoisonPoint),
};
```

### Related Abilities:
- **Static**: Same mechanics but inflicts paralysis (30% chance)
- **Flame Body**: Same mechanics but inflicts burn (30% chance)
- **Cute Charm**: Same mechanics but inflicts infatuation (30% chance)
- **Poison Touch**: Identical to Poison Point (shares same implementation)
- **Effect Spore**: Similar but 30% chance for sleep/paralysis/poison

### Abilities That Share This Code:
- **Venom Crown**: Uses PoisonPoint implementation + offensive boost
- **Blight Scale**: Uses PoisonPoint implementation + defensive boost
- **Poison Quills**: Combines PoisonPoint + Rough Skin effects

### Competitive Notes:
- Excellent deterrent against physical attackers
- Works well on defensive Pokemon that can survive contact moves
- Particularly effective against multi-hit moves (each hit can trigger)
- Can be used offensively with contact moves for extra status pressure
- Synergizes well with other poison-based strategies

### Pokemon That Learn This:
Common on Poison-type Pokemon like Nidoran lines, Qwilfish, and various Poison-type species in the Elite Redux roster.

### Version History:
- Gen 3+: 30% chance to poison on contact
- Elite Redux: Enhanced to work both offensively and defensively
- Elite Redux: Bypasses Safeguard when triggered