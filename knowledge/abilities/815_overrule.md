---
id: 815
name: Overrule
status: reviewed
character_count: 177
---

# Overrule - Ability ID 815

## In-Game Description
"Crits ignore resists and bypass abilities"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When this Pokemon's moves land critical hits, they ignore type resistances (any amount of resists, but not immunities) and defensive abilities that would normally reduce damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Overrule modifies the type effectiveness calculation specifically when the Pokemon lands a critical hit. The ability uses the `onAfterTypeEffectiveness` hook to intercept and modify type effectiveness values.

### Technical Implementation
```cpp
constexpr Ability Overrule = {
    .onAfterTypeEffectiveness =
        +[](ON_AFTER_TYPE_EFFECTIVENESS) {
            if (gIsCriticalHit && *mod && *mod < UQ_4_12(1.0)) *mod = UQ_4_12(1.0);
        },
};
```

### Activation Conditions
- Only activates when the Pokemon lands a critical hit (`gIsCriticalHit` is true)
- Only affects moves that have a type effectiveness modifier less than 1.0 (not-very-effective or immune)
- Does not affect moves that are already neutral (1.0x) or super-effective (>1.0x)

### Numerical Values
- **UQ_4_12(1.0)**: Represents neutral (1.0x) type effectiveness in the game's fixed-point number system
- **UQ_4_12 Format**: 4.12 fixed-point format where 1.0 = 4096 in the internal representation
- **Resistance Values**: Any modifier less than 1.0x gets converted to exactly 1.0x

### What Gets Bypassed
1. **Type Resistances**: 
   - 0.5x (not very effective) becomes 1.0x (neutral)
   - 0.25x (double resistance) becomes 1.0x (neutral)
   - 0x (immune) becomes 1.0x (neutral)

2. **Defensive Abilities**: The ability bypasses any defensive ability that reduces type effectiveness below 1.0x, including:
   - Wonder Guard (makes non-super-effective moves deal 0 damage)
   - Abilities that grant type immunities
   - Abilities that reduce specific type damage

### What Is NOT Affected
- Super-effective moves (2.0x, 4.0x) remain unchanged
- Neutral effectiveness (1.0x) moves remain unchanged
- Offensive stat modifiers, items, or other damage calculations
- Critical hit damage multiplier itself (the 1.5x crit bonus still applies)

### Strategic Implications
**Offensive Benefits:**
- Allows critical-hit-focused Pokemon to threaten defensive walls
- Makes moves like Stone Edge, Cross Chop, and Leaf Blade viable against resistant types
- Synergizes exceptionally well with high critical hit ratio moves and abilities

**Competitive Usage:**
- Excellent for wallbreaking strategies
- Strong against defensive teams that rely on type resistances
- Can surprise opponents by dealing unexpected damage to "safe" switches

### Interactions with Other Mechanics
**Critical Hit Rate Boosters:**
- Focus Energy, Dire Hit: Increase critical hit probability to maximize Overrule activation
- Super Luck: Doubles critical hit ratio, making Overrule more consistent
- High critical hit ratio moves (Stone Edge, Cross Chop): Natural synergy

**Ability Interactions:**
- **Sniper**: Critical hits deal 2.25x damage instead of 1.5x, stacking with Overrule's resistance negation
- **Battle Armor/Shell Armor**: Completely prevents Overrule from activating by blocking critical hits
- **Wonder Guard**: Becomes ineffective against critical hits from Overrule users

### Example Damage Calculations
**Scenario**: Fire-type move against Water-type Pokemon
- **Normal Hit**: 0.5x effectiveness = 50% damage
- **Critical Hit with Overrule**: 1.0x effectiveness x 1.5x crit bonus = 150% damage
- **Net Result**: 3x more damage than a normal resisted hit

**Scenario**: Normal-type move against Ghost-type Pokemon  
- **Normal Hit**: 0x effectiveness = 0% damage (immune)
- **Critical Hit with Overrule**: 1.0x effectiveness x 1.5x crit bonus = 150% damage
- **Net Result**: Goes from complete immunity to full neutral damage

### Common Users
Based on the codebase analysis, Overrule appears as an innate ability on at least one Pokemon in the Elite Redux roster. The ability is particularly valuable on Pokemon with:
- High critical hit ratio moves in their movepool
- Good offensive stats to capitalize on the resistance bypass
- Access to critical hit boosting moves or items

### Counters
**Direct Counters:**
- Battle Armor, Shell Armor: Prevent critical hits entirely
- Lucky Chant: Prevents critical hits for 5 turns
- Abilities that boost defensive stats rather than relying on type resistance

**Indirect Counters:**
- Pokemon with naturally high Defense/Special Defense stats
- Recovery moves to heal off the increased damage
- Priority moves to KO before Overrule user can land critical hits

### Synergies
**Items:**
- Scope Lens, Razor Claw: Increase critical hit ratio
- Life Orb: Boost damage further since resistances are negated
- Choice items: Lock into powerful moves with high crit ratios

**Moves:**
- Stone Edge, Cross Chop, Leaf Blade: High critical hit ratios
- Focus Energy: Guarantees critical hits for 2+ turns
- Slash, Night Slash, Psycho Cut: Reliable critical hit options

**Team Support:**
- Tailwind: Ensures Overrule user moves first to land critical hits
- Screens: Protect while setting up critical hit boosts
- Entry hazards: Chip damage to bring opponents into KO range

### Version History
- Added in Elite Redux as ability ID 815
- Part of the expanded ability roster introducing unique competitive mechanics
- Designed to create a new archetype focused on critical hit-based wallbreaking