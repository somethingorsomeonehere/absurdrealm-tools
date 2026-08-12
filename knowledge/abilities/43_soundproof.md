---
id: 43
name: Soundproof
status: reviewed
character_count: 81
---

# Soundproof - Ability ID 43

## In-Game Description
"Immune to sound-based moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants immunity to sound-based moves. Self-targeting sound moves are not blocked.

## Detailed Mechanical Explanation
*For Discord/reference use*

**SOUNDPROOF** is a defensive ability that provides complete immunity to all sound-based moves through the onImmune hook.

### Activation Mechanics:
- **Trigger**: When targeted by any move with the FLAG_SOUND flag
- **Check**: Uses IsSoundMove(attacker, move) function which returns true if:
  - Move has FLAG_SOUND flag, OR
  - Move is Normal-type AND attacker has Reverbate ability
- **Immunity Script**: BattleScript_SoundproofProtected displays "{Pokemon}'s {ability} blocks {move}!"
- **Exception**: Does NOT block sound moves that target the user (MOVE_TARGET_USER)

### Sound Move Categories Blocked:
1. **Damaging Sound Moves**:
   - Boomburst (140 BP Normal)
   - Hyper Voice (90 BP Normal) 
   - Disarming Voice (40 BP Fairy)
   - Bug Buzz (90 BP Bug)
   - Snarl (55 BP Dark)

2. **Status Sound Moves**:
   - Sing (Sleep)
   - Supersonic (Confusion)
   - Screech (Defense -2)
   - Metal Sound (Sp. Def -2)
   - Growl (Attack -1)
   - Roar (Forced switch)

3. **Utility Sound Moves**:
   - Heal Bell (Party status cure)
   - Perish Song (3-turn KO countdown)
   - Uproar (3-turn damage + prevents sleep)

### Technical Implementation:
```c
constexpr Ability Soundproof = {
    .onImmune = +[](ON_IMMUNE) -> int {
        CHECK(IsSoundMove(attacker, move))
        CHECK_NOT(GetBattlerBattleMoveTargetFlags(move, attacker) & MOVE_TARGET_USER) 
        *immunityScript = BattleScript_SoundproofProtected;
        return TRUE;
    },
    .breakable = TRUE,
    .isSoundproof = TRUE,
};
```

### IsSoundMove Function:
```c
int IsSoundMove(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_SOUND) return TRUE;
    if (gBattleMoves[move].type == TYPE_NORMAL && BattlerHasAbility(battler, ABILITY_REVERBATE, FALSE)) return TRUE;
    return FALSE;
}
```

### Ability Interactions:
- **Mold Breaker/Teravolt/Turboblaze**: Can break through Soundproof immunity (.breakable = TRUE)
- **Reverbate**: Normal moves from Reverbate users become sound moves and are blocked
- **Sound-based abilities**: Other abilities that reference IsSoundMove will recognize Soundproof users as immune
- **Related abilities**: Parroting and Noise Cancel also use Soundproof's onImmune function

### Strategic Applications:
1. **Defensive Wall**: Complete immunity to powerful sound moves like Boomburst
2. **Status Protection**: Blocks sleep from Sing, confusion from Supersonic
3. **Team Support**: Immune to Perish Song strategies
4. **Setup Opportunities**: Forces opponents to switch moves, potentially telegraphing their strategy

### Competitive Counters:
- **Mold Breaker users**: Haxorus, Excadrill, Drilbur line can bypass immunity
- **Non-sound moves**: Physical and special attacks without sound flag
- **Indirect damage**: Entry hazards, weather, status conditions
- **Self-targeting moves**: Moves like Substitute that target the user aren't blocked

### Elite Redux Specific Features:
- **isSoundproof flag**: Used by game engine for internal sound move interactions
- **Multiple sound-immune abilities**: Parroting and Noise Cancel share immunity mechanics
- **Extended sound move pool**: Elite Redux likely includes additional sound moves beyond standard Pokemon games

### Version History:
- Introduced in Generation III as complete sound immunity
- Elite Redux: Enhanced with additional sound move interactions and related abilities
- Maintains consistent immunity mechanics across all sound-based effects

### Notable Users:
Typically found on Pokemon with large ears or sound-dampening biology like Whismur line, though Elite Redux may expand this to additional species through the 4-ability system.