---
id: 313
name: Dragonslayer
status: reviewed
character_count: 217
---

# Dragonslayer - Ability ID 313

## In-Game Description
"Deals 1.5x damage to Dragons. Takes 0.5x damage from Dragons."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Deals 1.5x damage to Dragon-type Pokemon and takes 0.5x damage when attacked by Dragon-type Pokemon. Based on attacker/defender Pokemon types, not move types. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation

### Core Mechanics
DRAGONSLAYER modifies damage based on the **types of the Pokemon involved**, not the move types:

1. **Offensive Boost**: When attacking a Dragon-type Pokemon, all moves deal 1.5x damage
   - Checks if the target has Dragon as any of its types (type1, type2, or type3)
   - Applies to ALL moves, not just specific types
   - Works against dual-types and triple-types that include Dragon

2. **Defensive Resistance**: When being attacked BY a Dragon-type Pokemon, takes 0.5x damage
   - Checks if the ATTACKER has Dragon as any of its types
   - Reduces damage from ANY move used by that Dragon-type Pokemon
   - This means even if a Dragon-type uses a Fire-type move, it still deals 0.5x damage

### Implementation Details
- **Location**: `src/abilities.cc:3343`
- **Breakable**: Yes (can be suppressed by Mold Breaker and similar abilities)
- **Hooks Used**:
  - `onOffensiveMultiplier`: Applies 1.5x damage when attacking Dragons
  - `onDefensiveMultiplier`: Applies 0.5x damage when attacked by Dragons

### Key Clarifications
- **NOT based on move type** - it's based on the Pokemon's type
- The defensive reduction applies to ALL moves from Dragon-type Pokemon, regardless of the move's type
- The offensive boost applies to ALL your moves against Dragon-type Pokemon
- Works on partial Dragon-types (e.g., Dragonite being Dragon/Flying)

### Example Scenarios
- Dragonslayer user vs Dragonite: All moves deal 1.5x damage
- Garchomp using Earthquake vs Dragonslayer user: Earthquake deals 0.5x damage (because Garchomp is Dragon-type)
- Charizard using Dragon Pulse vs Dragonslayer user: Dragon Pulse deals 0.5x damage (because Charizard is Fire/Dragon-type in Elite Redux)

### Comparison to Similar Abilities
Unlike type-based damage modifiers that check move types (like Filter or Solid Rock), DRAGONSLAYER specifically checks the Pokemon's types themselves, making it unique in its targeting approach.
