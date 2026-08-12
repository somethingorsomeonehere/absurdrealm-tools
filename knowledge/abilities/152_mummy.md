---
id: 152
name: Mummy
status: reviewed
character_count: 136
---

# Mummy - Ability ID 152

## In-Game Description
"If hit, makes the attacker's ability Mummy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user receives a contact move from another Pokemon who does not have this ability, it replaces their current ability with Mummy.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- When the Mummy user is hit by a **contact move**, the attacker's ability is immediately replaced with Mummy
- The effect activates after damage calculation but before any other contact-based abilities
- Creates a "viral" spreading effect where multiple Pokemon can end up with Mummy

**Activation Conditions:**
1. **Move must hit**: Uses `ShouldApplyOnHitAffect(attacker)` which checks `DidMoveHit() && IsBattlerAlive(applyTo)`
2. **Contact required**: Uses `IsMoveMakingContact(move, attacker)` - only physical contact moves trigger the effect
3. **Attacker doesn't have Mummy**: Prevents redundant activation with `HasAbilityIgnoringSuppression(attacker, ability)`
4. **Ability can be changed**: Blocks activation against persistent/unsuppressable abilities via `IsPersistentOrUnsuppressableAbility(GetBattlerAbility(attacker))`
5. **No Ability Shield**: The Ability Shield held item blocks Mummy with `DoesBattlerHaveAbilityShield(attacker)`

**Technical Implementation:**
```cpp
constexpr Ability Mummy = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK_NOT(HasAbilityIgnoringSuppression(attacker, ability))
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK_NOT(IsPersistentOrUnsuppressableAbility(GetBattlerAbility(attacker)))
        CHECK_NOT(DoesBattlerHaveAbilityShield(attacker))

        UpdateAbilityStateIndicesForNewAbility(attacker, ability);
        ReplaceAbility(attacker, ability);
        BattleScriptCall(BattleScript_MummyActivates);
        return TRUE;
    },
};
```

**Abilities That Block Mummy:**
- **Persistent abilities**: Cannot be changed once set (like Multitype on Arceus)
- **Unsuppressable abilities**: Core form-dependent abilities that cannot be removed
- **Any ability protected by Ability Shield**: The held item provides complete protection

**Contact Moves That Trigger Mummy:**
- All physical moves that make contact (Tackle, Punch moves, Body Slam, etc.)
- Some special moves with contact flags (Grass Knot, Petal Dance in some implementations)
- **Does NOT trigger on**: Earthquake, Rock Slide, Flamethrower, Psychic, etc. (non-contact moves)

**Strategic Applications:**
1. **Disruption Tool**: Removes key abilities from physical attackers (Huge Power, Guts, Speed Boost, etc.)
2. **Team Spread**: Multiple opposing Pokemon can end up with Mummy through chain reactions
3. **Anti-Physical Tank**: Punishes contact-based physical attackers heavily
4. **Doubles Strategy**: Can disrupt both opponents' abilities if they both use contact moves

**Interactions with Other Mechanics:**
- **Trace**: Pokemon with Trace will copy Mummy, but won't spread it until hit by contact
- **Role Play/Skill Swap**: Can be copied/swapped normally since it's not unsuppressable
- **Neutralizing Gas**: Temporarily suppresses Mummy like other abilities
- **Multi-hit moves**: Mummy activates on the first hit that makes contact

**Common Users in Elite Redux:**
- **Dusclops**: Bulky physical wall with Mummy as disruption option
- **Yamask**: Early-game Mummy spreader with decent defensive stats
- **Cofagrigus**: Evolved form with improved bulk and Ghost/Steel typing for better survivability

**Damage Calculations:**
- Mummy activates AFTER damage is calculated, so the original ability affects the damage dealt
- Example: Huge Power Machamp hits Dusclops to Machamp deals doubled damage to Machamp loses Huge Power and gains Mummy

**Battle Message:**
- Displays "ATTACKER acquired MUMMY!" when the ability is successfully transferred
- Uses `BattleScript_MummyActivates` which calls `STRINGID_ATTACKERACQUIREDABILITY`

**Competitive Viability:**
- Strong anti-meta tool against physical sweepers
- Particularly effective in formats with common contact moves
- Can single-handedly shut down setup sweepers that rely on abilities
- Weak to special attackers and non-contact physical moves