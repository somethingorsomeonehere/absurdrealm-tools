---
id: 301
name: Feline Prowess
status: reviewed
character_count: 103
---

# Feline Prowess - Ability ID 301

## In-Game Description
"Doubles own Sp. Atk stat. Boosts raw stat, not base stat."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Feline Prowess increases the user's Special Attack stat by 2x. Multiplicative with other damage boosts.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Effect**: Doubles the Pokemon's Special Attack stat (2x multiplier)
- **Application**: Applied to the raw calculated stat, not the base stat
- **Timing**: Active immediately upon entering battle
- **Stacking**: Multiplicative with stat boosts, items, and other modifiers

### Technical Implementation
```cpp
constexpr Ability FelineProwess = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPATK) *stat *= 2;
        },
};
```

The ability hooks into the stat calculation system and applies a 2x multiplier whenever the Special Attack stat is calculated.

### Activation Conditions
- **Trigger**: Automatic when Special Attack stat is calculated
- **Requirements**: None - always active
- **Duration**: Permanent while the Pokemon is in battle
- **Scope**: Affects all special moves and stat calculations

### Numerical Values
- **Multiplier**: 2.0x (100% increase)
- **Example**: A Pokemon with 100 base Special Attack becomes effectively 200
- **With +1 boost**: 100 to 200 (Feline Prowess) to 300 (with +1 boost) = 3x total
- **With Choice Specs**: 100 to 200 (Feline Prowess) to 300 (with Choice Specs) = 3x total

### Stat Calculation Order
1. Base stat + EVs + IVs + nature = base calculated stat
2. Feline Prowess multiplies by 2.0x
3. Stat boosts (+/-6 stages) apply multiplicatively
4. Items like Choice Specs apply multiplicatively
5. Abilities like Hustle apply multiplicatively

### Common Users
- **Espeon Galaxy**: Primary forme with this as a regular ability (all 3 slots)
- **Meowth Partner Mega**: Has as an innate ability alongside other abilities
- **Various Cat-like Pokemon**: Given thematically to feline Pokemon

### Strategic Implications
- **Immediate Power**: Instant 2x Special Attack boost without setup
- **No Drawbacks**: Unlike abilities like Hustle, has no negative side effects
- **Stacking Potential**: Combines multiplicatively with stat boosts and items
- **Special Sweeping**: Ideal for special attackers that need immediate power
- **Choice Item Synergy**: Particularly powerful with Choice Specs for 3x total boost

### Competitive Usage Notes
- **Tier Impact**: Significantly raises the power level of any special attacker
- **Speed Control**: Often paired with speed control since raw power is guaranteed
- **Coverage Moves**: Makes even low base power coverage moves threatening
- **Entry Hazard Weakness**: No defensive benefits, so entry hazard support helpful
- **Priority Weakness**: Vulnerable to priority moves due to no defensive boost

### Counters and Weaknesses
- **Special Walls**: High Special Defense still walls effectively despite the boost
- **Priority Moves**: Physical priority moves bypass the special attack boost
- **Status Effects**: Burns don't affect special attacks, but paralysis/sleep still work
- **Abilities**: Abilities like Wonder Guard or Flash Fire can still provide immunities
- **Trick Room**: Speed control can limit effectiveness despite power boost

### Synergies
- **Choice Items**: Choice Specs for 3x total boost, Choice Scarf for speed + power
- **Stat Boosting**: Calm Mind, Nasty Plot stack multiplicatively
- **Weather**: Special attack boosting weather effects stack
- **Screens**: Light Screen on opponent's side doesn't reduce the base multiplier
- **Life Orb**: Stacks multiplicatively for even higher damage output

### Damage Calculation Examples
**Base Case**: 100 Special Attack Pokemon using 90 BP move
- Normal: ~45-53 damage vs neutral target
- With Feline Prowess: ~90-106 damage vs neutral target

**With Choice Specs**: 100 Special Attack + Feline Prowess + Choice Specs
- Total multiplier: 2.0x (Feline Prowess) x 1.5x (Choice Specs) = 3.0x
- Damage: ~135-159 vs neutral target

**With +1 Calm Mind**: 100 Special Attack + Feline Prowess + Calm Mind
- Total multiplier: 2.0x (Feline Prowess) x 1.5x (+1 boost) = 3.0x
- Damage: ~135-159 vs neutral target

### Version History
- **Elite Redux**: Introduced as ability ID 301
- **Current Status**: Active and implemented
- **Name Discrepancy**: Code refers to "Feline Prowess" while protobuf shows "Cryptic Power"

### Notes
- The ability name shows as "Cryptic Power" in the game data but is coded as "Feline Prowess"
- This may be a display name vs internal name difference
- Implementation is straightforward and reliable
- No known bugs or edge cases in current implementation