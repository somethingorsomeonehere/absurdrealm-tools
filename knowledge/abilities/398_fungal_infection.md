---
id: 398
name: Fungal Infection
status: reviewed
character_count: 108
---

# Fungal Infection - Ability ID 398

## In-Game Description
"Contact moves inflict Leech Seed on the target."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Spreads Leech Seed when using a contact move, draining 1/8th of the target's max HP at the end of each turn.

## Detailed Mechanical Explanation

### Basic Information
- **ID**: 398
- **Name**: Fungal Infection
- **Type**: Contact-based Status Infliction
- **Category**: Uncategorized

### Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 4104-4116
- **Function**: `FungalInfection`
- **Trigger**: `onAttacker`

### Implementation Details
```cpp
constexpr Ability FungalInfection = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK_NOT(IS_BATTLER_OF_TYPE(target, TYPE_GRASS))
        CHECK_NOT(gStatuses3[target] & STATUS3_LEECHSEED)
        CHECK(IsMoveMakingContact(move, battler))

        gStatuses3[target] |= battler;
        gStatuses3[target] |= STATUS3_LEECHSEED;
        BattleScriptCall(BattleScript_AbsorbantActivated);
        return TRUE;
    },
};
```

### Activation Conditions
1. **Contact Required**: Only triggers when the user makes physical contact with moves
2. **Target Validation**: Must pass `ShouldApplyOnHitAffect(target)` check
3. **Type Immunity**: Grass-type Pokemon are immune to the effect
4. **Status Check**: Target must not already have Leech Seed status
5. **Move Contact**: Move must have the contact flag (`IsMoveMakingContact`)

### Status Applied
- **Effect**: `STATUS3_LEECHSEED`
- **Mechanics**: Standard Leech Seed effect - drains 1/8 of target's max HP each turn and heals the source
- **Duration**: Persists until target switches out
- **Battle Script**: Uses `BattleScript_AbsorbantActivated`

## Pokemon Distribution

### Primary Ability Holders
1. **Paras** (Species: SPECIES_PARAS)
   - Type: Bug/Grass
   - Stats: 45/75/65/50/90/25
   - Other Abilities: Opportunist, Hyper Aggressive
   - Innates: Effect Spore, Overcoat, Dry Skin

2. **Brute Bonnet** (Species: SPECIES_BRUTE_BONNET)
   - Type: Grass/Dark (Paradox Pokemon)
   - Stats: 111/127/99/79/99/55
   - Other Abilities: Adaptability, Mycelium Might
   - Innates: Protosynthesis, Regenerator, Solar Power

### Innate Ability Holders
1. **Mega Breloom** (Species: SPECIES_BRELOOM_MEGA)
   - Type: Grass/Fighting
   - Stats: 60/140/130/50/110/70
   - Other Abilities: Long Reach, Stamina, Avenger
   - Other Innates: Perfectionist, Technician

## Strategic Analysis

### Competitive Viability: Medium
Fungal Infection offers consistent passive damage and healing, making it valuable for bulky Pokemon that frequently make contact. The ability to automatically apply Leech Seed without using a move slot provides significant utility.

### Strengths
1. **Passive Sustain**: Provides constant healing from Leech Seed effect
2. **No Move Slot Cost**: Applies Leech Seed without sacrificing moveset space
3. **Contact Punishment**: Deters physical attackers from making contact
4. **Stall Potential**: Excellent for defensive strategies and time-based wins
5. **Wide Coverage**: Works with any contact move in the user's arsenal

### Weaknesses
1. **Grass Immunity**: Completely ineffective against Grass-type Pokemon
2. **Contact Dependency**: Useless with special attacks or non-contact moves
3. **Status Blocking**: Cannot affect targets already under Leech Seed
4. **Switch Vulnerability**: Effect ends when target switches out
5. **Limited Distribution**: Available to relatively few Pokemon

### Optimal Pokemon Types
- **Bulky Physical Attackers**: Pokemon with high HP/Defense that use contact moves
- **Tank Builds**: Defensive Pokemon that can capitalize on the healing
- **Stall Teams**: Pokemon designed for long-term battles

## Related Abilities

### Similar Mechanics
1. **Absorbant** (Ability #425)
   - **Difference**: Only triggers on drain moves (Absorb, Dream Eater)
   - **Similarity**: Also applies STATUS3_LEECHSEED with same immunity conditions
   - **Code Location**: Lines 4402-4414 in abilities.cc

### Contact-Based Abilities
- **Poison Touch**: Applies poison on contact
- **Effect Spore**: Random status conditions on contact
- **Static**: Paralysis chance on contact

## Competitive Applications

### Team Synergy
1. **Entry Hazard Support**: Combines well with Spikes/Stealth Rock for residual damage
2. **Wish Support**: Leech Seed healing stacks with team healing moves
3. **Stall Cores**: Excellent in defensive team compositions

### Counter-Strategies
1. **Grass-type Pokemon**: Complete immunity to the effect
2. **Special Attackers**: Avoid contact moves entirely
3. **Rapid Switching**: Frequent switches remove Leech Seed status
4. **Non-Contact Moves**: Use moves without the contact flag

### Usage Patterns
- **Early Game**: Apply to walls and tanks for sustained pressure
- **Mid Game**: Use on switch-ins to force unfavorable trades
- **Late Game**: Stall out weakened opponents with residual damage

## Notable Interactions

### Move Interactions
- **Contact Moves**: All contact moves can trigger (Tackle, Punch moves, etc.)
- **Non-Contact**: Special attacks, projectiles, and non-contact physical moves won't trigger
- **Multi-Hit**: Each hit can potentially trigger the ability

### Status Interactions
- **Leech Seed Stack**: Cannot apply if target already has Leech Seed
- **Substitute**: May be blocked by Substitute (needs verification)
- **Magic Guard**: Target takes no damage but effect still applies

## Development Notes
- Uses the same battle script as Absorbant ability (`BattleScript_AbsorbantActivated`)
- Implemented as a contact-based onAttacker trigger
- Part of the newer ability additions (ID 398 in high number range)
- Currently categorized as "Uncategorized" in ability classification system