---
id: 74
name: Pure Power
status: reviewed
character_count: 80
---

# Pure Power - Ability ID 74

## In-Game Description
"Doubles own Attack stat. Boosts raw stat, not base stat."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the user's Attack stat by 2x. Multiplicative with other damage boosts.

## Detailed Mechanical Explanation
*For Discord/reference use*

**PURE POWER** is a stat-doubling ability that multiplies the user's Attack stat by 2, making it identical to Huge Power in functionality.

### Activation Mechanics:
- **Trigger**: Passive ability, always active
- **Stat Affected**: Attack stat only
- **Calculation**: Raw stat multiplication (not base stat)
- **Timing**: Applied during stat calculation phase

### Stat Modification Details:
1. **Calculation Order**:
   - Base Attack stat + IV + EV boost
   - Nature modification applied
   - Pure Power doubles the final result
   - Other temporary modifiers (stages, items) applied afterward

2. **Practical Impact**:
   - Effective Attack stat is doubled at all times
   - Works with all physical moves
   - Stacks multiplicatively with other boosts (Choice Band, attack stages)
   - Cannot be negated by abilities like Unaware

### Move Interactions:
- **Physical Moves**: All benefit from doubled Attack
- **Special Moves**: Unaffected (uses Special Attack)
- **Mixed Moves**: Physical component benefits, special component doesn't
- **Power-based Moves**: Foul Play uses opponent's Attack, not affected by user's Pure Power
- **Status Moves**: No direct interaction

### Competitive Interactions:
1. **Stat Stage Modifications**:
   - Attack boosts stack multiplicatively: +1 Attack + Pure Power = 3x effective Attack
   - Attack drops still apply: -1 Attack + Pure Power = 1.5x effective Attack

2. **Item Synergy**:
   - Choice Band: 1.5x boost stacks for 3x total Attack
   - Life Orb: 1.3x boost stacks for 2.6x total Attack
   - Muscle Band: 1.1x boost stacks for 2.2x total Attack

3. **Ability Counters**:
   - **Intimidate**: Still reduces by one stage (halves doubled Attack to 1x)
   - **Clear Body/Hyper Cutter**: Protects Pure Power user from Intimidate
   - **Unaware**: Does NOT ignore Pure Power (ignores stages, not ability multipliers)

### Technical Implementation:
```c
constexpr Ability PurePower = {
    .onStat = HugePower.onStat,  // References Huge Power implementation
};

// Huge Power implementation (shared):
constexpr Ability HugePower = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_ATK) *stat *= 2;
        },
};
```

### Elite Redux Usage:
- **Primary User**: Mega Medicham (all three ability slots)
- **Base Stats**: Medicham has 100 base Attack, becomes 200 effective Attack
- **Combined with**: Combat Specialist, Enlightened, Technician as innate abilities
- **AI Rating**: 10/10 (maximum offensive ability priority)

### Competitive Notes:
- Transforms moderate attackers into massive physical threats
- Essential for Mega Medicham's viability in competitive play
- Pairs excellently with priority moves and Choice items
- One of the few abilities that can make 100 base Attack feel like 200

### Differences from Similar Abilities:
- **vs Huge Power**: Identical functionality, different name
- **vs Guts**: Pure Power is permanent, Guts requires status condition
- **vs Sheer Force**: Pure Power affects all moves, Sheer Force only affects moves with secondary effects

### Version History:
- Gen 3+: Always doubled Attack stat
- Elite Redux: Functionally identical to mainline games, exclusively on Mega Medicham