---
id: 420
name: Primal Maw
status: reviewed
character_count: 197
---

# Primal Maw - Ability ID 420

## In-Game Description
"Biting moves hit twice. 2nd hit does 0.4x damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Primal Maw causes all biting moves to hit twice. The first hit deals 100% damage while the second hit deals 40% damage. Independently rolls secondary effects of attacks on each hit (except flinch).

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Primal Maw is an offensive ability that converts all biting moves into two-hit attacks. The ability modifies moves that have the Strong Jaw flag, causing them to strike twice with reduced damage on the second hit.

### Activation Conditions
- **Move requirement**: Move must have the Strong Jaw flag (biting moves)
- **Damage calculation**: 
  - First hit: 100% base damage
  - Second hit: 40% base damage (0.4x multiplier)
- **Total damage**: Approximately 140% of original move damage
- **Hit timing**: Both hits occur in rapid succession

### Technical Implementation
```c
// Primal Maw ability definition
constexpr Ability PrimalMaw = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType {
        CHECK(gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)
        return PARENTAL_BOND_PRIMAL_MAW;
    },
};

// Damage multiplier for second hit
case PARENTAL_BOND_PRIMAL_MAW:
    REQUIRE(turn)  // Only applies to second hit
    return UQ_4_12(0.4);  // 40% damage multiplier
```

### Affected Moves
All moves with the Strong Jaw flag are affected by Primal Maw:

#### Common Biting Moves
- **Bite**: Dark-type, 60 power, may flinch
- **Crunch**: Dark-type, 90 power, may lower Defense
- **Fire Fang**: Fire-type, 80 power, may burn or flinch
- **Ice Fang**: Ice-type, 80 power, may freeze or flinch
- **Thunder Fang**: Electric-type, 80 power, may paralyze or flinch
- **Poison Fang**: Poison-type, 80 power, may badly poison

#### Elite Redux Exclusive Biting Moves
Various custom moves in Elite Redux also have the Strong Jaw flag and will trigger Primal Maw's double-hit effect.

### Important Interactions
- **Status chances**: Each hit can trigger secondary effects independently
- **Contact moves**: Both hits make contact if the original move does
- **Abilities**: Abilities that trigger on contact activate for both hits
- **Life Orb/Rocky Helmet**: Damage/recoil applies for both hits
- **Substitute**: Can break substitute with first hit, damage Pokemon with second
- **Focus Sash/Band**: First hit can trigger Focus Sash, second hit can KO
- **King's Rock/Razor Fang**: Each hit can trigger flinch chance

### Damage Calculation
Total damage output: **140% of original move damage**
- Example with 100 base power move:
  - First hit: 100 power
  - Second hit: 40 power
  - Combined: 140 power equivalent

### Strategic Implications
- **Damage boost**: Significant 40% damage increase to all biting moves
- **Breaking defenses**: Can break through Focus Sash, Disguise, Ice Face
- **Status spreading**: Double chance for status effects like burn, paralysis
- **Substitute breaking**: Excellent at destroying substitutes
- **Multi-hit synergy**: Works well with items that benefit from multiple hits

### Common Users
- Physical attackers with access to biting moves
- Pokemon with naturally high Attack stats
- Dragon and Dark types with strong jaw-based movesets
- Pokemon that rely on fang moves for coverage

### Competitive Usage Notes
- **Meta positioning**: Strong against bulky defensive Pokemon
- **Item synergy**: Life Orb provides damage to both hits
- **Coverage moves**: Makes weaker coverage fangs more viable
- **Breaking point**: Can push certain matchups from 2HKO to OHKO
- **Consistency**: More reliable than single-hit high power moves

### Counters
- **Physical bulk**: High Defense stats reduce both hits
- **Intimidate**: Lowers Attack, affecting both hits
- **Burns**: Halves physical damage for both hits
- **Rocky Helmet**: Punishes contact biting moves heavily
- **Rough Skin/Iron Barbs**: Double recoil damage
- **Mold Breaker abilities**: Can disable Primal Maw

### Synergies
- **Choice Band**: Boosts both hits significantly
- **Life Orb**: Extra damage on both hits with manageable recoil
- **Strong Jaw ability**: If paired somehow, would boost both hits further
- **King's Rock**: Increases flinch chances with double hits
- **Tough Claws**: Boosts contact biting moves further

### Ability Interactions
- **Does NOT stack with**: Strong Jaw (different Pokemon would need both)
- **Blocked by**: Mold Breaker effects that suppress abilities
- **Enhanced by**: Items that boost physical attacks
- **Countered by**: Abilities that punish contact (if biting move makes contact)

### Version History
- Elite Redux exclusive ability
- ID 420 in the ability roster
- Uses Parental Bond multihit framework with custom damage multiplier
- Part of the expanded ability system with 800+ total abilities