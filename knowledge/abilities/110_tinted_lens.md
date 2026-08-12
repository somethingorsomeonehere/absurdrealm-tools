---
id: 110
name: Tinted Lens
status: reviewed
character_count: 130
---

# Tinted Lens - Ability ID 110

## In-Game Description
"Attacks deal double damage if resisted."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles damage when attacking into resistances. If a move would be resisted (0.5x damage or less), the damage is multiplied by 2x.

## Detailed Mechanical Explanation
Tinted Lens is an offensive ability that modifies damage calculation when the user's attacks would be resisted by the target.

### Mechanics:
- **Activation Condition**: Triggers when the type effectiveness multiplier is 0.5x or less
- **Damage Multiplication**: Applies a 2x multiplier to resisted attacks
- **Effect on Type Matchups**:
  - 0.5x resistance to becomes 1x neutral damage
  - 0.25x double resistance to becomes 0.5x single resistance
- **Stacking**: The 2x multiplier is applied after type effectiveness is calculated

### Implementation Details:
From the code analysis, Tinted Lens uses the `RESISTANCE(2)` macro when `typeEffectivenessMultiplier <= UQ_4_12(.5)`. This means:
- It checks if the type effectiveness is 0.5 or less (including double resistances at 0.25)
- It then applies a 2x resistance modifier, which effectively doubles the damage

### Strategic Applications:
- **Coverage Enhancement**: Makes the Pokemon's movepool more versatile by reducing the impact of resistances
- **Switch Punishment**: Opponents can't rely on resistances to safely switch in
- **Offensive Pressure**: Forces opponents to rely on immunities or raw bulk rather than type resistances
- **Synergy**: Works especially well on Pokemon with limited coverage options or those that rely on specific STAB moves

### Notable Users:
Tinted Lens is particularly valuable on special attackers and Pokemon with powerful but commonly resisted STAB types (like Bug or Poison). It allows them to break through traditional checks and counters.

### Comparison to Similar Abilities:
- Unlike abilities that boost super effective damage (like Neuroforce), Tinted Lens specifically helps with poor type matchups
- It's the offensive counterpart to Filter/Solid Rock, which reduce super effective damage taken