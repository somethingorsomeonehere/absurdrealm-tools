---
id: 196
name: Merciless
status: reviewed
character_count: 108
---

# Merciless - Ability ID 196

## In-Game Description
"Always crits slowed, poisoned, paralyzed, or bleeding foes."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees critical hits against targets who are poisoned, paralyzed, bleeding, or have their speed lowered. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Merciless forces critical hits against targets meeting specific conditions:
- **Poisoned**: Any poison status (regular poison, badly poisoned)
- **Paralyzed**: Standard paralysis status condition
- **Bleeding**: Elite Redux's bleeding status condition
- **Speed Lowered**: Any Pokemon with Speed stat stages below 0 (lowered from base)
- **Iron Ball**: Pokemon holding the Iron Ball item

### Technical Implementation
```cpp
constexpr Ability Merciless = {
    .onCrit = +[](ON_CRIT) -> int {
        if (gBattleMons[target].status1 & STATUS1_PSN_ANY) return ALWAYS_CRIT;
        if (gBattleMons[target].status1 & STATUS1_PARALYSIS) return ALWAYS_CRIT;
        if (gBattleMons[target].status1 & STATUS1_BLEED) return ALWAYS_CRIT;
        if (gBattleMons[target].statStages[STAT_SPEED] < DEFAULT_STAT_STAGE) return ALWAYS_CRIT;
        if (GetBattlerHoldEffect(target, TRUE) == HOLD_EFFECT_IRON_BALL) return ALWAYS_CRIT;
        return 0;
    },
};
```

### Activation Conditions
1. **Status Conditions**: Target must have poison, paralysis, or bleeding
2. **Stat Stages**: Target's Speed must be below 0 (any amount of Speed reduction)
3. **Items**: Target holds Iron Ball (reduces Speed and grounds Flying types)

### Numerical Values
- **Critical Hit Chance**: 100% (guaranteed) when conditions are met
- **Critical Hit Multiplier**: 1.5x damage (standard critical hit damage)
- **No Additional Damage**: Merciless only guarantees crits, doesn't add extra damage beyond the crit multiplier

### Affected Moves
- **All offensive moves** that can normally critical hit
- **Does not affect** moves that cannot crit (e.g., fixed damage moves)
- **Works with** multi-hit moves (each hit can crit if conditions are met)

### Interactions with Other Abilities/Mechanics
- **Stacks with**: High critical hit ratio moves (already guaranteed, so no additional benefit)
- **Battle Armor/Shell Armor**: These abilities prevent critical hits, negating Merciless
- **Sniper**: Increases critical hit damage to 2.25x when Merciless triggers
- **Super Luck**: Redundant with Merciless when conditions are met
- **Scope Lens/Razor Claw**: No additional benefit when Merciless conditions are met

### Strategic Implications
- **Offensive Synergy**: Pairs excellently with status-inducing moves
- **Team Support**: Benefits from teammates using status moves or speed control
- **Move Selection**: Prioritize moves that can inflict the relevant status conditions
- **Item Synergy**: King's Rock/Razor Fang for additional flinch chance on guaranteed crits

### Example Damage Calculations
**Scenario**: Level 50 Pokemon with 100 Attack vs Level 50 Pokemon with 100 Defense
- **Normal Hit**: 100% damage
- **Merciless Critical Hit**: 150% damage (1.5x multiplier)
- **With Sniper**: 225% damage (2.25x multiplier)

### Common Users
Merciless is found on Pokemon that often use status moves or have access to moves that can trigger the conditions:
- **Toxtricity**: Can poison with electric moves
- **Crobat**: Fast Pokemon that can inflict status
- **Ariados**: Spider Pokemon with access to status moves

### Competitive Usage Notes
- **Status Teams**: Excellent on teams focused on status condition spreading
- **Revenge Killer**: Effective against teams that rely on speed control
- **Setup Counter**: Punishes opponents who use stat-lowering moves defensively

### Counters
- **Battle Armor/Shell Armor**: Completely negates Merciless
- **Clerics**: Pokemon that can remove status conditions
- **Lum Berry/Pecha Berry**: Items that cure status conditions
- **Natural Cure**: Ability that removes status on switch-out
- **Speed Boost**: Can counteract speed reductions

### Synergies
- **Toxic Spikes**: Automatic poison setup for guaranteed crits
- **Thunder Wave**: Paralysis support for team
- **Sticky Web**: Speed reduction support
- **Corrosion**: Allows poisoning of Steel/Poison types
- **Prankster**: Priority status moves for setup

### Combination Abilities
**Depravity**: Merciless + Overcharge
- Combines guaranteed crits with type effectiveness manipulation
- Extremely powerful offensive combination

**Relentless**: Exploit Weakness + Merciless
- Guaranteed crits plus defensive stat targeting
- Devastating against weakened opponents

### Version History
- **Elite Redux**: Expanded to include bleeding status and Iron Ball interaction
- **Original**: Only affected poisoned and paralyzed targets
- **Elite Redux Addition**: Added speed reduction and bleeding conditions for more consistent activation