---
id: 418
name: Riptide
status: reviewed
character_count: 74
---

# Riptide - Ability ID 418

## In-Game Description
"Boosts Water-type moves by 1.3x, or 1.8x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Water-type moves by 30%, or by 80% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Riptide is a powerful offensive ability that provides conditional damage boosts to Water-type moves based on the user's current HP percentage. It uses the BOOSTED_SWARM_MULTIPLIER system with Water-type moves.

### Activation Conditions
- **Move type requirement**: Only affects Water-type moves
- **HP-based scaling**: Two different boost levels
  - Above 1/3 HP: 1.3x damage multiplier (30% increase)
  - At or below 1/3 HP: 1.8x damage multiplier (80% increase)
- **User independence**: Works regardless of the user's typing

### Technical Implementation
```c
// Riptide uses the BOOSTED_SWARM_MULTIPLIER macro
constexpr Ability Riptide = {
    .onOffensiveMultiplier = BOOSTED_SWARM_MULTIPLIER(TYPE_WATER),
};

// The macro definition:
#define BOOSTED_SWARM_MULTIPLIER(type)
    +[](ON_OFFENSIVE_MULTIPLIER) {
        if (moveType == type) {
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3))
                MUL(1.8);  // 80% boost when low HP
            else
                MUL(1.3);  // 30% boost when healthy
        }
    }
```

### HP Threshold Mechanics
- **Threshold calculation**: 1/3 of maximum HP (integer division)
- **Inclusive threshold**: Triggers at exactly 1/3 HP or below
- **Dynamic scaling**: Boost level changes as HP fluctuates during battle
- **No minimum damage**: Can work even at 1 HP for maximum effect

### Move Compatibility
- **All Water moves**: Affects every Water-type attack
- **Physical and Special**: Both categories receive the boost
- **Multi-hit moves**: Each hit gets the multiplier
- **Type-changing moves**: Only boosts if they become Water-type
- **Weather Ball**: Boosts when Weather Ball becomes Water-type in rain

### Ability Synergies
- **Similar abilities**: Shared pattern with Hellblaze (Fire), Forest Rage (Grass), Purgatory (Ghost), Gladiator (Fighting), and Rockhard Shaft (Rock)
- **Rain teams**: Excellent synergy with rain setters and Swift Swim users
- **Water STAB**: Stacks multiplicatively with Same Type Attack Bonus (1.5x)
- **Life Orb**: Can stack with item boosts for massive damage
- **Aquatic ability**: Pairs well with Pokemon that gain Water typing

### Strategic Applications
- **Early game power**: 30% boost provides consistent damage throughout battle
- **Comeback potential**: 80% boost creates powerful late-game sweeping opportunities
- **HP management**: Strategic use of berries or healing can control boost timing
- **Priority moves**: Aqua Jet becomes extremely powerful at low HP
- **Z-moves/Max moves**: Massive damage potential with the 1.8x multiplier

### Calculation Examples
- **Base 80 Water move at full HP**: 80 x 1.3 = 104 effective power
- **Base 80 Water move at low HP**: 80 x 1.8 = 144 effective power
- **With STAB and low HP**: 80 x 1.5 x 1.8 = 216 effective power
- **Surf with STAB at low HP**: 90 x 1.5 x 1.8 = 243 effective power

### Competitive Viability
- **Offensive presence**: Provides significant damage output throughout the match
- **Risk-reward gameplay**: Encourages aggressive play while rewarding low HP situations
- **Team building flexibility**: Works on any Pokemon with Water move coverage
- **Meta impact**: Can turn normally defensive Pokemon into offensive threats
- **Versatile activation**: Multiple ways to reach low HP threshold safely

### Common Users
- Water-type Pokemon with strong offensive stats
- Mixed attackers with Water move coverage
- Pokemon with recovery moves for HP manipulation
- Bulky Pokemon that can survive at low HP
- Priority move users (Aqua Jet abusers)

### Counters and Limitations
- **Non-Water moves**: Only affects one move type
- **HP management**: Opponent can KO before low HP boost activates
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Type immunities**: Water Absorb and Storm Drain can negate boosted attacks
- **Weather dependence**: Not weather-reliant but benefits from rain support

### Comparison to Similar Abilities
- **Torrent**: Riptide provides consistent 30% boost vs Torrent's 50% only at low HP
- **Overgrow/Blaze/Swarm**: Same low HP threshold but Riptide has higher base boost
- **Adaptability**: Riptide can work on non-Water types, Adaptability only on same-type
- **Sheer Force**: Riptide stacks with items, Sheer Force removes item effects

### Version History
- **Elite Redux exclusive**: Custom ability not found in official Pokemon games
- **Part of BOOSTED_SWARM family**: Shares implementation with five other similar abilities
- **Balanced design**: Provides both consistent power and comeback potential

### Advanced Interactions
- **Focus Sash**: Can guarantee survival to activate 1.8x multiplier
- **Substitute**: HP calculation uses current HP, not HP behind substitute
- **Transform**: Copying Riptide copies the ability's functionality
- **Skill Swap**: Can be transferred to other Pokemon for unexpected coverage
- **Gastro Acid**: Permanently disables the ability for the battle