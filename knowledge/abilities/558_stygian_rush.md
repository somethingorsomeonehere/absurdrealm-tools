---
id: 558
name: Stygian Rush
status: reviewed
character_count: 54
---

# Stygian Rush - Ability ID 558

## In-Game Description
"Dark-type moves get +1 priority at max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants +1 priority to Dark-type moves when at full HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Priority Boost**: +1 priority to Dark-type moves when at max HP
- **HP Requirement**: Must be at exactly 100% HP (gBattleMons[battlerId].hp == gBattleMons[battlerId].maxHP)
- **Type Check**: Uses `GetTypeBeforeUsingMove()` to determine if move is Dark-type before STAB/ability modifications

### Technical Implementation
```cpp
constexpr Ability DarkGaleWings = {
    .onPriority = GALE_WINGS_CLONE(TYPE_DARK),
};

#define GALE_WINGS_CLONE(type)                               \
    +[](ON_PRIORITY) -> int {                                \
        CHECK(GetTypeBeforeUsingMove(move, battler) == type) \
        CHECK(BATTLER_MAX_HP(battler))                       \
        return 1;                                            \
    }
```

### Activation Conditions
1. **Type Requirement**: Move must be Dark-type before any type changes
2. **HP Requirement**: Pokemon must be at exactly maximum HP
3. **Priority Calculation**: Adds +1 to the move's base priority

### Complete List of Affected Moves
All Dark-type moves benefit from this ability, including:
- **Physical Dark Moves**: Bite, Crunch, Knock Off, Sucker Punch, Throat Chop, etc.
- **Special Dark Moves**: Dark Pulse, Shadow Ball, Snarl, Nasty Plot (status), etc.
- **Status Dark Moves**: Taunt, Torment, Embargo, Hone Claws (if Dark-type), etc.

### Interactions with Other Mechanics
- **STAB**: Works independently of STAB bonuses
- **Type-changing Abilities**: Move type is checked before abilities like Pixilate modify it
- **Item Effects**: Unaffected by items that change move types
- **Multi-hit Moves**: Each hit retains the priority boost if HP condition is met
- **Other Priority Abilities**: Stacks with Quick Claw but conflicts with abilities like Stall

### Strategic Implications
#### Advantages
- **Fast Revenge Killing**: Sucker Punch becomes +2 priority at max HP
- **Early Game Control**: Dark Pulse, Snarl get priority on switch-in
- **Status Move Priority**: Taunt and other Dark status moves move first
- **Sweep Prevention**: Can interrupt setup with priority Dark moves

#### Limitations
- **One-time Use**: Lost after taking any damage
- **HP Dependency**: Stealth Rock, Spikes, or any chip damage disables it
- **Type Restriction**: Only benefits Dark-type moves
- **Predictable**: Opponents can play around the known HP requirement

### Example Damage Calculations
**Standard Priority Dark Pulse (Max HP)**:
- Base Priority: 0 to +1 with Stygian Rush
- Moves before most standard moves (priority 0)
- Still slower than Quick Attack (+1) and Extreme Speed (+2)

**Sucker Punch with Stygian Rush**:
- Base Priority: +1 to +2 with Stygian Rush
- Moves before almost all moves except Extreme Speed
- Extremely powerful for revenge killing

### Common Users
- **Dark-type Pokemon**: Natural STAB synergy with the ability
- **Mixed Attackers**: Can utilize both physical and special Dark moves
- **Lead Pokemon**: Benefit from guaranteed max HP on switch-in
- **Glass Cannons**: High-risk, high-reward playstyle fits the ability

### Competitive Usage Notes
#### Optimal Team Roles
- **Lead Pokemon**: Guaranteed activation on battle start
- **Switch-in Threats**: Priority Dark moves on entry
- **Revenge Killers**: Priority Sucker Punch for guaranteed KOs
- **Anti-Setup**: Priority Taunt to prevent setup

#### Common Strategies
- **Entry Hazard Synergy**: Partner with hazard setters to limit opponent's switching
- **Focus Sash Users**: Maintain max HP for longer periods
- **Choice Item Users**: Lock into powerful priority Dark moves

### Counters
#### Direct Counters
- **Entry Hazards**: Stealth Rock immediately disables the ability
- **Multi-hit Moves**: First hit disables ability for subsequent hits
- **Status Moves**: Toxic, Will-O-Wisp reduce HP and disable ability
- **Weather Damage**: Sandstorm/Hail chip damage

#### Strategic Counter-play
- **Fairy-types**: Immune to Dark-type moves entirely
- **Priority Moves**: +2 or higher priority moves still go first
- **Protect Users**: Can scout and waste the priority advantage
- **Bulky Setup**: Tank the priority hit and set up afterward

### Synergies
#### Ability Synergies
- **Life Orb**: Maximize damage but lose HP after attacking
- **Choice Band/Specs**: Lock into powerful priority moves
- **Focus Sash**: Helps maintain max HP longer

#### Move Synergies
- **Sucker Punch**: Becomes +2 priority for supreme revenge killing
- **Knock Off**: Priority utility removal
- **Dark Pulse**: Special priority for coverage
- **Taunt**: Priority status prevention

### Version History
- **Elite Redux**: Custom ability based on Gale Wings mechanics
- **Implementation**: Uses GALE_WINGS_CLONE macro for consistent behavior
- **Type Variant**: Part of a series including Gale Wings (Flying), Tidal Rush (Water), etc.

### Related Abilities
- **Gale Wings** (Flying-type variant)
- **Tidal Rush** (Water-type variant) 
- **Flaming Soul** (Fire-type variant)
- **Volt Rush** (Electric-type variant)
- **Frozen Soul** (Ice-type variant)
- **Early Grave** (Ghost-type variant)
- **Cute Antecedence** (Fairy-type variant)