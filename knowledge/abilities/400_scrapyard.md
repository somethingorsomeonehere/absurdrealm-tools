---
id: 400
name: Scrapyard
status: reviewed
character_count: 255
---

# Scrapyard - Ability ID 400

## In-Game Description
"Sets a layer of Spikes when hit (contact move)."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets a layer of Spikes on the opponent's side when the user is successfully hit by a contact move. Each layer damages switching grounded Pokemon by 12.5%, 16.7%, or 25% of max HP for 1-3 layers respectively. Each hit of a multihitting attack sets a layer.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Scrapyard is a defensive ability that automatically sets up entry hazards when the Pokemon is hit by contact moves. The ability places Spikes on the opponent's side of the field, creating a hazard that damages Pokemon switching in.

### Activation Conditions
- **Move requirement**: Must be hit by a contact move (physical moves that make contact)
- **Hit confirmation**: Move must successfully connect (DidMoveHit() check)
- **Layer limit**: Only triggers when opponent has fewer than 3 Spike layers
- **Timing**: Activates after taking damage from the contact move

### Technical Implementation
```c
constexpr Ability Scrapyard = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(DidMoveHit())
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK(gSideTimers[BATTLE_OPPOSITE(battler)].spikesAmount < 3)

        BattleScriptCall(BattleScript_DefenderSetsSpikeLayer_Scrapyard);
        return TRUE;
    },
};
```

### Spikes Damage Mechanics
- **1 Layer**: 12.5% (1/8) of max HP damage on switch-in
- **2 Layers**: 16.7% (1/6) of max HP damage on switch-in  
- **3 Layers**: 25% (1/4) of max HP damage on switch-in
- **Flying types**: Immune to Spikes damage
- **Levitate ability**: Immune to Spikes damage
- **Air Balloon**: Immune while holding item

### Contact Move Examples
Contact moves that trigger Scrapyard include:
- Physical attacks like Tackle, Body Slam, Earthquake
- Most melee-range physical moves
- Some special moves that make contact (rare)

### Non-Contact Moves
Moves that do NOT trigger Scrapyard:
- Projectile moves (Rock Slide, Stone Edge)
- Ranged attacks (Surf, Flamethrower)
- Most special attacks
- Moves with "no contact" flag

### Shared Implementation
Loose Quills ability shares the exact same implementation as Scrapyard:
```c
constexpr Ability LooseQuills = {
    .onDefender = Scrapyard.onDefender,
};
```

### Strategic Implications
- **Physical deterrent**: Discourages contact move spam
- **Entry hazard setup**: Provides free hazard layers without turn investment  
- **Passive punishment**: Punishes attackers for making contact
- **Team support**: Benefits teammates by setting up hazards
- **Stacking damage**: Multiple activations create significant switch penalty

### Synergies
- **Rocky Helmet**: Stacks contact damage with Scrapyard hazards
- **Iron Barbs/Rough Skin**: Additional contact punishment
- **Other entry hazards**: Combines with Stealth Rock for maximum pressure
- **Hazard control**: Benefits from Rapid Spin/Defog blocking
- **Trapping moves**: Prevents switching to avoid accumulated hazards

### Counters and Limitations
- **Non-contact moves**: Special attacks bypass the ability entirely
- **Ranged physical moves**: Rock Slide, Stone Edge, etc. don't trigger
- **Flying types**: Immune to the Spikes damage
- **Levitate/Air Balloon**: Hazard immunity negates benefit
- **Hazard removal**: Rapid Spin, Defog clear the Spikes
- **Magic Guard**: Takes no indirect damage from Spikes
- **Maximum layers**: Stops working once 3 layers are set

### Common Users
Based on trainer data, Scrapyard appears on defensive Pokemon that:
- Want to punish physical attackers
- Provide team support through hazards
- Have good bulk to survive contact moves
- Benefit from discouraging physical attacks

### Competitive Applications
- **Physical walls**: Punish common physical attackers
- **Hazard setters**: Passive hazard application
- **Anti-meta**: Counters contact-heavy physical offense  
- **Team support**: Provides entry hazard pressure
- **Momentum control**: Forces switches due to hazard accumulation

### Version History
- Custom ability in Elite Redux
- Shares implementation with Loose Quills
- Part of the expanded ability roster for strategic depth
- Designed to counter physical offense dominance