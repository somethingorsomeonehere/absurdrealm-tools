---
id: 783
name: Caretaker
status: reviewed
character_count: 293
---

# Caretaker - Ability ID 783

## In-Game Description
"Healer + Friend Guard."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gives a 30% chance to cure status conditions at the end of each turn for both the user and their ally if they are out in a double battle. Makes 2 separate checks for each Pokemon. In a double battle, the user's ally receives 50% less damage. Multiplicative with other damage reduction sources. 


## Detailed Mechanical Explanation
*For Discord/reference use*

Caretaker is a combination ability that merges the complete effects of both Healer and Friend Guard:

**Healer Component (onEndTurn):**
- 30% chance each turn to activate healing
- Prioritizes healing partner's status conditions first
- If partner has no status condition or is fainted, can heal self
- Works on all major status conditions (sleep, paralysis, burn, poison, freeze)
- Uses the same BattleScript_HealerActivates animation as regular Healer

**Friend Guard Component (damage reduction):**
- Reduces all damage dealt to the partner by 50% (0.5x multiplier)
- Applied during damage calculation in battle_util.c
- Works against all damaging moves targeting partner
- Does not protect against indirect damage (weather, entry hazards, etc.)
- Effect is passive and always active in double battles

**Strategic Value:**
- Exceptional support ability for double battle formats
- Provides both proactive healing and reactive damage mitigation
- Partner effectively has 2x effective HP against direct attacks
- The 30% healing chance provides consistent status cleansing support
- No effect in single battles beyond the self-healing aspect

**Implementation Notes:**
- Uses identical code structure to Healer for the healing component
- Friend Guard effect is hardcoded in the damage calculation routine
- Both effects function independently and can trigger simultaneously
- Partner must be alive for Friend Guard effect to apply