---
id: 701
name: Steel Beetle
status: reviewed
character_count: 261
---

# Steel Beetle - Ability ID 701

## In-Game Description
"Raging Boxer + Pollinate."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Causes punching moves to hit twice, with the first hit at 100% power and second hit at 40% power. Both attacks independently roll secondary effect chances (except flinch). Normal-type moves become Bug-type and they receive STAB regardless of the Pokemon's type.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Steel Beetle is a combination ability that merges two distinct offensive abilities: Raging Boxer (ID 319) and Pollinate (ID 381). This creates a unique hybrid that affects both punching moves and Normal-type moves simultaneously.

### Component Ability 1: Raging Boxer Effect
- **Trigger Condition**: Move must have the `FLAG_IRON_FIST_BOOST` flag (punching moves)
- **Effect Type**: Parental Bond variant (`PARENTAL_BOND_PRIMAL_MAW`)
- **Hit Count**: Converts single-hit punching moves into two-hit moves
- **Damage Distribution**:
  - First hit: 100% power
  - Second hit: 40% power (UQ_4_12(0.4))
- **Total Damage**: 1.4x effective multiplier for punching moves

### Component Ability 2: Pollinate Effect
- **Type Conversion**: All Normal-type moves are converted to Bug-type
- **Power Boost**: Converted moves receive a 1.2x damage multiplier
- **STAB Application**: Bug-type moves (including converted ones) always receive STAB regardless of the Pokemon's actual typing
- **ATE Mechanism**: Uses the `ATE_ABILITY(TYPE_BUG)` macro

### Technical Implementation
```cpp
constexpr Ability SteelBeetle = {
    .onParentalBond = RagingBoxer.onParentalBond,
    .onOffensiveMultiplier = Pollinate.onOffensiveMultiplier,
    .onMoveType = Pollinate.onMoveType,
};
```

### Affected Moves
**Punching Moves (Raging Boxer component)**:
- Bullet Punch, Fire Punch, Ice Punch, Thunder Punch
- Drain Punch, Focus Punch, Mach Punch
- Shadow Punch, Sucker Punch
- Any move with `FLAG_IRON_FIST_BOOST`

**Normal-type Moves (Pollinate component)**:
- Hyper Beam to Bug-type with 1.2x boost
- Body Slam to Bug-type with 1.2x boost  
- Return/Frustration to Bug-type with 1.2x boost
- Quick Attack to Priority Bug-type move
- Facade to Powerful Bug move when statused

### Interaction Between Components
**Non-overlapping Effects**: The two abilities target different move types:
- Raging Boxer only affects punching moves
- Pollinate only affects Normal-type moves
- No punching moves are Normal-type, so no conflicts occur

**Stacking Potential**: A Pokemon could theoretically benefit from both effects in the same battle using different moves, but not on the same move.

## Battle Implications

### Offensive Power
- **Punching Moves**: 1.4x total damage (100% + 40% hits)
- **Normal to Bug Moves**: 1.2x power boost plus guaranteed STAB
- **Type Coverage**: Access to both physical punching combos and special Bug-type attacks
- **Priority Options**: Bug-type Quick Attack and priority punching moves

### Strategic Considerations
**Versatile Offense**: 
- Physical attackers benefit from doubled punching moves
- Mixed attackers can use converted Normal moves as Bug-type special attacks
- Priority move access in both categories

**Contact Interactions**:
- Punching moves typically make contact, triggering abilities twice
- Normal moves vary in contact properties, converted to Bug-type

**Substitute Breaking**:
- Raging Boxer component can break substitutes with first hit, damage with second
- Single-hit Bug moves work normally against substitutes

## Pokemon With Steel Beetle

### Typical Users
Steel Beetle is likely found on Pokemon that can make use of both components:
- **Fighting-types** with diverse movesets including Normal moves
- **Bug-types** that also learn punching moves
- **Mixed attackers** with both physical and special capabilities
- **Pokemon with broad movepools** spanning multiple move categories

### As Innate Ability
- Would be particularly powerful as an innate ability due to its dual nature
- Complements Pokemon with naturally diverse offensive movepools
- Best on Pokemon with both strong Attack and Special Attack stats

## Synergies and Combinations

### Powerful Ability Combinations
**With Iron Fist**:
- Punching moves get 1.3x boost on both hits from Raging Boxer
- Total multiplier becomes ~1.82x for punching moves
- Creates extremely powerful physical combinations

**With Swarm**:
- Bug-type moves get additional boost when HP is low
- Converted Normal moves benefit from both Swarm and Pollinate
- Creates powerful late-game sweeping potential

**With Technician**:
- Boosts lower-power punching moves on both hits
- Also boosts converted Normal moves under 60 BP
- Maximizes damage from utility moves

### Item Synergies
- **Life Orb**: Boosts both punching combos and Bug conversions
- **Choice Band/Specs**: Excellent for specialized physical or special sets
- **Expert Belt**: Boosts super-effective hits from either component
- **Silver Powder**: Further boosts Bug-type moves from Pollinate

## Competitive Analysis

### Strengths
- **Dual Offensive Boost**: Two completely different boosting mechanisms
- **Move Variety**: Affects both physical punching and type-converted moves
- **Priority Access**: Both Bug-type Quick Attack and priority punches
- **No Internal Conflicts**: Components don't interfere with each other
- **Coverage Options**: Punching moves + Bug typing provides decent coverage

### Weaknesses
- **Ability Slot Intensive**: Takes up ability slot for two moderate effects
- **Situational Use**: Requires specific moveset to maximize both components
- **Type Resistance**: Bug-type has many resistances (Fire, Flying, Steel, etc.)
- **Contact Vulnerability**: Punching moves trigger contact effects twice
- **Move Pool Dependent**: Effectiveness varies greatly by available moves

### Ideal Pokemon Profiles
- **Mixed Attackers**: High Attack and Special Attack to use both components
- **Diverse Movepools**: Access to both punching moves and useful Normal moves
- **Speed Control**: Fast enough to make use of priority options
- **Bulk Considerations**: Able to survive retaliation from contact-based counters

## Counters

### Direct Counters
- **Fire/Flying/Steel types**: Resist Bug moves, may resist punching moves
- **Ghost-types**: Immune to Normal and Fighting-type punches
- **Pokemon with Rough Skin/Iron Barbs**: Punish the doubled contact from punching moves
- **Defensive Pokemon**: Can tank the boosted hits and retaliate

### Strategic Limitations
- **Weather Independence**: No weather synergy like some other combo abilities
- **Predictable**: Opponents can prepare for both Bug conversions and double punches
- **Resource Management**: May struggle with PP due to double hits on punching moves

## Version History
- **Elite Redux Creation**: Steel Beetle is a custom combination ability
- **Implementation**: Uses existing component abilities as templates
- **Balance**: Medium-tier combination that provides versatility over raw power

## Conclusion

Steel Beetle represents an interesting combination ability that merges offensive physical and type-conversion mechanics. While not as immediately powerful as some single-focus abilities, it provides remarkable versatility for Pokemon with appropriate movepools. The ability rewards diverse movesets and mixed offensive stats, making it particularly valuable on Pokemon that can effectively utilize both punching moves and Normal-type attacks. Its dual nature makes it unpredictable and allows for varied battle strategies, though it requires careful team building and move selection to maximize its potential.