---
id: 521
name: Phantom Thief
status: reviewed
character_count: 249
---

# Phantom Thief - Ability ID 521

## In-Game Description
"Attacks with 40BP Spectral Thief on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses a 40 BP Spectral Thief (a Ghost-type move) when switching in, targeting the opponent across from the user. Steals all positive stat boosts (before dealing damage) from the target and applies them to the user. Cannot miss and ignores Substitute.  

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Phantom Thief is an aggressive entry ability that automatically uses a modified version of Spectral Thief when the Pokemon switches into battle, forcing immediate offensive pressure and stat theft.

### Activation Conditions
- **Trigger**: Activates immediately upon switching into battle
- **Target selection**: Targets a random opponent in battle
- **Move properties**: Uses Spectral Thief with 40 BP instead of normal 90 BP
- **Type**: Ghost-type physical attack
- **Accuracy**: Cannot miss (ability-triggered moves bypass accuracy)

### Technical Implementation
```c
constexpr Ability PhantomThief = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_SPECTRAL_THIEF, 40); 
    },
};
```

The ability uses the `UseEntryMove` function to execute Spectral Thief with reduced power on switch-in.

### Spectral Thief Mechanics
Based on the move's implementation:
- **Stat stealing**: Takes all positive stat boosts (+1 to +6) from the target
- **Stat application**: Applies stolen boosts to the user, up to +6 maximum
- **Stat reset**: Target's boosted stats are reset to neutral (0)
- **Contact move**: Makes contact for abilities like Static, Flame Body
- **Affected stats**: Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, Evasion

### Important Interactions
- **STAB bonus**: Ghost-type users get 1.5x damage (40 BP becomes 60 effective BP)
- **Substitute piercing**: Spectral Thief bypasses Substitute to steal stats
- **Multi-target**: In doubles, targets one random opponent
- **Priority**: No priority; uses standard switch-in timing
- **Damage calculation**: Uses user's Attack stat and target's Defense stat

### Strategic Implications
- **Setup punisher**: Punishes opponents who try to set up stat boosts
- **Immediate pressure**: Forces damage and disruption on switch-in
- **Momentum swing**: Can steal crucial stat boosts and turn them against opponent
- **Entry hazard synergy**: Combines with hazard damage for KO potential
- **Mind games**: Opponents must consider stat boost timing carefully

### Defensive Counterplay
- **Ghost immunity**: Normal and Fighting types immune to the Ghost-type attack
- **Protect/Detect**: Can block the entry move if predicted
- **Intimidate**: Can reduce the incoming damage by lowering Attack
- **Rocky Helmet**: Deals contact damage back to the user
- **Rough Skin/Iron Barbs**: Punishes the contact move

### Common Users
Based on the ability ID (521), this is likely found on:
- Ghost-type Pokemon with thieving/sneaky themes
- Pokemon with high Attack stats to maximize damage
- Fast Pokemon who can capitalize on stolen Speed boosts
- Pokemon designed to disrupt setup strategies

### Competitive Usage Notes
- **Setup counter**: Excellent against setup sweepers and calm mind users
- **Pivot tool**: Can steal stats then pivot out with U-turn/Volt Switch
- **Early game pressure**: Creates immediate threats when switching in
- **Double battles**: Random targeting can disrupt opponent's strategy
- **Risk/reward**: Exposes user to retaliation but gains stolen stats

### Synergies
- **Choice items**: Can immediately use stolen stats with locked moves
- **Life Orb**: Boosts the entry move damage significantly
- **Entry hazards**: Combines damage for potential KOs
- **Pivot moves**: Steal stats then switch out to preserve them
- **Priority moves**: Use stolen Speed to outspeed and attack

### Counters
- **Ghost immunity**: Normal/Fighting types completely avoid the effect
- **Protective moves**: Protect, Detect, Spiky Shield block the move
- **Clear Body/White Smoke**: Prevents stat theft (target keeps boosts)
- **Hyper Cutter**: Protects Attack stat from being stolen
- **Contact punishment**: Abilities that punish contact moves

### Version History
- Elite Redux custom ability (ID 521)
- Part of the expanded ability roster beyond Generation VIII
- Uses existing Spectral Thief mechanics with entry trigger
- Reduced power balances the automatic activation

### Technical Notes
- Uses MOVE_SPECTRAL_THIEF (ID 666) with modified 40 BP
- Triggers through onEntry ability hook
- Benefits from all normal move mechanics (STAB, items, etc.)
- Subject to normal battle mechanics and type effectiveness