---
id: 467
name: Magma Eater
status: reviewed
character_count: 178
---

# Magma Eater - Ability ID 467

## In-Game Description
"Predator + Molten Down."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user knocks out an opponent with a direct hit, it immediately recovers 25% of its maximum HP. Fire-type are moves super effective against Rock-types instead of resisted. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Magma Eater is a dual-effect offensive ability that combines two powerful combat mechanics: predatory healing and molten type manipulation. This ability makes its user exceptionally dangerous in battle by rewarding successful KOs and providing type advantage coverage.

### Healing Component (SoulEater Effect)
- **Trigger**: When the Pokemon with Magma Eater faints an opponent through a direct attacking move
- **Effect**: Restores 25% of the user's maximum HP
- **Timing**: Healing occurs immediately after the opponent faints
- **Requirements**: 
  - Must not be at full HP already
  - Must be able to heal (not affected by Heal Block)
  - Opponent must faint from the user's direct attack

### Type Effectiveness Component (MoltenDown Effect)
- **Trigger**: When using a Fire-type move against a Rock-type target
- **Effect**: Fire-type moves deal 2x damage to Rock-type Pokemon instead of normal effectiveness
- **Coverage**: Transforms neutral matchup into super effective damage
- **Stacking**: Works with other damage modifiers and STAB

### Technical Implementation
```c
// Magma Eater combines two existing ability effects
constexpr Ability MagmaEater = {
    .onBattlerFaints = SoulEater.onBattlerFaints,        // 25% HP restore on KO
    .onTypeEffectiveness = MoltenDown.onTypeEffectiveness, // Fire vs Rock = 2x
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};

// Healing effect (25% HP recovery)
BattleScript_HandleSoulEaterEffect::
    tryhealpercenthealth BS_STACK_1, 25, BattleScript_Return

// Type effectiveness modification
.onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
    CHECK(moveType == TYPE_FIRE)
    CHECK(defType == TYPE_ROCK)
    *mod = UQ_4_12(2.0);  // 2x damage multiplier
    return TRUE;
},
```

### Important Interactions
- **Multi-hit moves**: Only heals once per opponent fainted, not per hit
- **Indirect damage**: Healing doesn't trigger from burns, poison, entry hazards, etc.
- **Full HP**: No healing occurs if already at maximum HP
- **Heal Block**: Healing component blocked by Heal Block status
- **Type effectiveness**: Fire vs Rock becomes 2x instead of 1x (neutral)
- **STAB interaction**: Stacks with Same Type Attack Bonus multiplicatively
- **Weather**: Fire power boost from sun stacks with type effectiveness bonus

### Strategic Applications
- **Sweeping potential**: Healing allows extended battles and multiple KOs
- **Rock-type coverage**: Gives Fire-type attackers better matchup coverage
- **Aggressive playstyle**: Rewards offensive momentum and direct confrontation
- **HP management**: Can recover from chip damage through successful KOs
- **Type coverage**: Improves Fire-type movesets against typically resistant Rock types

### Ideal Users
- **Fire-type attackers** with diverse movepools
- **Mixed attackers** who can reliably score KOs
- **Pokemon with high offensive stats** to secure faints
- **Sweepers** who benefit from mid-battle healing
- **Rock-type coverage seekers** in Fire-type focused teams

### Competitive Advantages
- **Sustained offense**: Healing extends staying power in battle
- **Type coverage improvement**: Better matchups against Rock-type walls
- **Snowball potential**: Each KO makes subsequent battles easier
- **Pressure creation**: Forces opponents to play around healing threat
- **Versatile threat**: Combines offensive and defensive utility

### Counters and Limitations
- **Heal Block**: Completely negates healing component
- **Indirect damage**: Burns, poison, and hazards don't trigger healing
- **Rock/Water or Rock/Ground types**: Still resist Fire despite type modification
- **Defensive walls**: Must actually faint opponents to benefit from healing
- **Priority moves**: Can be revenge killed before healing activates
- **Status conditions**: Sleep, paralysis can prevent follow-up attacks

### Synergies
- **Life Orb**: Recoil damage offset by healing from KOs
- **Choice items**: Locked moves still trigger healing on KO
- **Sun teams**: Fire power boost stacks with type effectiveness
- **Entry hazard support**: Chip damage helps secure KO thresholds
- **Flame Charge/Dragon Dance**: Speed boost + healing creates powerful setup
- **Fire Blast/Flamethrower**: Reliable Fire moves to trigger Rock effectiveness

### Team Composition
- **Sun setters**: Drought users to boost Fire move power
- **Entry hazard setters**: Stealth Rock, Spikes to weaken opponents
- **Speed control**: Thunder Wave, Trick Room to ensure attack order
- **Rock-type lures**: Draw in Rock types for super effective Fire attacks
- **Offensive cores**: Partners that can also score KOs for momentum

### Usage Notes
- **Primary mode**: Best used as an aggressive attacker rather than defensive pivot
- **Target selection**: Prioritize Rock-type opponents when possible
- **HP monitoring**: Most effective when not at full health to maximize healing
- **Move selection**: Ensure access to reliable Fire-type attacking moves
- **Timing**: Consider healing potential when choosing between opponents to target

### Version History
- **Elite Redux exclusive**: Custom combination ability
- **Component abilities**: Based on existing SoulEater (Predator) and MoltenDown effects
- **Balance considerations**: 25% healing is standard for KO-based healing abilities
- **Type effectiveness**: 2x multiplier provides meaningful but not overwhelming advantage