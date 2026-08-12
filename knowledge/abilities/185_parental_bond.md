---
id: 185
name: Parental Bond
status: reviewed
character_count: 196
---

# Parental Bond - Ability ID 185

## In-Game Description
"Moves hit twice. 1st hit at 100% power, 2nd hit at 25%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Makes all attacks hit twice in succession. The first hit deals 100%, while the second hit deals 25%. Each hit rolls secondary effects independently (except flinch). Bypasses Fort Knox/Wonder Skin.

## Detailed Mechanical Explanation

**Basic Information:**
- **Name**: Parental Bond
- **ID**: 185
- **Generation**: VI (X/Y)
- **Type**: Offensive Multi-hit

### Core Functionality
Parental Bond causes most moves to hit twice with the following power distribution:
- **First hit**: 100% power (full damage)
- **Second hit**: 25% power (quarter damage)

### Implementation Details
- Uses `PARENTAL_BOND_HYPER_AGGRESSIVE` type
- Power multiplier for second hit: `UQ_4_12(0.25)` (25%)
- Resistant to Fort Knox (ability cannot be suppressed by certain effects)

### Move Interactions
- **Works with**: Single-target damaging moves, most special moves
- **Doesn't work with**: Multi-hit moves (Bullet Seed, Rock Blast, etc.), status moves, moves that already hit multiple times
- **Each hit**: Calculated separately for damage, type effectiveness, and critical hits

### Strategic Advantages
1. **Focus Sash Breaking**: Second hit breaks Focus Sash after first hit survival
2. **Substitute Breaking**: Guaranteed to break Substitute unless it has very high HP
3. **Ability Triggers**: Each hit can trigger contact-based abilities (Static, Flame Body, etc.)
4. **Status Chances**: Each hit rolls for additional effects independently

### Battle Calculations
- Total damage about 125% of original move power (100% + 25%)
- Each hit calculated with full stats, type effectiveness, and modifiers
- Critical hits determined separately for each strike

## Competitive Usage

### Pokemon with Parental Bond
Primary users include:
- **Kangaskhan** (original user, main changeable ability)
- **Nidoqueen** (as innate ability)  
- **Zarude-Dada** (as changeable ability)
- **Various Elite Redux custom Pokemon** (as innate ability)

### Synergies
- **Life Orb**: Damage boost applies to both hits, recoil only once
- **Choice Items**: Power boost applies to both hits
- **STAB**: Type matching bonus applies to both hits
- **Abilities**: Works with Tough Claws, Iron Fist, and other damage-boosting abilities

### Counters
- **Rocky Helmet**: Damages user twice on contact moves
- **Iron Barbs/Rough Skin**: Contact damage applies to both hits  
- **Contact-based status**: Higher chance of paralysis, burn, etc.

## Unique Features
- One of the most powerful offensive abilities in the game
- Creates unique damage calculations not possible with other abilities  
- Makes normally weak moves viable through guaranteed double hits
- Excellent for revenge killing and priority move effectiveness

## Version History
- **Generation VI**: Introduced on Mega Kangaskhan
- **Generation VII**: Nerfed to 50% second hit power in official games
- **Elite Redux**: Maintains 25% second hit power, expanded to more Pokemon

## Related Abilities
- **Multi-Scale**: Defensive counterpart (reduces damage at full HP)
- **Skill Link**: Guarantees maximum hits for multi-hit moves
- **Strong Jaw/Tough Claws**: Damage boosting abilities that stack with Parental Bond