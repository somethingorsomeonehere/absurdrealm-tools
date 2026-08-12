---
id: 780
name: Gunman
status: reviewed
character_count: 177
---

# Gunman - Ability ID 780

## In-Game Description
"Mega Launcher + Status moves are Mega Launcher moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of pulse, aura, and projectile moves by 30%. Additionally, all status moves are treated as Mega Launcher moves, receiving boosts from abilities related to them.

## Detailed Mechanical Explanation
*For Discord/reference use*

Gunman is an enhanced version of Mega Launcher that provides the following effects:

### Core Mechanics
1. **Mega Launcher Boost**: All moves with the FLAG_MEGA_LAUNCHER_BOOST flag receive a 1.3x (30%) power multiplier
2. **Status Move Enhancement**: All status moves are treated as if they have the FLAG_MEGA_LAUNCHER_BOOST flag

### Implementation Details
- Uses the exact same `onOffensiveMultiplier` function as Mega Launcher
- Sets `megaLauncherBoost = TRUE` to enable the boost flag
- The key difference is in the `IsMegaLauncherBoosted` function, which returns TRUE for status moves when the user has Gunman

### Boosted Move Categories
**Traditional Mega Launcher moves include:**
- Water Gun (40 BP to 52 BP)
- Hydro Pump (110 BP to 143 BP)
- Aura Sphere (85 BP to 111 BP)
- Steel Beam (140 BP to 182 BP)
- Scale Shot (25 BP per hit to 33 BP per hit)
- Spike Cannon (25 BP per hit to 33 BP per hit)
- Rock Blast (25 BP per hit to 33 BP per hit)
- Anchor Shot (80 BP to 104 BP)
- Rock Wrecker (120 BP to 156 BP)
- Wyrm Wind (25 BP per hit to 33 BP per hit)

**Unique to Gunman:**
- ALL status moves receive the 30% boost (converted to damaging when applicable)
- Status moves trigger other projectile-based ability effects

### Synergies
Gunman works with other abilities that check for Mega Launcher boosted moves:
- **Artillery**: Makes Mega Launcher moves hit both opponents
- **Super Scope**: Same targeting effect as Artillery
- **Deadeye**: Mega Launcher moves gain perfect accuracy
- **Dual Wield**: Mega Launcher moves hit twice with reduced power
- **Pyro Shells**: Follows up Mega Launcher moves with Outburst

### Technical Implementation
```cpp
constexpr Ability Gunman = {
    .onOffensiveMultiplier = MegaLauncher.onOffensiveMultiplier,
    .megaLauncherBoost = TRUE,
};
```

The boost check in `IsMegaLauncherBoosted`:
```cpp
int IsMegaLauncherBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_MEGA_LAUNCHER_BOOST) return TRUE;
    if (IS_MOVE_STATUS(move) || BattlerHasAbility(battler, ABILITY_GUNMAN, FALSE)) return TRUE;
    return FALSE;
}
```

### Strategic Applications
- Extremely powerful ability that turns status moves into offensive tools
- Enhances both traditional projectile moves and status moves
- Creates unique strategic opportunities by making status moves interact with projectile-based effects
- Particularly valuable on Pokemon with diverse movepools containing both status and traditional pulse/aura moves