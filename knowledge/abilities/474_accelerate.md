---
id: 474
name: Accelerate
status: reviewed
character_count: 107
---

# Accelerate - Ability ID 474

## In-Game Description
"Moves that need a charge turn are now used instantly."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Accelerate eliminates the charging turn requirement for two-turn moves, allowing them to be used instantly.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Accelerate is an offensive utility ability that bypasses the charging turn requirement for two-turn moves. This allows Pokemon to immediately use powerful moves that would normally require preparation.

### Activation Conditions
- **Move requirement**: Must be using a move with a charging turn
- **Timing**: Takes effect when the move is selected, preventing the charging phase
- **No restrictions**: Works on all two-turn moves regardless of conditions

### Affected Move Categories

#### EFFECT_TWO_TURN_SECONDARY (Stat-boosting charge moves)
- **Skull Bash**: Normal/Physical, 120 BP, raises Attack during charge
- **Sky Attack**: Flying/Physical, 140 BP, raises Attack during charge  
- **Meteor Beam**: Rock/Special, 120 BP, raises Sp. Attack during charge
- **Freeze Shock**: Ice/Physical, 140 BP, 30% paralysis chance
- **Ice Burn**: Ice/Special, 140 BP, 30% burn chance

#### EFFECT_SOLARBEAM (Weather-affected charge moves)
- **Solar Beam**: Grass/Special, 120 BP, skips charge in sun normally
- **Electro Shot**: Electric/Special, 120 BP, skips charge in rain normally

#### EFFECT_SEMI_INVULNERABLE (Invulnerability-granting moves)
- **Fly**: Flying/Physical, 110 BP, user becomes untargetable
- **Dig**: Ground/Physical, 110 BP, user becomes untargetable
- **Dive**: Water/Physical, 110 BP, user becomes untargetable
- **Bounce**: Flying/Physical, 100 BP, 30% paralysis chance
- **Shadow Force**: Ghost/Physical, 120 BP, ignores protection
- **Phantom Force**: Ghost/Physical, 90 BP, ignores protection
- **Shadow Sneak** (Elite Redux): Dark/Physical, 120 BP
- **Stalwart Strike**: Rock/Physical, 110 BP
- **Possum Play**: Normal/Physical, 80 BP, 30% flinch chance
- **Toxic Dive**: Poison/Physical, 110 BP, 20% poison chance

#### EFFECT_BIDE (Damage-storing moves)
- **Bide**: Normal/Physical, stores damage for 2-3 turns then retaliates

### Technical Implementation

```c
// In battle_script_commands.c, line 3012-3013
if (gBattleScripting.moveEffect == MOVE_EFFECT_CHARGING) {
    if (gBattleMoves[gCurrentMove].effect == EFFECT_SOLARBEAM &&
        (IsBattlerWeatherAffected(gActiveBattler, WEATHER_SUN_ANY) || HasChloroplast(gActiveBattler)))
        gRoundStructs[gActiveBattler].chargingTurn = FALSE;
    else if (BattlerHasAbility(gActiveBattler, ABILITY_ACCELERATE, FALSE))
        gRoundStructs[gActiveBattler].chargingTurn = FALSE;
}

// In IsMoveAffectedByParentalBond function, line 13117
if (gBattleMoves[move].twoTurnMove && !BattlerHasAbility(battlerId, ABILITY_ACCELERATE, FALSE)) 
    return FALSE;
```

### Important Interactions

#### Parental Bond Compatibility  
- **Works with multi-hit abilities**: Accelerate allows two-turn moves to be affected by Parental Bond
- **Instant double hits**: Can get double Solar Beam, Sky Attack, etc. without charging

#### Weather Interactions
- **Overrides weather**: Even works on Solar Beam outside of sun and Electro Shot outside of rain
- **Stat boosts preserved**: Still get Attack boost from Sky Attack/Skull Bash instantly
- **No weather dependency**: Unlike natural weather interactions, always works

