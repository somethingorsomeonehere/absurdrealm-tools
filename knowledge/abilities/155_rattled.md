---
id: 155
name: Rattled
status: reviewed
character_count: 118
---

# Rattled - Ability ID 155

## In-Game Description
"If hit by Bug, Dark or Ghost move, or flinches: +1 Speed."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Speed by one stage when hit by Bug, Dark, or Ghost-type moves. Activates multiple times against multihit moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Rattled is a defensive ability that boosts the user's Speed stat by one stage (+50% Speed) when triggered by specific conditions.

### Current Implementation
```cpp
constexpr Ability Rattled = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(moveType == TYPE_DARK || moveType == TYPE_BUG || moveType == TYPE_GHOST)
        CHECK(CanRaiseStat(battler, STAT_SPEED))

        SetStatChanger(STAT_SPEED, 1);
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        return TRUE;
    },
};
```

### Activation Conditions
**Currently Implemented:**
- Hit by a Bug-type move that deals damage
- Hit by a Dark-type move that deals damage  
- Hit by a Ghost-type move that deals damage

**Listed in Description but Not Implemented:**
- When the Pokemon flinches (mentioned in proto description but no code implementation found)

### Technical Requirements
- `ShouldApplyOnHitAffect(battler)` must return true
- Move must be Bug, Dark, or Ghost type
- `CanRaiseStat(battler, STAT_SPEED)` must return true (Speed not at +6)
- Pokemon must survive the hit to gain the boost

### Stat Boost Details
- **Boost Amount**: +1 Speed stage (50% increase)
- **Maximum**: Won't trigger if Speed is already at +6 stages
- **Timing**: Activates after damage calculation, before move end
- **Battle Script**: Uses `BattleScript_TargetAbilityStatRaiseOnMoveEnd`

### Interaction Notes
- **Multi-Hit Moves**: Each hit can potentially trigger Rattled separately
- **Status Moves**: Do not trigger Rattled (damage-dealing moves only)
- **Substitute**: Blocked by Substitute (no damage = no trigger)
- **Magic Guard**: Still triggers even if Magic Guard prevents damage
- **Fainting**: Does not activate if the Pokemon faints from the triggering move

### Strategic Applications
**Defensive Utility:**
- Turns common attacking types (Dark, Ghost, Bug) into Speed boosts
- Particularly valuable on bulky Pokemon that can survive super-effective hits
- Synergizes with survival items like Focus Sash or Leftovers

**Speed Control:**
- Can potentially outspeed threats after taking a hit
- Useful for revenge killing or setting up on the following turn
- Combines well with priority moves for immediate retaliation

### Notable Users in Elite Redux
Based on the species data, Rattled appears on various Pokemon including:
- **Dratini line**: As a regular ability option
- **Pawmi line**: Speed-oriented Electric types
- **Fennekin line**: Fire starters with good Special Attack
- **Dugtrio**: Already fast Ground types
- **Tinkaton line**: Defensive Steel types
- Various other species as innate or regular abilities

### Competitive Considerations
**Strengths:**
- Provides immediate Speed control after taking super-effective damage
- Cannot be suppressed by Mold Breaker (ability activates post-hit)
- Useful on both offensive and defensive team roles

**Weaknesses:**
- Requires taking damage to activate (risky on frail Pokemon)  
- Limited to three specific types
- Flinch trigger apparently not implemented despite being in description
- One-time boost per battle scenario (unless Speed is lowered)

### Counters and Limitations
- **Taunt**: Prevents setup moves that might follow the Speed boost
- **Status Moves**: Paralysis or sleep negate the Speed advantage
- **Priority Moves**: Bypass the Speed boost entirely
- **Non-Triggering Types**: Many common attacking types don't activate it

### Synergistic Abilities and Items
**Items:**
- **Focus Sash**: Guarantees survival to gain the Speed boost
- **Weakness Policy**: Stacks with Rattled for both offensive and Speed boosts
- **Life Orb**: Capitalizes on the Speed boost with powered-up attacks

**Ability Combinations** (in Elite Redux's 4-ability system):
- **Quick Feet**: Double Speed boost when statused
- **Guts**: Attack boost to complement the Speed boost
- **Magic Guard**: Protects from residual damage while boosting

### Version History and Implementation Notes
- The description mentions flinch triggering Rattled, but current code implementation only handles the three move types
- This suggests either incomplete implementation or outdated description text
- AI evaluation rates this ability at 3/10 for competitive value

### Example Damage Calculations
On a Pokemon with base 100 Speed and no investment:
- **Before trigger**: 299 Speed (level 50, neutral nature)
- **After Rattled (+1)**: 448 Speed (50% increase)
- **After Rattled + Choice Scarf**: 672 Speed
- **After Rattled + Tailwind**: 896 Speed (quadruple boost scenario)