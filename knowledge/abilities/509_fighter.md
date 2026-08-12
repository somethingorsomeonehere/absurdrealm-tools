---
id: 509
name: Fighter
status: reviewed
character_count: 77
---

# Fighter - Ability ID 509

## In-Game Description
"Boosts Fight.-type moves by 1.2x, or 1.5x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Fighting-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fighter is an offensive ability that provides variable damage boosts to Fighting-type moves based on the user's current HP percentage. It follows the standard "Swarm" ability pattern but applies to Fighting-type moves instead of Bug-type.

### Activation Conditions
- **Move type requirement**: Only affects Fighting-type moves
- **HP-based scaling**:
  - Above 1/3 HP: 1.2x damage multiplier (20% boost)
  - At or below 1/3 HP: 1.5x damage multiplier (50% boost)
- **Always active**: No setup required, passive ability

### Technical Implementation
```c
// Fighter uses SWARM_MULTIPLIER for Fighting-type moves
#define SWARM_MULTIPLIER(type)
    if (moveType == TYPE_FIGHTING) {
        if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3))
            MUL(1.5);  // 50% boost when low HP
        else
            MUL(1.2);  // 20% boost when healthy
    }
```

### HP Threshold Calculation
- **1/3 HP threshold**: Calculated as maxHP / 3 (rounded down)
- **Dynamic scaling**: Boost changes immediately when crossing threshold
- **Examples**:
  - 300 HP Pokemon: High boost at 100 HP or below
  - 301 HP Pokemon: High boost at 100 HP or below  
  - 302 HP Pokemon: High boost at 100 HP or below
  - 303 HP Pokemon: High boost at 101 HP or below

### Important Interactions
- **Stacking**: Multiplies with Life Orb, Choice items, STAB, and type advantages
- **Move variety**: Affects all Fighting-type moves (physical, special, status moves with damage)
- **Multi-hit moves**: Each hit gets the full multiplier
- **Type-changing moves**: Only affects moves that are Fighting-type when used
- **Ability suppression**: Doesn't work if ability is suppressed by Mold Breaker effects

### Strategic Implications
- **Risk-reward gameplay**: Encourages staying at low HP for maximum power
- **Clutch potential**: Can turn around battles with desperate 50% boost
- **HP management**: Synergizes with moves like Endure, Focus Sash, or Sturdy
- **Late-game power**: Becomes more powerful as battle progresses
- **Consistent boost**: Even healthy Pokemon get 20% boost to Fighting moves

### Common Fighting-Type Moves Affected
- **Physical**: Close Combat, Superpower, Hammer Arm, Mach Punch
- **Special**: Focus Blast, Aura Sphere, Vacuum Wave
- **Priority**: Mach Punch, Vacuum Wave, Bullet Punch (if Fighting-type)
- **Multi-hit**: Arm Thrust, Triple Kick

### Optimal Usage Strategies
- **Focus Sash builds**: Guarantee survival to reach low HP threshold
- **Substitute + Berry**: Stay at low HP while maintaining safety
- **Endure combinations**: Deliberately reach 1 HP for maximum boost
- **Life Orb synergy**: Stack damage multipliers for massive power
- **Choice item synergy**: Lock into boosted Fighting moves

### Team Synergy
- **Fighting-type specialists**: Maximizes STAB Fighting moves
- **Mixed attackers**: Benefits both physical and special Fighting moves
- **Revenge killers**: Come in low HP to revenge kill with boosted priority
- **Late-game sweepers**: Clean up weakened teams with boosted moves

### Counters and Limitations
- **Type immunity**: Ghost-types completely avoid Fighting moves
- **Intimidate**: Reduces physical Fighting move effectiveness
- **Burn**: Halves physical Fighting move damage
- **Rocky Helmet/Iron Barbs**: Punishes contact Fighting moves
- **Defensive typing**: Steel, Psychic, Flying resist Fighting moves

### Comparison to Similar Abilities
- **Swarm**: Same mechanics but for Bug-type moves
- **Blaze/Torrent/Overgrow**: Same pattern for Fire/Water/Grass types
- **Guts**: Boosts Attack when statused instead of HP-based
- **Reckless**: Boosts recoil moves instead of type-specific moves

### Competitive Viability
- **Tier placement**: Solid ability for Fighting-type attackers
- **Usage scenarios**: Best on frail offensive Fighting-types
- **Meta considerations**: Effective against common Normal/Dark/Steel types
- **Item synergy**: Works well with Focus Sash, Life Orb, Choice items
- **Speed tier importance**: Often needs priority moves or speed control

### Notable Users
Ideal for Pokemon with:
- High Attack or Special Attack stats
- Access to diverse Fighting-type moves
- Naturally frail defensive stats
- Good speed or priority move access
- Ability to set up or use Focus Sash

### Version History
- Elite Redux implementation following standard Swarm ability pattern
- Consistent with other type-specific damage boosting abilities
- Part of the expanded ability roster for greater team diversity