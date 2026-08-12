---
id: 483
name: Natural Recovery
status: reviewed
character_count: 99
---

# Natural Recovery - Ability ID 483

## In-Game Description
"Natural Cure + Regenerator."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Cures all status conditions when switching out. Also restores 33% of maximum HP when switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Natural Recovery is a powerful hybrid ability that combines two of the most useful exit abilities in the game: Natural Cure and Regenerator. When the Pokemon switches out, both effects trigger simultaneously, providing complete status recovery and significant HP restoration.

### Activation Conditions
- **Trigger**: Activates when the Pokemon switches out of battle
- **Requirements**: Pokemon must be alive when switching out
- **Status cure**: Removes all major status conditions (burn, freeze, paralysis, poison, sleep, frostbite)
- **HP recovery**: Restores 33% of maximum HP if not at full health
- **Timing**: Both effects occur simultaneously during the exit process

### Technical Implementation
```c
// Natural Recovery combines two abilities using delegation
constexpr Ability NaturalRecovery = {
    .onExit = +[](ON_EXIT) -> int { 
        return NaturalCure.onExit(DELEGATE_EXIT) | Regenerator.onExit(DELEGATE_EXIT); 
    },
};

// Natural Cure component - status removal
NaturalCure.onExit: Clears all STATUS1_ANY conditions
// Regenerator component - HP recovery  
Regenerator.onExit: Heals 33% max HP via BattleScript_RegeneratorExits
```

### Status Conditions Cured
Natural Recovery removes all major status conditions:
- **Burn** - Including damage reduction effect
- **Freeze** - Complete immobilization removal
- **Paralysis** - Speed reduction and move failure chance
- **Poison** - Both regular and badly poisoned variants
- **Sleep** - Including sleep counter reset
- **Frostbite** - Special attack reduction removal

### HP Recovery Details
- **Amount**: 33% of maximum HP
- **Condition**: Only if current HP < maximum HP
- **Script**: Uses `tryhealpercenthealth BS_ATTACKER, 33`
- **Display**: Shows HP recovery animation and message
- **Stacking**: Does not stack with items like Leftovers during switch

### Important Interactions
- **Simultaneous effects**: Both status cure and HP recovery happen together
- **Switch-in safety**: Pokemon returns to battle fully status-free with boosted HP
- **U-turn/Volt Switch synergy**: Excellent with pivot moves for repeated benefit
- **Rest compatibility**: Can use Rest and switch out for immediate wake-up plus healing
- **Burn/Poison immunity**: Effectively immune to status damage due to instant cure

### Battle AI Recognition
The AI recognizes Natural Recovery in several contexts:
- **Smart switching**: AI will force switch if burned with only physical moves
- **Frostbite handling**: AI switches out if frostbitten with only special moves
- **Sleep cure**: AI considers switching when asleep to remove sleep status
- **Score bonus**: Gets switching score of 90 when status conditions warrant it

### Strategic Applications
- **Pivot strategy**: Excellent on U-turn/Volt Switch users for repeated healing
- **Status absorber**: Can safely switch into status moves without long-term penalty
- **Tank longevity**: Bulky Pokemon can repeatedly switch for sustained presence
- **Team support**: Acts as a reliable status cure and HP restoration for the team
- **Hit-and-run**: Perfect for hit-and-run tactics with guaranteed recovery

### Common Users in Elite Redux
Natural Recovery appears on various Pokemon as both regular and innate ability:
- **Support Pokemon**: Especially those with healing/support roles
- **Defensive walls**: Bulky Pokemon that benefit from repeated recovery
- **Pivot users**: Pokemon with U-turn, Volt Switch, or Flip Turn
- **Status-weak types**: Pokemon that particularly fear status conditions

### Synergistic Moves
- **U-turn/Volt Switch**: Repeated switching for constant benefit
- **Rest**: Immediate status cure without sleep drawback
- **Roost**: Can use Roost, then switch for additional recovery
- **Healing moves**: Stacks with in-battle healing for maximum longevity
- **Entry hazard removal**: Can switch in to clear hazards, then recover

### Counters and Limitations
- **Switching out required**: Must actually switch to gain benefit
- **Trapping moves**: Shadow Tag, Block, Mean Look prevent switching
- **Pursuit**: Takes damage when switching (though recovers after)
- **Entry hazards**: Hazard damage occurs after the ability benefits
- **One-time per switch**: Benefits only apply once per switch cycle

### Competitive Viability
Natural Recovery is considered one of the strongest abilities in Elite Redux due to:
- **Dual benefit**: Both status immunity and HP recovery in one ability
- **Reliability**: Always works when switching out (no conditions)
- **Team utility**: Provides consistent team support through repeated switching
- **Longevity**: Dramatically increases Pokemon's staying power
- **Flexibility**: Works with any playstyle that involves switching

### Comparison to Component Abilities
- **vs Natural Cure**: Adds significant HP recovery for better overall value
- **vs Regenerator**: Adds complete status immunity for enhanced utility
- **vs other exit abilities**: Generally superior due to dual benefits
- **Trade-off**: Takes up ability slot but provides two major benefits

### Version History
- Custom Elite Redux ability combining two classic abilities
- Part of the expanded ability system with over 500 abilities
- Designed to create powerful but balanced hybrid effects
- Available as both regular ability and innate ability depending on species