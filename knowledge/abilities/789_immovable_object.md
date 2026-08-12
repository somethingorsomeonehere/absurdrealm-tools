---
id: 789
name: Immovable Object
status: reviewed
character_count: 211
---

# Immovable Object - Ability ID 789

## In-Game Description
"Impenetrable + Sturdy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants immunity to all non-attack damage sources including entry hazards, weather damage, status conditions, and recoil. When at full HP, this Pokemon will survive any single attack with at least 1 HP remaining. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Immovable Object is a powerful defensive ability that combines two distinct protective mechanisms:

### Magic Guard Component (from Impenetrable)
- Prevents all indirect damage sources:
  - Status conditions (poison, burn, toxic)
  - Weather effects (sandstorm, hail, etc.)
  - Entry hazards (Stealth Rock, Spikes, Toxic Spikes)
  - Leech Seed damage
  - Terrain damage (Toxic Terrain)
  - Recoil damage from moves
  - Life Orb damage
  - Rocky Helmet/Iron Barbs contact damage
  - Curse damage (Ghost-type)

### Sturdy Component
- **Breakable Property**: Can be suppressed by Mold Breaker and similar effects
- **One-Hit KO Protection**: When at full HP, survives any attack that would otherwise cause a knockout, leaving the Pokemon with 1 HP instead
- **OHKO Move Immunity**: Completely immune to one-hit knockout moves like Fissure, Horn Drill, Guillotine, and Sheer Cold

### Implementation Details
- **Ability Structure**: `{.magicGuard = TRUE}` - inherits the same Magic Guard protection as Impenetrable
- **Sturdy Mechanics**: Shares the same `breakable = TRUE` property as regular Sturdy
- **Battle Script Integration**: Uses `BattleScript_SturdiedMsg` when surviving a would-be knockout
- **Suppression**: Can be bypassed by Mold Breaker abilities, Neutralizing Gas, and Gastro Acid

### Strategic Value
This ability makes a Pokemon extremely difficult to eliminate through conventional means, requiring either:
1. Multiple direct attacks to wear down HP
2. Abilities that can suppress or ignore the protection
3. Status moves that reduce stats rather than cause damage
4. Moves that bypass typical damage calculations

The combination makes it one of the most defensively robust abilities in the game, effectively requiring opponents to plan multi-turn strategies to eliminate the user.