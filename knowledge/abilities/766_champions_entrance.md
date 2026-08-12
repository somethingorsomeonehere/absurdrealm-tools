---
id: 766
name: Champions Entrance
status: reviewed
character_count: 184
---

# Champions Entrance - Ability ID 766

## In-Game Description
"Intimidate + Violent Rush"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, the user drops the Attack stat of all opposing Pokemon by one stage. The user gains a 50% Speed boost and 20% Attack boost on their first turn after switching in.


## Detailed Mechanical Explanation
*For Discord/reference use*

Champions Entrance is a powerful combination ability that triggers two distinct effects when the Pokemon switches into battle:

### Intimidate Component:
- Activates first upon switching in
- Lowers the Attack stat of all opposing Pokemon by one stage
- Functions identically to the standard Intimidate ability
- Cannot be prevented by abilities like Oblivious or Own Tempo that normally block intimidation

### Violent Rush Component:
- Activates immediately after the Intimidate effect
- Sets a temporary "violent rush" flag that lasts only for the first turn the Pokemon is active
- Provides two stat modifications while the flag is active:
  - **Speed**: Increased by 50% (multiplied by 1.5)
  - **Attack**: Increased by 20% (multiplied by 1.2)

### Technical Implementation:
- Defined in `src/abilities.cc` as a combination of `Intimidate.onEntry` and `ViolentRush.onEntry`
- The violent rush flag is stored in `gVolatileStructs[battler].violentRush`
- Speed boost is applied in `GetSpeedFromAbilities()` in `src/battle_main.c`
- Attack boost is applied in `CalculateBaseDamage()` in `src/battle_util.c` 
- The violent rush effect is automatically cleared at the end of the first turn via `CLEAR_ONE_TURN(violentRush)`

### Strategic Applications:
- Excellent for lead Pokemon or pivoting strategies
- The Intimidate component weakens physical attackers on the opposing team
- The Violent Rush component allows for immediate offensive pressure or fast setup moves
- Particularly effective on Pokemon with high base Attack and Speed stats
- Can potentially outspeed and KO threats that would normally be faster
- The Attack boost stacks with other offensive boosts like Choice Band or stat stages

### Interactions:
- Intimidate component can be blocked by abilities like Clear Body, Hyper Cutter, or White Smoke
- Violent Rush boosts are not affected by stat stage modifications (they're multipliers applied to base stats)
- The ability announces both effects with appropriate battle messages when triggered
- Works in both single and double battles, affecting all opposing Pokemon with Intimidate

This ability is particularly valuable on aggressive Pokemon that want to immediately apply pressure while also providing team support through Attack reduction of physical threats.