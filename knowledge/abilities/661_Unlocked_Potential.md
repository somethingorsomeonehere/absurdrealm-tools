---
id: 661
name: Unlocked Potential
status: reviewed
character_count: 293
---

# Unlocked Potential - Ability ID 661

## In-Game Description
Inner Focus + Berserk.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Focus Blast never misses. Unaffected by flinch, Intimidate, or Scare. When the user drops to half HP or below from an opposing attack, boosting its highest attacking stat by one stage. Triggers only once per battle. Other damage sources that bring you to half HP or below will not activate it.

## Detailed Mechanical Explanation

### Technical Implementation
- **onDefender**: When hit and HP falls to 50% or below, raises highest attacking stat (Attack or Special Attack) by 1 stage (inherited from Berserk)
- **onAccuracy**: Focus Blast bypasses accuracy checks and always hits (inherited from Inner Focus)  
- **tauntImmune**: Complete immunity to taunt-based moves
- **breakable**: Not affected by abilities like Mold Breaker

### Synergies
Works exceptionally well with:
- Focus Blast users seeking guaranteed accuracy
- Mixed attackers benefiting from situational stat boosts
- Pokemon with naturally high HP pools to safely reach the activation threshold
- Defensive sets that can survive to low HP consistently