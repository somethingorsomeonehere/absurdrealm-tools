---
id: 790
name: Frenzied Phantom
status: reviewed
character_count: 296
---

# Frenzied Phantom - Ability ID 790

## In-Game Description
"Hyper Aggressive + Shadow Tag."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Makes all attacks hit twice in succession. First hit deals 100%, second hit deals 25%. Each hit rolls secondary effects independently (except flinch). Prevents all non-Shadow Tag or Ghost-type foes from switching out. Pivot moves such as Volt Switch still allows them to switch (except Teleport.)

## Detailed Mechanical Explanation
*For Discord/reference use*

**Frenzied Phantom** is a rare combination ability that merges the offensive power of Parental Bond (Hyper Aggressive) with the field control of Shadow Tag, creating a uniquely powerful ability that excels at both damage output and battlefield control.

### Core Implementation
Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` at **line 8123-8127**:

```cpp
constexpr Ability FrenziedPhantom = {
    .onParentalBond = ParentalBond.onParentalBond,
    .onTrap = ShadowTag.onTrap,
    .shadowTag = TRUE,
};
```

The ability directly inherits both components:
- **Parental Bond mechanics**: For the dual-hit attack system
- **Shadow Tag mechanics**: For the trapping functionality

### Dual-Strike Component (Parental Bond/Hyper Aggressive)

#### Attack Mechanics
```cpp
// From ParentalBond implementation
.onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType { 
    return PARENTAL_BOND_HYPER_AGGRESSIVE; 
},
```

**Damage Calculation:**
- **First hit**: 100% damage (full power)
- **Second hit**: 25% damage (0.25x multiplier)
- **Total damage**: 125% of original move damage

**Battle Processing:**
- Hit count determined in `battle_script_commands.c`: Returns 2 hits
- Damage modifier applied in `battle_util.c`: 25% reduction on second hit
- Both hits maintain original move properties (accuracy, critical hit chance, type, etc.)

### Trapping Component (Shadow Tag)

#### Trapping Mechanics
```cpp
// From ShadowTag implementation
.onTrap = +[](ABILITY_ON_TRAP) -> int {
    ON_ABILITY(switchingBattler, FALSE, gAbilities[ability].shadowTag, return FALSE)
    return TRUE;
},
.shadowTag = TRUE,
```

**Trapping Rules:**
- Prevents normal switching for all opponent Pokemon
- **Ghost-types**: Completely immune to trapping (can switch freely)
- **Other Shadow Tag users**: Can switch freely (mutual immunity)
- Active as long as Frenzied Phantom user remains on field

### Strategic Analysis

#### Offensive Capabilities
1. **Guaranteed Damage Increase**: Every damaging move gets 25% more total damage
2. **Breaking Utility**: 
   - Focus Sash/Sturdy bypass with dual hits
   - Disguise piercing capability
   - Substitute breaking potential
3. **Secondary Effect Doubling**: Status chances apply twice per move

#### Control Capabilities
1. **Switching Denial**: Eliminates opponent's pivot options
2. **Revenge Killer Elimination**: Traps and KOs threats
3. **Setup Opportunities**: Trap passive Pokemon for free setup

#### Combined Synergy
The combination creates unique strategic opportunities:
- **Trap and Eliminate**: Guarantee KOs on specific threats
- **Momentum Control**: Force favorable matchups while dealing enhanced damage
- **Endgame Dominance**: Control late-game positioning with superior damage

### Limitations and Counters

#### Direct Counters
1. **Ghost-types**: 
   - Immune to trapping component
   - Still take enhanced damage from dual hits
   - Can switch freely and revenge kill
2. **Fort Knox/Wonder Skin**: 
   - Completely negate the dual-hit component
   - Trapping still functions normally
3. **Other Shadow Tag users**:
   - Can switch freely due to mutual immunity
   - Mirror matchups become standard battles

#### Escape Methods
Trapped Pokemon can escape via:
- **Switch moves**: U-turn, Volt Switch, Flip Turn, Parting Shot
- **Baton Pass**: Stat passing + switching
- **Teleport**: Negative priority switching
- **Ability switches**: Emergency Exit, Wimp Out
- **Item switches**: Eject Button, Eject Pack, Shed Shell
- **KOing the user**: Direct elimination

### Pokemon Distribution

Frenzied Phantom is an extremely rare ability in Elite Redux, typically found on:
- **Legendary/Mythical Pokemon**: As signature abilities
- **Elite Redux custom forms**: Special variants with unique roles
- **Innate abilities**: Always-active implementations

### Competitive Viability

#### Tier Assessment: **S-Tier**
Frenzied Phantom represents one of the most powerful abilities in Elite Redux due to its dual functionality.

**Strengths:**
- **Dual utility**: Both offensive and control capabilities
- **Guaranteed value**: Always provides damage boost + field control
- **Matchup coverage**: Handles both offensive and defensive threats
- **Late-game control**: Dominates endgame scenarios
- **Team building impact**: Forces opponent preparation

**Weaknesses:**
- **Ghost-type vulnerability**: Complete switching immunity
- **Fort Knox counter**: Negates damage component
- **Prediction requirements**: Must make good switching decisions
- **Rarity**: Limited distribution reduces availability

#### Best Use Cases
1. **Late-game closers**: Excel in endgame scenarios
2. **Threat elimination**: Remove specific problematic Pokemon
3. **Setup sweepers**: Combine setup with guaranteed KOs
4. **Wallbreakers**: Enhanced damage + trapping breaks stall

### Damage Calculations

#### Example Scenarios
**Base 100 Attack move:**
- Normal: 100 damage
- Frenzied Phantom: 125 damage (100 + 25)
- **25% damage increase**

**Against Focus Sash:**
- Normal: 1 damage (sash activates)
- Frenzied Phantom: KO (first hit breaks sash, second hit KOs)

**Against 200 HP opponent:**
- Normal 80 power move: ~80 damage
- Frenzied Phantom: ~100 damage (80 + 20)
- **2HKO becomes potential OHKO range**

### Related Abilities

#### Component Abilities
- **Parental Bond (#185)**: Identical dual-hit mechanics
- **Hyper Aggressive (#358)**: Same dual-hit implementation
- **Shadow Tag (#23)**: Same trapping mechanics

#### Similar Combination Abilities
- **Multi Headed (#347)**: 2-3 hits with different damage ratios
- **Primal Maw (#420)**: Dual hits for bite moves only
- **Arena Trap combos**: Trapping + other effects

#### Synergistic Abilities
- **Fort Knox**: Negates the dual-hit component
- **Wonder Skin**: Blocks multi-hit effects
- **Ghost typing**: Provides trapping immunity

### Technical Implementation Notes

#### Code Architecture
The ability leverages Elite Redux's modular ability system:
1. **Inheritance**: Directly inherits from existing abilities
2. **Hook system**: Uses both `onParentalBond` and `onTrap` hooks
3. **Flag system**: The `shadowTag = TRUE` provides immunity recognition

#### Integration Points
- **Battle engine**: Hooks into both damage and switching systems
- **AI system**: Recognizes both components for decision making
- **Animation system**: Handles dual-hit visual effects
- **Trapping UI**: Updates switching options in real-time

### Version History
Frenzied Phantom was introduced in Elite Redux as part of the expanded ability system, designed to create powerful signature abilities for legendary and special Pokemon. The combination represents the pinnacle of ability design, merging two of the game's most impactful mechanics.

### Team Building Considerations

#### Team Support
- **Ghost-type check**: Team needs answers to Ghost-type switch-ins
- **Fort Knox consideration**: Backup plans for ability negation
- **Entry hazards**: Maximizes trapping effectiveness
- **Speed control**: Ensures ability user moves appropriately

#### Opponent Adaptation
- **Ghost-type inclusion**: Nearly mandatory for opposing teams
- **Shed Shell users**: Emergency switching options
- **Priority moves**: Bypass speed control aspects
- **Status moves**: Cripple the ability user

## Summary
Frenzied Phantom stands as one of Elite Redux's most powerful abilities, combining the consistent damage output of Hyper Aggressive with the field control of Shadow Tag. This rare combination creates a nearly unstoppable force that excels in both offensive and control roles, though it remains vulnerable to Ghost-types and Fort Knox-style counters. The ability represents the pinnacle of Elite Redux's ability design philosophy, creating unique strategic interactions that define high-level gameplay.