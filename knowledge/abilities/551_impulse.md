---
id: 551
name: Impulse
status: reviewed
character_count: 120
---

# Impulse - Ability ID 551

## In-Game Description
"Non-contact moves use the Speed stat for damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Non-contact moves use Speed stat for damage instead of Attack/Special Attack. Choice Scarf does not affect this ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

**IMPULSE** transforms Speed into offensive power for all non-contact moves, creating unique special attacking opportunities.

### Core Mechanics:
- **Trigger**: Any non-contact move
- **Effect**: Replaces Attack/SpA with Speed in damage formula  
- **Stage Application**: Speed stages apply instead of offensive stages
- **Complete Replacement**: Full stat substitution

### Technical Implementation:
```cpp
constexpr Ability Impulse = {
    .onChooseOffensiveStat =
        +[](ON_CHOOSE_OFFENSIVE_STAT) {
            if (!(gBattleMoves[move].contact)) *atkStatToUse = STAT_SPEED;
        },
};
```

### Affected Moves:

**Special Non-Contact** (vast majority):
- Thunderbolt, Thunder, Discharge, Electro Ball
- Flamethrower, Fire Blast, Heat Wave, Overheat
- Ice Beam, Blizzard, Freeze-Dry
- Psychic, Psyshock, Psycho Boost
- Hurricane, Air Slash, Aeroblast
- Hydro Pump, Surf, Scald, Water Pulse
- Energy Ball, Giga Drain, Solar Beam

**Physical Non-Contact**:
- Earthquake, Earth Power, Bulldoze
- Rock Slide, Stone Edge, Rock Blast
- Razor Leaf, Seed Bomb
- Icicle Spear, Icicle Crash
- Poison Sting, Pin Missile

### Pokemon with Impulse:

**As Changeable Ability**:
- Zebstrika (Electric) - Base 116 Speed
- Wattrel (Electric/Flying) - Base 70 Speed
- Kilowattrel (Electric/Flying) - Evolution

**As Innate Ability**:
- One unidentified Pokemon in species data

### Strategic Applications:

1. **Stat Optimization**:
   - Max Speed EVs = Max damage
   - Timid/Jolly nature for +10% damage
   - No investment needed in SpA/Atk

2. **Item Synergy**:
   - Choice Scarf: 1.5x Speed = 1.5x damage
   - Choice Specs: Still 1.5x on special moves
   - Life Orb: Standard 1.3x boost
   - Salac Berry: Speed boost = damage boost

3. **Setup Potential**:
   - Agility/Rock Polish = +2 damage stages
   - Tailwind support = 2x damage
   - Speed Boost ability = incremental power

### Damage Comparison:

**Kilowattrel Example**:
- Special Attack: 300 (base 100)
- Speed: 375 (base 125)
- Using Thunderbolt: 25% more damage with Speed

### Move Selection Strategy:

1. **Prioritize Coverage**:
   - Most special moves are non-contact
   - Wide movepool access maintained
   - Type coverage unaffected

2. **Avoid Contact**:
   - Grass Knot (contact special)
   - Physical contact moves
   - Unless necessary for coverage

3. **Speed Synergy**:
   - Electro Ball (power scales with speed)
   - Weather speed abilities
   - Priority moves still useful

### Counters:

1. **Speed Control**:
   - Trick Room (complete reversal)
   - Paralysis (halves damage)
   - Sticky Web, Icy Wind
   - Tailwind on opposing side

2. **Priority Moves**: Bypass speed entirely

3. **Special Walls**: High SpDef still matters

### Notable Interactions:

**Unique Cases**:
- Psyshock/Psystrike: Use Speed but target Defense
- Body Press: Likely uses Defense as normal
- Foul Play: Unaffected
- Electro Ball: Double benefit from speed

**Weather Speed**:
- Swift Swim + Rain
- Chlorophyll + Sun  
- Sand Rush + Sand
- Slush Rush + Hail

### Common Sets:

**Kilowattrel @ Choice Specs**
- Hurricane
- Thunderbolt
- Heat Wave
- Volt Switch

**Zebstrika @ Life Orb**
- Thunderbolt
- Overheat
- Hidden Power Ice
- Volt Switch

### Competitive Analysis:

Impulse creates special attackers from speed demons, particularly valuable on Pokemon with naturally high Speed but mediocre Special Attack. The ability essentially provides "double value" from Speed investment - both turn order and raw power. Most effective on special attackers due to move distribution.

### Comparison to Similar:
- **Momentum**: Contact moves only
- **Terminal Velocity**: Adds 20% of Speed
- **Slipstream**: Different calculation

### Version Notes:
- Elite Redux exclusive
- Affects both physical and special non-contact
- Part of stat-replacement ability series