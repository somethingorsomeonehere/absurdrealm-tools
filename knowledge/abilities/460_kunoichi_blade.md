---
id: 460
name: Kunoichi's Blade
status: reviewed
character_count: 293
---

# Kunoichi's Blade - Ability ID 460

## In-Game Description
"Technician + Skill Link."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts moves with 60 BP or less by 1.5x. Does not boost moves with 60 BP or less if they potentially can have more than 60 BP, such as Revenge or Venoshock. Multihit moves to always hit 5 times. For moves that only hit 3 times or Population Bomb, there will be one accuracy check for all hits.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Kunoichi's Blade is a unique hybrid ability that combines two distinct offensive enhancement effects:
1. **Technician Effect**: Boosts the power of moves with 60 base power or less by 1.5x
2. **Skill Link Effect**: Forces multi-hit moves to always hit the maximum number of times

### Activation Conditions
#### Technician Component
- **Power threshold**: Only affects moves with 60 base power or less
- **Damage calculation**: Applied as a 1.5x multiplier to base power
- **Move examples**: Bullet Seed (25 BP to 37.5 BP per hit), Rock Blast (25 BP to 37.5 BP per hit)
- **Timing**: Applied during damage calculation phase

#### Skill Link Component
- **Multi-hit moves**: Forces moves that hit 2-5 times to always hit 5 times
- **Affected moves**: Bullet Seed, Rock Blast, Icicle Spear, Bone Rush, Pin Missile, etc.
- **Guaranteed consistency**: Eliminates RNG from multi-hit move damage

### Technical Implementation
```c
constexpr Ability KunoichiBlade = {
    .onOffensiveMultiplier = Technician.onOffensiveMultiplier,  // 1.5x for <=60 BP moves
    .skillLink = TRUE,  // Multi-hit moves always hit max times
};

// Technician component
if (basePower <= 60) MUL(1.5);
```

### Synergistic Power
The combination creates powerful synergy:
- Multi-hit moves typically have low base power (<=60 BP)
- Technician boosts each individual hit
- Skill Link guarantees maximum hits
- Result: Consistent high-damage multi-hit attacks

### Move Power Calculations
**Example with Bullet Seed:**
- Base power: 25 BP per hit
- With Technician: 25 x 1.5 = 37.5 BP per hit
- With Skill Link: Always 5 hits guaranteed
- Total effective power: 37.5 x 5 = 187.5 BP
- **Compared to normal Bullet Seed**: 25 x (2-5 random hits) = 50-125 BP average

### Optimal Move Coverage
**Best moves for Kunoichi's Blade:**
- **Bullet Seed** (Grass): 25 BP to 187.5 total effective BP
- **Rock Blast** (Rock): 25 BP to 187.5 total effective BP  
- **Icicle Spear** (Ice): 25 BP to 187.5 total effective BP
- **Pin Missile** (Bug): 25 BP to 187.5 total effective BP
- **Bone Rush** (Ground): 25 BP to 187.5 total effective BP

**Other Technician-boosted moves:**
- Moves <=60 BP that aren't multi-hit still get 1.5x boost
- Quick Attack, Bullet Punch, Mach Punch, etc.

### Strategic Implications
- **Consistency**: Eliminates multi-hit RNG, providing reliable damage output
- **Type coverage**: Access to multiple types through different multi-hit moves
- **Breaking substitutes**: Multi-hit moves break Substitute and Sturdy
- **Focus Sash counter**: Multiple hits bypass Focus Sash protection
- **Disguise/Ice Face**: Can break disguise effects with guaranteed multi-hits

### Important Interactions
#### Power Boosting Effects
- **STAB**: Applied after Technician boost (37.5 x 1.5 = 56.25 BP per hit)
- **Life Orb**: Stacks with both components for massive damage
- **Choice items**: Provide additional multipliers on top of ability effects
- **Weather boosts**: Sun/Rain boost compatible move types further

#### Defensive Interactions
- **Sturdy/Focus Sash**: Bypassed by guaranteed multi-hits
- **Substitute**: Broken by first hit, remaining hits damage the Pokemon
- **Rocky Helmet/Iron Barbs**: User takes damage for each hit (5x recoil)
- **Contact moves**: Multi-hit contact moves trigger contact effects multiple times

### Common Users and Team Roles
**Ideal Pokemon characteristics:**
- High Attack or Special Attack stats
- Access to multiple multi-hit moves
- Good Speed or bulk to use the ability effectively
- Diverse movepool for type coverage

**Team roles:**
- **Wallbreaker**: Consistent high damage breaks through bulky threats
- **Sweeper setup**: Can break through Focus Sash users reliably
- **Substitute breaker**: Handles Substitute strategies effectively
- **Anti-stall**: Consistent damage output pressures stall teams

### Competitive Advantages
- **Damage reliability**: No RNG in damage output
- **Breaking defensive strategies**: Counters common defensive items/abilities
- **Type flexibility**: Multiple multi-hit moves provide coverage options
- **Setup potential**: Consistent damage makes setup more viable

### Potential Weaknesses
- **Rocky Helmet users**: Take 5x contact damage from multi-hit contact moves
- **Rough Skin/Iron Barbs**: Similar recoil multiplication
- **Ability suppression**: Mold Breaker negates both components
- **Move PP**: Multi-hit moves often have lower PP, requiring PP management

### Synergistic Abilities and Items
**Team support:**
- **Speed control**: Tailwind, Trick Room depending on user's Speed
- **Stat boosts**: Attack/Special Attack boosters enhance damage further
- **Entry hazard support**: Weakens targets for guaranteed KOs

**Held items:**
- **Life Orb**: Massive damage boost with ability effects
- **Choice items**: Lock into powerful multi-hit moves
- **Focus Sash**: Ensures at least one turn of guaranteed multi-hit damage
- **Wide Lens**: Unnecessary due to Skill Link removing miss chance concerns

### Counters and Checks
**Direct counters:**
- **Mold Breaker**: Ignores ability completely
- **Wonder Guard**: Only weak to super-effective hits
- **Magic Guard**: Immune to indirect damage, but not direct damage

**Checks and pressure:**
- **Priority moves**: Bypass Speed issues
- **Status conditions**: Burn halves physical damage
- **Intimidate**: Reduces physical Attack stat
- **Defensive typing**: Resist common multi-hit move types

### Version History
- **Elite Redux exclusive**: Custom ability combining two existing effects
- **Design philosophy**: Rewards skillful move selection and team building
- **Balance considerations**: Powerful but requires specific move investment

### Advanced Applications
- **Choice item synergy**: Lock into a devastating multi-hit move
- **Setup sweeping**: Use after stat boosts for overwhelming power
- **Anti-meta role**: Counters common defensive strategies in competitive play
- **Team building**: Central ability requiring specific move and item support