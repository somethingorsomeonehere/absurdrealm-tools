---
id: 156
name: Magic Bounce
status: reviewed
character_count: 202
---

# Magic Bounce - Ability ID 156

## In-Game Description
"Bounces back the effect of status moves to their user."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reflects most status moves back to the user before they can take effect. The bounced move targets the original user with no additional accuracy check. Does not reflect moves that were already reflected.

## Detailed Mechanical Explanation
*For Discord/reference use*

Magic Bounce is a passive ability that automatically reflects status moves back to their user before they can affect the Magic Bounce user.

### Core Mechanics
- **Automatic Activation**: No user input required - activates whenever a qualifying move targets the Magic Bounce user
- **Pre-Effect Reflection**: The move is bounced before it can take effect on the Magic Bounce user
- **Original User Targeting**: The bounced move automatically targets the original user with no accuracy check
- **One-Time Bounce**: Moves can only be bounced once per turn - a bounced move that hits another Magic Bounce user will not bounce again

### Technical Implementation
```c
// From abilities.cc
constexpr Ability MagicBounce = {
    .breakable = TRUE,
    .magicBounce = TRUE,
};
```

The ability works by checking for the `FLAG_MAGIC_COAT_AFFECTED` flag on incoming moves:
```c
if (gBattleMoves[gCurrentMove].flags & FLAG_MAGIC_COAT_AFFECTED && !gRoundStructs[gBattlerAttacker].usesBouncedMove) {
    ON_ABILITY(gBattlerTarget, TRUE, gAbilities[ability].magicBounce, 
               gBattleScripting.abilityPopupOverwrite = ability;
               gRoundStructs[gBattlerTarget].usesBouncedMove = TRUE;
               gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_PKMNMOVEBOUNCEDABILITY;
               BattleScriptCall(BattleScript_MagicCoatBounce);
               return)
}
```

### Affected Moves (83 total)
Magic Bounce reflects moves with the `FLAG_MAGIC_COAT_AFFECTED` flag, including:

**Status Condition Moves:**
- Toxic, Poison Powder, Will-O-Wisp, Thunder Wave, Sleep Powder, Stun Spore
- Paralysis, poison, burn, and sleep-inducing moves

**Stat Modification Moves:**
- Sand Attack, Leer, Tail Whip, Growl, String Shot, Scary Face
- Most stat-lowering moves that target opponents

**Field Effect Moves:**
- Leech Seed, Spikes, Toxic Spikes, Stealth Rock
- Entry hazard moves

**Disruption Moves:**
- Taunt, Torment, Disable, Encore, Attract
- Moves that limit opponent's actions

**Sound-Based Status Moves:**
- Roar, Supersonic, Sing, Grass Whistle
- Non-damaging sound moves

### Moves NOT Affected
- **Damaging Moves**: Any move that deals direct damage
- **Self-Targeting Moves**: Moves that target the user (Swords Dance, Recover, etc.)
- **Multi-Target Moves**: Some moves that target multiple Pokemon
- **Specific Exceptions**: Moves specifically coded to bypass Magic Bounce

### Interactions with Other Abilities/Mechanics
- **Prankster Interaction**: If a Dark-type Pokemon uses a Prankster-boosted status move that gets bounced back, the move will fail against the Dark-type user
- **Magic Coat**: Magic Bounce has the same effect as the move Magic Coat but is automatic
- **Substitute**: Magic Bounce activates even if the user is behind a Substitute
- **Mold Breaker**: Abilities like Mold Breaker, Turboblaze, and Teravolt ignore Magic Bounce
- **Breakable Flag**: Magic Bounce can be suppressed by abilities that break other abilities

### Strategic Implications
**Defensive Utility:**
- Excellent counter to status-based strategies
- Forces opponents to use direct damage or switch
- Particularly effective against support Pokemon

**Team Building:**
- Valuable on defensive cores
- Synergizes well with other defensive abilities
- Can deter setup sweepers relying on status moves

**Offensive Considerations:**
- Provides setup opportunities when opponents expect status moves to work
- Can turn the tables on opponents trying to inflict status conditions

### Common Users in Elite Redux
Notable Pokemon with Magic Bounce as a regular or innate ability:
- **Natu/Xatu line**: Classic Magic Bounce users with Psychic typing
- **Espeon**: Fast special attacker with defensive utility
- **Hattrem/Hatterene line**: Psychic/Fairy types with strong special bulk
- **Sableye variants**: Defensive Dark/Ghost types
- **Various Psychic-types**: Many psychic Pokemon have access as innate ability

### Competitive Usage Notes
- **Tier Placement**: Highly valued in defensive team compositions
- **Meta Relevance**: Effectiveness depends on prevalence of status moves
- **Role Compression**: Provides passive status immunity while maintaining offensive presence
- **Prediction Factor**: Forces opponents to play around potential bounces

### Counters and Limitations
**Direct Counters:**
- Mold Breaker family abilities (Mold Breaker, Turboblaze, Teravolt)
- Direct damage moves
- Self-targeting setup moves

**Strategic Counters:**
- Physical attackers that don't rely on status moves
- Multi-hit moves and direct damage
- Pokemon with Natural Cure or similar status-clearing abilities

### Synergies
**Ability Combinations:**
- **Magic Guard**: Complete immunity to indirect damage (seen in Conjurer of Deceit)
- **Prankster**: Priority status moves that can be bounced for mind games
- **Psychic Surge**: Terrain support with status reflection

**Item Synergies:**
- **Leftovers**: Passive recovery complements defensive role
- **Light Clay**: Extends screen duration for defensive teams
- **Mental Herb**: Backup protection against mental status effects

### Version History
Magic Bounce has been a consistently powerful defensive ability since its introduction, with Elite Redux maintaining its core mechanics while expanding its distribution to various Pokemon as both a regular and innate ability. The ability's value fluctuates with the metagame's reliance on status moves but remains a solid defensive option in most competitive formats.