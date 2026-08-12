---
id: 401
name: Loose Quills
status: reviewed
character_count: 255
---

# Loose Quills - Ability ID 401

## In-Game Description
"Sets a layer of Spikes when hit (contact move)."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets a layer of Spikes on the opponent's side when the user is successfully hit by a contact move. Each layer damages switching grounded Pokemon by 12.5%, 16.7%, or 25% of max HP for 1-3 layers respectively. Each hit of a multihitting attack sets a layer.


## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Loose Quills is a defensive ability that automatically sets up Spikes entry hazards when the Pokemon is hit by contact moves. This creates a passive punishment for physical attackers while providing excellent team support through hazard control.

### Activation Conditions
- **Contact requirement**: Only triggers when hit by moves that make physical contact
- **Hit requirement**: The move must successfully hit and deal damage
- **Layer limit**: Will not activate if the opponent already has 3 layers of Spikes
- **No self-damage**: Does not activate on self-inflicted damage or recoil

### Technical Implementation
```c
// Loose Quills shares implementation with Scrapyard ability
constexpr Ability LooseQuills = {
    .onDefender = Scrapyard.onDefender,
};

// Scrapyard/Loose Quills implementation
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

### Spikes Damage Calculation
- **1 layer**: 12.5% of max HP (1/8)
- **2 layers**: 16.7% of max HP (1/6) 
- **3 layers**: 25% of max HP (1/4)

Damage is calculated based on the switching Pokemon's maximum HP and is not affected by type effectiveness.

### Contact Move Examples
**Triggers on:**
- Physical attacks like Tackle, Quick Attack, Thunder Punch
- Most Fighting, Normal, and physical moves
- U-turn, Volt Switch (if physical contact versions)

**Does NOT trigger on:**
- Special attacks (Thunderbolt, Flamethrower, etc.)
- Non-contact physical moves (Earthquake, Rock Slide)
- Status moves
- Moves that miss or are blocked

### Important Interactions
- **Long Reach**: Moves with Long Reach will not trigger Loose Quills
- **Protective Pads**: Held item prevents contact, so no Spikes are set
- **Magic Guard**: Still sets Spikes even if the defender takes no damage
- **Substitute**: Sets Spikes when Substitute is hit by contact moves
- **Multi-hit moves**: Only triggers once per multi-hit attack sequence

### Strategic Applications
- **Physical wall utility**: Punishes common physical attackers
- **Team support**: Provides passive hazard setting without move slots
- **Switch control**: Forces opponents to think twice about switching
- **Entry hazard stacking**: Can combine with Stealth Rock and Toxic Spikes
- **Revenge utility**: Punishes the attacker even if you're knocked out

### Synergies
- **Stealth Rock setters**: Maximize entry hazard damage
- **Toxic Spikes users**: Create multiple hazard layers
- **Spin blockers**: Ghost-types prevent hazard removal
- **Sturdy/Focus Sash**: Guarantees at least one Spikes layer
- **Rocky Helmet**: Stacks recoil damage with hazard setting

### Counters and Limitations
- **Special attackers**: Completely avoid triggering the ability
- **Non-contact moves**: Earthquake, Rock Slide, etc. don't trigger
- **Hazard removal**: Rapid Spin, Defog clear the Spikes
- **Magic Bounce**: Reflects the Spikes back to your side
- **Flying types/Levitate**: Immune to Spikes damage
- **Heavy-Duty Boots**: Negates Spikes damage on switch-in

### Competitive Viability
- **Defensive utility**: Excellent on bulky physical walls
- **Passive support**: Provides team utility without sacrificing moveslots  
- **Meta dependent**: More valuable in physical-heavy metagames
- **Hazard control**: Part of comprehensive entry hazard strategies
- **Prediction reward**: Rewards switching into predicted physical attacks

### Common Users
- Defensive Grass-types (especially those weak to U-turn)
- Steel-type walls that can tank physical hits
- Pokemon with high physical Defense stats
- Team supporters that don't need four attacking moves

### Version History
- Introduced in Elite Redux as ability ID 401
- Shares exact implementation with Scrapyard ability
- Part of the expanded ability roster for defensive utility

### Related Abilities
- **Scrapyard**: Identical effect and implementation  
- **Iron Barbs**: Damages contact attackers instead of setting hazards
- **Rough Skin**: Similar contact punishment concept
- **Toxic Debris**: Sets Toxic Spikes instead of regular Spikes