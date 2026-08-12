---
id: 464
name: Hunter's Horn
status: reviewed
character_count: 159
---

# Hunter's Horn - Ability ID 464

## In-Game Description
"Boost horn moves and heals 1/4 HP when defeating an enemy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of horn and drill-based attacks by 30%. When the user knocks out an opponent with a direct hit, it immediately recovers 25% of its maximum HP.

## Detailed Mechanical Explanation

Hunter's Horn combines two existing ability components:
1. **MightyHorn.onOffensiveMultiplier**: 1.3x power boost for horn-based moves
2. **SoulEater.onBattlerFaints**: 25% HP heal when defeating an enemy

**Power Boost Implementation:**
- **Exact multiplier**: 1.3x (30% power increase)
- **Code reference**: `MUL(1.3)` in `MightyHorn.onOffensiveMultiplier` function
- **Implementation**: Uses fixed-point arithmetic `UQ_4_12(1.3)` = 1331/1024 about 1.30x

**Heal on KO Implementation:**
- **Exact amount**: 25% of max HP (1/4 HP)
- **Code reference**: `tryhealpercenthealth BS_STACK_1, 25` in `BattleScript_HandleSoulEaterEffect`
- **Trigger**: Only when the Hunter's Horn user defeats (KOs) an opponent

## Trigger Conditions

**Horn Move Boost:**
- Triggers when using any move with the `horn: true` flag
- Applied during damage calculation phase

**Healing on KO:**
- Triggers when the Hunter's Horn user directly causes an opponent to faint
- Must not be at max HP and must be able to heal
- Works in both singles and doubles battles

## Numerical Effects

**Power Boost:**
- **Multiplier**: 1.3x (30% increase)
- **Examples**: 
  - Megahorn: 120 to 156 effective power
  - Horn Drill: 95 to 123.5 effective power
  - Horn Attack: 85 to 110.5 effective power

**Healing:**
- **Amount**: 25% of user's maximum HP
- **Conditions**: Must not be at max HP, must be able to heal

## Interactions

**Horn Moves List** (22 total moves with `horn: true` flag):
- Horn Attack (85 to 110.5), Fury Attack (25 to 32.5), Horn Drill (95 to 123.5)
- Peck (25 to 32.5), Drill Peck (90 to 117), Megahorn (120 to 156)
- Poison Jab (80 to 104), Psycho Cut (75 to 97.5), Drill Run (85 to 110.5)
- Horn Leech (75 to 97.5), Smart Strike (80 to 104), And 11 others

**With Other Abilities:**
- Stacks with other power-boosting effects (STAB, items, etc.)
- Healing component works regardless of move type or effectiveness

## Special Cases

- No stat boosts beyond the healing (despite in-game description mentioning Soul Eater)
- No accuracy changes or other side effects
- Pure offensive boost + healing on KO combination
- Works with multi-hit horn moves (Fury Attack gets boost on each hit)

## Notes

- **No Additional Effects Beyond Listed:**
  - No stat boosts per KO
  - No accuracy changes
  - No other side effects

- **Particularly Powerful On:**
  - Pokemon with access to high-power horn moves like Megahorn
  - Physical attackers that can reliably secure KOs for the healing
  - Pokemon that benefit from sustained offensive pressure

- The combination of offensive boost and healing makes it excellent for sweeping scenarios where the user can chain KOs while maintaining HP