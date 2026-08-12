---
id: 281
name: Electrocytes
status: reviewed
character_count: 47
---

# Electrocytes - Ability ID 281

## In-Game Description
"Boosts the power of Electric-type moves by 1.25x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Electrocytes boosts Electric-type moves by 25%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Damage Boost**: Provides exactly 1.25x (25%) damage multiplier to all Electric-type moves
- **Move Type Check**: Uses `moveType == TYPE_ELECTRIC` condition
- **Classification**: Applies to both physical and special Electric-type moves
- **Activation**: Triggers during the offensive multiplier calculation phase

### Technical Implementation
```cpp
constexpr Ability Electrocytes = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_ELECTRIC) MUL(1.25);
        },
};
```

### Activation Conditions
- Any Electric-type move used by the Pokemon with this ability
- No weather, terrain, or battle condition requirements
- Works in single, double, and multi battles
- Functions regardless of target's type or abilities

### Numerical Values
- **Base Multiplier**: 1.25x (25% increase)
- **Calculation**: Final damage = Base damage x 1.25 x other modifiers
- **Stacking**: Multiplicative with other damage boosts (items, weather, etc.)

### Complete List of Affected Moves
All Electric-type moves benefit from this ability, including but not limited to:
- Thunderbolt, Thunder, Discharge
- Volt Tackle, Wild Charge, Bolt Strike
- Thunder Wave (status moves don't gain damage boost)
- Electro Ball, Volt Switch, U-turn (if Electric-type)
- Hidden Power Electric, Tera Blast (when Electric-type)

### Interactions with Other Abilities/Mechanics
- **Stacks with**:
  - Electric Terrain (+50% when grounded)
  - Transistor (+50% Electric-type moves)
  - Electric Burst (+35% Electric-type moves, with recoil)
  - Choice items (+50% Attack/Sp. Attack)
  - Life Orb (+30% damage)
  - Expert Belt (+20% vs super-effective)

- **Comparison with Similar Abilities**:
  - Transistor: 1.5x boost (stronger)
  - Electric Burst: 1.35x boost but adds recoil
  - Electrocytes: 1.25x boost (moderate, no drawbacks)

### Strategic Implications
- **Role**: Consistent Electric-type damage enhancement
- **Best Use**: On Electric-type specialists or mixed attackers
- **Synergy**: Pairs well with high-power Electric moves
- **Positioning**: More conservative than Transistor but reliable

### Example Damage Calculations
**Base Scenario**: Pikachu using Thunderbolt (90 BP) against neutral target
- Without Electrocytes: 90 base power
- With Electrocytes: 90 x 1.25 = 112.5 effective base power

**With Electric Terrain**: 
- Transistor + Terrain: 90 x 1.5 x 1.5 = 202.5 effective BP
- Electrocytes + Terrain: 90 x 1.25 x 1.5 = 168.75 effective BP

### Common Users
Based on the species data, notable Pokemon with Electrocytes include:
- **Pichu**: As a regular ability option
- **Partner Pikachu forms**: As an innate ability
- **Eevee evolutions**: Various forms have it as a regular ability
- **Various Electric specialists**: Mixed offensive Pokemon

### Competitive Usage Notes
- **Tier Placement**: Solid mid-tier Electric-type ability
- **Usage Rate**: Moderate - reliable but not overpowered
- **Best Formats**: Singles and doubles where consistent damage is valued
- **Team Role**: Fits well on balanced teams needing Electric coverage

### Counters
- **Ground-type immunity**: Electric moves still don't hit Ground-types
- **Lightning Rod/Volt Absorb**: Redirects/absorbs Electric attacks
- **Electric-type resistance**: Grass, Electric, and Dragon types resist
- **Ability suppression**: Gastro Acid, Mold Breaker effects disable it

### Synergies
- **Electric Terrain**: Boosts Electric moves further when grounded
- **Rain teams**: Pairs with Thunder for perfect accuracy
- **Choice items**: Maximize the boosted Electric damage
- **Life Orb**: Additional damage multiplier stacking
- **Magnet/Zap Plate**: Item-based Electric move boosts

### Version History
- **Elite Redux**: Custom ability providing balanced Electric-type enhancement
- **Design Philosophy**: Moderate boost without drawbacks or complex conditions
- **Balance**: Positioned between weaker type boosters and stronger alternatives like Transistor