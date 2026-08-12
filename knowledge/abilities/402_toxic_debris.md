---
id: 402
name: Toxic Debris
status: reviewed
character_count: 267
---

# Toxic Debris - Ability ID 402

## In-Game Description
"Sets a layer of Toxic Spikes when hit by contact moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Toxic Debris automatically sets a layer of Toxic Spikes on the opponent's side when hit by a contact move. Each layer poisons switching grounded Pokemon: one layer causes regular poison, two layers cause badly poisoned. Each hit of a multihitting attack sets a layer.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Toxic Debris is a defensive ability that automatically sets up entry hazards whenever the Pokemon is damaged by a contact move. The ability provides passive board control by punishing physical attackers with hazard placement.

### Activation Conditions
- **Move requirement**: The attacking move must make contact with the Pokemon
- **Hit requirement**: The move must successfully connect and deal damage
- **Layer limit**: Will only activate if the opponent's side has fewer than 2 Toxic Spikes layers
- **Timing**: Activates immediately after taking damage from the contact move

### Toxic Spikes Mechanics
- **Layer 1**: Causes regular poison (lose 1/8 HP per turn) to grounded Pokemon that switch in
- **Layer 2**: Causes badly poisoned status (damage increases each turn: 1/16, 2/16, 3/16, etc.)
- **Maximum layers**: 2 layers total can be set on each side
- **Absorption**: Poison-type Pokemon absorb all layers when switching in
- **Immunity**: Flying-type, Levitate, and other non-grounded Pokemon are unaffected

### Technical Implementation
```c
constexpr Ability ToxicDebris = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(DidMoveHit())                                          // Move must hit
        CHECK(IsMoveMakingContact(move, attacker))                   // Must be contact move
        CHECK(gSideTimers[BATTLE_OPPOSITE(battler)].toxicSpikesAmount < 2)  // Max 2 layers

        BattleScriptCall(BattleScript_DefenderSetsToxicSpikeLayer);  // Set the layer
        return TRUE;
    },
};
```

### Important Interactions
- **Multi-hit moves**: Each hit can potentially trigger the ability (if layers available)
- **Substitute**: Ability won't activate if the Pokemon is behind a substitute
- **Ability suppression**: Doesn't work if ability is suppressed (Mold Breaker, etc.)
- **Battle message**: Displays "Poison spikes were scattered around [opponent's] feet!"
- **Contact moves only**: Non-contact moves (Earthquake, Flamethrower, etc.) won't trigger

### Contact Move Examples
**Common contact moves that trigger Toxic Debris:**
- Physical attacks: Tackle, Body Slam, Earthquake (wait, Earthquake isn't contact)
- Punch moves: Fire Punch, Ice Punch, Thunder Punch
- Slashing moves: Slash, Night Slash, Psycho Cut
- Biting moves: Bite, Crunch, Fire Fang

**Non-contact moves that DON'T trigger:**
- Earthquake, Rock Slide, Flamethrower
- Most special attacks
- Projectile moves like Rock Throw

### Strategic Implications
- **Passive hazard setting**: Forces entry hazards without using move slots
- **Physical deterrent**: Discourages contact move usage against the Pokemon
- **Team support**: Benefits the entire team by controlling switches
- **Chip damage accumulation**: Provides consistent damage over time
- **Stall synergy**: Excellent on defensive teams that want to wear down opponents

### AI Considerations
The AI recognizes Toxic Debris as a hazard-setting ability and will:
- Evaluate the benefit of setting Toxic Spikes layers
- Consider switching to non-contact moves when possible
- Factor hazard value into damage calculations

### Common Users
Toxic Debris is typically found on:
- Defensive Poison-type Pokemon
- Tank Pokemon that can survive multiple contact moves
- Pokemon designed for hazard stacking strategies
- Support Pokemon that benefit teams through passive effects

### Competitive Usage Notes
- **Entry hazard support**: Complements traditional hazard setters
- **Anti-physical**: Particularly effective against physical attackers
- **Residual damage**: Provides consistent chip damage throughout battle
- **Switch punishment**: Makes opponent's switching more costly
- **Stealth Rock synergy**: Works well with other entry hazards for maximum pressure

### Counters
- **Non-contact moves**: Use special attacks or non-contact physical moves
- **Rapid Spin/Defog**: Remove the hazards after they're set
- **Poison-types**: Switch in Poison-types to absorb the Toxic Spikes
- **Magic Guard**: Pokemon with Magic Guard ignore poison damage
- **Ability suppression**: Mold Breaker bypasses the ability entirely
- **Steel/Poison immunity**: These types can't be poisoned

### Synergies
- **Stealth Rock**: Combines with other hazards for maximum entry damage
- **Spikes**: Stacks with regular Spikes for even more switch punishment
- **Sticky Web**: Speed reduction plus poison creates switching nightmares
- **Toxic Spill**: Other Toxic Spikes setting abilities for faster setup
- **Pressure/Unnerve**: Other passive abilities that punish opponents

### Hazard Interaction Details
- **Maximum effectiveness**: 2 layers of Toxic Spikes + 3 layers of Spikes + Stealth Rock
- **Clearing methods**: Rapid Spin, Defog, and Court Change can remove hazards
- **Poison absorption**: Only Poison-types absorb Toxic Spikes, not other hazards
- **Flying immunity**: Flying-types avoid all ground-based hazards
- **Heavy-Duty Boots**: Completely negate all entry hazard damage

### Version History
- New ability introduced in Elite Redux
- Part of the expanded ability roster for enhanced strategic depth
- Fills the niche of passive hazard setting through defensive play
- Complements existing hazard-based strategies and team compositions