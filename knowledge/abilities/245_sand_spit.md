---
id: 245
name: Sand Spit
status: reviewed
character_count: 287
---

# Sand Spit - Ability ID 245

## In-Game Description
"If hit, summons a sandstorm that lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sand Spit activates when taking damage from an attack. Summons an 8-turn sandstorm (12 turns with Smooth Rock) that deals 1/16 max HP damage each turn to non-Ground, Rock, and Steel types. The user gains immunity to sandstorm damage. Does not activate if the user faints from the attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Activation Conditions
- **Trigger**: When the Pokemon with Sand Spit takes damage from any direct attack
- **Fails if**: Sandstorm is already active, or primal weather (Desolate Land, Primordial Sea, Delta Stream) is active
- **Works through**: Substitutes, focus sash activations, and even if the Pokemon faints from the triggering hit

### Weather Effects Created
1. **Sandstorm Weather**: Creates standard 8-turn sandstorm weather
2. **Duration**: 8 turns (can be extended with Smooth Rock)
3. **Damage**: 1/16 max HP per turn to all Pokemon not immune
4. **Type Immunity**: Ground, Rock, and Steel types take no sandstorm damage
5. **Ability Immunity**: Pokemon with Sand Veil, Sand Rush, Sand Force, Magic Guard, Overcoat, and other sand-immune abilities take no damage

### Interactions
- **Primal Weather**: Cannot override Desolate Land, Primordial Sea, or Delta Stream
- **Other Weather**: Will override rain, sun, hail, and fog
- **Multiple Activations**: If sandstorm ends and the Pokemon is hit again, Sand Spit can activate again
- **Utility Umbrella**: Does not block sandstorm effects (only blocks sun/rain)

### Sand Spit User Benefits
- **Sand Immunity**: The user takes no damage from sandstorm weather (sandImmune = TRUE)
- **Synergy**: Works perfectly with other sand-based abilities like Sand Veil (accuracy reduction), Sand Rush (speed boost), Sand Force (attack boost)

### Strategic Uses
1. **Defensive Setup**: Provides automatic weather control when taking hits
2. **Chip Damage**: Forces 1/16 HP damage on opponents each turn
3. **Sand Team Support**: Enables sand-based strategies without needing Sand Stream
4. **Weather Control**: Overwrites opponent's beneficial weather

### AI Behavior
- AI rates Sand Spit positively when evaluating taking damage (AI_SCORE_SANDSTORM)
- AI considers the defensive value of setting up sandstorm when making damage calculations

### Code Implementation
- **File**: `src/abilities.cc`
- **Trigger**: `onDefender` callback when taking damage
- **Checks**: Uses `ShouldApplyOnHitAffect()` to verify activation conditions
- **Weather Setting**: Uses `TryChangeBattleWeather(battler, ENUM_WEATHER_SANDSTORM, TRUE)`
- **Properties**: `sandImmune = TRUE` grants immunity to sandstorm damage