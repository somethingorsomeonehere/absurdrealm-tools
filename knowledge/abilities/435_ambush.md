---
id: 435
name: Ambush
status: reviewed
character_count: 103
---

# Ambush - Ability ID 435

## In-Game Description
"Guaranteed critical hit on first turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ambush guarantees a critical hit on the user's first turn after switching in or at the start of battle. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Ambush is an offensive ability that provides a guaranteed critical hit on the user's first turn after switching into battle. This creates immediate offensive pressure and allows for powerful opening moves.

### Activation Conditions
- **Turn requirement**: Only activates on the Pokemon's first turn after entering battle
- **Move requirement**: Works with any attacking move that can deal damage
- **No type restriction**: Functions with moves of any type
- **Switch timing**: Resets whenever the Pokemon switches out and back in

### Technical Implementation
```c
// Ambush guarantees critical hit on first turn
constexpr Ability Ambush = {
    .onCrit = +[](ON_CRIT) -> int {
        CHECK(gVolatileStructs[battler].isFirstTurn)
        return ALWAYS_CRIT;
    },
};
```

### Turn Tracking System
The game tracks turn states using `isFirstTurn` values:
- **2**: Just switched in (initial state)
- **1**: First turn after switch-in (Ambush activates)
- **0**: Subsequent turns (Ambush inactive)

### Important Interactions
- **Status moves**: Does not affect status moves as they cannot critically hit
- **Multi-hit moves**: Each hit can potentially crit, but only on the first turn
- **Priority moves**: Works with priority moves like Quick Attack or Bullet Punch
- **Choice items**: Synergizes well with Choice Band/Specs for massive first-turn damage
- **Critical hit immunities**: Bypassed by Ambush's guaranteed crit mechanism
- **Sniper**: Stacks with Sniper ability for 1.5x additional damage on crits

### Strategic Applications

#### Offensive Strategies
- **Lead sweeper**: Excellent on lead Pokemon for immediate pressure
- **Switch-in revenge**: Perfect for revenge killing after a teammate faints
- **U-turn/Volt Switch**: Combines well with pivot moves for repeated first-turn advantage
- **Choice item abuse**: Maximizes damage output with locked-in choice items
- **Setup disruption**: Forces opponents to play defensively on switch-ins

#### Team Building Synergies
- **Entry hazard support**: Spikes/Stealth Rock chip damage + guaranteed crit can secure KOs
- **Dual screens**: Protects from retaliation after the initial crit
- **Memento/Parting Shot**: Allows safe switch-ins with stat drops
- **Healing Wish/Lunar Dance**: Full restoration while maintaining first-turn status

### Competitive Usage
- **Surprise factor**: Opponents may not expect guaranteed critical hits
- **Momentum control**: Creates immediate offensive pressure upon entry
- **Wallbreaking**: Can break through defensive Pokemon on the first turn
- **Speed tier compression**: Less reliant on outspeeding when damage is guaranteed
- **Prediction rewarding**: Rewards good switch-in timing

### Related Abilities and Combinations

#### Hunter's Mark (Combined Effect)
- **Combination**: Ambush + Deadeye
- **Effect**: Guaranteed crit on first turn + perfect accuracy on projectile moves
- **Usage**: Provides both offensive power and reliability

#### Showdown Mode (Combined Effect)  
- **Combination**: Ambush + Violent Rush
- **Effect**: Guaranteed crit on first turn + speed boost mechanics
- **Usage**: Immediate power with sustained momentum

### Common Users
Typically found on:
- Fast offensive Pokemon that benefit from immediate damage
- Pokemon with high base Attack or Special Attack stats
- Species designed for hit-and-run tactics
- Pokemon with access to powerful STAB moves

### Counters and Limitations

#### Direct Counters
- **Shell Armor/Battle Armor**: Prevents critical hits entirely
- **Lucky Chant**: Team-wide critical hit immunity for 5 turns
- **Focus Sash/Sturdy**: Survives the guaranteed critical hit
- **Type immunities**: Normal immunity rules still apply

#### Strategic Counters
- **Intimidate**: Reduces physical Attack before the critical hit
- **Burn status**: Halves physical damage output
- **Reflect/Light Screen**: Reduces damage from special/physical attacks
- **Priority moves**: Can outspeed and KO before Ambush activates

### Weather and Terrain Interactions
- **No direct interactions**: Weather doesn't affect Ambush activation
- **Indirect synergies**: Weather boosts (sun/rain) can enhance crit damage
- **Terrain benefits**: Grassy Terrain priority boost can enhance first-turn pressure

### Version History
- Custom Elite Redux ability
- Part of the expanded ability system
- Designed to reward aggressive switching and offensive play
- Balanced by single-turn limitation

### Usage Tips
1. **Switch timing**: Best used when you can predict opponent's moves
2. **Move selection**: Choose your strongest STAB moves for maximum impact
3. **Item synergy**: Consider Choice Band/Specs for devastating first strikes
4. **Team support**: Use entry hazards to guarantee KOs with the critical hit
5. **Preserve advantage**: Consider switching out after the first turn to reset the ability