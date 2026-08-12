---
id: 140
name: Telepathy
status: reviewed
character_count: 88
---

# Telepathy - Ability ID 140

## In-Game Description
"Protects team from friendly fire."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Protects the Pokemon from all damage-dealing moves used by its allies in double battles. 

## Detailed Mechanical Explanation

Telepathy is a defensive ability that provides complete protection from damage caused by the Pokemon's allies in multi-battle formats. The implementation shows:

1. **Complete Friendly Fire Immunity**: The ability checks if the move is targeting a partner (ally) and if the move has power (is damage-dealing). If both conditions are met, it sets the damage modifier to 0, completely negating the damage.

2. **Implementation Details**:
   - Uses `onAfterTypeEffectiveness` hook to modify damage after type calculations
   - Checks if `target == BATTLE_PARTNER(battler)` to identify ally attacks
   - Only blocks moves with power (`gBattleMoves[move].power` > 0)
   - Sets `*mod = 0` to completely nullify damage

3. **Scope of Protection**:
   - Protects from all damage-dealing moves from allies
   - Includes both direct attacks and spread moves
   - Does not protect from status moves or other non-damaging effects
   - Only works on moves that would deal damage (have a power value)

4. **Ability Properties**:
   - Marked as `breakable = TRUE`, meaning it can be suppressed by abilities like Mold Breaker
   - Uses `APPLY_ON_ATTACKER_OR_TARGET` flag, allowing it to work from either perspective

5. **Common Use Cases**:
   - Allows safe use of Earthquake alongside Ground-weak allies
   - Enables Surf strategies without damaging Water-weak partners
   - Permits Discharge usage without harming Electric-weak teammates
   - Generally enables more aggressive spread move strategies in doubles/triples

This ability is particularly valuable in double and triple battles where spread moves are common, allowing for more flexible team compositions and strategies without worrying about damaging your own team members.