---
id: 354
name: Weather Control
status: reviewed
character_count: 240
---

# Weather Control - Ability ID 354

## In-Game Description
"Negates all weather based moves from enemies."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants immunity to weather-based moves: Thunder, Solar Beam/Blade, Hurricane, Blizzard, Silver Wind, Weather Ball, all Storm moves (not including Magma, Leaf, or Diamond), Sheer Cold, and Pledge moves. Does not stop weather setup or damage. 

## Detailed Mechanical Explanation

### Core Mechanics
Weather Control provides complete immunity to moves flagged as `FLAG_WEATHER_BASED` in the game's code. This is a hardcoded list of 18 specific moves, not a dynamic weather interaction. The ability shares its implementation with Delta Stream, using the same `onImmune` function.

### Code Implementation

Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` at line 3741:

```cpp
constexpr Ability WeatherControl = {
    .onImmune = DeltaStream.onImmune,
    .breakable = TRUE,
};
```

The immunity logic (shared with Delta Stream) at line 2043:

```cpp
.onImmune = +[](ON_IMMUNE) -> int {
    CHECK(gBattleMoves[move].flags & FLAG_WEATHER_BASED)
    CHECK_NOT(GetBattlerBattleMoveTargetFlags(move, attacker) & MOVE_TARGET_USER)
    *immunityScript = BattleScript_SoundproofProtected;
    return TRUE;
},
```

### Implementation Details
- **Hook**: Uses `onImmune` (same as Delta Stream ability #191)
- **Trigger**: When opponent uses a move with `FLAG_WEATHER_BASED` flag
- **Effect**: Complete immunity - move fails with "It doesn't affect [Pokemon]..."
- **Battle Message**: Uses the same "protected by its ability" message as Soundproof
- **Self-Exception**: The user's own weather-based moves are unaffected (prevents self-immunity)
- **Breakable**: Can be bypassed by Mold Breaker and similar abilities (`breakable = TRUE`)

### Complete List of Blocked Moves
1. **Bleakwind Storm** - Ice-type special move
2. **Blizzard** - Ice-type special move (normally gets accuracy boost in hail)
3. **Depletion Beam** - Normal-type special move
4. **Eerie Spell** - Psychic-type special move
5. **Fire Pledge** - Fire-type special pledge move
6. **Grass Pledge** - Grass-type special pledge move
7. **Hurricane** - Flying-type special move (normally gets accuracy boost in rain)
8. **Ominous Wind** - Ghost-type special move with stat boost chance
9. **Revival Blessing** - Normal-type status move (revival)
10. **Sandsear Storm** - Ground-type special move
11. **Sheer Cold** - Ice-type OHKO move
12. **Solar Beam** - Grass-type special move (normally charges faster in sun)
13. **Solar Blade** - Grass-type physical move (physical Solar Beam)
14. **Springtide Storm** - Fairy-type special move
15. **Thunder** - Electric-type special move (normally gets accuracy boost in rain)
16. **Water Pledge** - Water-type special pledge move
17. **Weather Ball** - Normal-type special move (changes type with weather)
18. **Wildbolt Storm** - Electric-type special move

### What It Does NOT Block
- Weather-setting moves (Rain Dance, Sunny Day, etc.)
- Moves that get power boosts from weather (Water moves in rain, Fire moves in sun)
- Moves with weather-dependent secondary effects (Morning Sun healing varies)
- Any moves not in the above list of 18

### Comparison to Similar Abilities
- **Delta Stream**: Also blocks these 18 moves PLUS sets Strong Winds weather
- **Cloud Nine/Air Lock**: Suppress weather effects but don't block specific moves
- **Magic Guard**: Prevents weather damage but doesn't block weather moves
- **Soundproof**: Similar immunity mechanism but for sound-based moves
- **Bulletproof**: Similar immunity mechanism but for ball and bomb moves

## Pokemon with Weather Control

Based on the species data, Weather Control appears primarily as an **innate ability** on the following Pokemon:

### Water-Type Weather Masters
- **Psyduck** - Duck Pokemon with psychic weather control
- **Golduck** - Evolved form with enhanced weather mastery

### The Weather Pokemon
- **Castform (all forms)** - Normal, Sunny, Rainy, Snowy, and Shadow forms
  - Base Castform and all weather-transformed variants
  - Thematically perfect fit as the Weather Pokemon

### Legendary Weather Controllers  
- **Dragonite** - Pseudo-legendary dragon with weather influence
- **Forces of Nature Trio**:
  - **Tornadus** (Incarnate and Therian forms) - Cyclone Pokemon
  - **Thundurus** (Incarnate and Therian forms) - Bolt Strike Pokemon  
  - **Landorus** (Incarnate and Therian forms) - Abundance Pokemon
- **Rayquaza** - Sky High Pokemon that controls atmospheric conditions
- **Enamorus** (Incarnate and Therian forms) - Love-Hate Pokemon

These Pokemon typically have Weather Control as one of their three innate abilities, alongside other powerful abilities that complement their legendary status and weather theme.

### Strategic Implications
Weather Control is a defensive ability that hard-counters specific moves rather than weather conditions. It's particularly effective against:
- **Rain teams** relying on Thunder's perfect accuracy
- **Sun teams** using Solar Beam/Solar Blade for instant charging
- **Hail teams** with Blizzard's enhanced accuracy
- **Storm move users** wielding the powerful signature Storm moves
- **Weather Ball abusers** who rely on type/power changes

The ability name is somewhat misleading - it doesn't control weather conditions but rather blocks a specific set of moves that happen to be weather-related in theme or function. This makes it a specialized defensive tool rather than a weather manipulation ability.

