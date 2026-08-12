---
id: 214
name: Queenly Majesty
status: reviewed
character_count: 113
---

# Queenly Majesty - Ability ID 214

## In-Game Description
"Protects itself and ally from priority moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Queenly Majesty prevents the user and its ally from being targeted by priority moves with priority higher than 0. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Queenly Majesty provides complete immunity to priority moves for both the user and its ally in doubles battles. The ability triggers when:
- An opposing Pokemon attempts to use a move with priority > 0
- The move targets the Queenly Majesty user or its ally
- The move is not an "extra attack" (pursuit-like mechanics don't apply)

### Technical Implementation
```cpp
constexpr Ability QueenlyMajesty = {
    .onImmune = +[](ON_IMMUNE) -> int {
        CHECK_NOT(gProcessingExtraAttacks)
        CHECK(GetBattlerSide(attacker) != GetBattlerSide(battler))
        CHECK(GetMovePriority(attacker, move, battler) > 0);
        *immunityScript = BattleScript_DazzlingProtected;
        return TRUE;
    },
    .onImmuneFor = APPLY_ON_ALLY,
    .breakable = TRUE,
};
```

### Priority Move Examples Blocked
- **Priority +3**: Fake Out
- **Priority +2**: Quick Attack, Extreme Speed
- **Priority +1**: Bullet Punch, Mach Punch, Sucker Punch, Aqua Jet, Ice Shard
- **Priority +0**: Normal moves (NOT blocked)
- **Negative Priority**: Moves like Trick Room are not affected

### Battle Message
When a priority move is blocked: "*Pokemon cannot use [move name]!*" after the ability pop-up displays.

### Interaction with Other Abilities/Items
- **Mold Breaker**: Bypasses Queenly Majesty completely
- **Turboblaze/Teravolt**: Also bypass the protection
- **Prankster**: Status moves with Prankster priority are blocked
- **Gale Wings**: Flying-type moves with Gale Wings priority are blocked

### Strategic Applications
- **Priority Protection**: Shuts down common revenge killers like Talonflame, Azumarill, and Lucario
- **Doubles Synergy**: Protects both team members from priority moves
- **Setup Sweeper Support**: Allows frail setup sweepers to boost safely
- **Anti-Suicide Prevention**: Blocks Fake Out + priority move combinations

### Common Users in Elite Redux
- **Tsareena**: Has Queenly Majesty as an innate ability alongside Keen Edge and Striker
- **Gardevoir**: Uses it as a main ability option (ability slot 0) with Soul Heart and Psychic Surge
- **Vespiquen**: Has it as an ability choice with Regenerator and Stamina
- **Salazzle**: Gets it as an innate ability for additional utility
- **Nidoqueen**: Uses it as an innate ability for bulk support
- **Meloetta**: Has it as a main ability for support roles
- **Ninetales**: Gets it as an innate ability for sun team support

### Competitive Usage Notes
- **Team Role**: Primarily defensive utility, enables setup sweepers
- **Doubles Impact**: Significantly more valuable in doubles than singles
- **Meta Relevance**: Counters priority-heavy metagames effectively
- **Positioning**: Best used on bulky Pokemon that can take non-priority hits

### Counters and Limitations
- **Mold Breaker abilities**: Completely bypass the protection
- **Non-priority moves**: Regular attacks still hit normally  
- **Status moves**: Non-priority status moves bypass protection
- **Ability suppression**: Gastro Acid, Worry Seed remove the protection
- **Skill Swap/Role Play**: Can transfer the ability to opponents

### Synergies
- **Setup moves**: Pairs well with Calm Mind, Nasty Plot, Quiver Dance users
- **Frail sweepers**: Protects glass cannons from priority revenge killing
- **Assault Vest users**: Combines defensive utility with special bulk
- **Choice item users**: Prevents being revenge killed by priority after KOs

### Version History
Queenly Majesty is based on the Generation VII ability but with Elite Redux's multi-ability system integration. In Elite Redux, it often appears as an innate ability rather than a main ability, providing additional utility to many Pokemon that wouldn't normally have access to priority protection.

The ability is particularly notable for its implementation alongside Dazzling and Armor Tail, which share the same core mechanic but may have different secondary effects or distributions across the Pokédex.