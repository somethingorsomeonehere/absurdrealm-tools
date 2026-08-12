---
id: 99
name: No Guard
status: reviewed
character_count: 59
---

# No Guard - Ability ID 99

## In-Game Description
Attacks used by and on this Pokemon bypass accuracy checks.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees hits for all moves used by and against the user. 

## Detailed Mechanical Explanation

### Basic Information
- **Ability ID**: ABILITY_NO_GUARD
- **Description**: "Attacks used by and on this Pokemon bypass accuracy checks."
- **AI Rating**: 8/10 (High value)
- **Breakable**: No

### Mechanics

### Core Effect
No Guard completely removes accuracy checks from battle calculations when either the attacker or defender has this ability. This means:
- All moves used BY a Pokemon with No Guard will always hit
- All moves used AGAINST a Pokemon with No Guard will also always hit
- This is a double-edged sword ability

### Technical Implementation
From `abilities.cc`:
```cpp
constexpr Ability NoGuard = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority { return ACCURACY_ALWAYS_HITS; },
    .onAccuracyFor = APPLY_ON_ATTACKER_OR_TARGET,
};
```

The `APPLY_ON_ATTACKER_OR_TARGET` flag means the ability triggers whether the Pokemon is attacking or being attacked.

### Battle Interactions

1. **Semi-Invulnerable States**: No Guard allows moves to hit Pokemon that are semi-invulnerable (e.g., during Fly, Dig, Dive)
2. **OHKO Moves**: One-hit KO moves like Sheer Cold, Fissure, and Horn Drill will always connect with No Guard
3. **Low Accuracy Moves**: Powerful but inaccurate moves like Focus Blast (70% accuracy) become guaranteed hits
4. **Evasion/Accuracy Modifiers**: All evasion boosts, accuracy drops, and weather effects (like Sand Attack, Double Team, or Sandstorm) are ignored

### AI Considerations
The AI values No Guard highly (8/10 rating) and specifically checks for it when determining move accuracy. The function `IsMoveEncouragedToHit()` explicitly checks for No Guard to determine if a move will bypass normal accuracy limitations.

## Strategic Analysis

### Advantages
- Makes low-accuracy, high-power moves completely reliable (Focus Blast, Stone Edge, Fire Blast)
- Ignores all evasion strategies from opponents
- Can hit through protect moves that make Pokemon semi-invulnerable
- Pairs excellently with OHKO moves for guaranteed KOs

### Disadvantages
- Opponents' moves also never miss, including OHKO moves
- Status moves like Hypnosis, Sleep Powder, and Will-O-Wisp become guaranteed
- Cannot benefit from evasion boosts or weather-based evasion
- Makes the Pokemon extremely vulnerable to being hit

### Common Pokemon
While specific Pokemon weren't identified in the search, No Guard is traditionally associated with Fighting-type Pokemon like Machamp's evolutionary line, where the guaranteed accuracy on Dynamic Punch (100 power, 50% accuracy, guaranteed confusion) makes it a signature strategy.

## Competitive Usage

### Recommended Movesets
- **Physical Attackers**: Dynamic Punch, Stone Edge, Iron Tail, Megahorn
- **Special Attackers**: Focus Blast, Fire Blast, Thunder, Blizzard
- **OHKO Strategy**: Fissure, Sheer Cold, Horn Drill, Guillotine

### Team Synergy
- Pairs well with Substitute users who can scout dangerous moves
- Benefits from speed control (Trick Room, Tailwind) to strike first
- Appreciates defensive pivots that can switch in on status moves

### Counters
- Priority moves (No Guard doesn't affect move priority)
- Pokemon with Sturdy (blocks OHKO moves)
- Ghost types (immune to Dynamic Punch)
- Status conditions that prevent attacking (paralysis, sleep)


## Summary
No Guard is a powerful but risky ability that exemplifies high-risk, high-reward gameplay. It transforms unreliable moves into consistent options while opening up significant defensive vulnerabilities. The ability is best suited for offensive Pokemon that can leverage the guaranteed accuracy on powerful moves while managing the increased risk through careful team support and positioning.