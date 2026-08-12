---
id: 430
name: Volt Rush
status: reviewed
character_count: 87
---

# Volt Rush - Ability ID 430

## In-Game Description
"At full HP, gives +1 priority to its Electric-type moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Volt Rush grants +1 priority to all Electric-type moves when the Pokemon is at full HP. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Volt Rush is a priority-boosting ability that functions identically to Gale Wings but specifically for Electric-type moves. It provides a significant speed advantage by allowing Electric moves to strike first, but only when the user maintains perfect health.

### Activation Conditions
- **HP requirement**: Pokemon must be at exactly full HP (100% of max HP)
- **Move type**: Only affects Electric-type moves
- **Priority boost**: Adds exactly +1 to move priority
- **Immediate loss**: Priority bonus is lost the instant HP drops below maximum

### Technical Implementation
```c
// Volt Rush uses the GALE_WINGS_CLONE macro for Electric type
constexpr Ability VoltRush = {
    .onPriority = GALE_WINGS_CLONE(TYPE_ELECTRIC),
};

// The macro implementation:
#define GALE_WINGS_CLONE(type)                               \
    +[](ON_PRIORITY) -> int {                                \
        CHECK(GetTypeBeforeUsingMove(move, battler) == type) \
        CHECK(BATTLER_MAX_HP(battler))                       \
        return 1;                                            \
    }

// Where BATTLER_MAX_HP is defined as:
#define BATTLER_MAX_HP(battlerId)(gBattleMons[battlerId].hp == gBattleMons[battlerId].maxHP)
```

### Important Interactions
- **Move typing**: Uses move's type after same-type conversion (e.g., Normalize, Aerilate)
- **Priority brackets**: Creates new priority bracket between +0 and +1
- **Multiple priority**: Stacks additively with other priority-boosting effects
- **Substitute**: Taking damage behind Substitute still disables the ability
- **Status conditions**: Burn, poison, and other damage-over-time effects disable priority

### Priority System Integration
- **Normal moves**: 0 priority to Electric moves get +1 priority at full HP
- **Quick Attack**: +1 priority to Electric moves match this speed tier
- **Extreme Speed**: +2 priority to Still faster than Volt Rush Electric moves
- **Within same priority**: Speed stats determine order as normal

### HP Management Considerations
- **Healing moves**: Roost, Recover, etc. can restore priority by reaching full HP
- **Leftovers/berries**: Gradual healing can restore the ability's effectiveness
- **Entry hazards**: Stealth Rock damage immediately disables priority on switch-in
- **Recoil moves**: Self-inflicted damage from moves like Volt Tackle disables ability
- **Life Orb**: Damage from Life Orb disables priority after first use

### Strategic Implications
- **Opening game**: Extremely powerful for first-turn positioning and revenge killing
- **Momentum control**: Allows slower Electric types to act as priority revenge killers
- **Entry hazard vulnerability**: Stealth Rock weakness significantly impacts usability
- **Risk-reward gameplay**: High reward for maintaining full HP, severe penalty for any damage
- **Team support**: Benefits from hazard control and healing support

### Common Users
Electric-type Pokemon that want to leverage priority for:
- **Revenge killing**: Finishing off weakened opponents
- **Speed control**: Outpacing naturally faster threats
- **First-turn advantage**: Getting crucial moves off before taking damage
- **Late-game cleanup**: Sweeping with priority Electric moves

### Competitive Usage Notes
- **Hazard weakness**: Stealth Rock severely limits switch-in opportunities
- **One-time use**: Often only effective once per battle due to HP requirement
- **Type coverage**: Limited to Electric moves reduces coverage options
- **Speed tier relevance**: Most valuable on naturally slower Pokemon
- **Item synergy**: Focus Sash can preserve HP for one crucial turn

### Counters
- **Entry hazards**: Stealth Rock, Spikes immediately disable ability
- **Multi-hit moves**: Guarantee HP loss to disable priority
- **Status conditions**: Burn, poison disable through damage over time
- **Priority moves**: Higher priority moves (+2 or higher) still move first
- **Thunder Wave**: Paralysis speed reduction paired with priority loss
- **Sandstorm/Hail**: Weather damage removes priority bonus

### Synergies
- **Rapid Spin/Defog**: Essential hazard removal for maintaining full HP
- **Healing Wish**: Full restoration can reactivate the ability
- **Aromatherapy/Heal Bell**: Status cure prevents damage over time
- **Electric Terrain**: Boosts Electric move power while maintaining priority
- **Focus Sash**: Preserves full HP through one otherwise fatal hit
- **Sturdy**: Similar HP preservation synergy on some users

### Move Interactions
Electric moves that benefit from Volt Rush priority:
- **Thunderbolt**: Reliable STAB priority option
- **Thunder**: High power with paralysis chance at priority
- **Volt Tackle**: Extreme power but recoil disables ability after use
- **Thunder Wave**: Priority paralysis support
- **Discharge**: AoE priority damage in doubles
- **Electro Ball**: Variable power based on speed differences

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Functions as Electric-type variant of Gale Wings
- Part of the priority-boosting ability family alongside Gale Wings variants
- Designed to provide Electric types with priority option while maintaining HP risk

### Elite Redux Specific Notes
- Part of the 4-ability system - can be either changeable or innate
- Integrates with the expanded priority system
- Benefits from Elite Redux's focus on offensive abilities
- Complements the game's faster-paced battle system