#### Status and Field Effects
- **Status immunity**: Cannot be disabled by paralysis, sleep, or freeze during charge turn (because there is none)
- **Priority moves**: Two-turn moves still use their normal priority when accelerated
- **Protection bypassing**: Semi-invulnerable moves still bypass Protect when accelerated

### Strategic Implications

#### Offensive Advantages
- **Immediate power**: Access to 120-140 BP moves without setup time
- **Unpredictability**: Opponents cannot prepare for two-turn moves
- **Action economy**: No turns wasted on charging
- **Combo potential**: Can use powerful moves in weather/terrain setups immediately

#### Defensive Considerations  
- **No protection phase**: Semi-invulnerable moves lose their defensive utility
- **Telegraphing**: Moves are still announced, allowing for prediction
- **PP efficiency**: Uses same PP but gets immediate effect

### Common Users Analysis

#### Fast Attackers
- **Pidgeot/Pidgeot-Mega**: Normal/Flying, benefits from instant Sky Attack
- **Barraskewda**: Water type, gets instant Bounce/Dive coverage
- **Absol**: Dark type, instant Shadow Force for STAB

#### Bulky Attackers  
- **Kabutops**: Rock/Water, fossil Pokemon with Shell Armor synergy
- **Toxapex**: Water/Poison, surprising offensive utility with instant Dive

#### Weather Sweepers
- **Solar Beam users**: Can fire immediately even outside sun
- **Mixed attackers**: Benefits from stat-boosting charge moves like Meteor Beam

### Competitive Usage Notes

#### Advantages
- **Surprise factor**: Unexpected immediate power from typically setup moves
- **Weather independence**: Solar Beam works without sun requirement
- **Speed control**: Fast Pokemon get immediate access to powerful moves
- **Versatility**: Works with both physical and special charge moves

#### Limitations
- **Move pool dependent**: Only valuable if Pokemon learns relevant moves
- **Predictable**: Once ability is known, opponents can prepare
- **No defensive benefit**: Loses the protective aspect of semi-invulnerable moves
- **Limited distribution**: Not widely available

### Counters and Responses

#### Direct Counters
- **Protect variants**: Still blocks the moves (except Shadow Force/Phantom Force)
- **Type resistances**: Moves still follow type effectiveness
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Speed control**: Outspeed and KO before they can attack

#### Strategic Responses
- **Prediction switching**: Switch to resist the expected powerful move
- **Priority moves**: Use priority to attack first
- **Status infliction**: Paralyze to reduce speed advantage
- **Entry hazards**: Chip damage limits longevity

### Synergies

#### Team Support
- **Weather setters**: Complements but doesn't require weather
- **Speed control**: Tailwind, Trick Room for positioning
- **Stat boosters**: Baton Pass setups with instant powerful moves
- **Entry hazard support**: Stealth Rock for guaranteed damage

#### Item Synergies
- **Choice items**: Lock into powerful moves immediately
- **Life Orb**: Boost the power of instant charge moves
- **Power Herb**: Becomes redundant with this ability
- **Type-boosting items**: Enhance specific move types

### Version History
- **Elite Redux exclusive**: New ability created for the hack
- **Current implementation**: Full compatibility with all two-turn move effects
- **Future potential**: May be expanded to affect other delayed moves

### Pokemon Distribution
Currently available on:
- **Pidgey line**: Normal/Flying, early game access
- **Kabutops**: Rock/Water fossil, innate ability
- **Lunatone/Solrock**: Rock/Psychic, various forms
- **Barraskewda line**: Water, late game power
- **Pyukumuku line**: Water, defensive pivot
- **Naganadel**: Poison/Dragon, ultra beast
- **Various others**: Check individual Pokemon for availability

### Design Philosophy
Accelerate represents the concept of supernatural speed and efficiency, allowing Pokemon to bypass the natural limitations of powerful moves. It rewards aggressive play and provides unique offensive options while maintaining the same resource costs (PP) as the original moves.