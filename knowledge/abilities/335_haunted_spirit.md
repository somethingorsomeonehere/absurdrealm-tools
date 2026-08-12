---
id: 335
name: Haunted Spirit
status: reviewed
character_count: 194
---

# Haunted Spirit - Ability ID 335

## In-Game Description
"Curses the attacker when knocked out by a contact move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Curses the attacker when knocked out by a direct hit. The curse inflicts 25% max HP damage per turn until the cursed Pokemon switches out or faints. Ghost-type attackers are immune to the curse.

## Detailed Mechanical Explanation

### Overview
Haunted Spirit is a defensive retaliation ability that punishes opponents for knocking out its user with contact moves. When the Pokemon with this ability faints, it leaves behind a spiritual curse that continuously damages the attacker.

### Mechanics

### Activation Conditions
1. **KO Requirement**: The Pokemon must be knocked out (reduced to 0 HP)
2. **Contact Move**: The move that deals the final blow must make contact
3. **Attacker Type**: The attacker cannot be a Ghost-type Pokemon
4. **Status Check**: The attacker must not already be cursed

### Curse Effect Details
- **Damage**: 1/4 of the cursed Pokemon's maximum HP per turn
- **Timing**: Damage occurs at the end of each turn during the "curse damage" phase
- **Duration**: Persists until the cursed Pokemon switches out or faints
- **Minimum Damage**: At least 1 HP if calculated damage would be 0
- **Protection**: Magic Guard and similar abilities prevent curse damage

### Implementation Specifics
The ability uses the `onDefender` trigger with the following checks:
- `ShouldApplyOnHitAffect(attacker)` - Standard hit effect validation
- `!IsBattlerAlive(battler)` - Pokemon must be KO'd
- `!IS_BATTLER_OF_TYPE(attacker, TYPE_GHOST)` - Ghost-types are immune
- `!(gBattleMons[attacker].status2 & STATUS2_CURSED)` - No double cursing
- `IsMoveMakingContact(move, attacker)` - Contact move requirement

## Strategic Applications

### Defensive Usage
- **Tank Punishment**: Forces opponents to think twice about using contact moves to finish off bulky Pokemon
- **Physical Wall Counter**: Particularly effective against physical attackers who rely on contact moves
- **Entry Hazard Synergy**: Combines well with hazards to wear down switch-ins after the curse

### Team Support
- **Momentum Control**: The curse effect can force switches, giving your team positional advantage
- **Late Game Pressure**: Particularly valuable in endgame scenarios where HP preservation is crucial
- **Wallbreaker Deterrent**: Discourages common contact-based wallbreaking moves

## Counterplay

### Direct Counters
- **Ghost-type Attackers**: Completely immune to the curse effect
- **Non-contact Moves**: Special attacks and non-contact physical moves avoid the trigger
- **Magic Guard**: Prevents curse damage entirely
- **Quick Switching**: Immediate switch-out removes the curse status

### Indirect Counters
- **Heal Bell/Aromatherapy**: Team-based status removal can cleanse curse
- **Natural Cure**: Switching out removes the curse anyway
- **Priority Moves**: Many priority moves are non-contact (Quick Attack, Bullet Punch exceptions noted)

## Notable Interactions

### Status Mechanics
- Curse stacks with other damage-over-time effects (poison, burn, etc.)
- Does not prevent the cursed Pokemon from using moves
- Visual indicator appears on the cursed Pokemon during battle
- AI recognizes curse status when calculating move values

### Battle Scenarios
- **U-turn/Volt Switch**: These contact moves can trigger the ability but immediately switch out
- **Multi-hit Moves**: Only the final hit needs to cause the KO for the curse to activate
- **Substitute**: The ability can trigger even if Substitute is present when KO'd

## Competitive Analysis

### Strengths
- Provides guaranteed retaliation against physical attackers
- No immunity beyond Ghost-types and Magic Guard
- Significant damage output (25% max HP per turn)
- Psychological deterrent effect

### Weaknesses
- Requires the Pokemon to faint to activate
- Limited to contact moves only
- Ghost-types completely bypass the effect
- One-time use per battle appearance

### Tier Placement: B-tier
While situational, Haunted Spirit provides valuable utility in the right circumstances. The ability to guarantee significant damage after fainting makes it a respectable defensive option, though its reliance on specific conditions prevents it from reaching higher tiers.

## Pokemon Distribution
This ability appears on Ghost-type Pokemon that thematically align with spiritual revenge concepts. Check the species data files for current distribution.

## Related Abilities
- **Aftermath**: Damages attackers when KO'd by contact moves (fixed damage)
- **Innards Out**: Damages attackers based on remaining HP when KO'd
- **Mummy**: Spreads ability to contact move users
- **Vengeful Spirit**: Combines Haunted Spirit with Vengeance effects

## Code References
- **Implementation**: `src/abilities.cc` (HauntedSpirit function)
- **Battle Script**: `data/battle_scripts_1.s` (BattleScript_HauntedSpiritActivated)
- **Status Handling**: `src/battle_util.c` (ENDTURN_CURSE case)
- **Ability ID**: 335 (ABILITY_HAUNTED_SPIRIT)

