---
id: 364
name: Looter
status: reviewed
character_count: 102
---

# Looter - Ability ID 364

## In-Game Description
"Dealing a KO heals 1/4 of this Pokemon's max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user knocks out an opponent with a direct hit, it immediately recovers 25% of its maximum HP.

## Detailed Mechanical Explanation

### Implementation Details
- **Trigger**: `onBattlerFaints` with `APPLY_ON_ATTACKER`
- **Condition**: Activates when the Pokemon with Looter knocks out an opponent
- **Effect**: Heals 25% of the user's maximum HP
- **Battle Script**: `BattleScript_HandleSoulEaterEffect`
- **Code Location**: `/src/abilities.cc` lines 3805-3808

### Code Implementation
```cpp
constexpr Ability Looter = {
    .onBattlerFaints = SoulEater.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

### Shared Implementation
Looter uses the exact same implementation as Soul Eater (#331), referencing the same lambda function and battle script. The underlying mechanics are identical:

```cpp
constexpr Ability SoulEater = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler));
        CHECK(CanBattlerHeal(battler));
        BattleScriptCall(BattleScript_HandleSoulEaterEffect);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

### Battle Script
```assembly
BattleScript_HandleSoulEaterEffect::
    tryhealpercenthealth BS_STACK_1, 25, BattleScript_Return
BattleScript_HandleSoulEaterEffect_AfterHeal:
    orword gHitMarker, HITMARKER_IGNORE_SUBSTITUTE
    healthbarupdate BS_STACK_1
    datahpupdate BS_STACK_1
    printstring STRINGID_STACKREGAINEDHEALTH
    waitmessage B_WAIT_TIME_LONG
    return
```

## Strategic Analysis

### Strengths
- **Consistent Healing**: Provides reliable 25% HP recovery on each knockout
- **Universal Trigger**: Works with any damaging move that causes a KO
- **Sustain Power**: Excellent for sweep scenarios and prolonged battles
- **No Type Restrictions**: Unlike some healing abilities, works regardless of move type
- **Immediate Effect**: Healing occurs right after the knockout

### Limitations
- **Requires Knockouts**: No benefit if the Pokemon can't secure eliminations
- **Full HP Check**: Cannot heal beyond maximum HP
- **Battle Format Dependent**: More valuable in singles than doubles due to knockout frequency
- **Vulnerable to Chip Damage**: Doesn't prevent residual damage between turns

### Tactical Applications
- **Late Game Sweeper**: Ideal for Pokemon designed to clean up weakened teams
- **Endurance Battles**: Excellent for long battles with multiple opponents
- **Recovery Strategy**: Allows risky plays knowing healing is guaranteed on success
- **Momentum Preservation**: Maintains offensive pressure by staying healthy

## Pokemon Distribution

### Sample Pokemon with Looter
Based on the species list analysis, Looter appears on various Pokemon including:
- **Rattata** (as one of three abilities: Hustle/Normalize/Looter)
- Multiple other species across different evolutionary lines
- Both as main abilities and innate abilities

### Ability Slot Usage
- **Primary Ability**: Available as one of the chooseable abilities
- **Innate Ability**: Also appears as an innate (always-active) ability on some species

## Related Abilities

### Abilities with Identical Implementation
These abilities share the exact same code and battle script as Looter:
- **Soul Eater** (#331) - Original implementation
- **Predator** (#363) - Uses `SoulEater.onBattlerFaints`
- **Scavenger** (#345) - Uses `SoulEater.onBattlerFaints`

### Abilities with Similar Healing Mechanics
- **Hunter's Horn** (#464) - Combines Looter's healing with offensive boosts
- **Magma Eater** (#467) - Combines healing with type effectiveness changes
- **Apex Predator** - Combines healing with Tough Claws effect
- **Jaws of Carnage** (#438) - 50% healing instead of 25% for bite moves
- **Bloodlust** - Combines Soul Eater healing with Blood Bath effects

### Competitive Comparison
- **Soul Eater vs Looter**: Functionally identical, different flavor names
- **Predator vs Looter**: Also identical mechanically, thematically similar
- **Scavenger vs Looter**: Same healing effect, different thematic approach

## Technical Notes
- Uses `tryhealpercenthealth` with 25% recovery value
- Healing bypasses Substitute due to `HITMARKER_IGNORE_SUBSTITUTE`
- Subject to standard healing restrictions (full HP check, healing ability check)
- Displays standard "regained health" message after successful healing
- Code reference: Line 9209 in ability mapping table

## Competitive Viability
Looter excels in formats where:
- Single battles are common (more knockout opportunities)
- Multiple weak opponents can be eliminated consecutively
- Sustain is valued over immediate power
- Long battles reward defensive capabilities

The ability transforms offensive Pokemon into self-sustaining threats, making them particularly dangerous in the late game when they can sweep through weakened opposing teams while maintaining their own health.