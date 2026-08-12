---
id: 388
name: Thundercall
status: reviewed
character_count: 271
---

# Thundercall - Ability ID 388

## In-Game Description
"Triggers Smite at 20% power when using an Electric move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After using any Electric-type move, Thundercall automatically triggers a follow-up Smite attack at 20% power (24 base power). This physical Electric attack has an 80% accuracy, can paralyze targets (20% chance), and applies the Smack Down effect - grounding Flying-types.

## Detailed Mechanical Explanation

## Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 4011-4018

### Implementation Details
```cpp
constexpr Ability Thundercall = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(moveType == TYPE_ELECTRIC)
        CHECK(AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_STANDARD))

        return UseAttackerFollowUpMove(battler, target, ability, MOVE_SMITE, .2 * gBattleMoves[MOVE_SMITE].power);
    },
};
```

### Trigger Conditions
1. User must use an Electric-type move
2. The Electric move must successfully hit the target
3. Target must be within range for the follow-up attack

### Follow-up Move: Smite
- **Base Power**: 120 (reduced to 24 via Thundercall's 20% modifier)
- **Type**: Electric
- **Accuracy**: 80%
- **PP**: 15
- **Split**: Physical
- **Effect**: Smack Down (removes Flying-type and Levitate)
- **Secondary Effect**: 20% paralysis chance
- **Description**: "Attacks from above with strong electricity. 20% paralysis chance. Smack Down effect."

## Strategic Analysis

### Competitive Tier: Medium
Thundercall provides consistent additional damage and utility but faces several limitations that prevent it from reaching higher tiers.

### Strengths
1. **Guaranteed Damage**: Every successful Electric move triggers additional damage
2. **Multi-Hit Utility**: Provides Smack Down effect, grounding Flying-types and Levitate users
3. **Status Pressure**: 20% paralysis chance adds status pressure
4. **Type Synergy**: Works with any Electric move, creating combo potential
5. **Physical Damage**: The follow-up is physical, allowing mixed attackers to benefit

### Weaknesses
1. **Low Power**: 24 effective power (20% of 120) is relatively modest
2. **Accuracy Issues**: 80% accuracy means the follow-up can miss
3. **Type Dependency**: Only works with Electric moves
4. **Predictable**: Opponents can anticipate the follow-up
5. **No Piercing**: Follow-up can be blocked by abilities like Wonder Guard

### Optimal Usage
- **Mixed Attackers**: Pokemon with both physical and special Electric moves
- **Electric Specialists**: Pokemon with diverse Electric movesets
- **Anti-Flying**: Effective against Flying-types and Levitate users
- **Status Support**: Works well with paralysis-based strategies

## Notable Users

### Primary Users (Innate Ability)
1. **Dragonite Mega** (Dragon/Electric)
   - High Attack stat makes the physical follow-up more effective
   - Dragon typing adds coverage options
   - Access to diverse Electric moves

2. **Pikachu Partner Mega** (Electric)
   - Pure Electric type maximizes ability synergy  
   - High Special Attack for initial Electric moves
   - Access to signature Electric moves

3. **Thundurus** (Electric/Flying)
   - Legendary stats provide strong foundation
   - Flying typing creates interesting dynamics with Smack Down
   - Excellent movepool diversity

## Competitive Applications

### Team Roles
- **Wallbreaker**: Consistent extra damage helps break through defensive walls
- **Flying Counter**: Smack Down effect neutralizes Flying-type advantages
- **Status Spreader**: Paralysis chance supports team's speed control

### Synergistic Partners
- **Electric Terrain Setters**: Boost initial Electric move power
- **Paralysis Abusers**: Pokemon that benefit from opponent paralysis
- **Ground-type Attackers**: Benefit from Smack Down grounding opponents

### Counterplay
- **Ground Types**: Immune to both Electric moves and the Electric follow-up
- **Lightning Rod/Volt Absorb**: Redirect or absorb the follow-up
- **Priority Moves**: Can interrupt before follow-up triggers
- **Substitute**: Blocks the follow-up attack

## Comparison to Related Abilities

### Similar Abilities
- **Galvanize**: Converts Normal moves to Electric (more consistent type conversion)
- **Volt Absorb**: Provides healing from Electric moves (defensive alternative)
- **Motor Drive**: Speed boost from Electric moves (utility alternative)

### Unique Aspects
- Only ability that provides Electric follow-up attacks
- Combines damage, status, and utility (Smack Down) in one package
- Creates interesting risk/reward dynamics with accuracy

## Battle Scenarios

### Scenario 1: Anti-Flying
User with Thundercall uses Thunderbolt against a Flying-type:
1. Thunderbolt deals standard damage and potential paralysis
2. Smite follow-up (24 power) hits, applying Smack Down
3. Flying-type loses Flying properties and Levitate immunity
4. Ground moves now affect the previously Flying target

### Scenario 2: Status Pressure
Against a fast opponent:
1. Electric move provides initial damage
2. Smite follow-up has 20% paralysis chance
3. If paralysis triggers, opponent's speed is quartered
4. Creates momentum shift in user's favor


## Conclusion

Thundercall occupies a unique niche as the only ability providing consistent Electric follow-up attacks. While not overwhelmingly powerful, it offers reliable additional damage, utility through Smack Down, and status pressure through paralysis. The ability works best on Pokemon with diverse Electric movepools and sufficient offensive stats to make both the initial move and follow-up meaningful.

The Medium competitive tier reflects its solid utility balanced against limitations like low follow-up power and accuracy issues. In the right hands and team composition, Thundercall can provide valuable consistent pressure and utility effects.