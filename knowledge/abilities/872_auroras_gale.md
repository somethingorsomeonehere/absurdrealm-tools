---
id: 872
name: Aurora's Gale
status: reviewed
character_count: 252
---

# Aurora's Gale - Ability ID 872

## In-Game Description
"Majestic Bird + Aurora Veil."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's Special Attack stat by 50%. Multiplicative with other damage boosts. Sets up Aurora Veil on entry, cutting physical and special damage recieved by half for your allies. Lasts 5 turns, or 8 turns with Light Clay. Immune to Hail damage.
 
## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Aurora's Gale is a compound ability that combines the effects of Majestic Bird and automatic Aurora Veil setup. This creates a unique offensive-defensive hybrid ability perfect for special attackers who need both power and survivability.

### Component Effects

#### Majestic Bird Component
- **Special Attack boost**: Multiplies Special Attack by 1.5x (50% increase)
- **Raw stat multiplication**: Applied to the final calculated stat, not the base stat
- **Permanent effect**: Active as long as the ability isn't suppressed
- **Stacks with other modifiers**: Works with items, stat boosts, and other effects

#### Aurora Veil Component  
- **Automatic setup**: Sets up Aurora Veil immediately upon switching in
- **Damage reduction**: Reduces damage from ALL attacks (physical and special)
  - 50% damage reduction in singles battles
  - 33% damage reduction in doubles battles
- **Duration**: Lasts 5 turns (8 turns with Light Clay)
- **Team protection**: Benefits all team members on the same side
- **Bypass conditions**: Cannot be bypassed by critical hits but can be bypassed by Infiltrator

### Activation Conditions
- **Entry trigger**: Aurora Veil sets up automatically when the Pokemon enters battle
- **Stat boost**: Special Attack boost is permanent while ability is active
- **No weather requirement**: Unlike the move Aurora Veil, the ability doesn't require hail
- **One-time setup**: Aurora Veil only sets up once per entry, not repeatedly

### Technical Implementation
```c
// Aurora's Gale combines Majestic Bird + Aurora Veil setup
constexpr Ability AurorasGale = {
    .onStat = +[](ON_STAT) {
        // Majestic Bird component - 1.5x Special Attack
        if (statId == STAT_SPATK) *stat *= 1.5;
    },
    .onEntry = +[](ON_ENTRY) -> int {
        // Aurora Veil component - set up protective veil
        if (gSideStatuses[GetBattlerSide(battler)] & SIDE_STATUS_AURORA_VEIL)
            return 0; // Don't override existing Aurora Veil
        
        int side = GetBattlerSide(battler);
        gSideStatuses[side] |= SIDE_STATUS_AURORA_VEIL;
        gSideTimers[side].auroraVeilTimer = SCREEN_DURATION;
        // Trigger setup message
        return 1;
    }
};
```

### Important Interactions
- **Light Clay synergy**: Extends Aurora Veil duration from 5 to 8 turns
- **Screen stacking**: Aurora Veil doesn't stack with Reflect or Light Screen
- **Infiltrator bypass**: Infiltrator abilities can bypass the Aurora Veil protection
- **Mold Breaker effects**: Ability suppression disables both components
- **Critical hits**: Don't bypass Aurora Veil protection (unlike Reflect/Light Screen individually)

### Strategic Implications
- **Immediate impact**: Provides both offensive and defensive utility from turn 1
- **Team support**: Aurora Veil benefits the entire team side
- **Special sweeper support**: Perfect for special attackers who need setup time
- **Entry hazard resistance**: Aurora Veil helps mitigate entry hazard damage
- **Momentum control**: Forces opponents to make difficult switching decisions

### Common Users
This is a signature ability, likely exclusive to specific Pokemon that embody both offensive prowess and protective instincts. Ideal for:
- Special attacking Pokemon with support tendencies
- Ice-type or Flying-type Pokemon with mystical themes
- Pokemon that serve as both sweepers and team supporters

### Competitive Usage Notes
- **Lead potential**: Excellent for lead Pokemon that need immediate board control
- **Late game sweeper**: Special Attack boost enables powerful late-game sweeps
- **Team composition**: Works well in balanced teams needing both offense and defense
- **Switch advantage**: Creates favorable switching scenarios for teammates
- **Priority protection**: Aurora Veil helps survive priority moves

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable both effects
- **Infiltrator**: Bypasses Aurora Veil component entirely
- **Taunt**: Prevents setup moves that might complement the ability
- **Physical attackers**: May still deal significant damage despite Aurora Veil
- **Multi-hit moves**: Can overwhelm despite damage reduction

### Synergies
- **Light Clay**: Essential item for maximum Aurora Veil duration
- **Special attacks**: Maximizes the Special Attack boost component
- **Setup moves**: Aurora Veil provides safety for Calm Mind, Nasty Plot, etc.
- **Team coordination**: Works well with other screen setters and supporters
- **Ice-type moves**: Thematic synergy with Aurora Veil's icy protection

### Version History
- Elite Redux exclusive ability
- Combines elements from Generation VII (Aurora Veil) with stat multiplication
- Part of the compound ability system in Elite Redux
- Designed for Pokemon that need both immediate offensive power and team support

### Notes
- This ability represents the pinnacle of offensive-defensive hybrid design
- The lack of weather requirement makes it more reliable than the Aurora Veil move
- Both components activate simultaneously, making it extremely value-efficient
- May be exclusive to legendary or pseudo-legendary Pokemon due to its power level