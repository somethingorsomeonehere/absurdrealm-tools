---
id: 247
name: Ripen
status: reviewed
character_count: 264
---

# Ripen - Ability ID 247

## In-Game Description
"Doubles resistance, healing and stat raises provided by Berries."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ripen doubles all beneficial berry effects. Healing berries restore twice as much HP, stat-boosting berries raise stats by 2 stages instead of 1, resist berries reduce super-effective damage by 75% instead of 50%, and PP-restoring berries restore twice as much PP.

## Detailed Mechanical Explanation
*For Discord/reference use*

Ripen is a comprehensive berry-enhancing ability that affects all types of beneficial berry effects:

### Affected Berry Categories:

1. **Healing Berries**: All HP-restoring berries have their healing doubled
   - Includes percent-based healing (Sitrus Berry, etc.) and fixed healing berries
   - Also affects healing from Berry Juice

2. **Stat-Boosting Berries**: Stat increases are doubled from 1 stage to 2 stages
   - Liechi Berry (Attack), Salac Berry (Speed), Petaya Berry (Sp. Attack), etc.
   - Ganlon Berry (Defense), Apicot Berry (Sp. Defense)
   - Lansat Berry (critical hit ratio), Starf Berry (random stat)
   - Micle Berry (accuracy boost)
   - Also affects stat boosts from Kee Berry (Defense when hit by physical) and Maranga Berry (Sp. Defense when hit by special)

3. **Resist Berries**: Type-resist berries provide enhanced damage reduction
   - Normal effectiveness: 50% damage reduction to 75% damage reduction (0.25x modifier)
   - Only triggers on super-effective moves or Normal-type moves
   - Includes berries like Occa Berry (Fire), Yache Berry (Ice), Chople Berry (Fighting), etc.

4. **Status Cure Berries**: No direct enhancement (they simply cure status conditions)
   - Pecha Berry (poison), Cheri Berry (paralysis), Rawst Berry (burn), etc.
   - These berries work normally with Ripen

5. **PP-Restoring Berries**: PP restoration is doubled
   - Leppa Berry restores twice as much PP to moves

6. **Retaliation Berries**: Damage dealt to attackers is doubled
   - Jaboca Berry (damages physical attackers) and Rowap Berry (damages special attackers)
   - Damage increases from 1/8 of attacker's max HP to 1/4

### Implementation Notes:
- Works with the HasRipenEffect() function which also includes Apple Pie and Sugar Rush abilities
- Unaffected by Unnerve ability (berry effects still trigger)
- Does not affect confusion berries' healing (they still heal normally and cause confusion if flavor is disliked)
- Berry consumption and activation conditions remain the same - only the effects are enhanced

### Competitive Usage:
- Particularly effective with Sitrus Berry for enhanced recovery
- Combines well with stat-boosting berries for setup sweepers
- Resist berries become extremely powerful defensive tools (75% damage reduction)
- Most beneficial on Pokemon that can reliably trigger berry consumption through self-damage or low HP thresholds