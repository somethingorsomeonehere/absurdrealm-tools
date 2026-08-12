---
id: 134
name: Heavy Metal
status: reviewed
character_count: 205
---

# Heavy Metal - Ability ID 134

## In-Game Description
"Doubles this Pokemon's weight."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles the Pokemon's weight. Makes weight-based attacks such as Low Kick deal more damage against this Pokemon. However, it also increases damage from the user's Heavy Slam and similar weight-based moves.

## Detailed Mechanical Explanation
Heavy Metal is an ability that doubles the Pokemon's weight during battle calculations. This has several important implications:

### Weight Modification
- The ability multiplies the Pokemon's base weight by exactly 2x
- This applies after the Pokemon's species weight is determined but before any other weight modifiers
- The effect stacks with other weight modifiers like Lead Coat (3x) or Float Stone item (0.5x)

### Defensive Implications
Weight-based moves that target this Pokemon will calculate damage based on the doubled weight:
- **Low Kick** and **Grass Knot**: These moves deal more damage to heavier targets, so Heavy Metal makes the user take increased damage
- The damage tiers for these moves are based on weight thresholds, so doubling weight can push a Pokemon into higher damage brackets

### Offensive Implications
Weight-based moves used BY this Pokemon benefit from the increased weight:
- **Heavy Slam** and **Heat Crash**: These moves deal more damage when the user is heavier than the target
- The damage calculation for Heat Crash uses the ratio of attacker weight to defender weight
- Heavy Metal effectively doubles this ratio when the user attacks

### Other Interactions
- **Autotomize**: This move reduces the user's weight. Heavy Metal's doubling effect applies to the base weight before Autotomize's reduction
- The ability's effect is always active and cannot be suppressed by Gastro Acid or similar moves
- In Elite Redux's multi-ability system, Heavy Metal can be one of the innate abilities, providing its effect alongside other abilities

### Strategic Considerations
Heavy Metal is a double-edged sword ability. While it makes the Pokemon more vulnerable to weight-based attacks, it also significantly boosts the power of the user's own weight-based moves. This makes it particularly valuable on Pokemon that can learn Heavy Slam or Heat Crash and have naturally high weight to begin with.