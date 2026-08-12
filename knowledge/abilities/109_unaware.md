---
id: 109
name: Unaware
status: reviewed
character_count: 68
---

# Unaware - Ability ID 109

## In-Game Description
"Ignores foes' stat changes, both positive and negative ones."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ignores all the foes' stat stage changes during damage calculations.

## Detailed Mechanical Explanation
*For Discord/reference use*

**UNAWARE** is a stat-ignoring ability that treats opponent Pokemon as having neutral stat stages when calculating damage.

### Core Mechanics:
- **Function**: Forces all opponent stat calculations to use stage 6 (neutral) instead of actual stat stages
- **Direction**: Only ignores opponent's stat changes; user's own stat changes work normally
- **Scope**: Affects all stats (Attack, Defense, Special Attack, Special Defense, Speed) when relevant to damage calculation

### Activation Conditions:
1. **As Attacker**: Ignores target's defensive stat changes (Defense/Special Defense)
2. **As Defender**: Ignores attacker's offensive stat changes (Attack/Special Attack)
3. **Special Moves**: Works with Foul Play (ignores user's own Attack changes), Body Press, etc.

### Technical Implementation:
```c
constexpr Ability Unaware = {
    .breakable = TRUE,
    .unaware = TRUE,
};

// In CalculateStat function:
if (isUnaware)
    statStage = DEFAULT_STAT_STAGE; // Sets to stage 6 (neutral)
```

### Stat Stage System:
- **Stage Range**: -6 to +6 (stages 0-12 internally)
- **Neutral Stage**: 6 (DEFAULT_STAT_STAGE)
- **Multipliers**: Stage 0 = 25% stats, Stage 6 = 100% stats, Stage 12 = 400% stats
- **Unaware Effect**: Forces calculation to always use stage 6 multiplier (1.0x)

### What Unaware Ignores:
- **Stat Boosts**: Swords Dance (+2 Attack), Calm Mind (+1 SpA/SpD), Shell Smash, etc.
- **Stat Drops**: Intimidate (-1 Attack), Overheat (-2 SpA), Hammer Arm (-1 Speed), etc.
- **Ability-Based Changes**: Simple (doubles stat changes), Contrary (reverses changes)
- **Item Effects**: Eviolite defensive boosts are NOT ignored (permanent stat modification)
- **Status Effects**: Burn's Attack reduction is NOT ignored (affects base stat, not stages)

### What Unaware Does NOT Ignore:
- **User's Own Stats**: User's stat changes work normally
- **Base Stats**: Natural stat differences between species
- **Items**: Choice Band, Life Orb, Eviolite effects
- **Status Conditions**: Burn, paralysis, frostbite effects on base stats
- **Abilities**: Wonder Room, Huge Power effects on base stats
- **Critical Hits**: Still get damage boost and ignore positive defensive changes normally

### Move Interactions:
1. **Foul Play**: Uses target's Attack stat but with Unaware user ignoring the target's Attack boosts
2. **Body Press**: Uses user's Defense stat, unaffected by Unaware when used by Unaware Pokemon
3. **Power Trip/Stored Power**: Damage calculation ignores target's stat changes when hit by Unaware Pokemon
4. **Psyshock**: Targets Defense, so Unaware ignores target's Defense changes

### Ability Interactions:
- **Competitive/Defiant**: These abilities DO NOT trigger when stats are ignored by Unaware
- **Simple**: Doubled stat changes are ignored by Unaware (treated as neutral)
- **Contrary**: Reversed stat changes are ignored by Unaware
- **Mold Breaker**: Cannot bypass Unaware (not a protective ability)

### Strategic Applications:
1. **Anti-Setup**: Counters sweepers who rely on stat boosts (Dragon Dance, Quiver Dance users)
2. **Consistent Damage**: Deals predictable damage regardless of opponent's stat manipulation
3. **Defensive Utility**: Ignores Attack drops from Intimidate or opponent's stat boosts
4. **Late Game**: Remains effective even after opponent has accumulated multiple stat changes

### Example Damage Calculations:
**Scenario**: Unaware Pokemon vs +6 Attack Adamant Garchomp using Earthquake
- **Normal Calculation**: 394 Attack * 4.0 (stage +6) = 1,576 effective Attack
- **With Unaware**: 394 Attack * 1.0 (stage 6 neutral) = 394 effective Attack
- **Result**: ~75% damage reduction from ignoring the +6 Attack boost

### Common Users:
- **Wobbuffet/Wynaut**: Tank setup sweepers with Shadow Tag
- **Quagsire**: Combines with good bulk and Water/Ground typing
- **Clefable**: Versatile support with Magic Guard and good stats
- **Pyukumuku**: Extreme special bulk with Unaware for physical attackers
- **Bibarel**: Simple Normal-type with decent bulk

### Competitive Utility:
- **Tier Placement**: Often OU/UU viable purely due to Unaware utility
- **Team Role**: Dedicated wall against physical/special setup sweepers
- **Item Synergy**: Leftovers for longevity, Rocky Helmet for chip damage
- **Move Synergy**: Haze/Clear Smog to remove stat changes, recovery moves

### Counters and Limitations:
1. **Critical Hits**: Still get increased damage and ignore positive defensive stat changes
2. **Multi-hit Moves**: Each hit benefits from Unaware separately
3. **Status Moves**: Doesn't protect against non-damaging moves
4. **Base Power Scaling**: Doesn't help against naturally powerful moves
5. **Type Effectiveness**: Still takes normal super effective damage

### Synergies:
- **Haze/Clear Smog**: Remove stat changes that Unaware would ignore anyway
- **Toxic Spikes**: Support move that benefits from Unaware's defensive utility
- **Stealth Rock**: Entry hazard support while walling setup attempts
- **Recover/Roost**: Essential for maintaining HP while checking setup sweepers

### Version History:
- **Generation 4**: Introduced with Bidoof line
- **Generation 5+**: Mechanics refined, became more competitively relevant
- **Elite Redux**: Functions identically to main series implementation