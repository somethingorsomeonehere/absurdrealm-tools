---
id: 397
name: Pyro Shells
status: reviewed
character_count: 168
---

# Pyro Shells - Ability ID 397

## In-Game Description
"Triggers 50 BP Outburst after using Mega Launcher moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Pyro Shells triggers a 50 BP Normal-type Outburst after any Mega Launcher-boosted move. Outburst has no secondary effects and hits all surrounding Pokemon on the field.

## Detailed Mechanical Explanation

## Detailed Mechanics

### Implementation Details
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (Lines 4095-4102)

```cpp
constexpr Ability PyroShells = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(IsMegaLauncherBoosted(battler, move))
        CHECK(AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_STANDARD))

        return UseAttackerFollowUpMove(battler, target, ability, MOVE_OUTBURST, 50);
    },
};
```

### Triggering Conditions
The ability activates when:
1. The user executes any move with the `mega_launcher: true` flag
2. The move successfully targets an opponent
3. Standard follow-up targeting conditions are met

### Mega Launcher-Boosted Moves
Pyro Shells triggers on any move that benefits from Mega Launcher (1.3x power boost), including but not limited to:

**Notable Trigger Moves**:
- **Water Pulse** - High PP, reliable trigger
- **Aura Sphere** - Always hits, Fighting-type coverage
- **Dark Pulse** - 20% flinch chance
- **Dragon Pulse** - Strong Dragon-type option
- **Heal Pulse** - Even status moves trigger the effect
- **Origin Pulse** - Powerful signature move
- **Techno Blast** - Variable typing based on Drive
- **Zap Cannon** - 120 BP with guaranteed paralysis
- **Hyper Beam** - 150 BP with recharge

### Follow-up Move: Outburst
**Move Data**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/MoveList.textproto` (Lines 12488-12502)

- **Base Power**: 250 (reduced to 50 by ability)
- **Type**: Normal
- **Effect**: EFFECT_EXPLOSION (user faints)
- **Target**: FOES_AND_ALLY
- **Accuracy**: 100%
- **PP**: 5
- **Description**: "The user explodes to inflict terrible damage even while fainting itself."

**Critical Note**: When triggered by Pyro Shells, Outburst does NOT cause the user to faint - only the follow-up damage is applied.

## Strategic Applications

### Offensive Utility
- **Double Damage**: Every Mega Launcher move becomes a two-hit combo
- **Coverage Enhancement**: Normal-type follow-up provides neutral coverage
- **Bulky Breaker**: 50 additional BP helps break through defensive walls
- **Chip Damage**: Consistent extra damage accumulates over time

### Combo Potential
1. **Water Pulse to Outburst**: Reliable combo with confusion chance
2. **Aura Sphere to Outburst**: Never-miss Fighting + Normal coverage
3. **Zap Cannon to Outburst**: Paralysis setup with guaranteed follow-up
4. **Dark Pulse to Outburst**: Flinch chance with immediate punishment

### Competitive Advantages
- **Pseudo-Parental Bond**: Similar to the banned ability but type-restricted
- **Move Diversity**: Works with both physical and special Mega Launcher moves
- **Status Integration**: Even status moves like Heal Pulse trigger the effect
- **Type Coverage**: Normal follow-up hits most types neutrally

## Pokemon with Pyro Shells

### Primary Users
1. **Magmortar** - Third ability slot
   - **Stats**: 75/95/67/125/95/83 (BST: 540)
   - **Typing**: Fire
   - **Role**: Special attacker with beam move focus
   - **Innates**: Molten Down, Dual Wield, Flash Fire

2. **Mega Toucannon** - Third innate ability
   - **Stats**: Enhanced from base Toucannon
   - **Typing**: Normal/Flying
   - **Role**: Mixed attacker with projectile moves
   - **Other Innates**: Steel Barrel, Iron Barrage

### Optimal Movesets
**Magmortar Example**:
- **Core Moves**: Fire Blast, Aura Sphere, Thunderbolt, Focus Blast
- **Mega Launcher Triggers**: Aura Sphere (Fighting coverage + guaranteed hit)
- **Coverage**: Thunder/Thunderbolt for Water-types
- **Utility**: Taunt or Substitute for setup prevention

## Related Abilities

### Similar Follow-up Mechanics
- **Volcano Rage (#382)**: Fire moves to 50 BP Eruption
- **Thundercall (#388)**: Electric moves to 20% power Smite
- **High Tide (#503)**: Water moves to 50 BP Surf
- **Frost Burn (#475)**: Fire moves to 40 BP Ice Beam
- **Aftershock (#491)**: Any powered move to 65 BP Magnitude

### Key Differences
- **Type Restriction**: Only works with Mega Launcher moves
- **Consistent Power**: Always 50 BP regardless of trigger
- **Wide Move Pool**: Large variety of triggering moves
- **No Type Requirement**: Unlike elemental follow-ups

## Competitive Analysis

### Strengths
1. **Damage Output**: Significant DPS increase on Mega Launcher users
2. **Move Flexibility**: Works with diverse move types and categories
3. **Reliable Activation**: Many common moves trigger the effect
4. **Breaking Point**: Helps overcome defensive thresholds

### Weaknesses
1. **Move Pool Dependency**: Requires access to Mega Launcher moves
2. **Predictable Pattern**: Opponents can anticipate the follow-up
3. **Type Limitation**: Only Normal-type follow-up damage
4. **No Immunity Bypass**: Can be blocked by Ghost-types or abilities

### Tier Justification: Medium
- **Pros**: Consistent damage boost, works with common moves, good coverage
- **Cons**: Restricted move pool, predictable pattern, no special mechanics
- **Verdict**: Strong ability for beam/pulse-focused attackers but not game-breaking

## Battle Applications

### Team Synergy
- **Choice Item Users**: Locked moves become more threatening
- **Wallbreakers**: Extra damage helps overcome bulky threats
- **Coverage Pokemon**: Diverse Mega Launcher moves provide type flexibility
- **Setup Sweepers**: More immediate pressure even before boosts

### Counters and Limitations
- **Ghost-types**: Immune to Normal-type follow-up damage
- **High Defense**: Bulky physical walls can tank the extra 50 BP
- **Priority Moves**: Can interrupt before follow-up resolves
- **Ability Suppression**: Neutralizing Gas disables the effect


## Conclusion

Pyro Shells is a solid offensive ability that enhances Pokemon focused on beam and pulse attacks. While not as versatile as unrestricted follow-up abilities, its synergy with the diverse Mega Launcher move pool makes it a reliable damage amplifier. The ability shines on special attackers like Magmortar who naturally learn multiple triggering moves, effectively giving them a pseudo-Parental Bond effect for their signature attack style.

The 50 BP follow-up provides meaningful damage without being overpowered, making Pyro Shells a well-balanced ability that rewards strategic movepool construction and type coverage planning.