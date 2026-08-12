---
id: 453
name: Raging Moth
status: reviewed
character_count: 146
---

# Raging Moth - Ability ID 453

## In-Game Description
"Fire moves hits twice, both hits at 70% power."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Fire moves to hit twice, with each hit dealing 70% of the move's normal damage. Secondary effects roll independently for each hit (except flinch).

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Raging Moth is an offensive ability that enhances Fire-type moves by making them hit twice in succession. Each individual hit deals 70% of the move's base power, resulting in a total damage multiplier of 1.4x (140% of original damage).

### Activation Conditions
- **Move type requirement**: Only Fire-type moves trigger this ability
- **All Fire moves affected**: Works on both physical and special Fire-type attacks
- **No move restrictions**: Affects all Fire moves regardless of power, accuracy, or effect
- **Parental Bond system**: Uses the same underlying mechanics as Parental Bond ability

### Technical Implementation
```c
// Raging Moth uses parental bond system for Fire moves
constexpr Ability RagingMoth = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType {
        CHECK(moveType == TYPE_FIRE)  // Only Fire moves
        return PARENTAL_BOND_DUAL_WIELD;  // 70% power per hit
    },
};

// Power calculation: each hit = 0.7x original power
case PARENTAL_BOND_DUAL_WIELD:
    return UQ_4_12(0.7);  // 70% power multiplier
```

### Damage Calculation
- **First hit**: 70% of move's base power
- **Second hit**: 70% of move's base power  
- **Total damage**: 140% of original move power
- **Both hits**: Use same accuracy roll, type effectiveness, and critical hit determination

### Important Interactions
- **Multi-hit moves**: Fire-type multi-hit moves (like Flame Burst) hit even more times
- **Contact effects**: Both hits can trigger contact-based abilities like Flame Body or Static
- **Item interactions**: Each hit can trigger items like Rocky Helmet or Rough Skin
- **Substitute breaking**: Can break Substitute with first hit, damage opponent with second
- **Focus Sash/Sturdy**: First hit can trigger these, second hit can potentially KO
- **Type effectiveness**: Both hits use same type matchup calculation
- **Critical hits**: Both hits have independent critical hit chances

### Strategic Implications
- **Damage output**: 40% increase in Fire-type move damage
- **Multi-hit benefits**: Breaks through Focus Sash, Substitute, and Disguise more reliably
- **Contact punishment**: Triggers contact-based revenge effects twice
- **Accuracy advantage**: Only one accuracy check for both hits
- **Critical synergy**: Doubled critical hit opportunities on Fire moves

### Synergistic Move Combinations
**High-power Fire moves become devastating:**
- **Fire Blast**: 110 to 154 effective power (2 x 77)
- **Flamethrower**: 90 to 126 effective power (2 x 63)
- **Overheat**: 130 to 182 effective power (2 x 91), but stat drop still applies once
- **Sacred Fire**: 100 to 140 effective power with burn chance on each hit

**Contact Fire moves trigger abilities twice:**
- **Flare Blitz**: Recoil calculated on total damage, but contact effects trigger twice
- **Fire Punch**: Each hit can trigger Static, Flame Body, etc.
- **Fire Fang**: Each hit has independent flinch and burn chances

### Counters and Weaknesses
- **Non-Fire moves**: Ability provides no benefit to non-Fire type attacks
- **Contact abilities**: Flame Body, Static, and Rocky Helmet punish twice as hard
- **Rough Skin/Iron Barbs**: Double damage to the user on contact moves
- **Multi-Scale/Shadow Shield**: Only broken after first hit
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the effect

### Team Building Considerations
- **Fire-type specialists**: Maximizes damage output of Fire-type attackers
- **Mixed attackers**: Benefits both physical and special Fire moves equally  
- **Wallbreakers**: Excellent for breaking through defensive cores
- **Late-game sweepers**: Increased damage helps secure KOs
- **Sun teams**: Pairs well with sun boost for Fire moves (1.5x x 1.4x = 2.1x total)

### Competitive Applications
- **Substitute breaker**: Reliably breaks Substitute + deals damage
- **Focus item counter**: Bypasses Focus Sash and Focus Band consistently
- **Disguise counter**: Breaks Mimikyu's Disguise and deals damage same turn
- **Endure/Sturdy punishment**: Can potentially KO through survival abilities
- **Priority breaking**: Can break priority users' Focus Sash

### Common Users
- Fire-type Pokemon who rely heavily on Fire-type STAB moves
- Mixed attackers with strong Fire-type coverage
- Wallbreakers who need maximum Fire-type damage output
- Pokemon with access to high-power Fire moves like Fire Blast or Overheat

### Notable Move Interactions
- **Will-O-Wisp**: Not affected (status move, not Fire-type attack)
- **Burn Up**: Still removes Fire typing after both hits
- **Fire-type Z-moves**: Z-power calculated on original power, then doubled
- **Choice items**: Still locked into the Fire move after using it
- **Life Orb**: Recoil damage applies to each hit separately

### Weather Interactions
- **Sun**: Fire moves get 1.5x boost, combined with Raging Moth = 2.1x total damage
- **Rain**: Fire moves get 0.5x reduction, combined with Raging Moth = 0.7x total damage
- **Harsh sun**: Fire moves cannot be weakened by water, full 2.1x damage potential

### Version History
- Custom Elite Redux ability
- Uses proven Parental Bond mechanics for reliability
- Designed to make Fire-type specialists more viable
- Balanced around 140% damage output to avoid being overpowered