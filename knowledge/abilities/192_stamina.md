---
id: 192
name: Stamina
status: reviewed
character_count: 122
---

# Stamina - Ability ID 192

## In-Game Description
"Raises Defense by 1 stage when hit. Critical hits raise Defense by 12 stages."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit, raises the user's Defense by 1 stage or maximizes it on critical hits. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation

Stamina is a defensive ability that converts incoming damage into defensive power. Each time the Pokemon takes damage, it gains a Defense boost, with critical hits providing an enormous defensive advantage.

### Basic Effect
- **Normal Hits**: Raises Defense by 1 stage (+50% Defense)
- **Critical Hits**: Raises Defense by 12 stages (maximizes Defense at +600%)

### Technical Implementation
```cpp
constexpr Ability Stamina = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(CanRaiseStat(battler, STAT_DEF))

        if (gIsCriticalHit) {
            SetStatChanger(STAT_DEF, 12);
            BattleScriptCall(BattleScript_TargetsStatWasMaxedOut);
        } else {
            SetStatChanger(STAT_DEF, 1);
            BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        }
        return TRUE;
    },
};
```

### Trigger Conditions
- Must be hit by a damaging move
- Defense stat must not be at maximum (+6 stages)
- Subject to `ShouldApplyOnHitAffect` restrictions

## Strategic Applications

### Defensive Walls
Perfect for defensive Pokemon like:
- **Bastiodon**: Already has massive Defense, becomes nearly unbreakable
- **Mudsdale**: Innate Stamina makes it an exceptional physical wall
- **Rhyperior**: Assault Vest + Stamina creates a mixed defensive threat

### Bulky Setup Sweepers
Enables aggressive defensive setups:
- **Conkeldurr**: Can set up with Bulk Up while gaining passive Defense
- **Chesnaught**: Becomes incredibly bulky while setting up screens
- **Torterra**: Curse + Stamina creates unstoppable physical presence

### Critical Hit Abuse
- **Hariyama**: With Skill Link, can potentially bait criticals for massive boosts
- **Swampert**: Defensive Mega evolution becomes even more formidable

This ability fundamentally changes how damage is perceived - every attack that doesn't knock out the Pokemon makes it stronger. The critical hit mechanism provides a powerful comeback potential, as a single critical hit can transform a Pokemon into an impenetrable fortress. Stamina excels on Pokemon with naturally high HP and defensive stats, as they can survive initial hits to begin accumulating defensive boosts.

## Competitive Viability

### Strengths
- Excellent on defensive walls and bulky attackers
- Provides passive Defense boosts without requiring setup moves
- Critical hit protection creates massive defensive spikes
- Works with all damaging moves (contact and non-contact)

### Weaknesses
- Provides no protection against special attacks
- Requires surviving hits to gain benefit
- Can be overwhelmed by powerful special attackers
- No benefit if Defense is already maximized

### Synergistic Items
- **Leftovers**: Sustains longevity to accumulate more boosts
- **Assault Vest**: Complements Defense boosts with Special Defense
- **Rocky Helmet**: Punishes contact moves while gaining Defense
- **Eviolite**: On pre-evolutions like Marshtomp for extreme bulk

## Notable Pokemon

### Mudsdale
- **Role**: Premier Stamina user with innate ability
- **Strategy**: Defensive wall with Counter and recovery moves
- **EVs**: Max HP/Defense investment for optimal bulk

### Swampert Line
- **Marshtomp**: Eviolite + Stamina creates incredible mid-stage bulk
- **Swampert**: Defensive sets with Flip Turn for momentum
- **Mega Swampert**: Retains Stamina before mega evolution

### Conkeldurr
- **Role**: Mixed defensive/offensive threat
- **Strategy**: Flame Orb activation + Guts while building Defense
- **Applications**: Doubles play with Swagger support

## Interactions and Edge Cases

### Stat Stage Limitations
- Will not trigger if Defense is at +6 stages
- `CanRaiseStat` check prevents unnecessary triggers

### Battle Script Integration
- Normal hits use `BattleScript_TargetAbilityStatRaiseOnMoveEnd`
- Critical hits use `BattleScript_TargetsStatWasMaxedOut`
- Proper battle messaging for both scenarios

### Multi-Hit Moves
- Each individual hit can trigger Stamina
- Particularly effective against moves like Bullet Seed or Rock Blast

Stamina represents one of the most unique defensive abilities, converting adversity into advantage through its innovative damage-to-defense conversion mechanism.
