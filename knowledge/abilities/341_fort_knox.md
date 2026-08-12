---
id: 341
name: Fort Knox
status: reviewed
character_count: 104
---

# Fort Knox - Ability ID 341

## In-Game Description
"Blocks most damage boosting and multihit abilities."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to all damage boosting ability effects from opponents, other than Parental Bond and Multi Headed.

## Detailed Mechanical Explanation

### Code Implementation

### Primary Definition
**File:** `src/abilities.cc` (lines 3611-3613)
```cpp
constexpr Ability FortKnox = {
    .fortKnox = TRUE,
};
```

### Detection Function
**File:** `src/battle_script_commands.c` (line 981-984)
```cpp
AbilityEnum HasFortKnox(int battler) {
    RETURN_ABILITY_IF_FLAG(battler, FALSE, fortKnox)
    return FALSE;
}
```

### Damage Multiplier Blocking
**File:** `src/battle_util.c` (lines 6828-6840)
```cpp
u16 CalculateAbilityMultipliers(...) {
    u16 multiplier = UQ_4_12(1.0);
    int hasFortKnox = HasFortKnox(battlerDef);

    if (!hasFortKnox) {
        // Apply offensive multipliers only if defender lacks Fort Knox
        for (int sourceBattler = 0; sourceBattler < gBattlersCount; sourceBattler++) {
            ON_ABILITY(sourceBattler, FALSE, 
                gAbilities[ability].onOffensiveMultiplier, 
                // Apply multiplier...
            )
        }
    }
    // Defensive multipliers still apply regardless of Fort Knox
}
```

### Multi-hit Blocking
**File:** `src/battle_script_commands.c` (lines 970-976)
```cpp
MultihitType GetParentalBondType(int battler, MoveEnum move, int moveType) {
    int hasFortKnox = HasFortKnox(target);

    ON_ABILITY(battler, FALSE,
        gAbilities[ability].onParentalBond && 
        (!hasFortKnox || gAbilities[ability].resistsFortKnox),
        int result = gAbilities[ability].onParentalBond(battler, move, moveType);
        if (result) return result
    )
    return MULTIHIT_SINGLE;
}
```

## Detailed Mechanical Explanation

**Fort Knox** is one of the most powerful defensive abilities in Elite Redux, providing comprehensive protection against offensive ability modifiers.

### Core Mechanics
Fort Knox operates by intercepting ability calculations during damage resolution:
1. When a Pokemon with Fort Knox is defending, it prevents the attacker's offensive abilities from applying
2. The ability specifically targets two hooks: `onOffensiveMultiplier` and `onParentalBond`
3. Implementation is remarkably simple: just `.fortKnox = TRUE` in the ability struct

### What Fort Knox Blocks

#### 1. Damage-Boosting Abilities (~158+ abilities)
Blocks ALL abilities that use `onOffensiveMultiplier`, including:

**Type-Based Boosts:**
- Overgrow, Blaze, Torrent (1.5x when HP < 1/3)
- Swarm variants for all types (Bug, Electric, etc.)
- -ate abilities (Pixilate, Refrigerate, Aerilate)

**Physical/Special Boosts:**
- Huge Power/Pure Power (2x Attack)
- Hustle (1.4x physical damage, line 886)
- Sheer Force (1.3x + removes secondary effects)
- Iron Fist (1.2x punching moves)
- Strong Jaw (1.5x biting moves)
- Mega Launcher (1.5x pulse/aura moves)

**Conditional Boosts:**
- Guts (1.5x physical when statused)
- Solar Power (1.5x special in sun)
- Analytic (1.3x when moving last, line 1692)
- Tinted Lens (2x on not very effective moves)
- Technician (1.5x on moves <=60 power)

**Weather/Terrain Boosts:**
- Sand Force (1.3x Rock/Ground/Steel in sand)
- Various weather-specific damage boosts

