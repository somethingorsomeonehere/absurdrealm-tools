---
id: 411
name: Toxic Spill
status: reviewed
character_count: 143
---

# Toxic Spill - Ability ID 411

## In-Game Description
"Non-Poison-types take 1/8 dmg every turn when on field."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Toxic Spill damages all non-Poison-type Pokemon by 1/8 HP each turn. Pokemon with Poison Heal recover instead. Disappears when the user leaves. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Toxic Spill is a field control ability that creates a persistent toxic waste environment. When a Pokemon with this ability enters battle, it announces the toxic spill and begins damaging all non-Poison-type Pokemon at the end of each turn.

### Activation Conditions
- **Entry trigger**: Activates immediately when the Pokemon enters battle
- **Field persistence**: Effect continues while the user is on the field
- **Exit cleanup**: Toxic waste dissipates when the user switches out or faints
- **Poison type immunity**: Poison-type Pokemon are completely immune to damage
- **Monotype exception**: Doesn't activate in Poison-type monotype champion battles

### Damage Mechanics
- **Damage amount**: 1/8 of the target's maximum HP per turn
- **Timing**: Activates during end-of-turn phase
- **Type immunity**: Only affects non-Poison-type Pokemon
- **Magic Guard bypass**: Deals damage even to Pokemon with Magic Guard
- **Toxic Boost immunity**: Pokemon with Toxic Boost are protected from damage

### Technical Implementation
```cpp
constexpr Ability ToxicSpill = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(getMonotypeChampType() == TYPE_POISON)
        BattleScriptPushCursorAndCallback(BattleScript_BattlerAnnouncedToxicSpill);
        return TRUE;
    },
    .onEndTurn = +[](ON_END_TURN) -> int {
        // Check for source abilities (Toxic Spill or Trash Heap)
        int any = FALSE;
        for (int target = 0; target < gBattlersCount; target++) {
            FILTER(IsBattlerAlive(target))
            
            // Poison Heal interaction - heal instead of damage
            if (BATTLER_HAS_ABILITY(target, ABILITY_POISON_HEAL)) {
                // Heal the target instead of damaging
                gStackBattler1 = target;
                BattleScriptExecute(BattleScript_ToxicWasteHeal);
                any = TRUE;
                continue;
            }
            
            // Skip Poison types, Magic Guard, and Toxic Boost
            FILTER_NOT(IS_BATTLER_OF_TYPE(target, TYPE_POISON))
            FILTER_NOT(IsMagicGuardProtected(target))
            FILTER_NOT(BATTLER_HAS_ABILITY(battler, ABILITY_TOXIC_BOOST))
            
            // Deal 1/8 damage
            gStackBattler1 = target;
            BattleScriptExecute(BattleScript_ToxicWasteTurnDmg);
            any = TRUE;
        }
        return any;
    },
    .onExit = +[](ON_EXIT) -> int {
        CHECK_NOT(getMonotypeChampType() == TYPE_POISON)
        BattleScriptCall(BattleScript_TheToxicWasHasDissapeared);
        return TRUE;
    },
};
```

### Special Interactions
- **Poison Heal synergy**: Pokemon with Poison Heal recover HP instead of taking damage
- **Magic Guard bypass**: Unlike most passive damage, this bypasses Magic Guard protection
- **Toxic Boost protection**: Pokemon with Toxic Boost are immune to the damage
- **Type immunity**: Only Poison-type Pokemon are completely immune
- **Multi-source stacking**: Multiple sources (Toxic Spill + Trash Heap) don't stack damage

### Battle Messages
- **Entry**: "{Pokemon} has spilled Toxic Waste on the field!"
- **Damage**: "{Pokemon} is hurt by the toxic waste!"
- **Healing**: "{Pokemon} restored HP using its Poison Heal!"
- **Exit**: "The Toxic Waste has disappeared!"

### Strategic Applications
- **Passive damage dealer**: Excellent for wearing down opponents over time
- **Switch punishment**: Forces opponent to make faster decisions
- **Stall breaking**: Counters defensive strategies and walls
- **Poison team support**: Provides field control without affecting team
- **Entry hazard alternative**: Creates ongoing pressure without hazard removal vulnerability

### Trash Heap Connection
Toxic Spill is also part of the **Trash Heap** ability (ID varies), which combines:
- **Toxic Spill effects**: All field control and damage mechanics
- **Corrosion effects**: Can poison Steel and Poison types with moves
- **Dual functionality**: Both field control and status infliction

### Counters and Weaknesses
- **Poison types**: Completely immune to damage
- **Poison Heal**: Turns damage into healing
- **Toxic Boost**: Provides immunity to the damage
- **Switching**: User must stay on field to maintain effect
- **Direct targeting**: Focus fire on the user to remove effect
- **Rapid KO**: Fast elimination prevents prolonged damage

### Team Synergies
- **Poison teams**: Natural immunity allows aggressive switching
- **Stall teams**: Provides passive damage while stalling
- **Pivot Pokemon**: Can switch in, cause damage, then pivot out
- **Entry hazard stackers**: Combines with hazards for multiple damage sources
- **Healing support**: Pairs with healing to outlast opponents

### Competitive Viability
- **Doubles format**: Affects all opponents simultaneously
- **Singles format**: Forces opponent switching and creates pressure
- **Defensive cores**: Breaks through defensive play styles
- **Late-game presence**: Excellent for finishing weakened opponents
- **Setup deterrent**: Discourages prolonged setup attempts

### Version Notes
- **Elite Redux exclusive**: Custom ability unique to this romhack
- **Field effect**: Creates persistent environmental hazard
- **Type-based immunity**: Follows Poison-type damage immunity rules
- **Ability interaction**: Complex interactions with multiple abilities
- **Balance consideration**: Bypasses some defensive abilities while respecting others