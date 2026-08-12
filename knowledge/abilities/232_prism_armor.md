---
id: 232
name: Prism Armor
status: reviewed
character_count: 106
---

# Prism Armor - Ability ID 232

## In-Game Description
"Takes 35% less damage from Super-effective moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super-effective attacks by 35%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Damage Reduction**: Reduces super effective damage by 35% (multiplies by 0.65)
- **Activation Threshold**: Triggers when type effectiveness multiplier is ≥2.0x
- **Calculation Order**: Applied after type effectiveness but before other damage modifiers

### Technical Implementation
```cpp
constexpr Ability PrismArmor = {
    .onDefensiveMultiplier = Filter.onDefensiveMultiplier,
    .breakable = TRUE,
};

// Filter implementation (shared with Prism Armor):
constexpr Ability Filter = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (typeEffectivenessModifier >= UQ_4_12(2.0)) MUL(.65);
        },
    .breakable = TRUE,
};
```

### Activation Conditions
- **2x Super Effective**: Normal super effective moves (65% damage taken)
- **4x Super Effective**: Double weakness moves (65% damage taken) 
- **Enhanced Super Effective**: Moves boosted by abilities like Tinted Lens still trigger reduction
- **No Effect on**: Not very effective, neutral, or resisted moves

### Affected Move Categories
- **All Attack Types**: Physical, special, and status moves that deal damage
- **Multi-hit Moves**: Each hit receives the damage reduction
- **Fixed Damage**: Does not affect moves like Seismic Toss or Dragon Rage
- **Critical Hits**: Reduction applies even on critical hits

### Interactions with Other Abilities/Items
**Synergistic Combinations:**
- **Solid Rock**: Stacks multiplicatively for extreme super effective resistance
- **Assault Vest**: Provides additional special bulk to complement damage reduction
- **Leftovers/Rocky Helmet**: Passive recovery/damage while tanking hits

**Countered By:**
- **Mold Breaker/Teravolt/Turboblaze**: Ignores Prism Armor completely
- **Sunsteel Strike/Moongeist Beam**: Bypasses ability effects
- **Multi-hit moves**: Each hit still deals significant cumulative damage

**Ability Interactions:**
- **Tinted Lens**: Opponent's Tinted Lens makes "not very effective" moves neutral, but doesn't affect Prism Armor
- **Neuroforce**: Opponent's Neuroforce boosts super effective moves by 1.35x, but Prism Armor still reduces by 35%
- **Life Orb/Choice Items**: User's items don't interfere with defensive ability

### Strategic Implications
**Defensive Value:**
- Converts 2x weakness to ~1.3x damage taken
- Converts 4x weakness to ~2.6x damage taken  
- Excellent for defensive pivots and tanks
- Allows risky switch-ins against predicted coverage moves

**Team Building Considerations:**
- Best on Pokemon with multiple weaknesses (Rock, Ice, Bug types)
- Complements high HP stats and recovery moves
- Valuable on defensive cores and stall teams
- Less useful on frail, offensive Pokemon

### Example Damage Calculations
**Scenario**: Prism Armor Pokemon with 100 HP, 80 Defense vs 120 Attack opponent

**Without Prism Armor:**
- Super effective move (2x): ~75% HP damage
- Double weakness (4x): OHKO (150% HP damage)

**With Prism Armor:**
- Super effective move: ~49% HP damage (75% x 0.65)
- Double weakness: ~98% HP damage (150% x 0.65)

### Common Users
**Notable Pokemon with Prism Armor:**
- **Necrozma**: Legendary with balanced bulk, benefits from weakness coverage
- **Silvally**: Adaptable Normal-type that can change forms while keeping protection

**Ideal Candidates** (if distributed):
- Rock/Ice types with 4x weaknesses (Amaura, Aurorus)
- Multi-weakness defensive Pokemon (Cradily, Armaldo)
- Bulky setup sweepers that need to tank coverage moves

### Competitive Usage
**Tier Placement**: High utility defensive ability
**Usage Patterns**:
- Defensive switching and pivoting
- Setup sweeper protection during setup turns
- Stall team anchor ability
- Coverage move insurance for offensive Pokemon

**Meta Considerations**:
- Excellent in metas with strong coverage moves
- Less valuable when priority moves or status moves dominate
- Complements current Elite Redux defensive options well

### Counters and Counterplay
**Direct Counters:**
- **Mold Breaker variants**: Completely bypasses the ability
- **Sunsteel Strike/Moongeist Beam**: Ignores ability effects
- **Status moves**: Sleep, paralysis, burns bypass damage reduction

**Indirect Counters:**
- **Multi-hit moves**: Skill Link + multi-hit can still overwhelm despite reduction
- **Setup sweepers**: Boosted neutral moves may outdamage reduced super effective moves  
- **Entry hazards**: Stealth Rock and spikes provide residual damage

**Counterplay Strategies:**
- Use neutral STAB moves instead of coverage
- Set up entry hazards for residual damage
- Apply status conditions before attacking
- Use multi-hit moves to overwhelm reduced damage

### Synergies
**Best Partners:**
- **Wish support**: Heal Bell + Wish provides recovery for tanking
- **Entry hazard control**: Rapid Spin/Defog to minimize residual damage
- **Screen support**: Light Screen/Reflect for additional bulk layers

**Core Strategies:**
- **Defensive core anchor**: Central defensive Pokemon with reliable switching
- **Setup support**: Provides turns for teammates to set up
- **Status absorber**: Can take status moves meant for frailer teammates

### Version History
- **Generation VII**: Introduced on Necrozma in Sun/Moon
- **Elite Redux**: Maintains original 25% reduction but enhanced to 35% for improved viability
- **Current Meta**: Well-positioned defensive ability in Elite Redux's high-power environment

### Design Philosophy
Prism Armor represents defensive adaptation against type-based weaknesses. Unlike abilities that provide immunity or absorption, it offers consistent percentage-based protection that scales with the opponent's damage output. The 35% reduction in Elite Redux provides meaningful but not overwhelming defensive value, maintaining the risk-reward balance of type matchups while giving defensive Pokemon better survivability options.