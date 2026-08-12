---
id: 372
name: Momentum
status: reviewed
character_count: 116
---

# Momentum - Ability ID 372

## In-Game Description
"Contact moves use the Speed stat for damage calculation."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact moves use Speed stat for damage instead of Attack/Special Attack. Choice Scarf does not affect this ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

**MOMENTUM** fundamentally alters damage calculation by replacing offensive stats with Speed for all contact moves.

### Core Mechanics:
- **Trigger**: Any contact move (physical or special)
- **Effect**: Replaces Attack/SpA with Speed in damage formula
- **Stage Application**: Speed stages apply instead of Atk/SpA stages
- **Complete Replacement**: Not additive, full substitution

### Technical Implementation:
**Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 3853-3858)
```cpp
constexpr Ability Momentum = {
    .onChooseOffensiveStat =
        +[](ON_CHOOSE_OFFENSIVE_STAT) {
            if (gBattleMoves[move].contact) *atkStatToUse = STAT_SPEED;
        },
};
```

### Affected Moves:
**Physical Contact** (most common):
- Volt Tackle, Flare Blitz, Double-Edge
- Close Combat, High Jump Kick, Cross Chop
- U-turn, Brave Bird, Acrobatics
- Quick Attack, Extreme Speed, Mach Punch
- All punching moves, Tackle variants

**Special Contact** (rare):
- Grass Knot
- Draining Kiss
- Petal Dance
- Trump Card

### Pokemon with Momentum:

**As Changeable Ability**:
- Crobat (Poison/Flying)
- Furret (Normal)
- Linoone (Normal)
- Zigzagoon (Normal)
- Skarmory Redux (Steel/Flying)
- Skarmory Mega Redux
- Voltorb/Electrode (Electric)
- Electrode Hisuian (Electric/Grass)
- Zebstrika (Electric)
- Accelgor (Bug)
- Tsareena Redux (Grass)
- Inteleon (Water)
- Velozel (Custom)

**As Innate Ability**:
- Iron Leaves (Grass/Psychic)

### Strategic Applications:

1. **Stat Efficiency**:
   - 252 Speed EVs provide both offense and turn order
   - No need to split between Speed and Attack
   - Can invest remaining EVs in bulk

2. **Setup Synergy**:
   - Agility = +2 to damage
   - Rock Polish = +2 to damage
   - Tailwind = double damage for team
   - Speed Boost = cumulative damage increase

3. **Item Optimization**:
   - Choice Scarf: 1.5x Speed = 1.5x damage
   - Life Orb: Standard 1.3x boost
   - Choice Band: Still 1.5x on physical contact

### Damage Example:
**Electrode with Momentum**:
- Attack: 150 (base 50)
- Speed: 450 (base 150)
- Using Volt Tackle: 3x more damage with Speed

### Counters:
1. **Speed Control**:
   - Paralysis (-50% Speed = -50% damage)
   - Sticky Web entry hazard
   - Icy Wind, Electroweb
   - Trick Room reversal

2. **Contact Punishment**:
   - Rough Skin, Iron Barbs
   - Rocky Helmet
   - Flame Body, Static
   - Spiky Shield variants

3. **Priority Moves**: Bypass speed advantage

### Notable Synergies:

**Weather/Abilities**:
- Swift Swim (2x Speed in rain)
- Chlorophyll (2x Speed in sun)
- Sand Rush (2x Speed in sand)
- Slush Rush (2x Speed in hail)

**Support**:
- Baton Pass (receive Speed boosts)
- Flame Charge (self-boost)
- Tailwind (team support)

### Common Sets:

**Zebstrika @ Choice Scarf**
- Volt Tackle
- Flare Blitz
- High Jump Kick
- U-turn

**Crobat @ Life Orb**
- Brave Bird
- Cross Poison
- U-turn
- Roost

### Important Interactions:
- Burn does NOT reduce damage (affects Attack only)
- Intimidate does NOT reduce damage
- Power Split averages Speed if using contact
- Foul Play ignores Momentum

### Competitive Value:
Momentum creates a unique niche for speed-focused Pokemon, turning defensive speedsters into offensive threats. The ability rewards aggressive speed control and synergizes with the fast-paced Elite Redux meta. Investment simplicity and setup potential make it extremely valuable on the right Pokemon.

### Version Notes:
- Elite Redux exclusive ability
- Works with both physical and special contact
- Integrates with 4-ability system