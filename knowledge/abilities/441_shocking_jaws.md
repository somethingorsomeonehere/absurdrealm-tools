---
id: 441
name: Shocking Jaws
status: reviewed
character_count: 130
---

# Shocking Jaws - Ability ID 441

## In-Game Description
"Biting moves have 50% chance to paralyze the target."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Shocking Jaws gives all biting moves a 50% chance to paralyze the target on hit. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shocking Jaws is an offensive ability that adds a paralysis effect to all biting moves. The ability activates when the Pokemon with Shocking Jaws uses any move with the `FLAG_STRONG_JAW_BOOST` flag, giving a 50% chance to paralyze the target.

### Activation Conditions
- **Move requirement**: Must use a move with the `FLAG_STRONG_JAW_BOOST` flag (biting moves)
- **Hit requirement**: Move must successfully hit the target (`ShouldApplyOnHitAffect` check)
- **Paralysis check**: Target must be able to be paralyzed (`CanBeParalyzed` check)
- **Chance**: Exactly 50% chance (`Random() % 2`)

### Affected Moves (Biting Moves)
The following moves can trigger Shocking Jaws:
- **Basic biting moves**: Bite, Crunch, Hyper Fang, Super Fang
- **Elemental fangs**: Fire Fang, Ice Fang, Thunder Fang, Poison Fang
- **Signature bites**: Psychic Fangs, Jaw Lock, Bug Bite, Pluck, Leech Life
- **Elite Redux exclusives**: Aqua Fang, Shadow Fangs, Iron Fangs, Draconic Fangs, Fertile Fangs, Jagged Fangs, Lovely Bite, Tectonic Fangs, Kilobite, Terror Charge, Rip and Tear, Deathroll, Bolt Beak, Fishious Rend, Snap Trap

### Technical Implementation
```c
constexpr Ability ShockingJaws = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBeParalyzed(battler, target))
        CHECK(gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)
        CHECK(Random() % 2)

        return AbilityStatusEffect(MOVE_EFFECT_PARALYSIS);
    },
};
```

### Paralysis Mechanics
When successfully triggered, Shocking Jaws inflicts standard paralysis:
- **Speed reduction**: Target's Speed is reduced by 50%
- **Move failure**: 25% chance each turn that the paralyzed Pokemon cannot move
- **Status immunity**: Electric-type Pokemon are immune to paralysis
- **Overrides**: Ground-type immunity to Electric moves doesn't apply to paralysis from this ability

### Important Interactions
- **Status immunity**: Electric-type Pokemon cannot be paralyzed
- **Existing status**: Cannot paralyze Pokemon that already have a status condition
- **Ability immunity**: Limber prevents paralysis from this ability
- **Mycelium Might**: Overrides type immunity if the user has Mycelium Might
- **Contact requirement**: Most biting moves make contact, but paralysis chance is independent of contact
- **Multi-hit moves**: Each hit has a separate 50% chance to paralyze
- **Substitute**: Blocked if target is behind a Substitute

### Strategic Implications
- **Offensive pressure**: Adds status pressure to physical attackers
- **Speed control**: Paralysis can cripple fast sweepers and setup Pokemon
- **Stacking effects**: Can be combined with other status-inducing moves/abilities
- **Revenge killing**: Paralysis can turn fast threats into easier targets
- **Setup prevention**: Paralysis chance can deter setup attempts

### Synergies
- **Strong Jaw**: Many Pokemon with biting moves also have Strong Jaw for damage boost
- **Status moves**: Pairs well with other status-inducing moves for reliability
- **Priority moves**: Paralysis makes priority moves more valuable
- **Choice items**: Paralysis from coverage moves while locked in
- **Assault Vest**: Provides special bulk while using status-inducing attacks

### Counters
- **Electric types**: Immune to paralysis entirely
- **Limber**: Ability that prevents paralysis
- **Substitute**: Blocks the status effect
- **Aromatherapy/Heal Bell**: Clears paralysis from team
- **Lum Berry/Pecha Berry**: Cures paralysis immediately
- **Natural Cure**: Switches out to cure paralysis
- **Status immunity**: Pokemon with abilities that prevent status conditions

### Competitive Usage Notes
- **Reliability**: 50% chance makes it reasonably reliable for status spreading
- **Coverage moves**: Adds utility to coverage biting moves
- **Physical attackers**: Best on Pokemon that naturally learn many biting moves
- **Mixed sets**: Can provide status support on mixed attacking sets
- **Team support**: Paralysis benefits slower teammates

### Common Users
Pokemon that would benefit from Shocking Jaws typically:
- Learn multiple biting moves naturally
- Have good physical Attack stats
- Want to provide team support through status
- Can pressure opponents with status + damage

### Version History
- Elite Redux exclusive ability (ID 441)
- Designed to provide utility to physical attackers with biting moves
- Part of the expanded ability system in Elite Redux

### Similar Abilities
- **Static**: 30% paralysis chance on contact (physical moves only)
- **Flame Body**: 30% burn chance on contact
- **Poison Point**: 30% poison chance on contact
- **Effect Spore**: 30% chance for random status on contact