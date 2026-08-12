---
id: 299
name: Earthbound
status: reviewed
character_count: 75
---

# Earthbound - Ability ID 299

## In-Game Description
"Boosts Ground-type moves by 1.2x, or 1.5x when under 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Ground-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Earthbound is a swarm-type ability that enhances Ground-type moves based on the user's current HP status:

- **Normal State (HP > 1/3)**: Ground-type moves deal 1.2x damage
- **Low HP State (HP <= 1/3)**: Ground-type moves deal 1.5x damage

### Technical Implementation
```cpp
constexpr Ability Earthbound = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_GROUND),
};

#define SWARM_MULTIPLIER(type)                                               \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.5);                                                    \
            else                                                             \
                MUL(1.2);                                                    \
        }                                                                    \
    }
```

### Activation Conditions
- **Move Type**: Only affects Ground-type moves
- **HP Threshold**: The 1.5x boost activates when current HP <= (max HP / 3)
- **Calculation**: HP threshold is calculated in real-time, not based on percentage displays

### Affected Moves (Examples)
Ground-type moves that benefit from Earthbound include:
- **Earthquake** (100 BP) to 120 BP normal / 150 BP low HP
- **Dig** (110 BP) to 132 BP normal / 165 BP low HP  
- **Bone Club** (80 BP) to 96 BP normal / 120 BP low HP
- **Bonemerang** (45 BP) to 54 BP normal / 67.5 BP low HP
- **Magnitude** (variable) to Enhanced based on rolled power
- **Fissure** (OHKO) to Damage boost irrelevant for OHKO moves

### Damage Calculations
For a Pokemon with 300 max HP using Earthquake (100 BP):
- **At 101+ HP**: 100 x 1.2 = 120 effective base power
- **At 100 HP or less**: 100 x 1.5 = 150 effective base power
- **Breakpoint**: Exactly 100 HP (300 / 3 = 100)

### Interactions with Other Mechanics
- **STAB**: Stacks multiplicatively (1.5 x 1.2/1.5 = 1.8/2.25 total)
- **Type Effectiveness**: Applied after Earthbound's multiplier
- **Item Boosts**: Stacks with items like Soft Sand or Earth Plate
- **Weather**: No direct interaction with weather effects
- **Abilities**: Stacks with other offensive abilities like Sheer Force
- **Critical Hits**: Applied independently of Earthbound's boost

### Strategic Implications
**Offensive Use:**
- Powerful late-game sweeping potential when HP is low
- Encourages aggressive play to reach low HP threshold
- Excellent with bulky Ground-types that can survive to low HP

**Defensive Considerations:**
- Makes the Pokemon more dangerous as it gets weaker
- Opponents may prioritize finishing off Earthbound users quickly
- Can discourage opponents from leaving the user at low HP

### Common Users
Notable Pokemon with Earthbound include:
- **Sandslash variants** - Natural Ground-type attackers
- **Dugtrio variants** - Speed + Ground STAB synergy
- **Marowak variants** - Bone-based Ground attacks
- **Rhyperior variants** - Bulky physical Ground attackers
- **Legendary Ground-types** - Enhanced offensive presence

### Competitive Usage Notes
**Strengths:**
- Consistent 1.2x boost provides reliable damage increase
- 1.5x boost at low HP creates comeback potential
- No setup required, passive damage enhancement
- Affects both physical and special Ground moves

**Weaknesses:**
- Type-locked to Ground moves only
- Requires low HP for maximum effectiveness
- Vulnerable to priority moves when at low HP
- Ground moves are commonly resisted (Flying, Grass, Bug)

### Counters
- **Flying-types**: Immune to Ground moves entirely
- **Levitate users**: Also immune to Ground attacks
- **Grass-types**: Resist Ground moves, reducing effective damage
- **Priority moves**: Can finish off low-HP Earthbound users
- **Air Balloon**: Grants temporary Ground immunity

### Synergies
**Abilities:**
- **Sand Rush**: Speed boost in sandstorm for Ground-type teams
- **Sand Force**: Additional Ground/Rock/Steel move boost in sand
- **Reckless**: Boosts recoil Ground moves like Take Down variants

**Items:**
- **Soft Sand**: Additional 1.2x Ground move boost
- **Earth Plate**: Another 1.2x Ground move boost  
- **Life Orb**: 1.3x boost to all moves (with recoil)
- **Focus Sash/Band**: Guarantees survival to activate low HP boost

**Team Support:**
- **Sandstorm setters**: Residual damage helps reach low HP threshold
- **Stealth Rock**: Chip damage assists in reaching activation point
- **Spikes/Toxic Spikes**: Additional passive damage sources

### Version History
- **Elite Redux**: Introduced as ability #299
- **Implementation**: Uses the standard SWARM_MULTIPLIER macro
- **Balance**: Matches power level of other swarm-type abilities (Overgrow, Blaze, Torrent, Swarm)

### Usage Tips
1. **HP Management**: Use entry hazards or sandstorm to safely reach low HP
2. **Move Selection**: Prioritize high-power Ground moves for maximum benefit
3. **Team Building**: Pair with Pokemon that can set up favorable conditions
4. **Timing**: Save powerful Ground moves for when the boost is most needed
5. **Coverage**: Include non-Ground moves for type coverage when boost isn't applicable