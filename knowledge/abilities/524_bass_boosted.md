---
id: 524
name: Bass Boosted
status: reviewed
character_count: 299
---

# Bass Boosted - Ability ID 524

## In-Game Description
"Amplifier + Punk Rock."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts sound-based moves by 30%. Single-target sound moves gain spread targeting to hit both opposing Pokemon. Does not spread with multihit moves. Also boosts the user's sound moves by another 30% and reduces incoming sound move damage by 50%. Damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Bass Boosted is a hybrid ability that combines the effects of two separate abilities: Amplifier and Punk Rock. This creates a powerful dual-purpose ability that both enhances sound move offense and provides defensive utility against sound-based attacks.

### Activation Conditions
- **Sound move detection**: Moves with the FLAG_SOUND flag are affected
- **Type conversion**: Normal-type moves become sound moves if the user has Reverbate ability
- **Target modification**: Sound moves hit both opponents in double battles when using single-target sound moves

### Component Abilities Analysis

#### Amplifier Component (Offensive)
- **Damage multiplier**: 1.3x (30% boost) to sound moves
- **Doubles targeting**: Single-target sound moves hit both opponents in doubles
- **Stacks with**: Other offensive multipliers and items

#### Punk Rock Component (Defensive)
- **Damage reduction**: 0.5x (50% reduction) from incoming sound moves
- **Defensive utility**: Significant protection against sound-based attacks
- **Breakable ability**: Can be bypassed by Mold Breaker-type abilities

### Technical Implementation
```c
constexpr Ability BassBoosted = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            // Amplifier effect (30% boost to sound moves)
            Amplifier.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
            // Punk Rock offensive effect (also 30% boost)
            PunkRock.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        },
    .onDefensiveMultiplier = PunkRock.onDefensiveMultiplier, // 50% reduction
    .breakable = TRUE,
};
```

### Sound Move Identification
```c
int IsSoundMove(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_SOUND) return TRUE;
    if (gBattleMoves[move].type == TYPE_NORMAL && BattlerHasAbility(battler, ABILITY_REVERBATE, FALSE)) return TRUE;
    return FALSE;
}
```

### Doubles Battle Mechanics
In double battles, Bass Boosted modifies targeting for sound moves:
- Single-target sound moves become multi-target (hit both opponents)
- This effect comes from the Amplifier component
- Provides significant tactical advantage in doubles format

### Sound Moves in Elite Redux
Common sound moves that benefit from Bass Boosted include:
- **Boomburst**: Extremely powerful spread move
- **Hyper Voice**: Reliable STAB option
- **Bug Buzz**: Special Attack lowering chance
- **Roar**: Phasing move (doesn't get damage boost)
- **Perish Song**: Status move (doesn't get damage boost)
- **Overdrive**: Electric-type sound move
- **Clanging Scales**: Dragon-type sound move

### Important Interactions
- **Ability suppression**: Mold Breaker, Teravolt, and Turboblaze bypass the defensive component
- **Soundproof immunity**: Pokemon with Soundproof are immune to all sound moves regardless of Bass Boosted
- **Substitute**: Sound moves pierce Substitute, so Bass Boosted still applies
- **Multiple hits**: Each hit of multi-hit sound moves gets the full bonus
- **Critical hits**: Damage multipliers apply before critical hit calculation

### Strategic Implications
- **Offensive powerhouse**: 30% boost makes sound moves extremely powerful
- **Defensive utility**: 50% reduction provides significant bulk against sound attacks
- **Doubles advantage**: Spread damage capability in doubles battles
- **Move priority**: Sound moves with priority (like Boomburst) become devastating
- **Team support**: Protects teammates from opposing sound moves

### Common Users
Bass Boosted appears as an innate ability on:
- **Toxtricity variants**: Electric/Poison types with sound move emphasis
- **Sound-based Pokemon**: Species that specialize in acoustic attacks
- **Doubles specialists**: Pokemon designed for doubles battle formats

### Competitive Usage Notes
- **Hyper Voice spam**: Extremely powerful with STAB and ability boost
- **Boomburst nuke**: One of the strongest spread moves in the game
- **Anti-sound counter**: Provides team protection against sound-based strategies
- **Choice item synergy**: Pairs well with Choice Specs for massive damage
- **Throat Spray**: Activates on sound moves for additional Special Attack boost

### Counters
- **Soundproof**: Complete immunity to all sound moves
- **Mold Breaker variants**: Bypass the defensive component
- **Assault Vest**: Provides special bulk to tank boosted sound moves
- **Sound absorbing abilities**: Abilities that benefit from being hit by sound moves
- **Priority moves**: Non-sound priority moves avoid the defensive benefit

### Synergies
- **Throat Spray**: Boosts Special Attack when using sound moves
- **Choice Specs**: Stacks with ability boost for maximum damage
- **Pixilate/Refrigerate**: Can convert sound moves to different types
- **Helping Hand**: Doubles partner can boost sound move damage further
- **Terrain effects**: Psychic Terrain blocks priority, Electric Terrain boosts Electric sound moves

### Power Calculation Example
Base Hyper Voice (90 BP) with Bass Boosted:
- Base damage: 90 BP
- Bass Boosted boost: 90 x 1.3 = 117 BP effective
- With STAB: 117 x 1.5 = 175.5 BP effective
- With Choice Specs: 175.5 x 1.5 = 263.25 BP effective

### Version History
- **Elite Redux exclusive**: Custom ability combining Amplifier and Punk Rock
- **Innate ability**: Appears on select Pokemon as fixed innate ability
- **Balanced design**: Provides both offensive and defensive utility
- **Doubles focus**: Particularly powerful in doubles battle format

### Lore and Flavor
Bass Boosted represents mastery over sound and acoustic vibrations, allowing the Pokemon to both amplify their own sound-based attacks and dampen incoming sonic assaults. The ability reflects musical themes and audio equipment terminology, fitting for Electric-type Pokemon like Toxtricity variants.