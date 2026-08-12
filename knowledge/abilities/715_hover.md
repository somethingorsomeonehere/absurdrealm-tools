---
id: 715
name: Hover
status: reviewed
character_count: 247
---

# Hover - Ability ID 715

## In-Game Description
"Adds Psychic type to itself. Avoids Ground attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Psychic to the user's current typing. Retains Psychic typing even upon losing the ability, going away only when switching out. The user is immune to Ground-type moves and other ground effects such as Spikes and terrains.

## Detailed Mechanical Explanation
*For Discord/reference use*

**HOVER** is a dual-function ability combining type addition with Ground immunity, creating unique defensive profiles.

### Activation Mechanics:
- **Trigger**: On entry (onEntry hook)
- **Type Addition**: Adds Psychic as third type
- **Message**: Shows type addition notification
- **Levitation**: Immediate Ground immunity

### Technical Implementation:
```cpp
constexpr Ability Hover = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return AddBattlerType(battler, TYPE_PSYCHIC); 
    },
    .breakable = TRUE,
    .levitate = TRUE,
};
```

### Effect Details:

1. **Type Addition**:
   - Uses AddBattlerType() for type3 slot
   - Permanent while Pokemon remains in battle
   - Affects STAB, resistances, and weaknesses

2. **Ground Immunity**:
   - Complete immunity to Ground moves
   - Immune to Spikes damage
   - Immune to Toxic Spikes poison
   - Works like Levitate ability

3. **Breakable Nature**:
   - Mold Breaker ignores both effects
   - Teravolt/Turboblaze also break it
   - When broken, loses both benefits

### Type Interaction Changes:

**New Resistances** (from Psychic):
- Fighting: 0.5x
- Psychic: 0.5x

**New Weaknesses** (from Psychic):
- Bug: 2x
- Ghost: 2x
- Dark: 2x

**Immunities**:
- Ground: 0x (from levitate property)

### Pokemon with Hover:

**As Innate Ability**:
- Ribombee Redux (Bug/Electric + Psychic)
- Ribombee Redux Mega
- Various other Redux forms

### Strategic Implications:

1. **Defensive Benefits**:
   - Free switch on Earthquake
   - Fighting resistance valuable
   - Hazard immunity (Spikes)
   - Can pivot on Ground moves

2. **Offensive Benefits**:
   - Psychic STAB added
   - Expands coverage options
   - Can run Psychic/Psyshock

3. **Defensive Drawbacks**:
   - U-turn becomes super effective
   - Knock Off/Sucker Punch weakness
   - Shadow Ball vulnerability
   - Three types can mean more weaknesses

### Battle Applications:

**Entry Hazard Interaction**:
- Stealth Rock: Still takes damage
- Spikes: Immune (levitation)
- Toxic Spikes: Immune (levitation)
- Sticky Web: Immune (levitation)

**Terrain Interaction**:
- Not grounded, so no terrain benefits
- No Electric Terrain sleep immunity
- No Grassy Terrain healing
- No Psychic Terrain priority block

### Notable Interactions:

1. **vs Mold Breaker**:
   - Earthquake hits for full damage
   - Loses Psychic type benefits
   - Complete ability nullification

2. **Type Coverage**:
   - Must account for 3 types
   - Can create unusual weaknesses
   - Type overlap considerations

3. **AI Behavior**:
   - AI recognizes type addition
   - Considers Ground immunity
   - May target new weaknesses

### Sample Set:

**Ribombee Redux @ Heavy-Duty Boots**
- Type: Bug/Electric/Psychic
- Moves:
  - Bug Buzz (Bug STAB)
  - Thunderbolt (Electric STAB)
  - Psychic (Psychic STAB)
  - U-turn/Sticky Web

### Competitive Analysis:

Hover provides significant utility through dual functionality. The Ground immunity alone is valuable for switching, while Psychic typing adds useful resistances and STAB options. However, the additional weaknesses require careful team support. Best on Pokemon that can utilize Psychic STAB effectively.

### Comparison to Similar:
- **Levitate**: Ground immunity only
- **Protean/Libero**: Changes to move type
- **Galvanize etc**: Adds type to moves

### Version Notes:
- Elite Redux exclusive combination
- Uses type3 slot for addition
- Breakable unlike standard Levitate