#### 2. Multi-Hit Abilities
Blocks abilities using `onParentalBond` hook:
- Ice Cold Hunter (2 hits in hail)
- Raging Boxer, Raging Moth, Raging Goddess
- Dual Wield, Dual Hammer
- Multi Headed variants
- Steel Beetle, Balloon Blitz
- Minion Control, Devourer
- And many more multi-hit variants

### Critical Exceptions - Abilities That Bypass Fort Knox

Only two abilities have the `resistsFortKnox = TRUE` flag:

#### 1. Parental Bond (Line 1982-1985)
```cpp
constexpr Ability ParentalBond = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType { 
        return PARENTAL_BOND_HYPER_AGGRESSIVE; 
    },
    .resistsFortKnox = TRUE,
};
```

#### 2. Multi Headed (Line 3669-3676)
```cpp
constexpr Ability MultiHeaded = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType {
        if (gBaseStats[gBattleMons[battler].species].flags & F_TWO_HEADED) 
            return PARENTAL_BOND_HYPER_AGGRESSIVE;
        if (gBaseStats[gBattleMons[battler].species].flags & F_THREE_HEADED) 
            return PARENTAL_BOND_THREE_HEADED;
        return MULTIHIT_SINGLE;
    },
    .resistsFortKnox = TRUE,
};
```

### Other Abilities with Fort Knox Flag

Several abilities also have the `fortKnox = TRUE` flag, making them Fort Knox variants:

1. **Wonder Skin** (Line 1688-1690)
2. **Prim And Proper** (Line 5236-5239) - Fort Knox + Cute Charm effect
3. **Wonder Scale** (Line 8456-8459) - Fort Knox + Shed Skin effect  
4. **Stainless Steel** (Line 8465-8468) - Fort Knox + Wonder Skin + Steel-type conversion

### What Fort Knox Does NOT Block
- Defensive abilities (onDefensiveMultiplier) - these still work normally
- Status moves and their effects
- Base stat modifications (like Intimidate)
- Speed modifications
- Accuracy/Evasion changes
- Weather/terrain setup
- Entry hazards
- Priority modifications
- Critical hit ratio changes

### Pokemon With Fort Knox

Based on `proto/SpeciesList.textproto`, Fort Knox appears on:
- **Geodude line** (Geodude, Graveler, Golem) - as regular ability
- **Various other species** including some as innate abilities
- **20 total instances found** across the species list

Example from Geodude (lines 14925-14954):
```
species {
  id: SPECIES_GEODUDE
  ...
  ability: ABILITY_ROCK_HEAD
  ability: ABILITY_SAND_FORCE
  ability: ABILITY_FORT_KNOX
  innate: ABILITY_LETS_ROLL
  innate: ABILITY_STURDY
  innate: ABILITY_SOLID_ROCK
}
```

### Strategic Implications

Fort Knox essentially neutralizes most offensive ability strategies:
- Shuts down Huge Power sweepers completely
- Prevents multi-hit spam strategies (except Parental Bond/Multi Headed)
- Counters weather-based attackers that rely on damage boosts
- Makes the defender rely purely on base stats and moves
- Forces attackers to use raw power or status moves

This makes Fort Knox Pokemon excellent defensive pivots and walls, particularly against ability-reliant offensive threats. The very limited exceptions (only Parental Bond and Multi Headed) provide the primary reliable methods to break through with ability-enhanced attacks.

### Competitive Analysis

Fort Knox represents one of the strongest defensive tools in Elite Redux:
- **Tier S+ defensive ability** - Nearly unbreakable wall against offensive abilities
- **Counters the meta** - Many powerful sweepers rely on damage-boosting abilities
- **Forces strategic adaptation** - Opponents must rely on base power or status effects
- **Balanced by exceptions** - Parental Bond and Multi Headed provide counterplay
- **Synergizes with defensive stats** - Best on naturally bulky Pokemon

The ability essentially creates a "pure stats" battle environment where abilities don't determine damage output, making it incredibly valuable for defensive team compositions.