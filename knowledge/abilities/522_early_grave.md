---
id: 522
name: Early Grave
status: reviewed
character_count: 50
---

# Early Grave - Ability ID 522

## In-Game Description
"Ghost-type moves get +1 priority at max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ghost-type moves gain +1 priority when at full HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

**EARLY GRAVE** is a priority-granting ability that gives Ghost-type moves +1 priority when the user is at maximum HP.

### Activation Mechanics:
- **Trigger**: When selecting a Ghost-type move while at full HP
- **Priority Bonus**: +1 to Ghost-type moves only
- **HP Requirement**: Must be at exactly 100% HP (BATTLER_MAX_HP)
- **Implementation**: Uses GALE_WINGS_CLONE macro for TYPE_GHOST

### Technical Details:
```c
// Uses the GALE_WINGS_CLONE macro
GALE_WINGS_CLONE(TYPE_GHOST)
// Which expands to:
// 1. Check if move is Ghost-type
// 2. Check if battler is at max HP
// 3. Return +1 priority if both true
```

### Priority Interactions:
- **Shadow Sneak**: Becomes +2 priority (base +1, ability +1)
- **Regular Ghost Moves**: Shadow Ball, Hex, etc. become +1 priority
- **Status Moves**: Ghost-type status moves also gain priority
- **Multi-hit**: Each hit maintains priority boost

### HP Threshold Mechanics:
- **Exact Requirement**: Must be at 100% HP, not 99.9%
- **Entry Hazards**: Stealth Rock/Spikes will break the condition
- **Residual Damage**: Poison, burn, sandstorm prevent activation
- **Healing**: Can restore priority by healing to full

### Pokemon with Early Grave:

1. **Gengar** (Innate ability)
   - Other innates: Vengeance, Ectoplasm
   - Benefits from high Speed and Special Attack

2. **Spiritomb** (Innate ability)
   - Other innates: Bone Zone, Rock Head
   - Slower but bulkier priority user

3. **Typhlosion-Hisuian** (Changeable ability option)
   - Can choose between: Early Grave, Ethereal Rush, Set Ablaze
   - Innates: Blaze, Pyromancy, Frisk
   - Mixed Fire/Ghost attacker with priority options

4. **Mega Typhlosion-Hisuian** (Innate ability)
   - Other innates: Hellblaze, Vengeful Spirit
   - Enhanced stats make priority even more threatening

### Competitive Notes:
- **Revenge Killing**: Switch in after a KO for guaranteed priority revenge
- **Lead Potential**: Strong turn 1 with guaranteed priority
- **Focus Sash Synergy**: Opponents can't break sash and outspeed
- **Hazard Weakness**: Very vulnerable to entry hazard chip
- **Healing Requirements**: May need Roost/Recover to maintain

### Strategy Tips:
- Pair with hazard removal support (Rapid Spin/Defog)
- Consider Magic Guard teammates to prevent hazards
- Leftovers helps maintain full HP between switches
- Life Orb breaks the synergy - avoid recoil items
- Can run Protect to scout and maintain HP

### Similar Abilities:
- **Gale Wings**: Flying-type version
- **Prankster**: Status moves only, no HP requirement
- **Triage**: Healing moves only
- **Grassy Glide**: Grassy Terrain requirement instead of HP