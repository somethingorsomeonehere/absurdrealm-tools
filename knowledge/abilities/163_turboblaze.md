---
id: 163
name: Turboblaze
status: reviewed
character_count: 290
---

# Turboblaze - Ability ID 163

## In-Game Description
"Moves bypass all defensive abilities and adds Fire type on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Allows moves to ignore the target's abilities and innates that interfere with effects or reduce damage. Does not bypass abilities that modify base stats such as Grass Pelt. Adds Fire to the user's typing. Retains Fire typing even upon losing the ability, going away only when switching out.

## Detailed Mechanical Explanation

### Primary Effects
1. **Mold Breaker Effect**: All moves used by the Pokemon ignore the target's defensive abilities that would normally block, reduce, or nullify the move's effects. This includes abilities like Levitate, Flash Fire, Water Absorb, and similar defensive abilities.

2. **Fire Type Addition**: Upon entering battle, the Pokemon gains Fire as an additional type (stored in type3 slot), making it effectively gain Fire-type STAB and Fire-type resistances/weaknesses.

### Technical Implementation
- **Entry Message**: "{Pokemon} is radiating a blazing aura!"
- **Mold Breaker Flag**: Sets HITMARKER_MOLD_BREAKER when attacking, processed by ShouldSetMoldBreaker() function
- **Type Addition**: Uses AddBattlerType(battler, TYPE_FIRE) on entry
- **Battle System**: Checked alongside ABILITY_MOLD_BREAKER and ABILITY_TERAVOLT in ability-ignoring mechanics

## Strategic Applications

### Offensive Benefits
- Bypasses common defensive abilities (Levitate, Flash Fire, Storm Drain, etc.)
- Ignores Wonder Guard on Shedinja-type Pokemon
- Fire-type STAB bonus on Fire moves after gaining the typing
- Crucial for dealing with ability-reliant defensive strategies

### Defensive Considerations  
- Fire typing addition brings new weaknesses (Water, Ground, Rock)
- May lose original type advantages depending on base typing
- Fire resistances to Fire, Grass, Ice, Bug, Steel, and Fairy moves

## Pokemon Distribution
Turboblaze appears on 15+ Pokemon species, primarily:
- **Fire-type specialists**: Rapidash variants, Darumaka line
- **Legendary/Mythical**: Various legendary Pokemon as ability or innate
- **Dragon hybrids**: Fire/Dragon combinations for offensive coverage
- **Mixed typings**: Ice/Fire, Psychic/Fire, Fighting/Dragon combinations

Notable users include Rapidash (as selectable ability), legendary Fire-types, and various Fire/Dragon legendary Pokemon.

## Competitive Viability
**Tier Assessment**: High utility in competitive play
- Essential for breaking through ability-based defensive cores
- Fire typing addition provides valuable STAB and resistances
- Particularly valuable against teams relying on immunity abilities
- Strong synergy with Fire-type movesets and sun team strategies

## Related Abilities
- **Teravolt**: Sister ability that adds Electric type instead of Fire
- **Mold Breaker**: Pure ability-ignoring effect without type addition
- **Mycelium Might**: Ignores abilities only for status moves
- **Deadly Precision**: Has mold breaker effect with super-effective moves