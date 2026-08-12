---
id: 49
name: Flame Body
status: reviewed
character_count: 124
---

# Flame Body - Ability ID 49

## In-Game Description
"30% chance to burn on contact. Also works on offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact with this Pokemon has a 30% chance to inflict burn. Non-contact has a 20% chance. Works offensively and defensively. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**FLAME BODY** is a contact-triggered status ability that can inflict burn on both offensive and defensive interactions.

### Activation Mechanics:
- **Trigger**: Any contact move made by or against the Flame Body user
- **Activation Rate**: 30% chance (Random() % 100 < 30)
- **Target**: The opposing Pokemon that initiated contact
- **Script**: Uses AbilityStatusEffectSafe(MOVE_EFFECT_BURN) with standard burn animation

### Contact Requirements:
1. **Move Must Make Contact**: 
   - Checked via `IsMoveMakingContact(move, gBattlerAttacker)`
   - Blocked by Long Reach ability or Protective Pads item
   - Special case: Shell Side Arm counts as contact when damage category swaps

2. **Hit Confirmation**:
   - Uses `ShouldApplyOnHitAffect(opponent)` which requires:
     - Move hit successfully (`DidMoveHit()`)
     - Target is still alive (`IsBattlerAlive()`)

3. **Burn Eligibility**:
   - Checked via `CanBeBurned(opponent)`:
     - No existing status condition
     - Not Fire-type (immune to burn)
     - Not protected by status immunity effects

### Burn Status Effects:
- **Damage**: 1/16 of max HP per turn at end of turn
- **Attack Reduction**: Physical attack reduced by 50%
- **Duration**: Permanent until cured or switched out
- **Interactions**: Can be cured by Natural Cure, Heal Bell, Aromatherapy, etc.

### Bidirectional Functionality:
Unlike most contact abilities, Flame Body works in both directions:
```c
ON_EITHER(FlameBody) {
    // Uses ON_EITHER_ABILITY macro for both onAttacker and onDefender
}
```

**As Attacker**: When Flame Body user attacks with contact moves
**As Defender**: When opponent attacks Flame Body user with contact moves

### Field Effect - Egg Hatching:
In the overworld, Flame Body doubles egg hatching speed:
```c
// In egg_hatch.c - GetEggStepsToSubtract()
if (ability == ABILITY_MAGMA_ARMOR || ability == ABILITY_FLAME_BODY || ability == ABILITY_SUPER_HOT_GOO)
    return 2; // Double egg steps
```

### Ability Combinations:
**Super Hot Goo** (Custom Elite Redux ability):
- Combines Flame Body with Gooey
- Retains full Flame Body functionality
- Adds Speed reduction on contact

### Technical Implementation:
```c
ON_EITHER(FlameBody) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(CanBeBurned(opponent))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))
    CHECK(Random() % 100 < 30)

    AbilityStatusEffectSafe(MOVE_EFFECT_BURN, battler, opponent);
    return TRUE;
}

constexpr Ability FlameBody = {
    ON_EITHER_ABILITY(FlameBody),
};
```

### Competitive Applications:
- **Physical Wall Support**: Deters physical attackers with burn threat
- **Breeding Utility**: Essential for efficient egg hatching
- **Contact Punish**: Works on both offense and defense unlike Static/Poison Point
- **Status Spreading**: Can burn on your own attacks, spreading chip damage

### Counters and Limitations:
- **Fire-types**: Completely immune to burn status
- **Non-contact moves**: No activation (Earthquake, Psychic, etc.)
- **Long Reach**: Prevents contact entirely
- **Protective Pads**: Blocks contact effects
- **Guts/Marvel Scale**: Turn burn into advantage
- **Magic Guard**: Prevents burn damage (but not Attack reduction)

### Strategic Considerations:
- More threatening on defensive Pokemon due to guaranteed contact from attacks
- Offensive use requires careful move selection (contact moves only)
- Excellent deterrent against physical setup sweepers
- Pairs well with Will-O-Wisp for consistent burn spreading
- Especially valuable in formats with limited status moves

### Version History:
- Gen 3: Contact-based burn chance introduced
- Elite Redux: Retains 30% activation rate, works bidirectionally