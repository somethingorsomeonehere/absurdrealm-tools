---
id: 415
name: Self Repair
status: reviewed
character_count: 110
---

# Self Repair - Ability ID 415

## In-Game Description
"Self Sufficient + Natural Cure."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Recovers 1/16th of max HP at the end of the turn and cures all status conditions when switching out of battle. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Self Repair is a combination ability that merges the effects of **Self Sufficient** and **Natural Cure**, providing both HP recovery and status condition removal when switching out of battle.

### Component Abilities
1. **Self Sufficient** (ID 307): Provides HP restoration upon switching out
2. **Natural Cure** (ID 30): Removes all status conditions upon switching out

### Activation Conditions
**Triggers on:**
- Manual switches by the player
- Forced switches from moves (Roar, Whirlwind, Dragon Tail, Circle Throw)
- Pivot moves (U-turn, Volt Switch, Flip Turn, Teleport)
- Items causing switches (Red Card activation)
- Emergency Exit/Wimp Out activation

**Does NOT trigger on:**
- Fainting/KO
- End of battle

### Technical Implementation
```c
// Self Repair combines both effects on switch out
.onExit = +[](ON_EXIT) -> int {
    // Self Sufficient component - HP restoration
    if (IsValid(battler) && !IsFullHP(battler)) {
        // Heal HP (exact percentage needs verification)
        RestoreHP(battler, percentage);
    }
    
    // Natural Cure component - status removal
    if (gBattleMons[battler].status1 & STATUS1_ANY) {
        gBattleMons[battler].status1 &= ~STATUS1_ANY;
        // Show status cure message
    }
}
```

### HP Restoration Details
Based on similar abilities like Regenerator, Self Sufficient likely restores:
- **Amount**: Needs verification (likely 25-33% of max HP)
- **Condition**: Only if below maximum HP
- **Timing**: Simultaneous with status cure on exit

### Status Conditions Cured
- Sleep (including Rest-induced sleep)
- Poison (regular and badly poisoned)
- Burn
- Paralysis
- Freeze

### Strategic Applications

**Ultimate Defensive Pivot:**
- Switch into status moves with impunity
- Absorb damage and status effects
- Switch out for full restoration
- Return to battle healthy and status-free

**Hazard Absorber:**
- Tank entry hazards damage
- Heal back the damage on switch out
- Immune to status from moves
- Excellent for hazard control teams

**Tank Support:**
- Absorb powerful attacks
- Heal significant damage on exit
- Remove status inflicted during stay
- Maintain defensive presence

### Synergies
- **U-turn/Volt Switch**: Maintain momentum while fully healing
- **Pivot strategies**: Perfect for VoltTurn cores
- **Defensive cores**: Excellent wall for balanced teams
- **Status absorption**: Protects team from status spam
- **Rest**: Can use Rest and cure sleep immediately on switch

### Advantages Over Individual Components
- **Better than Natural Cure alone**: Also heals HP damage
- **Better than Self Sufficient alone**: Also removes status
- **Superior to items**: Unlimited uses, can't be removed
- **Flexibility**: Provides both defensive needs in one ability

### Competitive Usage
Self Repair is ideal for:
- Defensive pivots that need both HP and status management
- Pokemon with naturally high bulk
- VoltTurn team members
- Status absorbers on balanced teams
- Pokemon that commonly face status moves

### Limitations
- **Switching requirement**: Must leave field to activate
- **No protection while active**: Still vulnerable to status/damage while in
- **Pursuit vulnerability**: Risky against Pursuit users
- **Entry hazard weakness**: Takes damage coming back in
- **No teammate benefits**: Only heals self

### Counters
- **Trapping abilities**: Arena Trap, Shadow Tag prevent switching
- **Trapping moves**: Mean Look, Block, Spider Web
- **Pursuit**: Punishes switch attempts
- **Entry hazards**: Damage on re-entry reduces net healing
- **Taunt**: Prevents setup moves that force switches

### Team Building Considerations
- **VoltTurn cores**: Essential member of pivot teams
- **Balanced teams**: Excellent defensive backbone
- **Hazard control**: Works well with Rapid Spin/Defog users
- **Status immunity**: Reduces need for dedicated clerics
- **Flexibility**: Allows for more aggressive item choices

### Related Abilities
- **Natural Recovery** (Natural Cure + Regenerator): Similar concept with different HP healing
- **Natural Cure**: Component ability for status removal
- **Self Sufficient**: Component ability for HP restoration
- **Regenerator**: Similar HP restoration mechanism

### Pokemon with Self Repair
Self Repair is likely found on:
- Defensive Pokemon that naturally learn both component abilities
- Pokemon designed as defensive pivots
- Tank Pokemon with good bulk and utility moves

### Version Notes
Self Repair represents Elite Redux's combination ability system, where two compatible abilities are merged into a single more powerful effect. This creates unique strategic options not available in standard Pokemon games.

### Verification Needed
- Exact HP restoration percentage from Self Sufficient
- Specific Pokemon that learn this ability
- Interaction with other healing effects
- Battle message text for both components