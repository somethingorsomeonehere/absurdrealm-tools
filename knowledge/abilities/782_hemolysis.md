---
id: 782
name: Hemolysis
status: reviewed
character_count: 129
---

# Hemolysis - Ability ID 782

## In-Game Description
"Poisoned foes lose all stat buffs and can't heal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user poisons a Pokemon, the poisoned target is cleared of all stat raises and they are unable to heal through any means.

## Detailed Mechanical Explanation
*For Discord/reference use*

Hemolysis is a passive field ability that creates a blood-corrupting aura affecting poisoned opponents. The ability functions through two main mechanisms implemented in the battle system:

**Healing Prevention (CanBattlerHeal function):**
- Any Pokemon with poison status (STATUS1_POISON_ANY) cannot heal HP while Hemolysis is active on the opposing side
- This blocks all forms of healing: moves like Recover/Roost, items like Leftovers/Berries, and abilities like Rain Dish
- The check specifically looks for `IsAbilityOnOpposingSide(battler, ABILITY_HEMOLYSIS)` combined with poison status

**Stat Buff Nullification (BenefitsFromStatBuffs function):**
- Poisoned Pokemon lose all benefits from stat increases (Attack, Defense, Speed, etc.)
- This affects both move-based stat boosts (Swords Dance, Dragon Dance) and ability-based boosts
- The poisoned Pokemon retains the visual stat boost indicators but gains no mechanical benefit

**Strategic Implications:**
- Synergizes extremely well with poison-inducing moves and abilities
- Counters stall strategies that rely on healing + stat boosts
- Forces opponents to cure poison or switch out to regain normal functionality
- Particularly effective against setup sweepers who become poisoned

**Counterplay:**
- Poison immunity (Poison/Steel types, Immunity ability)
- Status cure moves (Aromatherapy, Heal Bell)
- Switching out to remove poison status
- Priority moves that don't rely on stat boosts

The ability's name "Hemolysis" refers to the breakdown of red blood cells, thematically representing how poison corrupts the target's blood, preventing healing and weakening their enhanced capabilities.