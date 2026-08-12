---
id: 458
name: Purgatory
status: reviewed
character_count: 74
---

# Purgatory - Ability ID 458

## In-Game Description
"Boosts Ghost-type moves by 1.3x, or 1.8x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Ghost-type moves by 30%, or by 80% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Purgatory is an offensive ability that provides a damage boost to Ghost-type moves, with an enhanced effect when the user is at low health. This ability combines the concepts of type-boosting abilities (like Blaze) with the pinch activation mechanic of Swarm-like abilities.

### Activation Conditions
- **Move type requirement**: Only affects Ghost-type moves
- **HP threshold**: 
  - Normal boost: 1.3x multiplier when above 1/3 HP
  - Pinch boost: 1.8x multiplier when at or below 1/3 HP
- **Timing**: Applied during damage calculation before other multipliers

### Damage Calculation
```c
// Purgatory implementation using BOOSTED_SWARM_MULTIPLIER macro
if (moveType == TYPE_GHOST) {
    if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3))
        MUL(1.8);  // 80% boost at low HP
    else
        MUL(1.3);  // 30% boost at normal HP
}
```

### Technical Implementation
- **Macro**: Uses `BOOSTED_SWARM_MULTIPLIER(TYPE_GHOST)`
- **Function**: `onOffensiveMultiplier` callback
- **HP check**: Exact calculation is `hp <= maxHP / 3`
- **Type check**: Only applies to `TYPE_GHOST` moves
- **Stacking**: Multiplies with other damage modifiers

### Important Interactions
- **STAB stacking**: Multiplies with Same Type Attack Bonus (1.5x)
- **Item bonuses**: Stacks with type-boosting items like Spell Tag
- **Weather effects**: Combines with weather-based damage modifiers
- **Stat stages**: Applied after Attack stat modifications
- **Critical hits**: Multiplies with critical hit damage
- **Type effectiveness**: Applied before type effectiveness calculations

### HP Threshold Details
- **Activation point**: Exactly 1/3 of maximum HP or below
- **Real-time**: Checked each time a Ghost-type move is used
- **Healing interaction**: Boost changes if healed above threshold
- **Damage interaction**: Boost activates if damaged below threshold

### Strategic Applications
- **Pinch sweeping**: Becomes extremely dangerous at low HP
- **Risk/reward**: Encourages aggressive play at low health
- **Late-game power**: Excellent for cleaning up weakened teams
- **Suicide leads**: Can be used on frail Ghost-types for immediate pressure
- **Revenge killing**: Perfect for coming in after a teammate faints

### Move Synergies
- **Shadow Ball**: High-power special Ghost move
- **Poltergeist**: Physical Ghost move that can destroy items
- **Phantom Force**: Two-turn move with semi-invulnerability
- **Shadow Sneak**: Priority Ghost move for finishing
- **Hex**: Doubles power against statused targets
- **Shadow Claw**: High critical hit ratio physical move

### Type Coverage
Ghost-type moves are:
- **Super effective**: Against Psychic and Ghost types
- **Not very effective**: Against Dark types
- **No effect**: Against Normal types (unless ability like Scrappy)
- **Neutral**: Against all other types

### Competitive Usage
- **Offensive sweepers**: Ideal for fast, frail Ghost-types
- **Wallbreakers**: Enhanced power helps break through bulky targets
- **Endgame cleaners**: Devastating at low HP against weakened teams
- **Sash users**: Pairs well with Focus Sash for guaranteed pinch activation
- **Substitute users**: Can safely get to low HP behind Substitute

### Common Users
- Fast Ghost-type sweepers
- Frail but powerful Ghost-types
- Mixed attackers with Ghost-type coverage
- Pokemon with access to powerful Ghost-type moves
- Suicide leads that can threaten immediately

### Ability Comparisons
- **vs Adaptability**: Purgatory gives higher boost at pinch (1.8x vs 2.0x STAB)
- **vs Swarm**: Same mechanic but affects Ghost moves instead of Bug
- **vs Blaze/Torrent**: Similar pinch concept but with normal boost baseline
- **vs Rivalry**: More consistent than gender-dependent boosts

### Counters and Limitations
- **Type immunity**: Normal types are immune to Ghost moves
- **Dark types**: Resist Ghost-type moves
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable ability
- **HP management**: Opponent can avoid low HP range with careful play
- **Move restriction**: Only affects Ghost-type moves
- **Prediction**: Opponent can play around the HP threshold

### Synergistic Abilities
- **Levitate**: Immunity to Ground moves helps preserve HP
- **Magic Guard**: Prevents indirect damage for HP control
- **Sturdy**: Guarantees survival to 1 HP for maximum boost
- **Multiscale**: Reduces damage when healthy to preserve HP range

### Item Synergies
- **Focus Sash**: Guarantees low HP activation
- **Spell Tag**: Stacks with Purgatory for massive Ghost move power
- **Life Orb**: Additional power boost (with recoil to reach pinch)
- **Leftovers**: HP management to stay in optimal range
- **Sitrus Berry**: Emergency healing to escape dangerous HP range

### Version History
- New ability introduced in Elite Redux
- Uses the established BOOSTED_SWARM_MULTIPLIER framework
- Part of the expanded ability roster for enhanced gameplay depth
- Designed to give Ghost-types a unique offensive niche

### Calculation Examples
**Example 1**: Gengar with Purgatory using Shadow Ball
- Base power: 80
- STAB: 80 x 1.5 = 120
- Purgatory (healthy): 120 x 1.3 = 156
- Purgatory (pinch): 120 x 1.8 = 216

**Example 2**: With Spell Tag
- Base power: 80
- STAB: 80 x 1.5 = 120  
- Spell Tag: 120 x 1.2 = 144
- Purgatory (pinch): 144 x 1.8 = 259.2 effective power