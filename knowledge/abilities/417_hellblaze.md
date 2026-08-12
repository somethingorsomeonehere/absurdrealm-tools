---
id: 417
name: Hellblaze
status: reviewed
character_count: 73
---

# Hellblaze - Ability ID 417

## In-Game Description
"Boosts Fire-type moves by 1.3x, or 1.8x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Fire-type moves by 30%, or by 80% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Hellblaze is an offensive ability that provides conditional damage boosts to Fire-type moves based on the user's current HP. It functions as a "boosted Swarm" ability specifically for Fire-type attacks.

### Activation Conditions
- **Move type requirement**: Only affects Fire-type moves
- **HP thresholds**: 
  - **Above 1/3 HP**: 1.3x damage multiplier (30% boost)
  - **At or below 1/3 HP**: 1.8x damage multiplier (80% boost)
- **Timing**: Activates during damage calculation phase
- **Stacking**: Multiplies with other damage modifiers (items, weather, etc.)

### Technical Implementation
```c
// Hellblaze uses the BOOSTED_SWARM_MULTIPLIER macro with TYPE_FIRE
constexpr Ability Hellblaze = {
    .onOffensiveMultiplier = BOOSTED_SWARM_MULTIPLIER(TYPE_FIRE),
};

// The macro implementation:
#define BOOSTED_SWARM_MULTIPLIER(type)                                       \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.8);                                                    \
            else                                                             \
                MUL(1.3);                                                    \
        }                                                                    \
    }
```

### HP Calculation Details
- **1/3 HP threshold**: Calculated as `maxHP / 3` (integer division)
- **Exact threshold**: Ability activates when `currentHP <= (maxHP / 3)`
- **Examples**:
  - 300 HP Pokemon: Activates at 100 HP or below
  - 299 HP Pokemon: Activates at 99 HP or below
  - 301 HP Pokemon: Activates at 100 HP or below

### Strategic Applications
- **Late-game sweeping**: Massive damage boost when in the danger zone
- **Revenge killing**: Turn low HP disadvantage into offensive advantage
- **Berries synergy**: Sitrus Berry, Figy Berry line for controlled HP management
- **Recoil moves**: Life Orb, Flare Blitz recoil becomes beneficial
- **Substitute stalling**: Drop HP intentionally for maximum power

### Damage Calculations
With base power 80 Fire-type move:
- **Above 1/3 HP**: 80 x 1.3 = 104 effective base power
- **Below 1/3 HP**: 80 x 1.8 = 144 effective base power
- **Comparison**: 80% boost rivals Choice Band (50%) + Life Orb (30%)

### Important Interactions
- **Weather effects**: Stacks with sun boost (1.5x) for devastating combinations
- **STAB bonus**: Multiplies with STAB (1.5x) for pure Fire types
- **Choice items**: Stacks with Choice Band/Specs for extreme damage
- **Burn immunity**: Fire types typically immune to burn, no HP drain concern
- **Ability suppression**: Doesn't work if ability is negated

### Similar Abilities
Hellblaze is part of the "Boosted Swarm" family in Elite Redux:
- **Riptide**: Same mechanic for Water-type moves
- **Forest Rage**: Same mechanic for Grass-type moves
- **Purgatory**: Same mechanic for Ghost-type moves
- **Gladiator**: Same mechanic for Fighting-type moves
- **Rockhard Shaft**: Same mechanic for Rock-type moves

### Competitive Usage Notes
- **High-risk, high-reward**: Requires careful HP management
- **End-game closer**: Most effective in late battle scenarios
- **Priority moves**: Pairs well with priority Fire moves for guaranteed revenge kills
- **Substitute support**: Use to safely reach low HP thresholds
- **Healing timing**: Time recovery carefully to maintain low HP when needed

### Counters and Limitations
- **Non-Fire moves**: Provides no benefit to coverage moves
- **Priority moves**: Vulnerable to priority attacks when at low HP
- **Status conditions**: Poison/burn can push HP too low unintentionally
- **Multi-hit moves**: Can be KO'd before utilizing the boost
- **Healing moves**: Opponent can stall until HP is restored

### Optimal Pokemon Traits
- **High Attack/Special Attack**: Maximizes damage potential
- **Decent Speed**: Ensure you move first when at low HP
- **Bulk investment**: Survive hits to reach optimal HP range
- **Fire STAB**: Pure or dual Fire types benefit most
- **Recovery access**: Roost, Slack Off for controlled HP management

### Move Synergies
- **Flare Blitz**: High power recoil move benefits from both multipliers
- **Fire Blast**: High power special move for sweeping
- **Flame Charge**: Priority-like effect with damage boost
- **Eruption**: Ironically anti-synergistic due to HP-based power
- **Overheat**: One-shot power spike doesn't care about stat drops

### Team Building Considerations
- **Entry hazard support**: Stealth Rock chip damage helps reach threshold
- **Cleric support**: Aromatherapy/Heal Bell for status protection
- **Redirection**: Rage Powder, Follow Me to protect setup
- **Speed control**: Thunder Wave, Sticky Web for speed advantage
- **Weather support**: Sun teams maximize Fire-type effectiveness

### Version History
- Elite Redux exclusive ability as part of expanded ability roster
- Uses proven "Boosted Swarm" formula with Fire-type specialization
- Balanced alternative to traditional Fire-type abilities like Blaze

### Usage Tips
1. **Monitor HP carefully**: Know your exact threshold for maximum power
2. **Time recovery**: Use healing moves strategically to maintain optimal HP
3. **Priority awareness**: Watch for opponent's priority moves when low
4. **Setup opportunities**: Use the 1.3x boost to soften targets initially
5. **End-game planning**: Save your most powerful Hellblaze user for late game