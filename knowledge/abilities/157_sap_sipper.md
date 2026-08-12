---
id: 157
name: Sap Sipper
status: reviewed
character_count: 101
---

# Sap Sipper - Ability ID 157

## In-Game Description
"Redirects Grass moves. Absorbs them, ups highest Atk."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to Grass-type moves, and boost highest attacking stat by 1 stage when the user is hit by them.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sap Sipper is a dual-purpose ability that provides both defensive immunity and offensive enhancement when facing Grass-type moves. When a Pokemon with Sap Sipper is targeted by a Grass-type move:

1. **Move Absorption**: The Grass-type move is completely negated - it deals no damage and has no effect
2. **Stat Boost**: The Pokemon's highest attacking stat (Attack or Special Attack) is raised by one stage (+50% increase)
3. **Move Redirection**: In double battles, single-target Grass moves are redirected to the Sap Sipper Pokemon

### Technical Implementation
```cpp
constexpr Ability SapSipper = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_GRASS);
        *statId = GetHighestAttackingStatId(battler, TRUE);
        return ABSORB_RESULT_STAT;
    },
    .redirectType = TYPE_GRASS,
    .breakable = TRUE,
};
```

### Affected Moves
All Grass-type moves are absorbed by Sap Sipper, including but not limited to:
- **Physical**: Seed Bomb, Wood Hammer, Power Whip, Bullet Seed, U-turn (if Grass-type)
- **Special**: Solar Beam, Energy Ball, Giga Drain, Leaf Storm, Grass Knot
- **Status**: Leech Seed, Spore, Sleep Powder, Stun Spore, Grass Whistle

### Activation Conditions
- Must be hit by a Grass-type move (direct or indirect)
- Works on both damaging and non-damaging Grass moves
- Triggers even if the move would normally have no effect (e.g., Spore on already sleeping Pokemon)
- Does not activate on self-inflicted Grass moves

### Stat Boost Logic
The ability uses `GetHighestAttackingStatId(battler, TRUE)` to determine which stat to boost:
- Compares current Attack vs Special Attack stats (including modifiers)
- Boosts whichever stat is higher
- If stats are equal, typically defaults to Attack
- The boost is +1 stage (50% increase from base)

### Interactions with Other Abilities/Mechanics
- **Mold Breaker**: Can bypass Sap Sipper's immunity and redirection
- **Telepathy**: Does not prevent Sap Sipper from absorbing ally Grass moves in doubles
- **Magic Guard**: Sap Sipper's immunity takes precedence over Magic Guard
- **Substitute**: Sap Sipper works even if the Pokemon is behind a substitute
- **Wonder Guard**: Sap Sipper immunity overrides Wonder Guard's type effectiveness rules

### Strategic Applications
**Defensive Utility**:
- Complete immunity to Grass-type moves makes it excellent against Grass-type threats
- Particularly valuable against status moves like Spore and Sleep Powder
- Can safely switch into predicted Grass moves for momentum

**Offensive Potential**:
- Each Grass move absorbed provides a free Attack or Special Attack boost
- Can turn opponent's Grass moves into setup opportunities
- Especially potent in formats with common Grass-type moves

**Double Battle Tactics**:
- Redirects single-target Grass moves away from teammates
- Can protect frail partners from Grass-type attacks
- Synergizes well with Grass-weak teammates like Water/Ground types

### Example Damage Calculations
Before Sap Sipper activation:
- Azumarill with 50 base Attack: 150 Attack stat at level 50
- After +1 boost: 225 Attack stat (50% increase)

Practical impact:
- Aqua Jet damage: 40 BP x 225 Attack = significantly higher damage output
- Belly Drum becomes even more threatening with the extra boost

### Common Users
Notable Pokemon with Sap Sipper include:
- **Azumarill**: Synergizes with Huge Power for massive physical offense
- **Bouffalant**: Becomes an even more dangerous physical attacker
- **Mamoswine**: Covers its Grass weakness while boosting Attack
- **Sawsbuck**: Provides offensive momentum while maintaining Grass immunity

### Competitive Usage Notes
**Tier Assessment**: Highly valuable in formats with common Grass-type moves
**Usage Rate**: Moderate to high on Pokemon that can effectively use both attacking stats
**Niche Applications**: 
- Grass-type immunity in Grass-heavy metas
- Setup sweeper enabler after absorbing Grass moves
- Support role in doubles for move redirection

### Counters and Limitations
**Counters**:
- Mold Breaker abilities bypass the immunity
- Multi-hit moves can still trigger other abilities on subsequent hits
- Non-Grass type moves are unaffected

**Limitations**:
- Only works against Grass-type moves
- Stat boost may not always be useful if the Pokemon uses the non-boosted attacking stat
- Redirection only works on single-target moves in doubles

### Synergies
**Excellent Synergy**:
- **Huge Power/Pure Power**: Doubles the Attack boost from Sap Sipper
- **Choice items**: Turns Grass immunity into setup opportunities
- **Life Orb**: Increased damage output without recoil on absorbed moves

**Team Synergy**:
- Partners weak to Grass moves (Water/Ground/Rock types)
- Teams lacking reliable Grass-type answers
- Hyper offensive teams that benefit from stat boosts

### Version History
- Originally introduced in Generation V
- Elite Redux implementation maintains core functionality
- Enhanced with the extended ability system for detailed in-game descriptions
- Redirects both damaging and non-damaging Grass moves in doubles