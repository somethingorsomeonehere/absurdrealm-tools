---
id: 792
name: Metallic Jaws
status: reviewed
character_count: 295
---

# Metallic Jaws - Ability ID 792

## In-Game Description
"Metallic + Primal Maw."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Steel to the user's current typing. Retains Steel typing even upon losing the ability, going away only when switching out. all biting moves to hit twice. First hit deals 100% damage, second hit deals 40%. Each hit rolls secondary effects independently (except flinch).

## Detailed Mechanical Explanation
*For Discord/reference use*

Metallic Jaws is a composite ability that combines two powerful effects from the Metallic and Primal Maw abilities:

### Core Mechanics

**1. Metallic Component (On Entry Effect):**
- Upon switching into battle, the Pokemon gains the Steel type as an additional type
- This effect occurs immediately when the Pokemon enters the field
- The Steel typing provides resistance to Normal, Flying, Rock, Bug, Steel, Grass, Psychic, Ice, Dragon, and Fairy moves
- Grants immunity to poison status conditions while the Steel type is active
- The additional Steel typing stacks with the Pokemon's existing types

**2. Primal Maw Component (Parental Bond Effect):**
- When using moves with the `FLAG_STRONG_JAW_BOOST` flag, the attack hits twice
- First hit: 100% damage (full power)
- Second hit: 40% damage (reduced power from PARENTAL_BOND_PRIMAL_MAW multiplier)
- Total damage output: 140% of the original move's power
- This effect only triggers on moves that would normally be boosted by Strong Jaw

### Technical Implementation

```cpp
constexpr Ability MetallicJaws = {
    .onEntry = Metallic.onEntry,           // Adds Steel type on switch-in
    .onParentalBond = PrimalMaw.onParentalBond, // Enables double-hit for jaw moves
};

// Metallic component
constexpr Ability Metallic = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return AddBattlerType(battler, TYPE_STEEL); 
    },
};

// Primal Maw component  
constexpr Ability PrimalMaw = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType {
        CHECK(gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)
        return PARENTAL_BOND_PRIMAL_MAW;
    },
};
```

### Complete List of Affected Moves

All moves with the `strong_jaw: true` flag in the protobuf data, including:

**Primary Bite/Jaw Moves:**
- Bite (60 BP to 84 BP total)
- Crunch (80 BP to 112 BP total)  
- Hyper Fang (80 BP to 112 BP total)
- Thunder Fang (65 BP to 91 BP total)
- Ice Fang (65 BP to 91 BP total)
- Fire Fang (65 BP to 91 BP total)
- Poison Fang (50 BP to 70 BP total)

**Other Strong Jaw Boosted Moves:**
- Leech Life
- Any other moves marked with `strong_jaw: true` in the move data

### Interactions with Other Abilities/Mechanics

**Synergistic Interactions:**
- **Strong Jaw**: Would further boost the power of jaw moves by 30% before the double-hit calculation
- **Tough Claws**: Boosts contact moves, many jaw moves make contact
- **Sheer Force**: Could boost moves with secondary effects, though removes the secondary effect
- **STAB**: Steel-type moves gain Same Type Attack Bonus after gaining Steel typing

**Potential Conflicts:**
- **Multitype/RKS System**: May override the added Steel typing depending on held item
- **Color Change/Protean**: Could change typing away from Steel after attacking
- **Mold Breaker/Turboblaze/Teravolt**: Opponents with these abilities ignore the Steel type resistances

### Strategic Implications

**Offensive Advantages:**
- Massive damage output on jaw-based moves (140% total power)
- Steel typing provides additional STAB for Steel-type moves
- Excellent coverage with combination of original typing + Steel
- Priority moves like Bullet Punch gain STAB if the Pokemon learns them

**Defensive Benefits:**
- Steel typing grants numerous resistances and poison immunity
- Bulky Steel types can take advantage of the resistances while dealing huge damage
- Entry hazard immunity (Spikes) if already Steel-type

**Example Damage Calculations:**

*Crunch (80 BP) with Metallic Jaws:*
- First hit: 80 BP
- Second hit: 32 BP (80 x 0.4)
- Total: 112 BP effective power
- With Strong Jaw: 145.6 BP total (112 x 1.3)

### Common Users

This ability would be ideal for:
- Physical attackers with access to jaw-based moves
- Pokemon that benefit from Steel typing defensively
- Mixed attackers that can utilize both the Steel STAB and jaw moves
- Pokemon in need of both offensive presence and defensive utility

### Competitive Usage Notes

**Tier Implications:**
- Extremely powerful ability due to dual benefits
- The 140% damage multiplier on common moves like Crunch makes this very threatening
- Steel typing addition provides significant defensive utility
- Likely restricted to Pokemon with lower stats to maintain balance

**Common Sets:**
- Physical Choice Band/Choice Scarf sets to maximize jaw move damage
- Bulk offensive sets utilizing Steel resistances
- Mixed sets taking advantage of Steel STAB moves

### Counters

**Direct Counters:**
- **Mold Breaker variants**: Ignore the Steel typing resistances
- **Fire/Fighting/Ground type moves**: Deal super-effective damage to Steel typing
- **Burn status**: Cuts physical attack power in half, reducing jaw move effectiveness
- **Physical walls**: High Defense Pokemon can tank even the boosted jaw moves

**Indirect Counters:**
- **Will-O-Wisp users**: Apply burn status to cripple physical attacks
- **Intimidate**: Reduces Attack stat, lowering damage output
- **Rocky Helmet/Iron Barbs**: Punish the double-hit nature of jaw moves
- **Contact punishment abilities**: Rough Skin, Static, etc. trigger twice

### Synergies

**Team Support:**
- **Stealth Rock**: Provides entry hazard support while Steel typing resists it
- **Thunder Wave/paralysis support**: Slows down faster threats
- **Screens support**: Light Screen/Reflect help with bulk while setting up

**Item Synergies:**
- **Life Orb**: Boosts both hits of jaw moves significantly
- **Choice Band**: Massive power boost to already strong jaw moves  
- **Leftovers**: Provides recovery to take advantage of Steel resistances
- **Heavy-Duty Boots**: Protects from entry hazards while switching in

### Version History

- **Initial Implementation**: Added as ability ID 792 in Elite Redux
- **Current Status**: Fully functional composite ability
- **Balance Notes**: Combines two strong effects but limited to specific move types

This ability represents one of the most powerful offensive/utility combinations in Elite Redux, offering both immediate defensive benefits and devastating offensive potential with the right moveset.