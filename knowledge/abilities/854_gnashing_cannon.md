---
id: 854
name: Gnashing Cannon
status: reviewed
character_count: 166
---

# Gnashing Cannon - Ability ID 854

## In-Game Description
Mega Launcher + Mind Crunch.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts pulse, beam, ball, and aura moves by 30%. Biting moves use the Special Attack (still targets enemy's Defense unless stated otherwise) and deal 30% more damage.

## Detailed Mechanical Explanation

### Mechanical Analysis

### Component Abilities

**Mega Launcher Effect:**
- Boosts moves with FLAG_MEGA_LAUNCHER_BOOST by 30% (1.3x multiplier)
- Affected moves include: Water Gun, Hydro Pump, Aura Sphere, Dark Pulse, etc.
- Also boosts all status moves when the user has Gunman ability

**Mind Crunch Effect:**
- Inherits Strong Jaw's offensive multiplier (30% boost to FLAG_STRONG_JAW_BOOST moves)
- Changes offensive stat calculation: biting moves use Special Attack instead of Attack
- Affected moves include: Bite, Crunch, Fire Fang, Ice Fang, Thunder Fang, etc.

### Implementation Details

From `src/abilities.cc`:
```cpp
constexpr Ability GnashingCannon = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            MegaLauncher.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
            MindCrush.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        },
    .onChooseOffensiveStat = MindCrush.onChooseOffensiveStat,
};
```

### Strategic Usage

This ability is particularly powerful on Pokemon that can learn both:
1. Pulse/aura moves (Water Gun, Aura Sphere, Dark Pulse, etc.)
2. Biting moves (Bite, Crunch, elemental fangs)

The stat conversion effect makes physical biting moves scale with Special Attack, creating unique movepool synergies for mixed attackers.