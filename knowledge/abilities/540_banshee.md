---
id: 540
name: Banshee
status: reviewed
character_count: 100
---

# Banshee - Ability ID 540

## In-Game Description
"Sound moves get a 1.2x boost and become Ghost if Normal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of all sound-based moves by 20% and converts Normal-type sound moves to Ghost-type. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Banshee provides two distinct effects for sound-based moves:
1. **Damage Boost**: All moves with the `FLAG_SOUND` flag receive a 1.2x (20%) damage multiplier
2. **Type Conversion**: Normal-type sound moves are converted to Ghost-type before damage calculation

### Activation Conditions
- The ability activates when the user uses any move flagged with `FLAG_SOUND`
- Both effects apply simultaneously if conditions are met
- Type conversion only affects Normal-type moves; other types remain unchanged
- The damage boost applies to all sound moves regardless of original type

### Technical Implementation
```cpp
constexpr Ability Banshee = {
    .onOffensiveMultiplier = LiquidVoice.onOffensiveMultiplier,  // 1.2x boost for sound moves
    .onMoveType = +[](ON_MOVE_TYPE) -> int {
        CHECK(moveType == TYPE_NORMAL)              // Only affects Normal-type moves
        CHECK(gBattleMoves[move].flags & FLAG_SOUND); // Must be a sound move
        return TYPE_GHOST + 1;                      // Convert to Ghost-type
    },
};
```

### Complete List of Affected Sound Moves
**Status Moves:**
- Growl, Roar, Sing, Supersonic, Screech, Heal Bell, Metal Sound, Grass Whistle, Perish Song

**Damaging Moves:**
- Sonic Boom, Snore, Uproar, Hyper Voice, Bug Buzz, Chatter, Round, Echoed Voice, Relic Song, Snarl, Noble Roar, Boomburst, Parting Shot

**Normal-type Sound Moves (gain Ghost typing):**
- Growl, Roar, Sing, Supersonic, Screech, Sonic Boom, Snore, Uproar, Hyper Voice, Chatter, Round, Echoed Voice, Noble Roar, Boomburst

### Interactions with Other Abilities/Mechanics
- **Soundproof**: Completely blocks Banshee's sound moves, negating both damage boost and type conversion
- **Normalize**: If a Pokemon with both abilities uses a sound move, Normalize converts it to Normal first, then Banshee converts it to Ghost
- **STAB (Same Type Attack Bonus)**: Ghost-type Pokemon gain 1.5x STAB on converted moves, stacking multiplicatively with Banshee's 1.2x boost (total 1.8x)
- **Punk Rock**: If paired with Punk Rock (via ability modification), effects would stack for even greater sound move power
- **Throat Chop**: Pokemon affected by Throat Chop cannot use sound moves, preventing Banshee activation

### Strategic Implications
**Offensive Applications:**
- Transforms typically weak Normal-type sound moves into powerful Ghost-type attacks
- Provides consistent 20% damage boost to already-powerful sound moves like Boomburst
- Ghost typing offers excellent neutral coverage and hits Psychic/Ghost types super-effectively
- Allows Normal-type Pokemon to hit Normal and Fighting types for neutral damage instead of resisted

**Defensive Considerations:**
- Ghost-type moves cannot hit Normal-type Pokemon, potentially reducing move effectiveness
- Sound moves are blocked by Soundproof ability users
- Doesn't provide any defensive benefits unlike other signature abilities

### Example Damage Calculations
**Boomburst (Base Power 140, Normal to Ghost conversion + 1.2x boost):**
- Without Banshee: 140 BP Normal-type move
- With Banshee: 140 x 1.2 = 168 effective BP Ghost-type move
- With STAB (Ghost-type user): 168 x 1.5 = 252 effective BP
- Compared to Boomburst on non-Ghost type: 140 x 1.5 = 210 BP (if same type)

**Hyper Voice calculation example:**
- Base: 90 BP Normal-type
- With Banshee: 90 x 1.2 = 108 effective BP Ghost-type
- Super-effective vs Psychic: 108 x 2 = 216 effective BP

### Common Users
- **Toxtricity Redux Fuzz**: Primary user of this ability in Elite Redux
- Sound-based Ghost-type Pokemon that might receive this ability
- Pokemon with diverse sound move pools benefit most from the type conversion utility

### Competitive Usage Notes
**Strengths:**
- Significant power boost to already-strong sound moves
- Type conversion provides coverage options
- Consistent damage boost unlike situational abilities
- Works well in sound-move focused team compositions

**Weaknesses:**
- Completely shut down by Soundproof
- Ghost typing cannot hit Normal types (coverage loss)
- No defensive utility
- Limited to sound moves only

### Counters
- **Soundproof users**: Completely immune to all Banshee-boosted attacks
- **Normal-type Pokemon**: Immune to converted Ghost-type sound moves
- **Throat Chop**: Prevents use of sound moves for two turns
- **Sound-move absorbing abilities**: Any hypothetical sound-absorbing abilities would counter this strategy

### Synergies
- **Choice Specs/Choice Band**: Stacks multiplicatively with damage boost
- **Life Orb**: Additional damage boost with recoil trade-off
- **Ghost-type STAB**: Natural synergy for converted moves
- **Sound move tutors**: Access to diverse sound move pools maximizes utility
- **Throat Spray**: Activates on sound move use, boosting Special Attack

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Part of the signature abilities for certain Pokemon forms
- Based on the Liquid Voice template but with Ghost-type conversion instead of Water-type