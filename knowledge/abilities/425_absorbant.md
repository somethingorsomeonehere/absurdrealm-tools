---
id: 425
name: Absorbant
status: reviewed
character_count: 168
---

# Absorbant - Ability ID 425

## In-Game Description
"Drain moves recover +50% HP & apply Leech Seed."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Absorbant boosts HP recovery from drain moves by 50% and applies Leech Seed to the target on hit, draining the target for 1/8th of their max HP at the end of each turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Absorbant is a unique ability that enhances drain moves in two ways: it increases HP recovery and applies the Leech Seed status effect to targets hit by drain moves.

### Activation Conditions
- **Move type requirement**: Only activates when using moves with EFFECT_ABSORB or EFFECT_DREAM_EATER
- **Target requirements**: Target must not be Grass-type and must not already have Leech Seed
- **Damage requirement**: The drain move must successfully hit and deal damage

### Drain Move Enhancement
The ability provides a 50% bonus to HP recovery from drain moves:
- **Base drain moves**: Normally recover 50% of damage dealt
- **With Absorbant**: Recover 75% of damage dealt (50% + 25% bonus)
- **High-drain moves**: Some moves already drain 75%, these become 100%+ recovery

### Leech Seed Application
After a successful drain move hit, Absorbant applies Leech Seed to the target:
- **Leech Seed effect**: Target loses 1/8 max HP each turn, healer gains that HP
- **Immunity**: Grass-type Pokemon are immune to Leech Seed
- **Non-stacking**: Won't apply if target already has Leech Seed
- **Duration**: Lasts until the target switches out or faints

### Technical Implementation
```c
constexpr Ability Absorbant = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK_NOT(IS_BATTLER_OF_TYPE(target, TYPE_GRASS))
        CHECK_NOT(gStatuses3[target] & STATUS3_LEECHSEED)
        CHECK(gBattleMoves[move].effect == EFFECT_ABSORB || gBattleMoves[move].effect == EFFECT_DREAM_EATER)

        gStatuses3[target] |= battler;
        gStatuses3[target] |= STATUS3_LEECHSEED;
        BattleScriptCall(BattleScript_AbsorbantActivated);
        return TRUE;
    },
};
```

### Compatible Moves
Moves that trigger Absorbant include:
- **Absorb**: Basic 20 BP drain move
- **Mega Drain**: 40 BP Grass-type drain move
- **Giga Drain**: 75 BP Grass-type drain move
- **Drain Punch**: 75 BP Fighting-type drain move
- **Dream Eater**: 100 BP Psychic-type move (works on sleeping targets)
- **Leech Life**: 80 BP Bug-type drain move
- **Horn Leech**: 75 BP Grass-type physical drain move
- **Draining Kiss**: 50 BP Fairy-type drain move

### Strategic Applications
- **Sustain tank**: Provides excellent HP recovery and gradual damage
- **Stall breaking**: Leech Seed prevents opponent from stalling
- **Setup support**: Forces switches while maintaining HP
- **Wall breaking**: Consistent damage from both move and Leech Seed

### Important Interactions
- **Big Root**: Stacks with Absorbant for even more HP recovery
- **Liquid Ooze**: Opponent's ability can turn drain moves into damage
- **Grass-type immunity**: Cannot seed Grass-types, limiting effectiveness
- **Magic Guard**: Protects from Leech Seed damage but not initial drain move
- **Substitute**: Blocks Leech Seed application but not the drain effect

### Synergies
- **Big Root item**: Further boosts drain move recovery
- **Life Orb**: Increases drain move damage and thus recovery
- **Choice items**: Lock into powerful drain moves for consistent pressure
- **Leftovers**: Stacks with drain recovery for maximum sustain
- **Recovery moves**: Combines with natural healing for incredible bulk

### Counters
- **Grass-types**: Immune to Leech Seed application
- **Magic Bounce**: Reflects Leech Seed back to user
- **Liquid Ooze**: Reverses drain move healing into damage
- **Substitute**: Blocks Leech Seed while taking drain damage
- **Rapid Spin**: Can remove Leech Seed from the user's team

### Competitive Usage
- **Bulky attackers**: Pokemon that can survive long enough to benefit from both effects
- **Pivot Pokemon**: Switch in, seed the opponent, and switch out
- **Stall teams**: Provides consistent damage pressure and healing
- **Anti-setup**: Forces opponents to switch rather than set up

### Common Users
Absorbant works best on Pokemon with:
- **Good bulk**: To survive and make use of the healing
- **Drain move access**: Natural or through TMs
- **Defensive typing**: To switch in safely
- **Support moves**: To capitalize on forced switches

### Version History
- New ability introduced in Elite Redux
- Unique combination of enhanced drain and status application
- Part of the expanded ability roster for diverse strategies
- Designed to make drain moves more viable in competitive play