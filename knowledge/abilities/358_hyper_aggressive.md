---
id: 358
name: Hyper Aggressive
status: reviewed
character_count: 164
---

# Hyper Aggressive - Ability ID 358

## In-Game Description
"Moves hit twice. Second hit does 25% damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Makes all attacks hit twice in succession. The first hit deals 100%, while the second hit deals 25%. Each hit rolls secondary effects independently (except flinch).

## Detailed Mechanical Explanation

**Hyper Aggressive** is a powerful offensive ability that causes all damaging moves to hit twice, with the second hit dealing reduced damage.

### Core Implementation
Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` at **line 3774-3776**:

```cpp
constexpr Ability HyperAggressive = {
    .onParentalBond = ParentalBond.onParentalBond,
};
```

The ability inherits the exact same implementation as Parental Bond, which is defined at **line 1982-1985**:

```cpp
constexpr Ability ParentalBond = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType { return PARENTAL_BOND_HYPER_AGGRESSIVE; },
    .resistsFortKnox = TRUE,
};
```

### Damage Calculation Mechanics

#### Hit Count Logic
The ability is processed in `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_script_commands.c` at **line 988-992**:

```cpp
int GetParentalBondCount(int battler, MultihitType parentalBondType) {
    switch (parentalBondType) {
        case PARENTAL_BOND_HYPER_AGGRESSIVE:
        // ... other cases
            return 2;
```

#### Damage Multiplier Logic
The damage reduction for the second hit is handled in `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_util.c` at **line 7330-7332**:

```cpp
u16 GetParentalBondMultiplier(MultihitType parentalBondType, int turn) {
    switch (parentalBondType) {
        case PARENTAL_BOND_HYPER_AGGRESSIVE:
            REQUIRE(turn)
            return UQ_4_12(0.25);
```

This means:
- **First hit (turn 0)**: 100% damage (no modifier applied)
- **Second hit (turn 1)**: 25% damage (0.25x multiplier)

### Strategic Analysis

#### Damage Output Comparison
- **Total damage multiplier**: 1.25x (100% + 25% = 125% of original damage)
- **Compared to Parental Bond**: Identical mechanics and damage output
- **Advantage over standard moves**: 25% damage increase

#### Battle Applications

**Offensive Benefits:**
- **Consistent damage boost**: Every damaging move gets 25% more total damage
- **Breaking substitutes/sashes**: Two hits can break Focus Sash, Sturdy, and Disguise
- **Multi-hit synergy**: Works with items like King's Rock for multiple flinch chances
- **Status spreading**: Moves with secondary effects (like paralysis) get two chances to activate

**Strategic Considerations:**
- **Predictable pattern**: Opponents know exactly when the second hit will occur
- **Fort Knox vulnerability**: Completely negated by Fort Knox and Wonder Skin abilities
- **Priority interaction**: Both hits maintain the same priority level
- **Contact moves**: Both hits make contact if the original move does

### Pokemon Distribution

Hyper Aggressive appears on **79 different Pokemon** in Elite Redux, making it one of the more common offensive abilities. It appears as both:
- **Regular ability**: Available through normal ability slots
- **Innate ability**: Always active regardless of ability slot

### Competitive Viability

#### Tier Assessment: **A-Tier**
Hyper Aggressive is a consistently powerful offensive ability that provides reliable damage increases.

**Strengths:**
- **Universal applicability**: Works with all damaging moves
- **Substantial damage boost**: 25% increase is significant
- **Breaking utility**: Can break through defensive options
- **No setup required**: Always active

**Weaknesses:**
- **Fort Knox counter**: Completely shut down by defensive abilities
- **Diminishing returns**: Less effective against already bulky targets  
- **Predictable timing**: Opponents can play around the two-hit pattern

#### Best Use Cases
1. **Physical attackers**: Maximizes the damage boost on high-power physical moves
2. **Multi-effect moves**: Double chances for secondary effects to activate
3. **Breaking strategies**: Reliable way to break through defensive options
4. **Item synergy**: Excellent with contact-based held items

### Related Abilities

#### Identical Mechanics
- **Parental Bond (#185)**: Exact same implementation and damage calculation

#### Similar Multi-Hit Abilities
- **Multi Headed (#347)**: 2-3 hits based on species flags, different damage ratios
- **Primal Maw (#420)**: Double hits specifically for bite moves
- **Dual Wield (#433)**: Double hits for specific move categories

#### Countered By
- **Fort Knox (#341)**: Completely negates the ability
- **Wonder Skin (#147)**: Blocks the multi-hit effect

### Technical Implementation Notes

#### Code Structure
The ability uses the `onParentalBond` hook system, which is Elite Redux's framework for handling multi-hit abilities. This system:

1. **Checks for ability activation** during move execution
2. **Returns MultihitType** to determine hit count and damage modifiers
3. **Applies damage reduction** through the GetParentalBondMultiplier function
4. **Maintains move properties** across all hits (accuracy, critical hit chance, etc.)

#### Integration Points
- **Battle engine**: Hooks into damage calculation pipeline
- **Move execution**: Modifies hit count during move processing
- **Animation system**: Handles visual effects for multiple hits
- **Sound system**: Manages audio cues for each hit

### Version History
Hyper Aggressive was introduced as part of Elite Redux's expanded ability system, designed to provide more offensive options while maintaining balance through the Fort Knox counter-system.

## Summary
Hyper Aggressive is a straightforward but powerful offensive ability that increases damage output by 25% through a two-hit mechanic. While it shares identical mechanics with Parental Bond, its widespread distribution makes it a common sight in competitive play. The ability excels at breaking through defensive strategies and providing consistent damage increases, though it remains vulnerable to Fort Knox-style counters.