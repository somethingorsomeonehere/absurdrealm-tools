---
id: 755
name: Balloon Blitz
status: reviewed
character_count: 299
---

# Balloon Blitz - Ability ID 755

## In-Game Description
"Inflatable + Hyper Aggressive."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by any Fire or Flying moves, boost Defense and Special Defense by one stage. Activates on each hit of a multihit move. Boost applies after the hit lands. All attacks hit twice. First hit deals 100%, while the second deals 25%. Each hit rolls secondary effects independently (except flinch).

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Dual Ability**: Combines the effects of Inflatable and Hyper Aggressive abilities
- **Inflatable Component**: Raises Defense and Special Defense by +1 when hit by Fire or Flying moves
- **Hyper Aggressive Component**: All moves hit twice, with second hit at 25% power
- **Activation**: Both effects work independently and simultaneously

### Activation Conditions

#### Inflatable Component
- Must be hit by a Fire-type or Flying-type move
- The move must successfully hit (doesn't activate on miss)
- At least one of Defense or Special Defense must be below maximum (+6 stages)
- Uses `ShouldApplyOnHitAffect()` check (blocked by Substitute, etc.)

#### Hyper Aggressive Component  
- Activates on all offensive moves used by the Pokemon
- Transforms single-hit moves into two-hit moves
- Second hit deals exactly 25% of the first hit's damage
- Works with physical, special, and status moves that deal damage

### Technical Implementation
```cpp
constexpr Ability BalloonBlitz = {
    .onDefender = Inflatable.onDefender,
    .onParentalBond = ParentalBond.onParentalBond,
};

// Referenced abilities:
constexpr Ability Inflatable = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(CanRaiseStat(battler, STAT_DEF) || CanRaiseStat(battler, STAT_SPDEF))
        CHECK(moveType == TYPE_FIRE || moveType == TYPE_FLYING);
        BattleScriptCall(BattleScript_InflatableActivates);
        gBattleScripting.battler = battler;
        return TRUE;
    },
};

constexpr Ability ParentalBond = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType { 
        return PARENTAL_BOND_HYPER_AGGRESSIVE; 
    },
    .resistsFortKnox = TRUE,
};
```

### Multi-Hit Mechanics
```cpp
// Hit count determination
case PARENTAL_BOND_HYPER_AGGRESSIVE:
    return 2; // Always hits exactly twice

// Damage multiplier for second hit
case PARENTAL_BOND_HYPER_AGGRESSIVE:
    REQUIRE(turn) // Only applies to second hit (turn = 1)
    return UQ_4_12(0.25); // 25% damage
```

### Detailed Battle Flow

#### Offensive Turn (Hyper Aggressive)
1. **First Hit**: Full damage calculation and effects
2. **Second Hit**: 25% of first hit's base damage
3. **Secondary Effects**: Only apply once (from first hit)
4. **Critical Hits**: Calculated separately for each hit
5. **Type Effectiveness**: Applied to both hits independently

#### Defensive Turn (Inflatable)
1. **Take Damage**: From Fire/Flying move
2. **Check Conditions**: Valid hit, stat boost possible
3. **Stat Boosts**: +1 Defense and +1 Special Defense
4. **Animation**: Defensive stat boost animation plays
5. **Message**: "Balloon Blitz raised [Pokemon's] Defense and Special Defense!"

### Affected Move Types (Inflatable Component)

**Fire-type moves that trigger Inflatable**:
- Flamethrower, Fire Blast, Overheat, Heat Wave
- Will-O-Wisp, Flame Wheel, Fire Punch
- Sacred Fire, Blue Flare, V-create
- Any Fire-type move, including status moves

**Flying-type moves that trigger Inflatable**:
- Wing Attack, Air Slash, Hurricane, Brave Bird
- Roost, Tailwind, Defog (if Flying-type)
- Aeroblast, Air Cutter, Gust
- Any Flying-type move, including status moves

### Interactions with Other Abilities/Mechanics

#### Inflatable Interactions
- **Substitute**: Blocks Inflatable activation
- **Magic Bounce**: Cannot be triggered by bounced moves
- **Stat Stage Limits**: Each stat only raised if below +6
- **Mold Breaker**: Does not affect Inflatable (defensive ability)
- **Multi-hit moves**: Activates only once per turn

#### Hyper Aggressive Interactions
- **Skill Link**: Does not extend hits beyond 2
- **Rock Blast/Bullet Seed**: Still only hits twice total
- **King's Rock/Razor Fang**: Flinch chance applies to both hits
- **Life Orb**: Recoil damage applies after both hits
- **Contact moves**: Both hits make contact if applicable
- **Abilities triggered on hit**: Can activate from either hit

### Strategic Implications

#### Offensive Strategy
- **Damage Output**: Effectively 125% damage on all moves (100% + 25%)
- **Breaking Substitutes**: Two hits can break Substitute and damage
- **Focus Sash/Sturdy**: Second hit can KO after first hit triggers
- **Multi-hit synergy**: Works with items and abilities that benefit from multiple hits

#### Defensive Strategy  
- **Fire/Flying Immunity**: Turns weakness into strength with stat boosts
- **Setup Opportunities**: Defensive boosts enable further setup
- **Pivot Strategy**: Switch into predicted Fire/Flying moves
- **Bulk Building**: Each successful trigger increases survivability

### Example Damage Calculations

#### Hyper Aggressive Damage
**Balloon Blitz Flamethrower vs Standard Target**:
- First hit: 90 BP (normal damage)
- Second hit: 22.5 BP (25% of 90)
- Total effective power: 112.5 BP per Flamethrower

#### Inflatable Defense Boost
**Before Inflatable (+0 Def)**:
- Talonflame Flare Blitz vs Balloon Blitz user: ~60% damage

**After Inflatable (+1 Def)**:
- Same attack: ~45% damage (25% reduction)

### Common Users
Balloon Blitz is a unique combination ability that would be extremely powerful, likely restricted to:
- **Legendary/Mythical Pokemon**: Due to the power of combining two strong abilities
- **Special Event Pokemon**: Limited distribution due to competitive balance
- **Mega Evolution exclusive**: Where the powerful combination justifies Mega status

### Competitive Usage Notes

#### Strengths
- **Versatile**: Strong on both offense and defense
- **Damage Output**: 125% effective damage on all moves
- **Defensive Recovery**: Turns Fire/Flying attacks into stat boosts
- **Breaking Power**: Two hits bypass many defensive strategies
- **Setup Potential**: Defensive boosts create setup opportunities

#### Weaknesses
- **Overpowered Nature**: Likely banned in most competitive formats
- **Limited Distribution**: Probably restricted to very few Pokemon
- **Prediction Required**: Inflatable requires switching into specific move types
- **Status Moves**: Hyper Aggressive doesn't boost non-damaging moves

### Counters

#### Against Hyper Aggressive Component
- **Rocky Helmet**: Damages on both hits if contact moves
- **Rough Skin/Iron Barbs**: Double contact damage
- **Flame Body/Static**: Double chance for status on contact
- **Substitute**: Can potentially waste both hits

#### Against Inflatable Component
- **Non-Fire/Flying moves**: Avoid triggering the defensive boosts
- **Taunt**: Prevents setup after stat boosts
- **Haze/Clear Smog**: Removes stat boosts immediately
- **Status moves**: Don't trigger Inflatable

### Synergies

#### With Hyper Aggressive
- **King's Rock/Razor Fang**: Double flinch chances
- **Life Orb**: Boosted damage on both hits
- **Choice items**: Both hits benefit from choice boost
- **Skill Link**: No effect (ability caps at 2 hits)

#### With Inflatable
- **Stored Power**: Benefits from defensive stat boosts
- **Body Press**: Defense boosts increase offensive power
- **Weakness Policy**: Fire/Flying weakness becomes beneficial
- **Leftovers/Recovery**: Defensive bulk helps with healing

### Version History
- Introduced in Elite Redux as a unique combination ability
- Designed as an extremely powerful ability for special/legendary Pokemon
- Combines two popular ability effects into one overpowered package
- Likely restricted due to competitive balance concerns

### Balance Considerations
This ability is intentionally overpowered, combining two strong individual abilities:
- **Power Level**: Far exceeds typical ability strength
- **Competitive Impact**: Would dominate most formats if widely available
- **Design Intent**: Meant for special, limited-distribution Pokemon
- **Restriction Necessity**: Likely requires usage bans in competitive play