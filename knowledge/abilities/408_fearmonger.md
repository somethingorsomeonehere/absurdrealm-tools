---
id: 408
name: Fearmonger
status: reviewed
character_count: 177
---

# Fearmonger - Ability ID 408

## In-Game Description
"Intimidate + Scare; 10% para chance on contact moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Fearmonger lowers both Attack and Special Attack of opposing Pokemon upon entry by one stage. Additionally provides a 10% chance to inflict paralysis when landing contact moves. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fearmonger is a hybrid intimidation ability that combines the effects of both Intimidate (lowers Attack) and Scare (lowers Special Attack) while also providing a contact-based paralysis chance. It serves as one of the most comprehensive entry hazard abilities for disrupting opposing offensive teams.

### Activation Conditions
- **Entry effect**: Activates upon switching into battle
  - Lowers Attack by 1 stage on all opposing Pokemon
  - Lowers Special Attack by 1 stage on all opposing Pokemon
  - Affects both opponents in double battles
- **Contact effect**: 10% chance to inflict paralysis
  - Triggers when the user makes contact with moves
  - Requires the move to successfully hit and deal damage
  - Subject to paralysis immunity and status condition blocking

### Technical Implementation
```c
// Entry effect uses UseIntimidateClone with dual stat reduction
constexpr Ability Fearmonger = {
    .onEntry = UseIntimidateClone,  // Triggers intimidate clone system
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBeParalyzed(battler, target))
        CHECK(IsMoveMakingContact(move, battler))
        CHECK(Random() % 100 < 10)  // 10% chance

        return AbilityStatusEffect(MOVE_EFFECT_PARALYSIS);
    },
};

// Intimidate clone data defines which stats are lowered
{
    .ability = ABILITY_FEARMONGER,
    .numStatsLowered = 2,
    .statsLowered = {STAT_ATK, STAT_SPATK, 0},  // Both physical and special attack
    .targetBoth = TRUE,  // Affects both opponents in doubles
}
```

### Stat Changes on Entry
- **Attack**: Reduced by 1 stage on all opposing Pokemon
- **Special Attack**: Reduced by 1 stage on all opposing Pokemon
- **Targeting**: Affects all opposing Pokemon (both in double battles)
- **Timing**: Occurs immediately upon entry, before other abilities

### Contact Paralysis Effect
- **Activation rate**: 10% on contact moves
- **Requirements**:
  - Move must make contact (physical moves that touch the opponent)
  - Move must successfully hit and deal damage
  - Target must be capable of being paralyzed
- **Interaction with immunities**:
  - Electric-types are immune to paralysis
  - Limber ability prevents paralysis
  - Already paralyzed Pokemon cannot be paralyzed again

### Important Interactions
- **Intimidate immunity**: Pokemon with abilities like Clear Body, White Smoke, or Hyper Cutter are immune to the stat reductions
- **Guard Dog**: Causes Guard Dog to activate, raising Attack instead of lowering it
- **Defiant/Competitive**: Triggers these abilities, potentially giving the opponent stat boosts
- **Substitute**: Contact moves hitting a substitute do not trigger the paralysis effect
- **Multi-hit moves**: Each hit can potentially trigger paralysis
- **Ability suppression**: Mold Breaker and similar abilities don't affect entry intimidation but may affect contact paralysis

### Strategic Applications
- **Entry hazard**: Immediate offensive disruption upon switching in
- **Mixed wall**: Reduces both physical and special damage output from opponents
- **Status support**: Provides additional utility through paralysis infliction
- **Anti-setup**: Particularly effective against setup sweepers who rely on stat boosts
- **Pivot utility**: Can switch in, disrupt, and potentially cripple with paralysis

### Defensive Utility
- **Immediate impact**: Unlike many abilities, provides value instantly upon entry
- **Dual coverage**: Affects both physical and special attackers equally
- **Team support**: Benefits the entire team by weakening opposing offensive presence
- **Longevity**: Paralysis can provide long-term speed control and damage reduction

### Counters and Limitations
- **Intimidate immunity**: Clear Body, White Smoke, Hyper Cutter, Full Metal Body
- **Stat boost abilities**: Defiant, Competitive turn the debuffs into buffs
- **Non-contact moves**: Special attackers using non-contact moves avoid paralysis
- **Status immunity**: Electric-types and Limber users ignore paralysis
- **Taunt**: Doesn't prevent the ability from working (unlike setup moves)
- **Substitute**: Blocks the contact paralysis effect

### Common Users
Based on SpeciesList.textproto analysis, Fearmonger appears on:
- **Legendary/Mythical Pokemon**: High-tier threats with exceptional stats
- **Dark-type specialists**: Often paired with Dark Aura or shadow abilities
- **Physical walls**: Pokemon that benefit from reducing offensive pressure
- **Utility Pokemon**: Those designed for support and disruption roles
- **Mixed attackers**: Pokemon that can take advantage of the disruption they create

### Synergies
- **Entry hazards**: Stealth Rock, Spikes compound the switching pressure
- **Status moves**: Thunder Wave, Will-O-Wisp for additional status spreading
- **Pivoting moves**: U-turn, Volt Switch to maximize entry opportunities
- **Recovery moves**: Roost, Recover to maintain longevity for repeated entries
- **Dark Aura**: Common pairing that boosts Dark-type moves
- **Shadow Shield**: Often paired for additional bulk

### Competitive Usage Notes
- **Tier considerations**: Appears primarily on high-tier legendary Pokemon
- **Role compression**: Combines multiple forms of utility in one ability
- **Meta impact**: Forces opponents to consider both physical and special attacking options
- **Team building**: Excellent on defensive pivots and bulky utility Pokemon
- **Doubles viability**: Particularly strong in doubles where it affects both opponents

### Version History
- Elite Redux original ability combining classic intimidation effects
- Unique implementation using the intimidate clone system
- One of the few abilities that combines entry effects with contact effects
- Designed for high-tier Pokemon to provide immediate battle impact

### Notable Pokemon Users
From the codebase analysis, some notable users include:
- Nidoking (as innate ability)
- Various Shadow/Dark-type legendaries
- High-tier utility Pokemon with mixed defensive roles
- Pokemon designed for disruption and support roles

### Comparison to Similar Abilities
- **Intimidate**: Only lowers Attack; Fearmonger adds Special Attack reduction
- **Scare**: Only lowers Special Attack; Fearmonger adds Attack reduction and paralysis
- **Static/Flame Body**: Only 30% contact status; Fearmonger adds entry intimidation
- **Pressure**: Different utility focus; doesn't provide immediate offensive disruption