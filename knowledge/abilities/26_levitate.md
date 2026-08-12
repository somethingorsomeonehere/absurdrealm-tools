---
id: 26
name: Levitate
status: reviewed
character_count: 140
---

# Levitate - Ability ID 26

## In-Game Description
"Immune to Ground-type moves. Ups own Flying moves by 1.25x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user is immune to Ground-type moves and other ground effects such as Spikes and terrains. Boosts the damage of Flying-type moves by 25%.

## Detailed Mechanical Explanation
*For Discord/reference use*

**LEVITATE** is a dual-purpose ability providing both defensive immunity and offensive enhancement for flying-based strategies.

### Ground Immunity Mechanics:
- **Coverage**: Complete immunity to ALL Ground-type moves, both damaging and non-damaging
- **Implementation**: Uses the `.levitate = TRUE` flag, processed through `CheckLevitatingEffects()`
- **Affected Moves**: Earthquake, Earth Power, Magnitude, Dig, Sand Attack, Mud Shot, Spikes (when switching in), etc.
- **Bypass Methods**: NONE - Cannot be negated by Gravity, Smack Down, or Thousand Arrows (unlike true Flying-types)
- **Message**: Shows "{Pokemon} avoided the attack!" when hit by Ground moves

### Flying-Type Boost Mechanics:
- **Multiplier**: 1.25x power boost to ALL Flying-type moves
- **Application**: Applied during damage calculation via `onOffensiveMultiplier` hook
- **Coverage**: Affects all Flying moves regardless of category (Physical, Special, Status that deal damage)

### Technical Implementation:
```cpp
constexpr Ability Levitate = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FLYING) MUL(1.25);
        },
    .breakable = TRUE,
    .levitate = TRUE,
};
```

Ground immunity check:
```c
static AbilityEnum CheckLevitatingEffects(u8 battlerId) {
    if (gStatuses3[battlerId] & STATUS3_TELEKINESIS)
        return TRUE;
    else if (gStatuses3[battlerId] & STATUS3_MAGNET_RISE)
        return TRUE;
    else if (GetBattlerHoldEffect(battlerId, TRUE) == HOLD_EFFECT_AIR_BALLOON)
        return TRUE;
    RETURN_ABILITY_IF_FLAG(battlerId, TRUE, levitate)
    return FALSE;
}
```

### Complete List of Affected Ground Moves:
**Damaging Moves**: Earthquake, Earth Power, Magnitude, Dig, Mud Shot, Mud Bomb, Bulldoze, Drill Run, Bone Club, Bonemerang, Bone Rush, Fissure, etc.

**Status Moves**: Sand Attack, Mud-Slap, Spikes (entry damage), Toxic Spikes (entry poison), etc.

### Interactions with Other Mechanics:
- **vs Iron Ball**: Levitate immunity overrides Iron Ball's grounding effect
- **vs Gravity**: Unlike Flying-types, Levitate users remain immune to Ground moves even under Gravity
- **vs Smack Down**: Cannot be grounded by Smack Down like Flying-types can
- **vs Thousand Arrows**: Maintains immunity (unlike Flying-types which lose it)
- **Mold Breaker**: Can be bypassed by Mold Breaker, Teravolt, and Turboblaze
- **Ring Target**: Immunity is negated if holding Ring Target

### Strategic Applications:
1. **Defensive Pivot**: Safe switch-in against Ground-type attacks
2. **Earthquake Immunity**: Can use Earthquake alongside teammates without self-damage
3. **Flying STAB Enhancement**: 25% boost makes Flying moves significantly more threatening
4. **Utility Counter**: Immune to entry hazard damage from Spikes

### Example Damage Calculations:
- **Hurricane** (110 BP) with Levitate: 110 x 1.25 = 137.5 effective BP
- **Air Slash** (75 BP) with Levitate: 75 x 1.25 = 93.75 effective BP
- **Earthquake** vs Levitate user: 0 damage (complete immunity)

### Common Users:
- **Charizard** (innate): Fire/Dragon type with Levitate as innate ability
- **Charizard-Mega-X** (innate): Fire/Dragon type retains Levitate
- **Venomoth** (innate): Bug/Poison type with Levitate innate
- **Crobat** (innate): Poison/Flying type with Levitate innate

### Competitive Advantages:
- Earthquake immunity provides excellent defensive utility
- Flying-type boost enhances STAB or coverage moves
- Cannot be grounded by most conventional methods
- Valuable on balanced teams for Ground immunity

### Counters and Limitations:
- **Mold Breaker family**: Completely bypasses both immunity and boost
- **Ring Target**: Negates Ground immunity if forced to hold it
- **Breakable**: Can be suppressed by abilities like Neutralizing Gas
- No protection against other move types

### Ability Synergies:
- **With Flying-type STAB**: Double benefit from type matching and ability boost
- **With Choice items**: Enhanced Flying moves become significantly more powerful
- **With Life Orb**: Stacks multiplicatively with the 1.25x boost
- **Team synergy**: Allows safe use of Earthquake by teammates

### Version History:
- **Gen 3-4**: Ground immunity only
- **Gen 5+**: Various games maintained immunity
- **Elite Redux**: Added 1.25x Flying-type move boost, making it more offensively viable