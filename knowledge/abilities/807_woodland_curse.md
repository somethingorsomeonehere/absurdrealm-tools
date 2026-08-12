---
id: 807
name: Woodland Curse
status: reviewed
character_count: 226
---

# Woodland Curse - Ability ID 807

## In-Game Description
"Uses Forest's Curse on Entry. Adds Grass type on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, uses Forest's Curse on a random opponent, adding Grass typing. When opponents make contact with the user, they also gain Grass as an extra type. Only affects non-Grass types. Persists until switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Woodland Curse is a dual-trigger ability that operates on two distinct conditions:

1. **Entry Effect**: Automatically uses Forest's Curse (move ID 571) when the Pokemon enters battle
2. **Contact Effect**: Adds Grass typing to opponents that make physical contact

### Technical Implementation

#### Entry Effect
```cpp
.onEntry = +[](ON_ENTRY) -> int { 
    return UseEntryMove(battler, ability, MOVE_FORESTS_CURSE, 0); 
}
```

- Triggers Forest's Curse move automatically on entry
- Forest's Curse is a status move with 100% accuracy, 20 PP
- Effect: `EFFECT_THIRD_TYPE` with argument `TYPE_GRASS`
- Adds Grass as the target's third type (`type3`)

#### Contact Effect
```cpp
ON_EITHER(WoodlandCurse) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))
    CHECK_NOT(IS_BATTLER_OF_TYPE(opponent, TYPE_GRASS))
    
    gBattleMons[opponent].type3 = TYPE_GRASS;
    PREPARE_TYPE_BUFFER(gBattleTextBuff1, gBattleMons[opponent].type3);
    gStackBattler1 = opponent;
    BattleScriptCall(BattleScript_StackBecameTheTypeFull);
    return TRUE;
}
```

### Activation Conditions

#### Entry Effect
- Activates immediately when Pokemon switches in or battle begins
- No conditions other than successful entry

#### Contact Effect
- Requires physical contact between moves
- Only affects opponents that don't already have Grass typing
- Must pass the `ShouldApplyOnHitAffect` check (ability not suppressed, target alive, etc.)

### Type System Mechanics

#### Third Type Addition
- Uses the `type3` field in the battle data structure
- Pokemon can have up to 3 types simultaneously (type1, type2, type3)
- Grass type is added as the third type, not replacing existing types
- If target already has Grass typing (any of type1, type2, or type3), the effect fails

#### Type Effectiveness Interactions
- Added Grass typing affects all type effectiveness calculations
- Makes the target weak to Fire, Ice, Flying, Bug, and Poison moves
- Makes the target resist Water, Electric, Grass, and Ground moves
- Target gains immunity to powder moves and Leech Seed

### Strategic Implications

#### Offensive Usage
- Creates additional type weaknesses on opponents
- Particularly effective against Water, Ground, Rock types
- Forces type-based strategic recalculations from opponents

#### Defensive Usage
- Contact moves become risky for physical attackers
- Creates mind games around contact vs. non-contact move selection
- Punishes common physical moves like Earthquake, Close Combat, etc.

### Affected Moves
All moves flagged with `FLAG_CONTACT` trigger the contact effect, including:
- Most physical attacks (Tackle, Punch moves, etc.)
- Some special moves that make contact (Grass Knot, etc.)
- Multi-hit contact moves trigger on each hit

### Interactions with Other Abilities/Mechanics

#### Ability Interactions
- Suppressed by Gastro Acid, Core Enforcer, etc.
- Long Reach, Protective Pads prevent contact effect
- Does not interact with abilities that change move types

#### Item Interactions
- Protective Pads prevent the contact effect
- No interaction with type-enhancing items (plates, etc.)

#### Move Interactions
- Moves that change typing (Reflect Type, etc.) can remove the added Grass type
- Baton Pass does not transfer the type change
- U-turn/Volt Switch removes the type change when switching

### Example Scenarios

#### Entry Effect
```
Turn 1: Opponent's Swampert (Water/Ground) is on field
Player sends out Pokemon with Woodland Curse
-> Forest's Curse automatically targets Swampert
-> Swampert becomes Water/Ground/Grass type
-> Now weak to Grass moves (4x), Ice moves (4x), Bug moves (2x)
```

#### Contact Effect
```
Turn 2: Opponent's Machamp uses Close Combat (contact move)
-> Woodland Curse activates on contact
-> Machamp becomes Fighting/Grass type
-> Now weak to Fire, Ice, Flying, Psychic, Fairy moves
```

### Damage Calculations
The type addition affects damage calculations immediately:

**Example**: Fire Blast vs. Swampert after Woodland Curse
- Original: Fire vs Water/Ground = 0.5x (resisted by Water)  
- After Curse: Fire vs Water/Ground/Grass = 1x (neutral, Water resists but Grass is weak)

### Common Users
This is a custom Elite Redux ability, so users depend on the specific ROM hack's distribution.

### Competitive Usage Notes
- High-impact entry ability that immediately affects type matchups
- Contact punishment creates additional pressure on physical attackers  
- Most effective against defensive Pokemon that rely on type resistances
- Can backfire if opponent switches to a Pokemon that benefits from Grass typing

### Counters
- Non-contact moves completely avoid the contact effect
- Grass-type Pokemon are immune to both effects
- Abilities like Long Reach, items like Protective Pads
- Rapid switching to remove type changes
- Ability suppression moves (Gastro Acid, etc.)

### Synergies
- Pairs well with Fire/Ice/Flying moves to exploit created weaknesses
- Works with moves that hit on switch-in (Pursuit-like effects)
- Combines with other type-changing abilities for complex interactions

### Version History
- Added in Elite Redux as ability ID 807
- Part of the expanded ability system beyond Generation 8