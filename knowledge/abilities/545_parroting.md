---
id: 545
name: Parroting
status: reviewed
character_count: 160
---

# Parroting - Ability ID 545

## In-Game Description
"Copies sound moves used by others. Immune to sound."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When any Pokemon on the field uses a sound move, this Pokemon immediately uses the same move after. Triggers once per move. Also grants immunity to sound moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Parroting combines two distinct abilities:
1. **Sound Immunity** - Complete immunity to all sound-based moves
2. **Sound Move Copying** - Automatically copies and uses sound moves used by opponents

### Activation Conditions
- **Sound Immunity**: Triggers when targeted by any move with the `FLAG_SOUND` flag
- **Sound Move Copying**: Triggers when any battler uses a sound move during battle

### Implementation Details
```cpp
constexpr Ability Parroting = {
    .onImmune = Soundproof.onImmune,
    .onCopyMove = +[](ON_COPY_MOVE) -> int {
        CHECK(IsSoundMove(attacker, move))
        return UseOutOfTurnAttack(battler, target, ability, move, 0);
    },
    .breakable = TRUE,
    .isSoundproof = TRUE,
};
```

### Sound Move Detection
Sound moves are identified by the `IsSoundMove` function:
```cpp
int IsSoundMove(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_SOUND) return TRUE;
    if (gBattleMoves[move].type == TYPE_NORMAL && BattlerHasAbility(battler, ABILITY_REVERBATE, FALSE)) return TRUE;
    return FALSE;
}
```

### Complete List of Affected Sound Moves
- **Growl** - Attack-lowering roar
- **Roar** - Forced switching move
- **Sing** - Sleep-inducing lullaby
- **Supersonic** - Confusion-causing sound
- **Screech** - Defense-lowering screech
- **Perish Song** - Fainting countdown
- **Heal Bell** - Status cure sound
- **Uproar** - Multi-turn rampage move
- **Hyper Voice** - High-power Normal attack
- **Round** - Doubled power if ally uses same move
- **Echoed Voice** - Power increases with repeated use
- **Boomburst** - Extremely powerful sound attack
- **And many more moves with FLAG_SOUND**

### Timing and Execution
- **Immediate Response**: Copied moves are executed using `UseOutOfTurnAttack`, triggering immediately after the original move
- **No Turn Consumption**: The copied move doesn't use the Pokemon's turn
- **Original Power**: Copied moves maintain their original power and effects
- **Same Target**: The copied move targets the same Pokemon that used the original sound move

### Restrictions and Limitations
- **Status Conditions**: Cannot copy moves if the Pokemon is asleep or frozen
- **Dancer Prevention**: Cannot trigger if the Pokemon already used a Dancer-type move this turn
- **Breakable**: This ability can be suppressed by moves like Gastro Acid or abilities like Neutralizing Gas
- **Alive Requirement**: Must be alive to copy moves (except for specific abilities like Victory Bomb)

### Interactions with Other Abilities
- **Soundproof Synergy**: Shares the same immunity function as Soundproof
- **Liquid Voice**: Can copy Normal-type moves converted to Water-type by Liquid Voice
- **Punk Rock**: Can copy boosted sound moves from Punk Rock users
- **Reverbate**: Can copy Normal-type moves that become sound moves via Reverbate

### Strategic Implications
- **Defensive Wall**: Immune to popular sound moves like Boomburst and Hyper Voice
- **Offensive Counter**: Turns enemy sound moves into immediate counterattacks
- **Team Support**: Can copy beneficial sound moves like Heal Bell for team support
- **Versatile Coverage**: Gains access to diverse move types through copying

### Example Scenarios
1. **Enemy uses Boomburst**: Parroting Pokemon is immune and immediately retaliates with Boomburst
2. **Ally uses Heal Bell**: Parroting Pokemon copies Heal Bell, providing additional team healing
3. **Multi-target Round**: Can copy Round for potential power doubling effects

### Common Users
Parroting is typically found on:
- Sound-based Pokemon that need immunity to their own type of moves
- Support Pokemon that can benefit from copying beneficial sound moves
- Defensive Pokemon that want to counter sound-based attackers

### Competitive Usage Notes
- **Sound Meta Counter**: Excellent against teams relying on sound moves
- **Unpredictable**: Forces opponents to reconsider using sound moves
- **Support Potential**: Can copy beneficial sound moves for team advantage
- **Niche Pick**: Situational but powerful in sound-heavy metagames

### Counters
- **Non-sound Moves**: Use physical or special moves without sound flags
- **Gastro Acid**: Suppresses the ability entirely
- **Neutralizing Gas**: Prevents ability activation
- **Priority Moves**: Fast moves that don't rely on sound

### Synergies
- **Soundproof Partners**: Team with other sound-immune Pokemon
- **Sound Move Users**: Allies that can provide beneficial sound moves to copy
- **Status Support**: Pairs well with Pokemon that can heal or support

### Version History
- **Elite Redux**: Custom ability combining Soundproof immunity with Dancer-like copying mechanics
- **Unique Implementation**: Uses the `onCopyMove` callback system for immediate retaliation