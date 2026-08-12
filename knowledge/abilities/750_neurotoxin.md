---
id: 750
name: Neurotoxin
status: reviewed
character_count: 126
---

# Neurotoxin - Ability ID 750

## In-Game Description
"Inflicting poison also lowers Attack, SpAtk, and Speed."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When inflicting poison on an opponent, drop their Attack, Special Attack, and Speed by one stage immediately after it applies.

## Detailed Mechanical Explanation
*For Discord/reference use*

Neurotoxin is a reactive ability that triggers additional stat debuffs whenever the user successfully poisons an opponent. It's built on the "PoisonPuppeteer" framework, which tracks poison infliction and applies secondary effects.

### Core Mechanics
- **Trigger Condition**: When the user inflicts poison on any opponent
- **Primary Effect**: Lowers target's Attack, Special Attack, and Speed by 1 stage each
- **Activation Timing**: Immediately after poison is successfully applied
- **Multi-target Support**: Affects all targets that get poisoned in the same turn

### Technical Implementation
```cpp
static int NeurotoxinCondition(int battler, int target) {
    return CanLowerStat(target, STAT_ATK) || CanLowerStat(target, STAT_SPATK) || CanLowerStat(target, STAT_SPEED);
}

constexpr Ability Neurotoxin = {
    .onReactive = +[](ON_REACTIVE) -> int { return PoisonPuppeteerClone(ability, battler, NeurotoxinCondition, BattleScript_Neurotoxin); },
    .onBattlerFaints = PoisonPuppeteer.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_OTHER,
    .setStateOnEffect = MOVE_EFFECT_POISON,
};
```

### Activation Requirements
- The user must successfully inflict poison (regular poison or badly poisoned)
- Target must not be immune to stat reduction
- At least one of the three stats (Attack, Sp. Attack, Speed) must be lowerable

### Battle Script Effects
The battle script `BattleScript_Neurotoxin` performs the following sequence:
1. Attempts to lower Attack by 1 stage
2. Attempts to lower Special Attack by 1 stage  
3. Attempts to lower Speed by 1 stage
4. Shows appropriate messages for each successful/failed stat change
5. Plays stat decrease animation for all affected stats simultaneously

### Affected Moves and Methods
Neurotoxin triggers from any source of poison infliction:
- **Direct Poison Moves**: Poison Gas, Poison Powder, Toxic, etc.
- **Secondary Effect Moves**: Sludge Bomb, Poison Jab, Sludge Wave (30% poison chance)
- **Status-Inflicting Moves**: Poison Sting, Twineedle
- **Ability-Based Poison**: Poison Point, Effect Spore (if user has Neurotoxin)
- **Item-Based Poison**: Toxic Orb (when passed to opponent)

### Interactions with Other Mechanics

**Stat Reduction Immunities**:
- Clear Body, White Smoke, Full Metal Body prevent all stat drops
- Hyper Cutter prevents Attack reduction specifically
- Keen Eye prevents accuracy reduction (not relevant here)

**Competitive Interactions**:
- **Substitute**: Cannot lower stats of a Pokemon behind Substitute
- **Mist**: Prevents stat reduction while active
- **Sacred Sword/Chip Away**: Ignores stat changes but doesn't prevent them
- **Contrary**: Would boost stats instead of lowering them

### Strategic Applications

**Offensive Strategy**:
- Pairs excellently with multi-hit poison moves like Poison Jab
- Synergizes with Toxic Spikes for entry hazard control
- Works well with poison-spreading abilities and moves

**Defensive Strategy**:
- Weakens physical and special attackers simultaneously
- Speed reduction helps with revenge kills and priority moves
- Creates momentum through stat pressure

### Common Users
- **Mega Arbok**: Poison/Dark type with strong offensive presence
- **Gliscor (Redux Form)**: Poison/Fire variant with enhanced offensive capabilities

### Competitive Viability

**Strengths**:
- Immediate impact beyond just poison damage
- Multi-stat debuff creates significant swing turns
- Stacks with other stat-reducing effects
- Works on both physical and special attackers

**Weaknesses**:
- Requires successful poison infliction to activate
- Blocked by stat immunity abilities
- Single-use per target (poison immunity after first application)
- Many Pokemon carry Pecha Berry or similar items

### Counters and Responses
- **Poison Immunity**: Poison, Steel types naturally immune
- **Immunity Abilities**: Immunity, Poison Heal, Water Veil (burns only)
- **Restoration**: Aromatherapy, Heal Bell remove poison and stop future triggers
- **Stat Immunity**: Clear Body, White Smoke, etc. prevent debuffs
- **Cleric Support**: Teammates with status removal moves

### Synergistic Abilities and Moves
- **Merciless**: Extra damage against poisoned targets
- **Hex**: Double damage against status-afflicted targets  
- **Venoshock**: Double damage against poisoned targets
- **Toxic Spikes**: Automatic poison on switch-in
- **Corrosion**: Allows poisoning of Steel and Poison types

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Built on the PoisonPuppeteer framework for consistent poison-trigger mechanics
- Designed to give poison-type specialists more battlefield control options