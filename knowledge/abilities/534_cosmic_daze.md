---
id: 534
name: Cosmic Daze
status: reviewed
character_count: 155
---

# Cosmic Daze - Ability ID 534

## In-Game Description
"2x damage vs confused. Enemies take 2x confusion damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Attacks against confused targets deal double damage. Additionally, confused enemies hurt themselves for double damage when hitting themselves in confusion.

## Detailed Mechanical Explanation

### Core Mechanics
Cosmic Daze is an offensive ability that enhances damage against confused targets in two ways:

1. **Double Damage vs Confused Targets**: When the user attacks a confused opponent, the damage is multiplied by 2x. This applies to all damaging moves, regardless of type or category.

2. **Double Confusion Self-Damage** (Note: Currently commented out in code): When implemented, confused opponents would take double damage when hitting themselves in confusion (80 base power instead of the standard 40).

### Activation Conditions
- **For 2x damage**: Target must have the confusion status condition
- **Damage multiplier**: Applied after all other damage calculations
- **Universal application**: Works on all damaging moves (physical, special, and fixed damage)

### Synergies
- **Confusion-inducing moves**: Confuse Ray, Swagger, Psybeam, Confusion, Hurricane, etc.
- **Abilities that cause confusion**: Intimidate variants, entry hazards with confusion effects
- **Held items**: Moves or items that can inflict confusion status

### Notable Users
- **Multiple Pokemon** have access to this ability, including some with it as an innate ability
- Often paired with other psychic or mind-affecting abilities
- Appears on Pokemon with confusion-inducing movepools

### Competitive Notes
- Creates a powerful win condition when combined with reliable confusion sources
- The 2x damage multiplier is significant and can turn weak attacks into KOs
- Confusion's inherent RNG (33% self-hit chance in Gen 7+) adds risk/reward element
- Currently, only the offensive damage boost is active; the confusion self-damage increase appears to be disabled

### Technical Implementation
- Implemented as an `onOffensiveMultiplier` effect in abilities.cc
- Checks for `STATUS2_CONFUSION` on the target
- Simple 2x multiplier (`MUL(2)`) when condition is met
- The confusion self-damage modification exists in battle_util.c but is commented out