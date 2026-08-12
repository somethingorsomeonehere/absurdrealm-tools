---
id: 547
name: Purifying Salt
status: reviewed
character_count: 169
---

# Purifying Salt - Ability ID 547

## In-Game Description
"Immune to status conditions. Take 1/2 damage from Ghost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to all status conditions. Additionally reduces all Ghost-type damage by 50%. If afflicted with status when gaining this ability, conditions are immediately cured. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**PURIFYING SALT** is a dual-effect defensive ability providing comprehensive status protection and Ghost-type resistance.

### Core Implementation:
```cpp
constexpr Ability PurifyingSalt = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_GHOST) RESISTANCE(.5);
        },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_STATUS1)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Status Immunity Component:
- **Coverage**: All major status conditions (CHECK_STATUS1)
  - Sleep (including Yawn delayed sleep)
  - Paralysis (speed reduction and move failure)
  - Burn (damage over time and attack reduction)
  - Freeze (move prevention)
  - Poison (regular and badly poisoned/Toxic)
- **Mechanism**: `onStatusImmune` callback blocks status application
- **Cleansing**: `removesStatusOnImmunity = TRUE` cures existing status when ability is gained

### Ghost-Type Damage Reduction:
- **Multiplier**: 0.5x (50% reduction) against Ghost-type moves
- **Mechanism**: `onDefensiveMultiplier` with `RESISTANCE(.5)`
- **Calculation**: Applied during damage calculation phase
- **Stacking**: Multiplicative with type effectiveness and other resistances

### Protected Status Sources:
1. **Direct Status Moves**: Sleep Powder, Thunder Wave, Will-O-Wisp, etc.
2. **Secondary Effects**: Scald's burn chance, Body Slam's paralysis chance
3. **Ability-Induced**: Static, Flame Body, Effect Spore
4. **Item-Induced**: Flame Orb, Toxic Orb, Sticky Barb
5. **Field Effects**: Toxic Spikes
6. **Self-Inflicted**: Rest, Yawn

### Ghost Moves Affected:
All Ghost-type attacks including:
- **Physical**: Shadow Claw, Phantom Force, Shadow Punch
- **Special**: Shadow Ball, Hex, Moongeist Beam
- **Status**: Curse (when used by Ghost-types)
- **Signature**: Spectral Thief, Never-Ending Nightmare

### Damage Calculation Examples:
**Ghost-type move vs Normal-type with Purifying Salt:**
- Base damage x 1.0 (neutral) x 0.5 (ability) = 0.5x damage

**Ghost-type move vs Psychic-type with Purifying Salt:**
- Base damage x 2.0 (super effective) x 0.5 (ability) = 1.0x damage

**Ghost-type move vs Dark-type with Purifying Salt:**
- Base damage x 0.5 (not very effective) x 0.5 (ability) = 0.25x damage

### Ability Properties:
- **breakable = TRUE**: Suppressed by Mold Breaker, Teravolt, Turboblaze
- **removesStatusOnImmunity = TRUE**: Cleanses status when gained mid-battle
- **Passive**: Both effects are always active while ability is present

### Interactions:

**With Mold Breaker Effects:**
- Both status immunity and Ghost resistance are completely bypassed
- Pokemon with suppressing abilities can inflict status and deal full Ghost damage

**With Corrosion:**
- Status immunity still applies (Corrosion only bypasses poison immunity specifically)
- Ghost damage reduction unaffected

**With Status Moves:**
- Sleep Talk cannot be used (no sleep status to activate it)
- Guts, Quick Feet, Marvel Scale never activate
- Facade remains at base 70 power

**With Toxic Spikes:**
- User can switch in safely without absorbing or being affected by spikes
- Multiple layers have no effect

### Strategic Applications:

**Defensive Utility:**
1. **Status Absorber**: Safe switch into status moves and spreaders
2. **Ghost Wall**: Significantly reduces damage from Ghost-type coverage
3. **Setup Enabler**: Can boost stats without fear of status disruption
4. **Stall Counter**: Immune to Toxic stalling strategies

**Team Support:**
1. **Pivot Safety**: Can switch into predicted status moves
2. **Anti-Lead**: Counters status-spreading lead Pokemon
3. **Hazard Immunity**: Safe from Toxic Spikes
4. **Coverage Check**: Resists common Ghost-type coverage moves

### Competitive Viability:
- **Tier**: High utility defensive ability
- **Usage**: Excellent on defensive pivots and walls
- **Value**: Dual protection makes it consistently useful
- **Niche**: Particularly valuable against status-heavy metagames

### Common Users:
Pokemon with Purifying Salt benefit significantly from:
- High defensive stats to capitalize on Ghost resistance
- Movepool that appreciates status immunity
- Role as defensive pivot or wall
- Weakness to Ghost-type coverage moves

### Counters:
1. **Mold Breaker Family**: Completely bypasses both effects
2. **Non-Status Conditions**: Confusion, attraction, torment still work
3. **Physical/Special Moves**: Other attacking types deal normal damage
4. **Ability Suppression**: Gastro Acid, Worry Seed remove protection

### Synergies:
1. **Leftovers/Recover**: Reliable recovery without status interruption
2. **Setup Moves**: Can boost without status chip damage
3. **Toxic Immunity**: Pairs with stall strategies
4. **Ghost Resistance**: Valuable on types weak to Ghost coverage

### Version History:
- **Generation 9**: Introduced in Scarlet/Violet
- **Elite Redux**: Implemented with standard mechanics, maintaining both status immunity and Ghost resistance at 50% reduction

Purifying Salt represents one of the most comprehensive defensive abilities, providing reliable protection against two of the most common forms of indirect damage in competitive play.