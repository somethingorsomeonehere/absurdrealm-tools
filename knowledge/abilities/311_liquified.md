---
id: 311
name: Liquified
status: reviewed
character_count: 138
---

# Liquified - Ability ID 311

## In-Game Description
"Takes 1/2 dmg from contact moves but Water moves hurt it 2x more."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Liquified reduces contact move damage by 50% but doubles Water-type move damage taken. Multiplicative with other damage reduction sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Contact Move Resistance**: Reduces damage from contact moves by 50% (multiplier of 0.5)
- **Water Move Weakness**: Doubles damage from Water-type moves (multiplier of 2.0)
- **Breakable**: Can be suppressed by Mold Breaker, Neutralizing Gas, and similar abilities

### Activation Conditions
The ability triggers on the defensive multiplier phase of damage calculation:
1. **For Water-type moves**: Applies 2x damage multiplier regardless of contact
2. **For contact moves**: Applies 0.5x damage multiplier regardless of type

### Technical Implementation
```cpp
constexpr Ability Liquified = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_WATER) RESISTANCE(2);
            if (IsMoveMakingContact(move, attacker)) MUL(0.5);
        },
    .breakable = TRUE,
};
```

### Contact Move Detection
The ability uses `IsMoveMakingContact(move, attacker)` which checks:
- Move's natural contact flag
- Abilities that modify contact (Long Reach removes contact)
- Items that modify contact (Protective Pads prevent contact)

### Complete List of Affected Moves
**Contact moves (reduced damage):**
- Most physical moves: Tackle, Body Slam, Earthquake, etc.
- Punch moves: Fire Punch, Ice Punch, Thunder Punch, etc.
- Bite moves: Bite, Crunch, etc.
- Multi-hit contact moves: Fury Attack, Bullet Seed (if contact), etc.

**Water-type moves (increased damage):**
- All Water moves: Surf, Hydro Pump, Water Gun, Scald, etc.
- Physical Water moves: Waterfall, Aqua Tail, Liquidation, etc.
- Special Water moves: Hydro Cannon, Origin Pulse, etc.

### Interactions with Other Abilities/Mechanics
- **Mold Breaker**: Suppresses Liquified entirely
- **Long Reach**: Prevents contact, so no damage reduction
- **Protective Pads**: Holder's contact moves don't trigger damage reduction
- **Type changing abilities**: If a move becomes Water-type (e.g., via Normalize), it triggers the weakness
- **Fluffy comparison**: Similar defensive profile but Fluffy resists Fire instead of being weak to Water

### Strategic Implications
**Advantages:**
- Excellent physical bulk against non-Water contact moves
- Forces opponents to use special attacks or Water moves
- Synergizes with recovery moves and defensive strategies

**Disadvantages:**
- Severe Water weakness limits usage in water-heavy environments
- Breakable nature makes it unreliable against certain opponents
- No protection against non-contact physical moves (Earthquake, Rock Slide)

### Example Damage Calculations
Assuming base 100 damage:
- **Contact move**: 100 to 50 damage (50% reduction)
- **Water move**: 100 to 200 damage (100% increase)
- **Water contact move**: 100 to 200 damage (Water weakness overrides contact resistance)

### Common Users
Based on SpeciesList analysis:
- **Grimer line**: Grimer, Muk - Poison/sludge themed
- **Reuniclus line**: Solosis, Duosion, Reuniclus - Psychic gel Pokemon
- **Swalot line**: Gulpin, Swalot - Stomach bag Pokemon
- **Goomy line**: Goomy - Soft-bodied Dragon
- **Oricorio (Sensu Style)**: Ghost/Flying dancer form
- **Snorlax Redux**: Modified Snorlax variant

### Competitive Usage Notes
- **Defensive pivot**: Excellent against physical attackers lacking Water moves
- **Team support**: Pairs well with Water absorbers or resisters
- **Meta dependency**: Effectiveness varies with Water-type usage in format
- **Hazard synergy**: Works well with Stealth Rock support to pressure switch-ins

### Counters
- **Water-type moves**: Exploit the doubled weakness
- **Special attackers**: Bypass the contact move resistance
- **Mold Breaker users**: Suppress the ability entirely
- **Non-contact physical moves**: Earthquake, Rock Slide, etc.

### Synergies
- **Recovery moves**: Roost, Recover to maintain bulk
- **Water Absorb/Storm Drain teammates**: Handle Water attacks
- **Intimidate support**: Further reduce physical damage
- **Stealth Rock**: Pressure Water-type switch-ins

### Version History
- **Elite Redux**: Custom ability created for the ROM hack
- **ID 311**: Assigned in the custom ability expansion
- **Implementation**: Added via abilities.cc system with breakable flag