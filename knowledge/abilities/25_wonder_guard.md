---
id: 25
name: Wonder Guard
status: reviewed
character_count: 182
---

# Wonder Guard - Ability ID 25

## In-Game Description
"Is only hit by Super-effective attacks or indirect damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Only super-effective attacks or indirect damage can hurt the user. All other direct attacks deal zero damage. Other sources such as poison or ability damage still function as normal.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Wonder Guard provides complete immunity to all direct damage that isn't super-effective (2x or greater). The ability checks type effectiveness after damage calculation and sets damage to 0 if the modifier is less than 2.0x.

### Technical Implementation
```cpp
constexpr Ability WonderGuard = {
    .onAfterTypeEffectiveness =
        +[](ON_AFTER_TYPE_EFFECTIVENESS) {
            if (*mod < UQ_4_12(2.0)) *mod = 0;
        },
    .onAfterTypeEffectivenessFor = APPLY_ON_TARGET,
    .breakable = TRUE,
    .randomizerBanned = TRUE,
};
```

Additional check in `battle_util.c`:
```c
if (abilityDef == ABILITY_WONDER_GUARD && modifier <= UQ_4_12(1.0) && gBattleMoves[move].power) 
    modifier = UQ_4_12(0.0);
```

### Damage Immunities
**Blocked damage types:**
- Not very effective moves (0.5x)
- Neutral effectiveness moves (1x)  
- Any damaging move below 2x effectiveness

**Damage that bypasses Wonder Guard:**
- Super-effective moves (2x or greater)
- Status conditions (poison, burn, etc.)
- Weather damage (sandstorm, hail)
- Entry hazards (Stealth Rock, Spikes)
- Leech Seed, Curse, Nightmare
- Recoil damage
- Struggle (typeless damage)

### Ability Interactions
**Can be bypassed by:**
- Mold Breaker (and variants like Turboblaze, Teravolt)
- Any ability with mold-breaking properties

**Cannot be copied by:**
- Skill Swap (explicitly banned)
- Role Play (explicitly banned)
- Trace (would be too powerful)

### Restrictions
- Banned from randomizer modes
- Cannot be given to other Pokemon through normal means
- Specifically designed for Shedinja's 1 HP gimmick

### Shedinja in Elite Redux
**Stats:** 1 HP / 90 Atk / 45 Def / 90 SpA / 30 SpD / 80 Spe

**Type:** Bug/Ghost

**Abilities:**
- Innate: Wonder Guard, Haunted Spirit, Adaptability
- Changeable: Overcoat, Suppress, Recurring Nightmare

**Type effectiveness (with Wonder Guard):**
- Immune to: Normal, Fighting, Poison, Ground, Bug, Steel, Water, Grass, Electric, Psychic, Ice, Dragon, Fairy
- Vulnerable to: Flying, Rock, Ghost, Fire, Dark (all 2x effective)

### Strategic Implications
- **Team preview**: Opponents must ensure they have super-effective coverage
- **Hazard weakness**: Entry hazards bypass Wonder Guard
- **Status vulnerability**: Can be worn down by poison/burn
- **Weather teams**: Sandstorm and hail chip through Wonder Guard

### Common Strategies
**Using Wonder Guard:**
- Heavy Duty Boots to avoid hazards
- Toxic Spikes immunity (Poison type move)
- Safety Goggles for weather immunity
- Substitute to block status

**Countering Wonder Guard:**
- Entry hazards (especially Stealth Rock)
- Weather damage
- Status moves (Will-O-Wisp, Toxic)
- Mold Breaker abilities
- Super-effective coverage

### Competitive Usage Notes
Wonder Guard Shedinja creates a unique team-building constraint where opponents must have answers or lose to it. Despite only 1 HP, proper support can make Shedinja surprisingly difficult to remove. The ability is balanced by numerous indirect damage sources and the prevalence of super-effective coverage in competitive play.

### Version History
Wonder Guard has remained mechanically consistent since Generation 3. The main changes have been the addition of new ways to bypass it (Mold Breaker in Gen 4) and new forms of indirect damage. The ability remains exclusive to Shedinja in official games, though ROM hacks like Elite Redux may expand its availability.