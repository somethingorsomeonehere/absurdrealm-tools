---
id: 533
name: Hubris
status: reviewed
character_count: 99
---

# Hubris - Ability ID 533

## In-Game Description
"KOs raise SpAtk by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's Special Attack by one stage whenever it knocks out an opponent with a direct hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Hubris is the Special Attack equivalent of Moxie, triggering when the Pokemon with this ability knocks out an opponent through direct damage.

### Activation Conditions
- Must directly KO an opponent with a damaging move (power > 0)
- The Pokemon with Hubris must be the attacker that deals the finishing blow
- Only triggers when using the selected move during the turn
- Does not activate from:
  - Status moves
  - Indirect damage (poison, burn, entry hazards, weather)
  - Recoil damage
  - Abilities like Aftermath or Rough Skin

### Technical Implementation
```cpp
constexpr Ability Hubris = {
    .onBattlerFaints = GrimNeigh.onBattlerFaints,  // Uses same logic as Grim Neigh
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,       // Only applies to the attacker
};

// Shared implementation with Grim Neigh:
.onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int { 
    return MoxieClone(battler, STAT_SPATK); 
},

// MoxieClone function checks:
static int MoxieClone(int battler, int stat) {
    CHECK(HasAttackerFaintedTarget())  // Validates proper KO conditions
    CHECK(ChangeStatBuffs(battler, 1, stat, MOVE_EFFECT_AFFECTS_USER | STAT_BUFF_DONT_SET_BUFFERS, NULL))
    BattleScriptCall(BattleScript_RaiseStatOnFaintingTarget);
    return TRUE;
}
```

### Numerical Values
- **Stat boost**: +1 stage to Special Attack per KO
- **Maximum boost**: +6 stages (400% of base Special Attack)
- **Boost stacking**: Each additional KO adds another +1 stage
- **Stage calculation**: Each stage = 50% increase (1.5x, 2.0x, 2.5x, 3.0x, 3.5x, 4.0x)

### Interactions with Other Abilities/Mechanics
- **Stacks with**: Choice Specs, Life Orb, other stat-boosting items/abilities
- **Blocked by**: Clear Body, White Smoke, Full Metal Body (prevents stat reduction, not boost)
- **Reset by**: Switching out, Haze, Clear Smog, stat-resetting moves
- **Copyable**: Can be copied by Trace, Role Play, Skill Swap
- **Suppressible**: Affected by Gastro Acid, Core Enforcer

### Strategic Implications
- **Sweeping potential**: Exceptional for special attackers in late-game scenarios
- **Snowball effect**: Each KO makes subsequent KOs easier to achieve
- **Team synergy**: Benefits from entry hazard support to weaken opponents
- **Risk/reward**: Requires aggressive positioning to secure KOs

### Example Damage Calculations
Base 100 Special Attack Pokemon at level 50:
- **+0 stages**: 100 Special Attack
- **+1 stage (1 KO)**: 150 Special Attack (+50%)
- **+2 stages (2 KOs)**: 200 Special Attack (+100%)
- **+3 stages (3 KOs)**: 250 Special Attack (+150%)
- **+6 stages (6 KOs)**: 400 Special Attack (+300%)

### Common Users in Elite Redux
Based on game data, Hubris appears on various special attacking Pokemon, typically those with:
- High base Special Attack stats
- Good offensive movepools
- Solid Speed or bulk to survive initial exchanges

### Competitive Usage Notes
- **Best in**: Late-game cleanup scenarios, versus weakened teams
- **Struggles against**: Bulky special walls, priority users, stat resetters
- **Team support needed**: Entry hazards, status support, pivoting moves
- **Timing critical**: Most effective when opponent's team is already damaged

### Counters
- **Stat manipulation**: Haze, Clear Smog, Topsy-Turvy
- **Defensive abilities**: Wonder Guard (if type immune), Magic Guard users
- **Priority moves**: Sucker Punch, Aqua Jet, Ice Shard
- **Passive damage**: Forcing switches through status/hazards before KOs

### Synergies
- **Life Orb**: Increased damage output to secure more KOs
- **Choice items**: Higher initial power, but locks into moves
- **Speed control**: Tailwind, Thunder Wave support
- **Entry hazards**: Stealth Rock, Spikes for damage chip
- **Pivoting support**: U-turn, Volt Switch to bring in safely

### Version History
- **Elite Redux implementation**: Uses the proven Moxie framework adapted for Special Attack
- **Consistency**: Shares exact mechanics with Moxie (Physical) and Grim Neigh (Special Attack)
- **Balance consideration**: Requires direct KOs, preventing easy abuse through indirect damage