---
id: 108
name: Forewarn
status: reviewed
character_count: 248
---

# Forewarn - Ability ID 108

## In-Game Description
"Casts an 80 BP Future Sight on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Casts an 80 BP Future Sight on the opposing Pokemon when switching in. Strikes 2 turns later, bypassing substitutes and other protections. The attack cannot miss once initiated and ignores accuracy checks. This cannot target the same Pokemon twice.

## Detailed Mechanical Explanation

Forewarn in Elite Redux has been completely reworked from its vanilla version. Instead of revealing the opponent's highest base power move, it now offensively casts Future Sight upon entry.

### Key Mechanics:
1. **Automatic Cast**: When a Pokemon with Forewarn enters battle, it immediately casts Future Sight targeting an opponent
2. **Fixed Power**: The Future Sight has 80 base power (not affected by the user's stats at cast time)
3. **Turn Delay**: The attack strikes after 3 turns (on the 3rd turn after casting)
4. **Target Selection**: 
   - Prioritizes the opposing Pokemon directly across from the user
   - If that target already has a Future Sight pending, it targets their partner instead
   - Cannot target a fainted Pokemon
5. **Type**: The Future Sight attack is Psychic-type and ignores type immunities (hits Dark types)
6. **Stacking**: Cannot stack multiple Future Sights on the same target - each Pokemon can only have one pending

### Battle Flow:
- Turn 1: Pokemon with Forewarn switches in to "foresaw an attack!" message to Future Sight timer starts
- Turn 2: Future Sight pending
- Turn 3: Future Sight strikes the target

### Strategic Implications:
- Provides guaranteed chip damage on switch-in
- Forces opponents to consider the incoming damage when planning switches
- Synergizes well with offensive pivoting strategies
- Can pressure defensive Pokemon that would normally wall the user
- The damage occurs even if the Forewarn user switches out or faints

### Interactions:
- Does not trigger if both opponents already have Future Sight pending
- The damage calculation uses the original caster's Special Attack stat
- Can be blocked by Protect/Detect on the turn it strikes
- Wonder Guard does not block Future Sight damage