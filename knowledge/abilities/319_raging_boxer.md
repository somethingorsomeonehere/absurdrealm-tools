---
id: 319
name: Raging Boxer
status: reviewed
character_count: 184
---

# Raging Boxer - Ability ID 319

## In-Game Description
"Punching moves hit twice. 1st hit at 100% power, 2nd hit at 40%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raging Boxer causes punching moves to hit twice, with the first hit at 100% power and second hit at 40% power. Both attacks independently roll secondary effect chances (except flinch).

## Detailed Mechanical Explanation

### Basic Information
- **ID**: 319 (ABILITY_RAGING_BOXER)
- **Name**: Raging Boxer

### Mechanics

### Core Functionality
- **Trigger Condition**: Move must have the `FLAG_IRON_FIST_BOOST` flag (punching moves)
- **Effect Type**: Parental Bond variant (`PARENTAL_BOND_PRIMAL_MAW`)
- **Hit Count**: Converts single-hit punching moves into two-hit moves
- **Damage Distribution**:
  - First hit: 100% power
  - Second hit: 40% power (UQ_4_12(0.4))

### Technical Implementation
```cpp
constexpr Ability RagingBoxer = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType {
        CHECK(IsIronFistBoosted(battler, move))
        return PARENTAL_BOND_PRIMAL_MAW;
    },
};
```

### Affected Moves
Any move with `FLAG_IRON_FIST_BOOST` flag, including:
- **Bullet Punch** - Steel-type priority punching move
- **Fire Punch** - Fire-type punching move  
- **Ice Punch** - Ice-type punching move
- **Thunder Punch** - Electric-type punching move
- **Drain Punch** - Fighting-type punching move with HP recovery
- **Focus Punch** - High-power Fighting-type punching move
- **Mach Punch** - Fighting-type priority punching move
- **Shadow Punch** - Ghost-type punching move
- **Sucker Punch** - Dark-type priority punching move
- And other moves flagged for Iron Fist boosting

### Special Interactions
- **Iron Fist Compatibility**: Works alongside Iron Fist ability for combined effects
- **Dragon-type Punches**: Also works with Dragon-type moves if the user has Brawling Wyvern ability (extends Iron Fist to Dragon moves)
- **Priority Moves**: Maintains priority when used with priority punching moves
- **Status Moves**: Does not affect non-damaging moves

## Battle Implications

### Offensive Power
- **Effective Multiplier**: 1.4x total damage (100% + 40%)
- **Crit Calculation**: Each hit rolls for critical hits independently
- **Type Effectiveness**: Each hit applies type effectiveness separately
- **Ability Triggers**: Abilities like Weak Armor trigger twice

### Strategic Considerations
- **Contact Moves**: Most punching moves make contact, triggering contact-based abilities/items twice
- **Substitutes**: Can break substitutes with first hit, then damage the Pokemon with second hit
- **Focus Sash/Sturdy**: First hit can trigger these effects, second hit can potentially KO
- **Multiscale/Shadow Shield**: Second hit occurs at reduced HP, potentially bypassing damage reduction

## Pokemon With Raging Boxer

### As Regular Ability
- **Mega Machamp** - Fighting-type powerhouse
- **Various Fighting-type Pokemon** - Particularly those focused on physical combat

### As Innate Ability
- **Mewtwo variants** - Psychic-type legendary with innate punching prowess
- **Mixed Martial Arts Pokemon** - Combined with other fighting-focused abilities
- **Specialized forms** - Various Pokemon with combat-focused stat distributions

## Synergies and Combinations

### Powerful Ability Combinations
- **+ Iron Fist**: 1.3x damage boost on both hits (total ~1.82x multiplier)
- **+ No Guard**: Ensures both hits always connect
- **+ Sheer Force**: Removes secondary effects but boosts power of both hits
- **+ Technician**: Boosts lower-power punching moves on both hits

### Item Synergies
- **Life Orb**: Boosts both hits with recoil after both
- **Choice Band**: Significantly increases damage of both hits
- **Punching Glove**: Makes punching moves not make contact (removes some drawbacks)
- **Expert Belt**: Boosts super-effective punching moves on both hits

## Competitive Analysis

### Strengths
- **High Damage Output**: 1.4x effective damage multiplier
- **Substitute Breaking**: Can break subs and still deal damage
- **Defensive Ability Breaking**: Bypasses Multiscale-type abilities
- **Priority Punching**: Excellent with moves like Bullet Punch and Mach Punch

### Weaknesses
- **Limited Move Pool**: Only affects punching moves
- **Contact Vulnerability**: Most punching moves trigger contact-based effects twice
- **Reduced Second Hit**: 40% power on second hit may not always be significant
- **Ability Dependence**: Requires specific move types to function

### Ideal Pokemon Profiles
- **High Attack**: Benefits most from the doubled hits
- **Speed Control**: Priority punching moves or speed boosting
- **Move Variety**: Access to multiple types of punching moves
- **Bulk Considerations**: Ability to survive contact-based retaliation

## Conclusion

Raging Boxer is a specialized offensive ability that significantly boosts the power of punching moves through a unique Parental Bond-style effect. While limited to specific moves, it provides substantial damage output for Pokemon with appropriate movesets, particularly Fighting-types and those with diverse punching move access. The 40% second hit creates meaningful additional damage while maintaining the strategic depth of multi-hit moves in competitive play.