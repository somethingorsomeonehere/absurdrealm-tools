---
id: 37
name: Huge Power
status: reviewed
character_count: 80
---

# Huge Power - Ability ID 37

## In-Game Description
"Doubles own Attack stat. Boosts raw stat, not base stat."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the user's Attack stat by 2x. Multiplicative with other damage boosts.

## Detailed Mechanical Explanation
*For Discord/reference use*

**HUGE POWER** is a stat-modifying ability that provides a massive boost to physical offensive power.

### Stat Modification Mechanics:
- **Trigger**: Applied during stat calculation (onStat hook)
- **Effect**: Multiplies Attack stat by 2.0 before other modifiers
- **Application Order**: Base stat to Huge Power to stat stages to items/other effects
- **Stat Type**: Only affects STAT_ATK (Attack), no other stats modified

### Calculation Order:
1. **Base Attack stat** (from species data)
2. **Huge Power multiplication** (x2.0)
3. **Stat stage modifiers** (+1 Attack = x1.5, etc.)
4. **Item effects** (Choice Band, Life Orb, etc.)
5. **Other ability effects** (Guts, Hustle damage multiplier, etc.)

### Key Interactions:
- **vs Hustle**: Huge Power affects raw stat calculation, Hustle affects damage multiplier. Both stack multiplicatively
- **vs Choice Band**: Huge Power doubles the stat, Choice Band multiplies damage by 1.5x. Stack multiplicatively
- **vs Stat Stages**: Attack boosts (+1, +2, etc.) apply after Huge Power doubling
- **vs Burn**: Burn's Attack reduction applies to the doubled stat, so still deals significant damage

### Ability Relationships:
- **Pure Power (ID 74)**: Functionally identical ability with same effect
- **Both abilities share code**: `PurePower.onStat = HugePower.onStat`
- **AI Rating**: Valued at 10 (maximum priority) by battle AI

### Technical Implementation:
```c
constexpr Ability HugePower = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_ATK) *stat *= 2;
        },
};
```

### Pokemon Distribution in Elite Redux:
- **As Main Ability**: Various Pokemon including select legendaries
- **As Innate Ability**: Common on physical attackers across multiple evolution lines
- **Notable Users**: Azumarill line, Mawile, and many custom Elite Redux Pokemon
- **Pure Power Users**: Meditite/Medicham line (functionally identical)

### Competitive Analysis:
- **Power Level**: Extremely high - effectively doubles physical damage output
- **Synergy**: Exceptional with high base Attack stats and physical movesets
- **Counters**: Status moves (burn), defensive abilities, switching tactics
- **Team Role**: Enables frail Pokemon to become physical powerhouses

### Common Misconceptions:
- **NOT a damage multiplier**: Affects the stat itself, not final damage calculation
- **Works with all physical moves**: Unlike some abilities, has no move restrictions
- **Stacks with everything**: Since it modifies the base stat, it multiplies with all other effects
- **Not affected by Mold Breaker**: Stat modifications cannot be suppressed

### Strategic Applications:
1. **Sweeper Setup**: Combined with stat boosts, creates overwhelming physical presence
2. **Pivot Utility**: High Attack makes even resisted moves threatening
3. **Item Synergy**: Choice Band/Life Orb become incredibly potent
4. **Priority Moves**: Makes priority attacks hit like full-power moves

### Version History:
- **Gen 3**: Introduced on Azurill/Azumarill and Meditite/Medicham
- **Elite Redux**: Expanded to numerous Pokemon as both main and innate ability
- **Implementation**: Uses modern callback system with precise stat timing