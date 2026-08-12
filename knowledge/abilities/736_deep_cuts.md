---
id: 736
name: Deep Cuts
status: reviewed
character_count: 272
---

# Deep Cuts - Ability ID 736

## In-Game Description
"Slashing moves have a 50% chance to inflict bleeding."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Keen Edge have a 50% chance to inflict bleeding on hit. Bleeding causes 1/16 max HP damage per turn, prevents healing, and negates the effects of stat stages. Rock and Ghost types are immune to bleeding.immune to bleeding. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Deep Cuts is an offensive ability that adds a bleeding status effect to slashing moves. When the user lands a slashing attack, there's a 50% chance the target will begin bleeding.

### Activation Conditions
- **Move requirement**: The move must have the `FLAG_KEEN_EDGE_BOOST` flag (slashing moves)
- **Hit requirement**: The move must successfully hit and deal damage
- **Status requirement**: Target must be able to receive bleeding status
- **Probability**: 50% chance per eligible move hit

### Technical Implementation
```c
constexpr Ability DeepCuts = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBleed(target))
        CHECK(gBattleMoves[move].flags & FLAG_KEEN_EDGE_BOOST)
        CHECK(Random() % 2)

        return AbilityStatusEffect(MOVE_EFFECT_BLEED);
    },
};
```

### Bleeding Status Effect
- **Damage**: 1/16 of max HP per turn (`BLEED_DAMAGE(hp) = hp / 16`)
- **Duration**: Until healed or switched out
- **Timing**: Damage occurs at end of turn
- **Minimum damage**: Always at least 1 HP if bleeding

### Eligible Moves
Deep Cuts works with all moves that have the `FLAG_KEEN_EDGE_BOOST` flag, including:
- **Slash**: Basic slashing move
- **Fury Cutter**: Consecutive slashing attack
- **Razor Wind**: Two-turn slashing move
- **Night Slash**: Dark-type slashing move
- **Psycho Cut**: Psychic-type slashing move
- **Air Slash**: Flying-type slashing move
- **Sacred Sword**: Fighting-type blade move
- **Leaf Blade**: Grass-type cutting move
- And many others with the Keen Edge designation

### Bleeding Immunity
Certain Pokemon types cannot be affected by bleeding:
- **Rock types**: Cannot bleed due to mineral composition
- **Ghost types**: Cannot bleed due to incorporeal nature
- **Pokemon with status**: Cannot receive bleeding if already statused
- **Status immunity**: Pokemon with abilities that prevent status

### Important Interactions
- **Status immunity**: Doesn't work on Pokemon with status immunity abilities
- **Magic Guard**: Prevents bleeding damage but not the status itself
- **Healing**: Bleeding can be cured by items, moves, or switching out
- **Stacking**: Cannot stack with other major status conditions
- **Multi-hit moves**: Each hit has separate 50% chance to inflict bleeding

### Strategic Applications
- **Pressure damage**: Forces opponents to heal or switch frequently
- **Stallbreaking**: Counters defensive strategies with gradual damage
- **Finisher potential**: Can secure KOs on weakened opponents
- **Team support**: Provides chip damage for team cleanup
- **Status spreading**: Forces opponents to use healing resources

### Counters and Limitations
- **Type immunity**: Rock and Ghost types are completely immune
- **Status immunity**: Abilities like Limber, Water Veil prevent bleeding
- **Healing items**: Pecha Berry, Full Heal cure bleeding immediately
- **Natural Cure**: Ability removes bleeding when switching out
- **Cleric support**: Heal Bell and Aromatherapy cure bleeding
- **Non-slashing moves**: Ability only works with Keen Edge flagged moves

### Synergies
- **Keen Edge**: Boosts damage of same moves that can cause bleeding
- **Choice items**: Locked slashing moves maximize bleeding chances
- **Multi-hit moves**: Increases bleeding application opportunities
- **Pursuit**: Can punish bleeding Pokemon trying to switch
- **Entry hazards**: Combines with Stealth Rock for maximum pressure

### Competitive Usage
- **Physical attackers**: Best on Pokemon with strong slashing movesets
- **Pressure builds**: Excellent for wearing down bulky opponents
- **Anti-stall**: Counters defensive teams that rely on recovery
- **Hit-and-run**: Good for Pokemon that can switch after applying bleeding
- **Revenge killing**: Bleeding can finish off weakened sweepers

### Team Building Considerations
- **Move selection**: Prioritize slashing moves in moveset
- **Coverage**: Ensure access to multiple slashing move types
- **Speed tiers**: Faster Pokemon apply bleeding more reliably
- **Support**: Pair with entry hazards and other chip damage
- **Healing**: Team should pressure opponents' healing resources

### Version History
- Added in Elite Redux as part of expanded ability roster
- Unique status-inflicting ability for physical attackers
- Designed to provide alternative to standard status moves