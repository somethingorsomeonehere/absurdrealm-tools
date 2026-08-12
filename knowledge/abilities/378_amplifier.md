---
id: 378
name: Amplifier
status: reviewed
character_count: 164
---

# Amplifier - Ability ID 378

## In-Game Description
"Ups sound moves by 30% and makes them hit both foes."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Amplifier boosts sound-based moves by 30% damage. Single-target sound moves gain spread targeting to hit both opposing Pokemon. Does not spread with multihit moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

Amplifier is a sound-focused offensive ability that provides both damage enhancement and tactical advantages in doubles battles. It shares its core damage boost mechanic with Punk Rock but lacks the defensive component.

**Offensive Effects:**
- Increases damage of all sound moves by 30% (1.3x multiplier)
- Applies to any move with the FLAG_SOUND property
- Stacks multiplicatively with other damage modifiers (STAB, type effectiveness, items, etc.)

**Doubles Battle Targeting:**
- Single-target sound moves automatically hit both opposing Pokemon
- This targeting change is handled in battle_util.c (line 130-132)
- Provides significant tactical advantage by creating spread damage from normally single-target moves
- Does not affect moves that are already spread moves (like Boomburst)

**Sound Move Classification:**
Sound moves are determined by the FLAG_SOUND property and include common moves like:
- **Offensive**: Hyper Voice (95 BP), Boomburst (140 BP), Round (60 BP), Bug Buzz (90 BP)
- **Special**: Overdrive (80 BP Electric), Clanging Scales (110 BP Dragon)
- **Status**: Roar, Sing, Supersonic, Grass Whistle (damage boost doesn't apply)

**Technical Implementation:**
```c
// abilities.cc lines 3931-3933
constexpr Ability Amplifier = {
    .onOffensiveMultiplier = PunkRock.onOffensiveMultiplier,
};
```

The ability directly uses Punk Rock's offensive multiplier function:
```c
// PunkRock implementation (lines 2666-2676)
.onOffensiveMultiplier =
    +[](ON_OFFENSIVE_MULTIPLIER) {
        if (IsSoundMove(battler, move)) MUL(1.3);
    },
```

**Doubles Targeting Implementation:**
```c
// battle_util.c lines 130-132
else if ((BATTLER_HAS_ABILITY(battler, ABILITY_AMPLIFIER) || 
          BATTLER_HAS_ABILITY(battler, ABILITY_BASS_BOOSTED)) && 
         (IsSoundMove(battler, moveId)) &&
         gBattleMoves[moveId].target == MOVE_TARGET_SELECTED)
    return MOVE_TARGET_BOTH;
```

**Strategic Applications:**
- **Singles**: Straightforward 30% damage boost to sound moves
- **Doubles**: Game-changing spread damage capability
- **Hyper Voice**: Becomes a powerful spread STAB move with 123.5 effective BP
- **Choice item synergy**: Pairs excellently with Choice Specs for massive damage
- **Team disruption**: Forces opponents to account for spread pressure

**Key Differences from Related Abilities:**
- **vs Punk Rock**: Lacks defensive component (no 50% sound move damage reduction)
- **vs Bass Boosted**: Bass Boosted combines Amplifier + Punk Rock for both offensive and defensive benefits
- **vs Liquid Voice**: Different conversion mechanic (Normal to Water vs sound enhancement)

**Competitive Viability:**
- **Medium tier**: Strong offensive ability but lacks defensive utility
- **Format dependent**: Much stronger in doubles than singles
- **Niche but effective**: Excellent on sound-focused attackers
- **Team support**: Spread damage helps with field control

**Common Users and Synergies:**
Amplifier appears as an innate ability on select Pokemon with sound-move emphasis. It synergizes well with:
- **Throat Spray**: Boosts Special Attack when using sound moves
- **Choice Specs**: Stacks damage multipliers for extreme power
- **Sound moves with secondary effects**: Bug Buzz's Sp. Atk drop affects both targets in doubles

**Counters and Limitations:**
- **Soundproof**: Complete immunity to all sound moves
- **Mold Breaker variants**: Can bypass defensive abilities that would normally block sound moves
- **Limited movepool**: Effectiveness depends on access to good sound moves
- **No defensive utility**: Unlike Punk Rock, provides no protection against opposing sound moves

**Interactions:**
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, and Turboblaze
- **Substitute**: Sound moves pierce Substitute, so Amplifier still applies
- **Multi-hit moves**: Each hit of multi-hit sound moves gets the full 30% bonus
- **Critical hits**: Damage multiplier applies before critical hit calculation

**Power Calculation Example:**
Base Hyper Voice (90 BP) with Amplifier:
- Base damage: 90 BP
- Amplifier boost: 90 x 1.3 = 117 BP effective
- With STAB: 117 x 1.5 = 175.5 BP effective
- In doubles: Hits both opponents at full power

**Version History:**
- **Elite Redux exclusive**: Custom ability that extracts Punk Rock's offensive component
- **Doubles focus**: Particularly designed for doubles battle utility
- **Balanced design**: Provides offensive power without the defensive safety of Punk Rock
- **Targeting innovation**: Unique spread targeting mechanic for sound moves

**Lore and Flavor:**
Amplifier represents mastery over sound projection and acoustic enhancement, allowing the Pokemon to amplify their vocalizations to reach wider areas and deal increased damage. The name evokes audio equipment and sound engineering, fitting for Pokemon that specialize in sonic attacks and battlefield control through sound manipulation.