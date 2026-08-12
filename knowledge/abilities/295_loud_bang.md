---
id: 295
name: Loud Bang
status: reviewed
character_count: 82
---

# Loud Bang - Ability ID 295

## In-Game Description
"Sound-based moves have 50% chance to confuse the foe."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sound-based attacks have a 50% chance to confuse the target upon a successful hit. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Loud Bang is an offensive ability that activates when the user successfully hits an opponent with a sound-based move, providing a 50% chance to inflict confusion on the target.

### Activation Conditions
The ability triggers when ALL of the following conditions are met:
1. The Pokemon with Loud Bang uses a sound-based move
2. The move successfully hits the opponent
3. The target is not immune to confusion effects
4. A 50% random chance check passes (`Random() % 2`)

### Technical Implementation
```c
constexpr Ability LoudBang = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBeConfused(target))
        CHECK(IsSoundMove(battler, move))
        CHECK(Random() % 2)

        return AbilityStatusEffect(MOVE_EFFECT_CONFUSION);
    },
};
```

### Sound Move Detection
A move is considered a sound move if:
- It has the `FLAG_SOUND` flag in its move data, OR
- It's a Normal-type move and the user has the Reverberate ability

### Complete List of Affected Moves
Common sound moves that trigger Loud Bang include:
- **Growl** - Lowers Attack, Special attack with 60 power
- **Roar** - Forces target to switch out
- **Sing** - Puts target to sleep
- **Supersonic** - Confuses target
- **Screech** - Lowers Defense
- **Hyper Voice** - 90 power Normal-type attack
- **Perish Song** - Causes both Pokemon to faint in 3 turns
- **Heal Bell** - Cures status conditions
- **Uproar** - 90 power attack that prevents sleep for 3 turns
- **Metal Sound** - Lowers Special Defense
- **Howl** - Raises Attack
- **Bug Buzz** - 90 power Bug-type attack with 10% chance to lower Special Defense
- **Chatter** - 65 power Flying-type attack with 100% confusion chance
- **Round** - 60 power Normal-type attack that doubles if ally uses it
- **Echoed Voice** - Increases power each consecutive turn
- **Relic Song** - Meloetta's signature move
- **Boomburst** - 140 power Normal-type attack hitting all nearby Pokemon
- **Parting Shot** - Lowers Attack and Special Attack, then switches out
- **Sparkling Aria** - 90 power Water-type attack that cures burns
- **Clanging Scales** - 110 power Dragon-type attack that lowers Defense
- **Clangorous Soul** - Lowers HP to boost all stats
- **And many custom moves added in Elite Redux**

### Interactions with Other Abilities/Mechanics
- **Soundproof**: Pokemon with Soundproof are immune to sound moves, so Loud Bang cannot affect them
- **Own Tempo**: Pokemon with Own Tempo cannot be confused, blocking Loud Bang's effect
- **Mental Herb**: Cures confusion immediately, negating the effect
- **Substitute**: Sound moves bypass Substitute, so Loud Bang can still trigger
- **Throat Chop**: If the user is affected by Throat Chop, they cannot use sound moves for 2 turns
- **Multi-hit moves**: Each hit has a separate 50% chance to confuse if it's a sound move

### Strategic Implications
- **Offensive Utility**: Provides additional disruption potential to sound-based attackers
- **Move Selection**: Encourages use of sound moves even if they're not the most powerful option
- **Team Building**: Pairs well with Pokemon that learn multiple sound moves
- **Disruption Factor**: Can turn utility moves like Growl into potential confusion setters

### Example Damage Calculations
Loud Bang itself doesn't affect damage calculations, but the confusion it causes can:
- Confused Pokemon have a 33% chance to hurt themselves instead of attacking
- Self-damage from confusion is calculated as a 40 power typeless physical attack against the user's own Defense stat

### Common Users
In Elite Redux, Loud Bang is typically found on:
- Sound-themed Pokemon (Exploud line, Chatot, etc.)
- Pokemon with strong sound move coverage
- Support Pokemon that use sound-based utility moves

### Competitive Usage Notes
- **Disruption Tool**: Excellent for disrupting opposing sweepers and setup Pokemon
- **Utility Enhancement**: Makes normally weak sound moves like Growl potentially game-changing
- **Stacking Effects**: Can combine with other confusion-inducing moves for consistent disruption
- **Counter-Setup**: Particularly effective against Pokemon trying to set up with stat-boosting moves

### Counters
- **Soundproof**: Complete immunity to sound moves prevents activation
- **Own Tempo**: Immunity to confusion effects
- **Mental Herb/Persim Berry**: Immediate confusion cure
- **Substitute**: While sound moves bypass Substitute, some strategies can still work around it
- **Taunt**: Prevents use of status sound moves

### Synergies
- **Throat Spray**: Boosts Special Attack when using sound moves, creating offensive pressure
- **Amplifier/Bass Boosted**: Other abilities that enhance sound moves
- **Choice items**: Lock into powerful sound moves for consistent confusion chances
- **Wide Lens**: Increases accuracy of sound moves to ensure they connect

### Version History
- Added in Elite Redux as part of the expanded ability system
- Part of the 295+ ability range for custom Elite Redux abilities
- Designed to provide utility to sound-based movesets and Pokemon