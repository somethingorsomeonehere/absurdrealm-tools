---
id: 663
name: Funeral Pyre
status: reviewed
character_count: 78
---

# Funeral Pyre - Ability ID 663

## In-Game Description
"Non-Ghost and Dark-types take 1/4 damage every turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All non-Ghost and Dark-types lose 25% of their max HP at the end of each turn. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Mechanics
- **Damage**: 1/4 (25%) of max HP per turn
- **Timing**: Activates at the end of each turn
- **Targets**: All Pokémon on the field except the ability holder
- **Type Immunity**: Ghost-type and Dark-type Pokémon are completely immune
- **Ability Immunity**: Magic Guard protects against this damage
- **Stacking**: Multiple Funeral Pyre abilities on the field don't stack damage
- **Switch-in Message**: Announces when a Pokémon with this ability enters battle

### Technical Implementation
- Uses `onEndTurn` callback to apply damage
- Checks all living battlers on the field
- Filters out Ghost/Dark types and Magic Guard holders
- Applies fraction damage (1/4 max HP) via battle script
- Visual effect shows cursed status animation when damage occurs

### Strategic Implications
- Creates immense pressure on non-Ghost/Dark teams
- Forces switches or quick knockouts
- Synergizes with entry hazards and other passive damage
- Encourages Ghost/Dark team compositions as counters
- Can quickly wear down defensive teams
- Makes stall strategies against the user very difficult

### Common Users
- Gyaradeath Mega X (innate ability)
- Typically found on Ghost-type themed Pokémon
- Often paired with defensive stats to maximize field time

### Competitive Usage Notes
- Excellent for breaking defensive cores
- Pairs well with Protect/Substitute strategies
- Can be combined with trapping moves/abilities
- Forces opponents to carry Ghost/Dark coverage
- Makes switching in frailer Pokémon extremely risky

### Counters and Counterplay
- **Type Immunity**: Use Ghost or Dark-type Pokémon
- **Magic Guard**: Completely negates the damage
- **Quick Offense**: KO the user before taking too much damage
- **Taunt**: Prevent defensive plays that prolong exposure
- **Priority Moves**: Finish off the user quickly
- **Type Changing**: Protean/Color Change to become Ghost/Dark

### Synergies
- **Entry Hazards**: Compounds switching costs
- **Status Moves**: Will-O-Wisp, Toxic add more pressure
- **Defensive Abilities**: Levitate, Wonder Guard for survivability
- **Trapping**: Arena Trap, Shadow Tag prevent escape
- **Weather/Terrain**: Additional passive damage sources
- **Substitute**: Protects the user while damage accumulates

### Notes
- One of the most oppressive field control abilities
- Dramatically warps team building around it
- Effectively a stronger, type-selective Bad Dreams
- The 25% damage is significant enough to 4HKO any Pokémon
- Animation uses the "cursed" status effect for thematic consistency