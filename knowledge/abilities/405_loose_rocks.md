---
id: 405
name: Loose Rocks
status: reviewed
character_count: 214
---

# Loose Rocks - Ability ID 405

## In-Game Description
"Deploys Stealth Rocks when hit by contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Set Stealth Rock on the opponent's side when the user is hit by any contact move. Stealth Rock deals 1/8th of the opponent's max HP when switching. Considered Rock-type damage and is modified by type effectiveness. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Loose Rocks is a defensive punishing ability that automatically sets up Stealth Rock hazards on the opponent's side of the field whenever the ability holder is hit by a contact move. This creates a powerful deterrent against physical attacks and punishes opponents for making contact.

### Activation Conditions
- **Move requirement**: The incoming move must make contact with the defender
- **Hit requirement**: The move must successfully hit (not miss, be blocked, etc.)
- **Side status check**: Stealth Rock must not already be present on the opponent's side
- **Battle timing**: Can only activate once per battle per opposing side

### Contact Move Examples
Contact moves that trigger Loose Rocks include:
- **Physical attacks**: Tackle, Body Slam, Earthquake, Close Combat
- **Status moves**: Thunder Wave (if it makes contact)
- **Multi-hit moves**: Each hit can potentially trigger (but only once per side)

### Non-Contact Moves
These moves will NOT trigger Loose Rocks:
- **Projectile moves**: Rock Slide, Flamethrower, Ice Beam
- **Sound moves**: Hyper Voice, Boomburst
- **Pulse moves**: Aura Sphere, Dragon Pulse
- **Long-range moves**: Surf, Earthquake (in some contexts)

### Technical Implementation
```cpp
constexpr Ability LooseRocks = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(DidMoveHit())
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK_NOT(gSideStatuses[BATTLE_OPPOSITE(battler)] & SIDE_STATUS_STEALTH_ROCK)

        BattleScriptCall(BattleScript_DefenderSetsStealthRock);
        return TRUE;
    },
};
```

### Stealth Rock Mechanics
When Loose Rocks triggers, it sets up Stealth Rock on the opponent's side:
- **Entry hazard**: Damages switching Pokemon based on Rock-type effectiveness
- **Damage calculation**: 1/8 max HP x type effectiveness multiplier
- **Type effectiveness**: 
  - 2x damage to Fire, Flying, Bug, Ice types
  - 1x damage to most types
  - 0.5x damage to Steel, Fire types with resist
  - 0.25x damage to Steel types that resist

### Strategic Implications
- **Physical deterrent**: Discourages opponents from using contact moves
- **Switching punishment**: Forces opponents to take hazard damage when switching
- **One-time use**: Can only set Stealth Rock once per battle per side
- **Passive setup**: Requires no turns or move slots to deploy hazards
- **Defensive value**: Provides utility even on defensive Pokemon

### Important Limitations
- **Single activation**: Only works once per battle per opposing side
- **Contact dependency**: Useless against special attackers using ranged moves
- **Hazard clearing**: Opponent can remove with Rapid Spin, Defog, etc.
- **No self-protection**: Doesn't prevent the contact move from dealing damage

### Timing and Interactions
- **Damage first**: The triggering contact move deals its damage first
- **Then hazards**: Stealth Rock is set up after damage calculation
- **Fainting**: Can still trigger even if the ability holder faints from the contact move
- **Substitute**: May not trigger if opponent attacks through Substitute

### Team Synergy
- **Hazard stacking**: Combines well with other hazard setters (Spikes, Toxic Spikes)
- **Spinner blocking**: Pairs with Ghost types that block Rapid Spin
- **Pressure builds**: Works well on teams that force switches
- **Defensive cores**: Excellent on bulky Pokemon that expect physical hits

### Competitive Applications
- **Physical walls**: Great on defensive Pokemon that wall physical attackers
- **Hazard support**: Provides passive hazard setting without moveslot investment
- **Meta dependent**: More valuable in metas with common contact moves
- **Surprise factor**: Opponents may not expect immediate Stealth Rock setup

### Common Users
- **Rock-type Pokemon**: Thematically fits Rock types that might shed stones
- **Defensive Pokemon**: Bulky defensive walls that can survive contact moves
- **Ground types**: Pokemon associated with rocky terrain and debris
- **Physically defensive**: Pokemon built to take physical hits repeatedly

### Counters and Counterplay
- **Special attacks**: Use special moves that don't make contact
- **Hazard removal**: Rapid Spin, Defog, Magic Bounce
- **Long-range moves**: Projectile and pulse moves bypass the ability
- **Status moves**: Many status moves don't make contact
- **One-time limitation**: Once triggered, won't activate again

### Weather and Field Interactions
- **Weather independence**: Not affected by weather conditions
- **Terrain effects**: May interact with terrain but doesn't depend on it
- **Field effects**: Can stack with other field hazards
- **Priority moves**: Contact priority moves can still trigger it

### Related Abilities
- **Iron Barbs**: Also punishes contact but with damage instead of hazards
- **Rough Skin**: Similar contact punishment mechanic
- **Aftermath**: Punishes contact moves that cause fainting
- **Static/Flame Body**: Status-based contact punishment

### Ability Interactions
- **Mold Breaker**: Ignores Loose Rocks and prevents activation
- **Magic Bounce**: Can reflect moves but doesn't affect this ability
- **Neutralizing Gas**: Suppresses the ability while active
- **Trace**: Can copy this ability but effectiveness varies

### Version History
- **Elite Redux original**: This is a custom Elite Redux ability
- **Hazard meta**: Designed for hazard-heavy competitive play
- **Contact punishment**: Part of the suite of contact-punishing abilities
- **Defensive utility**: Provides passive team support for defensive builds