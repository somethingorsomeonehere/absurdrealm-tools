---
id: 396
name: Liquid Voice
status: reviewed
character_count: 101
---

# Liquid Voice - Ability ID 396

## In-Game Description
"Sound moves get a 1.2x boost and become Water if Normal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sound-based moves receive a 1.2x power boost and Normal-type sound moves are converted to Water-type.

## Detailed Mechanical Explanation

### Basic Information
- **Ability Name**: Liquid Voice
- **Internal ID**: 396 (ABILITY_LIQUID_VOICE, enum value 204)
- **Type**: Sound/Water Enhancement
- **Introduced**: Generation VII equivalent

### Technical Implementation

### Source Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Implementation Lines**: 2213-2223
- **Ability Table Entry**: Line 9056

### Code Implementation
```cpp
constexpr Ability LiquidVoice = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IsSoundMove(battler, move)) MUL(1.2);
        },
    .onMoveType = +[](ON_MOVE_TYPE) -> int {
        CHECK(moveType == TYPE_NORMAL)
        CHECK(gBattleMoves[move].flags & FLAG_SOUND)
        return TYPE_WATER + 1;
    },
};
```

### Mechanics Breakdown
1. **Sound Move Boost**: All sound moves (identified by `IsSoundMove()` function) receive a 1.2x power multiplier
2. **Type Conversion**: Normal-type moves with the `FLAG_SOUND` flag are converted to Water-type
3. **Triggering Conditions**: 
   - Move must have sound-based properties (`FLAG_SOUND`)
   - For type conversion: Move must be Normal-type initially

## Pokemon with This Ability

### Regular Ability Holders
- **Mega Lapras**: All three ability slots (Triple Liquid Voice)
- **Wailmer**: One of three regular abilities (alongside Stamina, Drizzle)  
- **Tympole**: Hidden ability option (alongside Hydration, Soundproof)
- **Palpitoad**: Hidden ability option (alongside Damp, Sand Song)

### Innate Ability Holders
- **Wailord**: Innate ability (permanent passive effect)
- **Brionne**: Innate ability (permanent passive effect)  
- **Primarina**: Innate ability (permanent passive effect)
- **Mega Primarina**: Innate ability (permanent passive effect)

## Strategic Analysis

### Competitive Viability: Medium Tier
Liquid Voice offers solid utility for sound-based movesets with both offensive enhancement and type flexibility.

### Strengths
1. **Power Enhancement**: 1.2x multiplier applies to all sound moves regardless of type
2. **Type Coverage**: Converts Normal sound moves to Water-type for better coverage
3. **STAB Synergy**: Water-type Pokemon gain STAB on converted moves
4. **Broad Application**: Works with any sound-based move

### Weaknesses
1. **Move Dependence**: Limited to sound-based moves only
2. **Moderate Boost**: 1.2x multiplier is decent but not overwhelming
3. **Type Restriction**: Only converts Normal-type sound moves
4. **Situational**: Effectiveness depends on moveset composition

### Optimal Usage
- **Water-type Specialists**: Pokemon like Primarina benefit from STAB on converted moves
- **Sound Move Sets**: Pokemon with multiple sound moves maximize the power boost
- **Mixed Coverage**: Provides Water-type coverage on otherwise Normal sound moves

## Related Abilities

### Similar Type-Converting Sound Abilities
Liquid Voice is part of a family of abilities that convert Normal sound moves to different types:

1. **Sand Song** (Ability #274): Converts to Ground-type
   - Found on: Palpitoad as regular ability
   - Implementation shares `LiquidVoice.onOffensiveMultiplier`

2. **Banshee** (Ability #540): Converts to Ghost-type  
   - Implementation shares `LiquidVoice.onOffensiveMultiplier`

3. **Snow Song** (Ability #624): Converts to Ice-type
   - Implementation shares `LiquidVoice.onOffensiveMultiplier`

4. **Power Metal** (Ability #657): Converts to Steel-type
   - Implementation shares `LiquidVoice.onOffensiveMultiplier`

### Other Sound-Related Abilities
- **Soundproof**: Immunity to sound moves
- **Punk Rock**: Enhanced sound moves (1.3x boost) and sound move resistance
- **Amplifier**: Found on Brionne/Primarina, likely sound-related enhancement

## Competitive Applications

### Team Building Considerations
1. **Sound Move Synergy**: Pairs well with Pokemon that learn multiple sound moves
2. **Water-type Teams**: Enhances mono-Water team strategies
3. **Coverage Options**: Provides unexpected Water-type attacks from Normal moves

### Counter-Strategies
1. **Soundproof**: Complete immunity to sound-based attacks
2. **Water-type Resistances**: Grass and Water-types resist converted moves
3. **Sound Move Disruption**: Abilities or moves that prevent sound attacks

### Notable Move Interactions
- **Hyper Voice**: Normal sound move to Water-type with 1.2x boost
- **Boomburst**: Normal sound move to Water-type with 1.2x boost  
- **Round**: Normal sound move to Water-type with 1.2x boost
- **Echoed Voice**: Normal sound move to Water-type with 1.2x boost

## Conclusion

Liquid Voice represents a balanced approach to sound-based enhancement, offering both power and utility through type conversion. While not game-breaking, it provides solid strategic value for Pokemon with appropriate movesets, particularly Water-types that can leverage STAB bonuses on converted moves. The ability's design fits well within Elite Redux's philosophy of providing meaningful but not overpowered enhancements to existing mechanics.

The shared implementation pattern with similar elemental sound conversion abilities (Sand Song, Banshee, etc.) demonstrates good code design while maintaining consistent mechanics across related abilities.