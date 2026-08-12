---
id: 538
name: Voodoo Power
status: reviewed
character_count: 249
---

# Voodoo Power - Ability ID 538

## In-Game Description
"30% chance to bleed when hit by special attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Voodoo Power gives the user a 30% chance to inflict bleeding on attackers when hit by special moves. Bleeding causes 1/16 max HP damage per turn, prevents healing, and negates the effects of stage stages. Rock and Ghost types are immune to bleeding.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger**: When the Pokemon with Voodoo Power is hit by a special attack
- **Activation Rate**: 30% chance (Random() % 100 < 30)
- **Effect**: Inflicts bleeding status on the attacker
- **Bleeding Damage**: 1/16 of max HP per turn (minimum 1 HP)

### Activation Conditions
1. **ShouldApplyOnHitAffect(attacker)** - Standard contact effect checks
2. **IS_MOVE_SPECIAL(move)** - Move must be classified as special attack
3. **CanBleed(attacker)** - Attacker must not be immune to bleeding
4. **30% Random Chance** - Uses standard RNG check

### Technical Implementation
```c
constexpr Ability VoodooPower = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IS_MOVE_SPECIAL(move))
        CHECK(CanBleed(attacker))
        CHECK(Random() % 100 < 30)

        AbilityStatusEffect(MOVE_EFFECT_AFFECTS_USER | MOVE_EFFECT_BLEED);
        return TRUE;
    },
};
```

### Special Attack Classification
Special moves include all moves that use the Special Attack stat:
- **Elemental attacks**: Thunderbolt, Flamethrower, Ice Beam, Energy Ball
- **Psychic moves**: Psychic, Psybeam, Future Sight
- **Dark moves**: Dark Pulse, Shadow Ball
- **Status moves that deal damage**: Hidden Power, Weather Ball (when special)

### Bleeding Status Effect
- **Damage Formula**: `BLEED_DAMAGE(maxHP) = maxHP / 16`
- **Minimum Damage**: 1 HP per turn
- **Duration**: Until cured or Pokemon faints
- **Status Type**: STATUS1_BLEED
- **Interaction with Healing**: Bleeding prevents many recovery moves from working

### Immunity and Interactions
**Pokemon that cannot bleed:**
- Pokemon with abilities that grant status immunity
- Steel-type Pokemon (if bleeding follows poison immunity rules)
- Pokemon already affected by bleeding

**Ability Interactions:**
- **Magic Guard**: Protects from bleeding damage
- **Poison Heal**: Does not interact with bleeding
- **Blood Stain**: Creates pseudo-bleeding effect

### Comparison to Similar Abilities
**vs. Spike Armor (ID 537):**
- Spike Armor: 30% bleed chance on **contact moves** (physical)
- Voodoo Power: 30% bleed chance on **special moves**
- Both use same bleeding mechanics but different triggers

**vs. Poison Point:**
- Poison Point: Contact-based poison infliction
- Voodoo Power: Special move-based bleeding infliction
- Different status effects with different damage calculations

### Strategic Implications
**Defensive Usage:**
- Punishes special attackers for making contact
- Provides passive damage over time
- Forces switches or healing investment
- Particularly effective against special sweepers

**Counters:**
- Physical attackers bypass the ability entirely
- Pokemon immune to bleeding
- Status moves that don't deal damage
- Magic Guard users ignore bleeding damage
- Rapid switching to avoid turn damage

### Competitive Viability
**Strengths:**
- Passive damage accumulation
- Deters special attackers
- No contact requirement unlike similar abilities
- Stacks with other forms of passive damage

**Weaknesses:**
- Only 30% activation rate
- No effect against physical moves
- Many Pokemon can cure bleeding easily
- Doesn't affect non-damaging moves

### Example Damage Calculations
**Against 100 HP Pokemon:**
- Bleeding damage per turn: 100 ÷ 16 = 6 HP
- Total potential damage over 5 turns: 30 HP

**Against 400 HP Pokemon:**
- Bleeding damage per turn: 400 ÷ 16 = 25 HP  
- Total potential damage over 5 turns: 125 HP

### Common Users
This ability would typically be found on:
- Defensive Ghost/Dark-type Pokemon
- Voodoo/mystic-themed Pokemon
- Pokemon designed to counter special attackers
- Bulky support Pokemon with retaliatory abilities

### Version History
- Added in Elite Redux as part of expanded ability system
- Uses established bleeding mechanics from other abilities
- Part of counter-based ability design philosophy