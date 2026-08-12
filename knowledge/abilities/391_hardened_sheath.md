---
id: 391
name: Hardened Sheath
status: reviewed
character_count: 77
---

# Hardened Sheath - Ability ID 391

## In-Game Description
"Ups Attack by +1 when using horn moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Every successful horn-based attack raises Attack by one stage after it lands.

## Detailed Mechanical Explanation

## Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 4035-4045
- **Function**: `HardenedSheath`

### Implementation Details
```cpp
constexpr Ability HardenedSheath = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(gBattleMoves[move].hornBased)
        CHECK(ChangeStatBuffs(battler, 1, STAT_ATK, MOVE_EFFECT_AFFECTS_USER, NULL))

        BattleScriptCall(BattleScript_AttackBoostActivates);
        gBattleScripting.battler = battler;
        return TRUE;
    },
};
```

### Trigger Conditions
1. **ShouldApplyOnHitAffect**: Confirms the move successfully hit the target
2. **gBattleMoves[move].hornBased**: Verifies the move has the `hornBased` flag set to TRUE
3. **ChangeStatBuffs**: Attempts to raise Attack by +1 stage (fails if already at +6)

## Horn-Based Moves

### Confirmed Horn-Based Moves
Based on analysis of `/Users/joel/Github/eliteredux/eliteredux-source/include/generated/data/battle_moves.h`, the following moves trigger Hardened Sheath:

#### Physical Contact Moves
- **Horn Attack** - Basic horn strike
- **Fury Attack** - Multi-hit horn attack
- **Horn Drill** - One-hit KO move
- **Drill Peck** - High critical hit ratio
- **Submission** - High damage with recoil
- **Zen Headbutt** - Physical psychic headbutt
- **Dual Chop** - Dragon-type contact move
- **Sacred Sword** - Ignores stat stages
- **Tectonic Fangs** - Causes bleeding effect
- **Ceaseless Edge** - Sets hazards
- **Beatdown** - High damage move
- **Icicle Impale** - Ice-type piercing move
- **Toxic Plunge** - Poison-type contact move
- **Depletion Beam** - Energy draining move
- **Oni Fist** - Fighting-type punch move

#### Special Moves
- **Drill Run** - Ground-type special move
- **Shocking Edge** - Electric-type special move

#### Custom Elite Redux Moves
Many Elite Redux custom moves also have the `hornBased` flag, expanding the pool of compatible moves significantly.

## Strategic Analysis

### Strengths
1. **Snowball Potential**: Each successful horn move increases Attack, creating powerful momentum
2. **Move Variety**: Works with both physical and special horn-based moves
3. **Stacking Effect**: Can reach +6 Attack with repeated use
4. **No Drawbacks**: Pure offensive boost with no negative side effects

### Weaknesses
1. **Move Dependency**: Only works with horn-based moves, limiting moveset flexibility
2. **Hit Dependency**: Requires moves to successfully hit to activate
3. **Limited Move Pool**: Not all Pokemon with this ability may have access to multiple horn moves
4. **Accuracy Issues**: Some horn moves have lower accuracy, making consistent activation challenging

### Competitive Applications

#### Setup Sweeper Role
- Use bulky Pokemon with horn moves to set up Attack boosts
- Pair with moves like Substitute or defensive capabilities
- Create win conditions through accumulated Attack boosts

#### Revenge Killer Enhancement
- Transform revenge killers into late-game threats
- Use after opponent's key Pokemon are weakened
- Capitalize on horn move priority or speed

#### Team Support
- Baton Pass strategies to transfer Attack boosts
- U-turn/Volt Switch to maintain momentum while preserving boosts
- Entry hazard support to guarantee KOs at higher Attack stages

## Related Abilities

### Similar Mechanics
- **Moxie** (#153): Raises Attack when knocking out opponents
- **Beast Boost** (#224): Raises highest stat when knocking out opponents
- **Defiant** (#128): Raises Attack when stats are lowered

### Synergistic Abilities
- **Sheer Force** (#125): Removes secondary effects but increases power
- **Iron Fist** (#89): Boosts punch-based moves (some overlap with horn moves)
- **Reckless** (#120): Increases power of recoil moves

### Counterplay Abilities
- **Intimidate** (#22): Lowers Attack upon switching in
- **Clear Body** (#29): Prevents stat reduction
- **Unaware** (#109): Ignores stat changes when calculating damage

## Pokemon Distribution

### Potential Users
Based on the horn-based theme, this ability would be most fitting on:
- **Rhyhorn/Rhydon/Rhyperior**: Natural horn users
- **Tauros**: Bull with prominent horns
- **Heracross**: Beetle with horn-like protrusions
- **Nidoking/Nidoqueen**: Poisonous horn users
- **Seaking**: Aquatic horn user
- **Goldeen**: Horn-based fish Pokemon

## Competitive Viability

### Tier Assessment: Medium
- **Pros**: Reliable setup mechanism, good move variety, no activation cost
- **Cons**: Move restriction, hit dependency, gradual setup required
- **Best Use Cases**: Bulky setup sweepers, late-game cleaners, Baton Pass teams

### Format Considerations
- **Single Battles**: Good for setup sweepers and late-game threats
- **Double Battles**: More challenging due to target selection and faster pace
- **Battle Facilities**: Excellent for long battles where setup is viable


## Conclusion

Hardened Sheath represents a solid offensive enhancement ability that rewards consistent use of horn-based moves. While it requires specific move selection and successful hits to activate, the ability to stack Attack boosts makes it a threatening late-game tool. The variety of horn-based moves available provides some flexibility in team building, though users must balance offensive potential with the need for reliable hit rates.

The ability shines best on bulky Pokemon that can survive long enough to accumulate multiple boosts, or on fast Pokemon that can quickly capitalize on early boosts. Its medium competitive tier reflects its usefulness without being overwhelming, making it a strategic choice for players who enjoy setup-based playstyles.