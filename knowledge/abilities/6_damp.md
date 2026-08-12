---
id: 6
name: Damp
status: reviewed
character_count: 245
---

# Damp - Ability ID 6

## In-Game Description
"Makes the target become Water-type on contact. Also works on offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

If the user makes contact with another Pokemon, offensively or defensively, the other Pokemon's type is changed to pure Water. This happens immediately for multihit or priority moves and can remove STAB in the middle of an enemy's multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Damp has been completely reimagined in Elite Redux as an aggressive type-changing ability:

1. **Type Change Mechanic**
   - Triggers on any contact move (offensive or defensive)
   - Changes the opponent to pure Water-type
   - Sets both type1 and type2 to Water
   - Sets type3 to Mystery type
   - Permanent until switched out or changed again

2. **Activation Conditions**
   - Either the attacker or defender must have Damp
   - The move must make contact
   - Standard on-hit effect conditions apply
   - Target must not already be Water-type

### Technical Implementation

**Code Implementation** (`src/abilities.cc`):
```cpp
ON_EITHER(Damp) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))
    CHECK_NOT(IS_BATTLER_OF_TYPE(opponent, TYPE_WATER))
    
    gBattleMons[opponent].type1 = TYPE_WATER;
    gBattleMons[opponent].type2 = TYPE_WATER;
    gBattleMons[opponent].type3 = TYPE_MYSTERY;
    
    PREPARE_TYPE_BUFFER(gBattleTextBuff1, TYPE_WATER);
    gStackBattler1 = opponent;
    BattleScriptCall(BattleScript_StackBecameTheTypeFull);
    return TRUE;
}
```

### Complete Rework from Vanilla
**Original Damp**: Prevented Self-Destruct, Explosion, Mind Blown, and Misty Explosion
**Elite Redux Damp**: Forces type change to Water on contact

This represents a complete philosophical shift from a defensive/preventative ability to an aggressive type-manipulation ability.

### Strategic Implications

1. **Offensive Benefits**
   - Remove opponent's STAB moves
   - Force Water-type weaknesses (Electric, Grass)
   - Eliminate problematic type immunities (Ground to Electric, etc.)
   - Set up for super effective follow-up attacks

2. **Defensive Benefits**
   - Neutralize Fighting, Fire, Rock effectiveness
   - Remove dangerous STAB attacks from opponent
   - Predictable defensive typing for calculations

### Interactions with Other Abilities/Mechanics
- **Protean/Libero**: Type changes after, potentially overwriting
- **Color Change**: Would change Damp user's type to Water if hit
- **Soak move**: Essentially gives Soak effect on contact
- **Type-based abilities**: May activate/deactivate based on new typing
- **Weather**: Makes opponent vulnerable to rain-boosted Water moves

### Example Battle Scenarios

**Scenario 1 - Offensive**:
- Damp user uses Close Combat on Garchomp
- Garchomp becomes Water-type, loses Dragon/Ground STAB
- Now weak to teammate's Thunderbolt

**Scenario 2 - Defensive**:
- Blaziken uses Blaze Kick on Damp user
- Blaziken becomes Water-type, loses Fire/Fighting STAB
- Future Fire attacks deal reduced damage

### Common Users
The reimagined Damp would logically appear on:
- Water-type Pokemon with "soaking" themes
- Pokemon with aquatic or amphibious characteristics
- Potentially some Poison-types (dampening opponents)

### Competitive Usage Notes
- S-tier disruption ability
- Counters setup sweepers by removing STAB
- Enables Electric/Grass coverage to be more valuable
- Can neutralize type-based strategies
- Particularly strong on fast physical attackers

### Counters
- **Non-contact moves**: Special attackers avoid the effect
- **Long-range physical moves**: Earthquake, Rock Slide, etc.
- **Pivot moves**: U-turn/Volt Switch to reset typing
- **Water-types**: Immune to the type change
- **Type-reset moves**: Could potentially restore original typing

### Synergies
- **Electric/Grass coverage**: Exploit new Water weakness
- **Contact spam**: Multiple chances to trigger
- **Fake Out leads**: Guaranteed type change turn 1
- **Pursuit trappers**: Punish forced switches
- **Weather teams**: Rain boosts Water moves against new Water-types

### Version History
- **Original Games**: Prevented explosion moves
- **Elite Redux**: Complete rework into type-changing ability