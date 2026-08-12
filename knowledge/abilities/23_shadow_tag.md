---
id: 23
name: Shadow Tag
status: reviewed
character_count: 212
---

# Shadow Tag - Ability ID 23

## In-Game Description
"Prevents the enemy from escaping. Ghost types are immune."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all non-Shadow Tag or Ghost-type foes from switching out. Pokemon holding Shed Shell or using a pivot move such as Flip Turn can escape. Activates during the next turn if the user switches in mid battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shadow Tag is a powerful trapping ability that prevents opponents from switching. Implementation in `src/abilities.cc`:

```c
constexpr Ability ShadowTag = {
    .onTrap = +[](ABILITY_ON_TRAP) -> int {
        ON_ABILITY(switchingBattler, FALSE, gAbilities[ability].shadowTag, return FALSE)
        return TRUE;
    },
    .shadowTag = TRUE,
};
```

### Key Features

1. **Trapping Mechanism**:
   - Uses `onTrap` callback triggered when opponent attempts to switch
   - Returns TRUE to prevent the switch
   - Active as long as Shadow Tag user remains on field

2. **Immunity Conditions**:
   - **Ghost-types**: Complete immunity to Shadow Tag's trapping
   - **Other Shadow Tag users**: Can switch freely (checked via `.shadowTag` flag)
   - The `ON_ABILITY` macro checks for these immunities

3. **AI Recognition**:
   - AI Rating: 10 (maximum value, indicating extreme power)
   - AI heavily values this ability for its trapping potential

### Escape Methods
Trapped Pokemon can only escape via:
- **KOing the Shadow Tag user**
- **Switching moves**: U-turn, Volt Switch, Flip Turn, Parting Shot
- **Baton Pass**: Passes stats and switches
- **Teleport**: Switches out with negative priority
- **Emergency Exit/Wimp Out**: Ability-triggered switches
- **Eject Button/Eject Pack**: Item-triggered switches

### Related Abilities

1. **Frenzied Phantom** (ABILITY_FRENZIED_PHANTOM):
   - Combination ability with Parental Bond + Shadow Tag
   - Provides both multi-hit and trapping effects

2. **Similar Trapping Abilities**:
   - **Arena Trap**: Traps only grounded Pokemon
   - **Magnet Pull**: Traps only Steel-types
   - Shadow Tag is the most universal trapper

### Strategic Implications

**Offensive Trapping**:
- Eliminates specific threats by trapping them
- Enables guaranteed KOs on trapped targets
- Pursuit becomes unnecessary with guaranteed trapping

**Support Trapping**:
- Perish Song + Shadow Tag combo
- Setup opportunities against trapped walls
- Encore lock into unfavorable moves

**Team Preview Impact**:
- Opponents must consider Shadow Tag in team selection
- Forces Ghost-type or escape move inclusion
- Creates team building restrictions

### Pokemon with Shadow Tag
In Elite Redux, Shadow Tag appears on:
- Traditional users (Wobbuffet, Wynaut)
- Elite Redux custom forms and Pokemon
- Both as changeable abilities and innate abilities

### Competitive Usage Notes

**Advantages**:
- Removes opponent's switching advantage
- Guarantees favorable matchups
- Eliminates revenge killers
- Controls battle flow

**Limitations**:
- Ghost-types completely immune
- No effect on other Shadow Tag users
- Requires good prediction
- Vulnerable to U-turn momentum

### Counters
- **Ghost-types**: Complete immunity
- **Shed Shell**: Item that allows switching
- **Switch moves**: U-turn, Volt Switch, etc.
- **Shadow Tag**: Mirror matches allow switching
- **Knock Off**: Remove trapping by KOing

### Synergies
- **Perish Song**: Guaranteed KO in 3 turns
- **Pursuit**: Not needed but still effective
- **Setup moves**: Trap walls and set up
- **Encore**: Lock into resisted moves
- **Destiny Bond**: Force lose-lose scenarios

### Doubles/VGC Implications
- Can trap both opponents simultaneously
- Enables partner setup or free attacks
- Countered by Ghost-type leads
- Protect stalling becomes more viable

### Technical Details
- The `.shadowTag = TRUE` flag identifies Shadow Tag-type abilities
- Immunity check prevents Shadow Tag users from trapping each other
- Ghost-type immunity is built into the trapping check

### Version History
Shadow Tag has been consistently powerful but received nerfs over generations:
- Gen 3-5: Trapped everything including Ghost-types
- Gen 6+: Ghost-types became immune
- Elite Redux: Maintains Gen 6+ mechanics with Ghost immunity

The ability remains one of the most powerful in the game due to its ability to control switching, a fundamental battle mechanic.