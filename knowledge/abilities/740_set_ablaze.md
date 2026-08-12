---
id: 740
name: Set Ablaze
status: reviewed
character_count: 176
---

# Set Ablaze - Ability ID 740

## In-Game Description
"Inflicting burn also inflicts fear."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user applies burn, they also apply fear. Fear traps the target for 2 turns and they take 50% more damage. If forced out by moves like Whirlwind, the target loses Fear.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Set Ablaze is a unique offensive ability that adds fear status to any successful burn infliction. This creates a dual status condition combo that provides both damage over time and battlefield control.

### Activation Conditions
- **Primary trigger**: Whenever the Pokemon successfully inflicts burn on an opponent
- **Sources include**:
  - Burn-inducing moves (Scald, Flamethrower, Will-O-Wisp, etc.)
  - Contact burns from other abilities like Flame Body
  - Secondary burn effects from moves
- **Fear application**: Occurs immediately after burn is confirmed

### Technical Implementation
The ability uses the `setStateOnEffect` mechanism combined with `PoisonPuppeteerClone` pattern:

```c
constexpr Ability SetAblaze = {
    .onReactive = BloodBath.onReactive,  // Uses reactive trigger system
    .onBattlerFaints = PoisonPuppeteer.onBattlerFaints,  // State management
    .onBattlerFaintsFor = APPLY_ON_OTHER,
    .setStateOnEffect = MOVE_EFFECT_BURN,  // Triggers on burn application
};
```

The ability:
1. Monitors for burn status infliction via `setStateOnEffect = MOVE_EFFECT_BURN`
2. Uses the reactive system to apply fear to targets that don't already have fear
3. Executes via `BattleScript_Bloodlust` which sets `MOVE_EFFECT_FEAR`

### Fear Status Mechanics
Fear is a volatile status that:
- **Prevents switching**: Target cannot switch out normally
- **Blocks status moves**: Target cannot use non-damaging moves
- **Temporary effect**: Fear wears off after several turns or when the fear-inflicting Pokemon switches out
- **No immunity**: Most Pokemon cannot be immune to fear (unlike other statuses)

### Important Interactions
- **Burn immunity**: If target is immune to burn, fear is not applied
- **Already burned**: Fear can still be applied to already burned targets if they lack fear
- **Scald interactions**: Works perfectly with Scald's 30% burn chance
- **Flame Body synergy**: Contact moves can trigger both burn and fear
- **Status overlap**: Burn and fear can coexist with other status conditions

### Strategic Applications

#### Offensive Control
- **Switch trapping**: Forces opponents to stay in unfavorable matchups
- **Status move lockdown**: Prevents setup moves, recovery, and utility moves
- **Momentum control**: Maintains offensive pressure by preventing switches

#### Team Synergy
- **Hazard support**: Pairs well with entry hazards since opponents can't switch
- **Setup opportunities**: Teammates can set up while opponent is fear-locked
- **Wallbreaking**: Breaks defensive cores by preventing switches to counters

### Move Synergies
- **Scald**: Perfect STAB move with reliable burn chance
- **Will-O-Wisp**: Guaranteed burn + fear combo (if hits)
- **Flamethrower/Fire Blast**: Solid burn chances with good damage
- **Sacred Fire**: High burn rate with excellent power
- **Lava Plume**: Spread burn potential in doubles

### Ability Synergies
- **Pyromancy**: Boosts burn chances for more fear opportunities  
- **Serene Grace**: Doubles secondary effect chances including burns
- **Water Compaction**: On Water/Fire types for defensive utility
- **Flash Fire**: Fire immunity while retaining burn capability

### Counters and Limitations
- **Burn immunity**: Fire types, Water Veil, etc. prevent the combo entirely
- **Fear immunity**: Very rare, but some effects can prevent fear
- **Substitute**: Blocks status infliction entirely
- **Magic Bounce**: Reflects Will-O-Wisp back at user
- **Switching moves**: U-turn, Volt Switch, etc. can escape fear

### Competitive Viability
- **Control archetype**: Excellent for control-oriented teams
- **Anti-setup**: Shuts down setup sweepers effectively  
- **Wallbreaker support**: Traps walls for teammates to break
- **Hazard synergy**: Maximizes entry hazard damage
- **Late-game closer**: Powerful endgame control tool

### Common Users
Pokemon that benefit most from Set Ablaze:
- **Fire/Water types**: Natural access to burn moves
- **Bulky attackers**: Can survive to utilize the control aspect
- **Hazard setters**: Maximize trapped opponent punishment
- **Mixed attackers**: Benefit from both physical and special burn moves

### Version History
- **Elite Redux exclusive**: Custom ability not found in mainline games
- **Inspired by**: Control abilities like Shadow Tag and Arena Trap
- **Unique mechanic**: First ability to link two different status effects

### Usage Tips
1. **Priority targets**: Use on setup sweepers and defensive pivots
2. **Timing**: Apply early to maintain control throughout battle
3. **Team building**: Include hazards and setup sweepers as teammates
4. **Coverage**: Ensure burn moves hit different types effectively
5. **Endgame**: Save for crucial late-game control moments