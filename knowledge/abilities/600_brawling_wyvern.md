---
id: 600
name: Brawling Wyvern
status: reviewed
character_count: 108
---

# Brawling Wyvern - Ability ID 600

## In-Game Description
"Perfect accuracy for all moves. Dragon moves gain 30% power and punch interactions."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees hits for all moves used by and against the user. Dragon-type moves are treated as punching moves.

## Detailed Mechanical Explanation

Brawling Wyvern combines No Guard's perfect accuracy with Dragon-type move enhancement. All moves used by and against this Pokemon will never miss, ignoring accuracy and evasion modifiers. Dragon-type moves gain Iron Fist treatment, boosting power by 30% and enabling interactions with punching-move mechanics like Punching Glove's contact negation.

### Strategic Applications
- **Offensive Enhancement**: Dragon-type moves receive significant power boost
- **Accuracy Guarantee**: High-power, low-accuracy moves become reliable
- **Item Synergy**: Dragon moves work with Punching Glove for contactless attacks
- **Defensive Vulnerability**: Opponent's moves also gain perfect accuracy
- **Type Coverage**: Makes Dragon STAB more threatening

### Technical Implementation
- **No Guard Effect**: `.onAccuracy = NoGuard.onAccuracy`
- **Dragon-Punch Conversion**: `IsIronFistBoosted()` returns TRUE for Dragon-type moves
- **Power Multiplier**: Iron Fist applies 1.3x damage multiplier
- **Item Interactions**: Compatible with Punching Glove effects

### Competitive Viability
High-tier ability that transforms Dragon-type attackers into formidable threats. The accuracy guarantee eliminates risk from powerful but inaccurate moves, while the Dragon-punch conversion provides consistent damage boost. Excellent for mixed attackers utilizing both physical and special Dragon moves.