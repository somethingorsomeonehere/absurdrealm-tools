---
id: 55
name: Hustle
status: reviewed
character_count: 101
---

# Hustle - Ability ID 55

## In-Game Description
"0.9x accuracy. Boosts damage by 1.4x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of attacks by 1.4x but reduces their accuracy by 10%. Only affects non-status moves. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**HUSTLE** is a double-edged ability that significantly increases offensive power at the cost of accuracy, creating a high-risk, high-reward playstyle.

### Activation Mechanics:
- **Power Trigger**: onOffensiveMultiplier hook applies 1.4x damage boost
- **Accuracy Trigger**: onAccuracy hook applies 0.9x accuracy reduction (90% accuracy)
- **Move Classification**: Only affects non-status moves (SPLIT_PHYSICAL and SPLIT_SPECIAL)
- **No Announcement**: Ability works silently without battle messages

### Technical Implementation:
```c
constexpr Ability Hustle = {
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) { MUL(1.4); },
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK_NOT(IS_MOVE_STATUS(move)) *accuracy *= .9;
        return ACCURACY_MULTIPLICATIVE;
    },
};
```

### Core Mechanics:
1. **Power Boost**:
   - Applies 1.4x multiplier to all physical and special attacking moves
   - Stacks multiplicatively with other damage modifiers
   - No power boost for status moves

2. **Accuracy Reduction**:
   - Reduces accuracy to 90% of original value (multiply by 0.9)
   - Only affects physical and special moves
   - Status moves maintain their original accuracy
   - Uses ACCURACY_MULTIPLICATIVE priority level

### Move Category Effects:
- **Physical Moves**: +40% power, 90% accuracy
- **Special Moves**: +40% power, 90% accuracy  
- **Status Moves**: No power change, normal accuracy (100% for most)

### Accuracy Calculations:
- **100% Accuracy Move**: 100% x 0.9 = 90% accuracy
- **95% Accuracy Move**: 95% x 0.9 = 85.5% accuracy
- **90% Accuracy Move**: 90% x 0.9 = 81% accuracy
- **80% Accuracy Move**: 80% x 0.9 = 72% accuracy
- **70% Accuracy Move**: 70% x 0.9 = 63% accuracy

### Power Calculations:
Example with 100 Base Power move:
- **Normal**: 100 BP x 1.0 = 100 effective power
- **With Hustle**: 100 BP x 1.4 = 140 effective power
- **Net Effect**: 40% more damage per hit, 10% more misses

### AI Evaluation:
- **AI Score**: 7/10 (positive rating indicates AI considers it beneficial)
- **Trade-off Analysis**: AI values the power boost more than the accuracy reduction
- **Move Selection**: AI may favor higher accuracy moves to mitigate the penalty

### Pokemon with Hustle:
Notable users include:
- **Rattata/Raticate lines** (both Kantonian and Alolan forms)
- **Nidoran lines** (various regional forms)
- **Togepi line** (Togepi only)
- **Darumaka lines** (all regional variants)
- **Various other physical attackers**

### Strategic Applications:
1. **Frail Sweepers**: Hustle maximizes damage output for Pokemon that might not survive long
2. **Choice Item Synergy**: Pairs well with Choice Band/Specs for massive damage
3. **Priority Moves**: Benefits moves like Quick Attack and Extreme Speed
4. **Status Move Coverage**: Can use status moves without accuracy penalty

### Competitive Analysis:
**Advantages:**
- Significant power increase makes OHKOs and 2HKOs more achievable
- Doesn't affect status moves, maintaining utility options
- Excellent for hit-and-run tactics with frail attackers
- Pairs well with high-accuracy moves (100% becomes 90%)

**Disadvantages:**
- 10% accuracy loss can be crucial in competitive play
- Poor synergy with already-inaccurate moves
- Risk of missing at critical moments
- Can be unreliable for consistent damage output

### Synergies and Counters:
**Synergistic Strategies:**
- **High-Accuracy Moves**: Prioritize 100% accuracy moves that become 90%
- **Choice Items**: Choice Band/Specs stack for devastating power
- **Priority Moves**: Quick Attack, Extreme Speed get both power and speed
- **Status Backup**: Use status moves when attacks might miss

**Optimal Move Selection:**
- Favor moves with 95%+ base accuracy
- Avoid moves with 85% or lower accuracy
- Prioritize high base power moves to maximize the 1.4x boost
- Include status moves for utility without accuracy penalty

**Items that Help:**
- **Wide Lens**: +10% accuracy partially compensates (90% to 99%)
- **Zoom Lens**: +20% accuracy when moving second (90% to 108%, capped at 100%)
- **Choice Items**: Stack damage boosts for maximum impact

### Calculation Examples:
**Scenario 1: 100 BP Move with Choice Band**
- Base: 100 BP
- Hustle: 100 x 1.4 = 140 effective BP
- Choice Band: 140 x 1.5 = 210 effective BP
- Accuracy: 90%

**Scenario 2: Stone Edge (100 BP, 80% accuracy)**
- Power: 100 x 1.4 = 140 effective BP
- Accuracy: 80% x 0.9 = 72%
- **Not recommended due to low final accuracy**

**Scenario 3: Body Slam (85 BP, 100% accuracy)**
- Power: 85 x 1.4 = 119 effective BP
- Accuracy: 100% x 0.9 = 90%
- **Good choice - reliable accuracy with decent power**

### Version History:
- **Gen 3-4**: Physical moves only affected
- **Gen 5+**: Affects both physical and special moves
- **Elite Redux**: Follows Gen 5+ implementation affecting all attacking moves