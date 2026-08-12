---
id: 720
name: Stun Shock
status: reviewed
character_count: 153
---

# Stun Shock - Ability ID 720

## In-Game Description
"Attacks have a 60% chance to Paralyze or Poison."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user lands an attack, there's a 60% chance of inflicting poison or paralysis, chosen randomly. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Stun Shock is an offensive ability that applies additional status effects to attacks. Each time the Pokemon successfully hits an opponent, there's a 60% chance to inflict either Paralysis or Poison.

### Activation Conditions
- **Hit requirement**: Must successfully hit the target with an attack
- **Trigger chance**: 60% probability per successful hit
- **Status selection**: Random choice between Paralysis (50%) and Poison (50%)
- **Contact check**: Uses `ShouldApplyOnHitAffect` function for validation
- **Immunity check**: Respects standard status immunity rules

### Technical Implementation
```c
constexpr Ability StunShock = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target)) 
        CHECK(Random() % 100 < 60) 
        switch (Random() % 2) {
            case 0:
                CHECK(CanBePoisoned(battler, target, MOVE_NONE));
                AbilityStatusEffect(MOVE_EFFECT_POISON);
                return TRUE;
            case 1:
                CHECK(CanBeParalyzed(battler, target))
                AbilityStatusEffect(MOVE_EFFECT_PARALYSIS);
                return TRUE;
        }
        return FALSE;
    },
};
```

### Status Effects Applied
- **Paralysis**: 25% speed reduction, 25% chance to be unable to move
- **Poison**: Deals 1/8 max HP damage at end of each turn
- **Random selection**: Equal 50/50 chance between the two effects

### Important Interactions
- **Type immunity**: Poison-types cannot be poisoned, Electric-types cannot be paralyzed
- **Ability immunity**: Limber prevents paralysis, Poison Heal/Immunity prevent poison
- **Already statused**: Cannot apply status to already statused Pokemon
- **Substitute**: Blocked by Substitute
- **Multi-hit moves**: Can trigger on each hit of multi-hit moves
- **Status Orb items**: Can interact with Flame/Toxic Orb holders

### Battle Strategy
- **Pressure tool**: Forces opponents to deal with status conditions
- **Disruption**: Slows down fast sweepers with paralysis
- **Chip damage**: Poison provides consistent damage over time
- **Setup prevention**: Status effects can disrupt setup attempts
- **Switch pressure**: Forces switches to avoid status accumulation

### Synergies
- **Multi-hit moves**: U-turn, Bullet Seed, Rock Blast for multiple chances
- **Contact moves**: Physical attacks benefit most from the effect
- **Status punishment**: Hex, Venoshock deal extra damage to statused foes
- **Guts users**: Can punish Guts activation with poison instead of burn

### Counters
- **Type immunity**: Electric and Poison types resist respective effects
- **Status immunity**: Limber, Poison Heal, Natural Cure abilities
- **Clerics**: Heal Bell, Aromatherapy remove status conditions  
- **Substitute**: Blocks the status application entirely
- **Non-contact moves**: Special attacks may avoid triggering conditions
- **Already statused**: Cannot stack status effects

### Competitive Viability
- **Disruption value**: High chance to inflict useful status effects
- **Unpredictability**: Random status selection keeps opponents guessing
- **Consistent pressure**: 60% chance provides reliable disruption
- **Team support**: Helps teammates by weakening opponents
- **Entry deterrent**: Makes switching into the Pokemon risky

### Common Users
Best suited for Pokemon that:
- Make frequent contact attacks
- Have good offensive presence
- Benefit from opponent disruption
- Can capitalize on status effects
- Need additional utility beyond raw damage

### Version History
- Elite Redux custom ability
- Part of the expanded ability roster
- Designed to provide offensive status spreading
- Balanced with 60% activation rate for consistency without being overpowered