---
id: 794
name: Deadly Precision
status: reviewed
character_count: 174
---

# Deadly Precision - Ability ID 794

## In-Game Description
"Super-effective moves never miss and ignore abilities."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Always land super effective attacks on the opponent. Allows super effective attacks to ignore the target's abilities and innates that interfere with effects or reduce damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Deadly Precision provides two key benefits when using super-effective moves (2.0x effectiveness or higher):

1. **Perfect Accuracy**: Super-effective moves automatically hit regardless of accuracy modifiers
2. **Ability Ignoring**: Super-effective moves bypass the target's defensive abilities

### Activation Conditions
- Move must deal super-effective damage (2.0x type effectiveness or higher)
- Works with both single-type and dual-type super-effective matchups
- Does not activate on moves that are normally effective (1.0x) or not very effective (<1.0x)
- Only applies to attacking moves, not status moves

### Technical Implementation
The ability works through two distinct code paths:

**Accuracy Component**:
```cpp
.onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
    CHECK_NOT(IS_MOVE_STATUS(move))
    CHECK(CalcTypeEffectivenessMultiplier(move, moveType, battler, target, TRUE) >= UQ_4_12(2.0))
    return ACCURACY_HITS_IF_POSSIBLE;
}
```

**Ability Ignoring Component**:
```cpp
// In battle_script_commands.c attackcanceler function
if (BATTLER_HAS_ABILITY(gBattlerAttacker, ABILITY_DEADLY_PRECISION)) 
    gHitMarker |= HITMARKER_MOLD_BREAKER;
// Only applies if move is super-effective
if (!isMoldBreakerActive && typeEffectiveness < UQ_4_12(2.0)) 
    gHitMarker &= ~HITMARKER_MOLD_BREAKER;
```

### Affected Defensive Abilities
Deadly Precision bypasses all defensive abilities when landing super-effective hits, including:

**Type Immunities**:
- Levitate (Ground immunity)
- Flash Fire (Fire immunity/boost)
- Water Absorb (Water immunity/heal)
- Volt Absorb (Electric immunity/heal)
- Motor Drive (Electric immunity/Speed boost)
- Sap Sipper (Grass immunity/Attack boost)
- Storm Drain (Water immunity/Special Attack boost)
- Lightning Rod (Electric immunity/Special Attack boost)

**Damage Reduction**:
- Filter/Solid Rock (super-effective damage reduction)
- Multiscale (full HP damage reduction)
- Shadow Shield (full HP damage reduction)
- Thick Fat (Fire/Ice damage reduction)
- Heatproof (Fire damage reduction)
- Dry Skin (Fire weakness amplification is bypassed)

**Other Defensive Effects**:
- Wonder Guard (only super-effective moves hit - but this bypasses it entirely)
- Magic Guard (indirect damage immunity)
- Overcoat (weather/powder immunity)

### Interactions with Other Mechanics

**Does NOT bypass**:
- Items (Focus Sash, Air Balloon, etc.)
- Type changes from moves like Soak or Forest's Curse
- Stat changes or defensive stat modifications
- Weather effects
- Terrain effects
- Entry hazards

**Stacks with**:
- Other accuracy-boosting effects (though not needed due to perfect accuracy)
- Other ability-ignoring effects like Mold Breaker
- Damage-boosting abilities and items

### Strategic Implications

**Offensive Benefits**:
- Guarantees super-effective moves connect against evasive opponents
- Eliminates defensive ability counterplay against super-effective coverage
- Particularly powerful on mixed attackers with wide coverage
- Excellent for breaking through defensive cores

**Best Coverage Moves**:
- Ice Beam/Blizzard (hits Grass/Ground/Flying/Dragon)
- Thunderbolt (hits Water/Flying)
- Earthquake (hits Fire/Electric/Poison/Rock/Steel)
- Rock Slide (hits Fire/Ice/Flying/Bug)

### Common Users
While the specific Pokemon with this ability aren't definitively known from the code analysis, it would typically be found on:
- Offensive Pokemon with diverse movepools
- Mixed attackers that can leverage both physical and special super-effective moves
- Pokemon designed to break through defensive strategies

### Competitive Usage Notes

**Pros**:
- Eliminates accuracy-based counterplay on super-effective moves
- Bypasses common defensive abilities
- Creates reliable offensive pressure
- Excellent for wallbreaking strategies

**Cons**:
- Only works on super-effective moves
- No benefit against neutrally effective or resisted moves
- Doesn't provide defensive utility
- Relatively situational activation

### Counters

**Direct Counters**:
- Focus Sash/Sturdy (survives one hit regardless)
- Air Balloon (prevents Ground-type super-effective hits)
- Resist Berries (reduce super-effective damage)
- Switching to resist the super-effective move

**Strategic Counters**:
- Using Pokemon without easily exploitable weaknesses
- Priority moves to revenge kill
- Defensive pivoting and momentum control
- Status moves and non-damaging strategies

### Synergies

**Ability Synergies**:
- Download (boosts attacking stats for more damage)
- Adaptability (STAB moves hit harder)
- Technician (boosts weaker super-effective moves)

**Item Synergies**:
- Life Orb (boosts all moves)
- Expert Belt (further boosts super-effective moves by 20%)
- Choice items (massive power boost)
- Focus Sash (ensures survival to use super-effective moves)

**Move Synergies**:
- Wide coverage movesets
- Hidden Power for specific coverage
- Moves that change target's typing (Soak, Trick-or-Treat)

### Example Damage Calculations
Assuming a base 80 BP super-effective move with equal Attack/Special Attack and Defense/Special Defense:

**Without Deadly Precision**:
- 50% chance to miss against +6 Evasion
- Reduced damage against Filter/Solid Rock (2.0x to 1.5x effectiveness)
- Complete miss against Levitate with Ground moves

**With Deadly Precision**:
- Always hits regardless of evasion
- Full 2.0x damage against Filter/Solid Rock
- Hits Levitate users with Ground moves for full super-effective damage

### Version History
- Introduced in Elite Redux as a powerful offensive ability
- Part of the expanded ability system featuring combination effects
- Designed to counter defensive ability stacking strategies

### Notes
- The ability combines aspects of No Guard (guaranteed accuracy) and Mold Breaker (ability ignoring)
- Only applies these effects conditionally on super-effective moves
- Represents a more tactical approach to ability bypassing compared to unconditional Mold Breaker