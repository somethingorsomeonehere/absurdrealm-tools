---
id: 438
name: Jaws of Carnage
status: reviewed
character_count: 143
---

# Jaws of Carnage - Ability ID 438

## In-Game Description
"Devours 1/2 of the foe when defeating it."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Restores 50% max HP when defeating foes with biting moves or 25% with other moves. Only activates when knocking out a target with a direct hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Jaws of Carnage is a recovery ability that triggers when the Pokemon defeats an opponent, providing different healing amounts based on the move used to secure the knockout.

### Activation Conditions
- **KO requirement**: Must defeat an opponent to trigger
- **HP requirement**: Only activates when the user is not at maximum HP
- **Healing capability**: Must be able to heal (no Heal Block, etc.)
- **Move dependence**: Healing amount varies by move type

### Healing Mechanics
- **Biting moves (50% healing)**: When the finishing move has FLAG_STRONG_JAW_BOOST
  - Examples: Bite, Crunch, Thunder Fang, Ice Fang, Fire Fang, Poison Fang
  - Calls BattleScript_HandleJawsOfCarnageEffect (50% max HP)
- **Other moves (25% healing)**: When finishing move lacks FLAG_STRONG_JAW_BOOST  
  - All non-biting moves
  - Calls BattleScript_HandleSoulEaterEffect (25% max HP)

### Technical Implementation
```c
constexpr Ability JawsOfCarnage = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler))        // Must not be at full HP
        CHECK(CanBattlerHeal(battler))            // Must be able to heal
        if (gBattleMoves[gCurrentMove].flags & FLAG_STRONG_JAW_BOOST)
            BattleScriptCall(BattleScript_HandleJawsOfCarnageEffect);  // 50% heal
        else
            BattleScriptCall(BattleScript_HandleSoulEaterEffect);      // 25% heal
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,  // Applies to the attacker
};
```

### Battle Scripts
```assembly
BattleScript_HandleJawsOfCarnageEffect::
    tryhealpercenthealth BS_STACK_1, 50, BattleScript_Return  ; 50% heal
    goto BattleScript_HandleSoulEaterEffect_AfterHeal

BattleScript_HandleSoulEaterEffect::
    tryhealpercenthealth BS_STACK_1, 25, BattleScript_Return  ; 25% heal
BattleScript_HandleSoulEaterEffect_AfterHeal:
    orword gHitMarker, HITMARKER_IGNORE_SUBSTITUTE
    healthbarupdate BS_STACK_1
    datahpupdate BS_STACK_1
    printstring STRINGID_STACKREGAINEDHEALTH
    waitmessage B_WAIT_TIME_LONG
    return
```

### Strong Jaw Boost Moves
Moves that trigger 50% healing (FLAG_STRONG_JAW_BOOST):
- **Bite** - Dark-type physical move
- **Crunch** - Dark-type physical move, lowers Defense
- **Thunder Fang** - Electric-type, can paralyze and flinch
- **Ice Fang** - Ice-type, can freeze and flinch
- **Fire Fang** - Fire-type, can burn and flinch
- **Poison Fang** - Poison-type, can badly poison
- **Bug Bite** - Bug-type, steals and eats held Berry
- **Psychic Fangs** - Psychic-type, breaks Light Screen/Reflect
- Various other biting/jaw-based moves

### Important Interactions
- **Heal Block**: Prevents the ability from working
- **Maximum HP**: No effect if already at full health
- **Multi-KO**: Can trigger multiple times in a single turn
- **Substitute**: Healing ignores Substitute when displaying HP bar
- **Priority**: Healing occurs immediately after the KO

### Strategic Applications
- **Sweeping potential**: Sustains sweepers through multiple KOs
- **Biting move synergy**: Rewards using thematic jaw-based attacks
- **Bulk enhancement**: Effectively increases survivability in long battles
- **Team support**: Allows for more aggressive play patterns

### Competitive Usage
- **Physical sweepers**: Pairs well with Pokemon that learn multiple biting moves
- **Mixed attackers**: Can use both biting and non-biting moves strategically
- **Endgame closers**: Excellent for cleaning up weakened teams
- **Stallbreaking**: Sustained healing allows pressure on defensive teams

### Synergies
- **Strong Jaw**: Combines excellently for both damage and healing
- **Life Orb**: Recoil damage offset by frequent healing
- **Choice items**: Sustains through locked-in attacks
- **Biting move coverage**: Thunder Fang, Ice Fang, Fire Fang for type coverage

### Counters and Limitations
- **Heal Block**: Completely prevents the healing effect
- **Priority moves**: Can KO before healing triggers
- **Maximum HP**: No benefit when already healthy
- **Non-KO damage**: Doesn't heal from chip damage or status
- **Substitute**: Can block the finishing blow

### Team Building Considerations
- **Move selection**: Prioritize Pokemon with access to multiple biting moves
- **Coverage planning**: Use elemental fangs for type coverage
- **Entry hazard support**: Helps secure KOs for healing triggers
- **Speed control**: Ensures the Pokemon can land finishing blows

### Notable Users
Pokemon that can effectively utilize Jaws of Carnage typically have:
- Access to multiple biting moves
- Good physical attack stats
- Decent bulk to survive until healing
- Speed or priority to secure KOs

### Version Notes
- Introduced in Elite Redux as an enhanced version of similar healing abilities
- Part of the expanded ability system with 4-ability mechanics
- Balances aggressive play with sustainable recovery
- Encourages thematic movepool usage with biting attacks