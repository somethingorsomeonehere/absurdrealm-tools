---
id: 489
name: Enlightened
status: reviewed
character_count: 182
---

# Enlightened - Ability ID 489

## In-Game Description
"Emanate + Inner Focus."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves to Psychic-type and grants STAB for Psychic moves, regardless of the user's type. Focus Blast never misses. Unaffected by flinch, Intimidate, or Scare.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Enlightened is a composite ability that combines two existing abilities: Emanate and Inner Focus, representing a Pokemon that has achieved mental enlightenment and perfect psychic focus.

### Emanate Component
- **Type conversion**: All Normal-type moves become Psychic-type
- **STAB bonus**: Provides STAB for all Psychic-type moves regardless of the user's typing
- **Move types affected**: Any Normal-type move including physical and special attacks
- **Damage boost**: Converted moves receive the ateBoost flag for enhanced power

### Inner Focus Component  
- **Focus Blast accuracy**: Focus Blast always hits (ACCURACY_ALWAYS_HITS)
- **Taunt immunity**: Cannot be affected by Taunt moves (tauntImmune = TRUE)
- **Mental fortitude**: Maintains concentration under mental pressure

### Technical Implementation
```c
constexpr Ability Enlightened = {
    .onMoveType = Emanate.onMoveType,           // Convert Normal to Psychic
    .onStab = Emanate.onStab,                   // Psychic STAB
    .onOffensiveMultiplier = Emanate.onOffensiveMultiplier,
    .onAccuracy = InnerFocus.onAccuracy,        // Focus Blast never misses
    .breakable = TRUE,                          // Can be suppressed
    .tauntImmune = TRUE,                        // Immune to Taunt
};
```

### Strategic Applications
- **Type coverage**: Transform Normal moves into powerful Psychic attacks
- **STAB utilization**: Get Psychic STAB regardless of actual typing
- **Precision strikes**: Focus Blast becomes a reliable 120 BP move
- **Mental immunity**: Cannot be disrupted by Taunt strategies
- **Setup potential**: Reliable Focus Blast enables powerful special sweeping

### Affected Moves
**Normal moves converted to Psychic:**
- Return, Body Slam, Hyper Beam become powerful Psychic attacks
- Quick Attack gains Psychic typing with priority
- Boomburst becomes a devastating special Psychic move

**Focus Blast enhancement:**
- 120 base power with perfect accuracy
- Reliable special Fighting coverage from Psychic-types
- No longer hindered by 70% accuracy

### Limitations
- **Ability suppression**: Can be broken by Mold Breaker family abilities
- **Type immunity**: Dark-types resist/immune to converted Psychic moves
- **Single move enhancement**: Only Focus Blast gets accuracy boost
- **Predictable**: Type conversion is consistent and telegraphed

### Competitive Usage
- **Special attackers**: Excellent on special sweepers needing reliable coverage
- **Mixed attackers**: Physical Normal moves become special Psychic attacks
- **Anti-stall**: Focus Blast never missing breaks through defensive walls
- **Setup sweepers**: Taunt immunity allows safe setup opportunities
- **STAB abusers**: Non-Psychic types gain powerful Psychic STAB

### Version History
- Elite Redux custom ability combining two existing effects
- Part of the expanded ability system for enhanced strategic depth
- Represents the pinnacle of psychic development and mental discipline