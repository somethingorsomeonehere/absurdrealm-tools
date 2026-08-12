---
id: 30
name: Natural Cure
status: reviewed
character_count: 47
---

# Natural Cure - Ability ID 30

## In-Game Description
"Heals status condition upon switching out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Cures all status conditions when switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Natural Cure removes all major status conditions when the Pokemon switches out through any means except fainting. The ability provides a reliable way to cure status without using items or moves.

### Technical Implementation
From `/src/abilities.cc`:
```cpp
.onExit = +[](ON_EXIT) -> int {
    CHECK(gBattleMons[battler].status1 & STATUS1_ANY)
    gBattleMons[battler].status1 &= ~STATUS1_ANY;
    // Trigger battle script to show cure message
}
```

The ability:
1. Triggers on exit from battle
2. Checks for any STATUS1 condition
3. Clears all status flags
4. Shows cure notification

### Status Conditions Cured
- Sleep (including Rest)
- Poison (including Toxic)
- Burn
- Paralysis  
- Freeze

### Activation Conditions
**Triggers on:**
- Manual switch
- Forced switches (Roar, Whirlwind, Dragon Tail)
- U-turn, Volt Switch, Flip Turn
- Baton Pass
- Teleport
- Emergency Exit/Wimp Out activation

**Does NOT trigger on:**
- Fainting
- End of battle

### AI Behavior
Special AI logic in `battle_ai_switch_items.c`:
- Function `ShouldSwitchIfNaturalCure()` evaluates switching
- AI more likely to switch if:
  - Pokemon is asleep
  - Has Natural Cure or related abilities
  - Random chance favors switching

### Related Abilities
Natural Cure is a component of:
1. **Self Repair**: Self Sufficient + Natural Cure
2. **Natural Recovery**: Natural Cure + Regenerator

These combination abilities provide both status healing and HP recovery.

### Pokemon with Natural Cure
Common users include:
- Oddish line (innate ability)
- Staryu/Starmie
- Chansey/Blissey
- Roselia/Roserade
- Swablu/Altaria
- Various other Pokemon in Elite Redux

### Strategic Applications

**Offensive pivot:**
- Absorb status moves
- U-turn/Volt Switch out to cure
- Maintain offensive pressure

**Defensive sponge:**
- Switch into predicted status moves
- Cure status while bringing in counter
- Preserve defensive utility

**Status absorber:**
- Dedicated team member for status moves
- Prevents status from crippling key Pokemon
- Forces opponent to reconsider status moves

### Synergies
- **U-turn/Volt Switch**: Cure status while maintaining momentum
- **Regenerator**: Heal HP and status in one switch
- **Wish/Healing Wish**: Support teammates after curing self
- **Sleep Talk**: Use if put to sleep, cure when switching

### Advantages
- No item slot required (vs Lum Berry)
- Unlimited uses (vs one-time berries)
- Works on all status types
- Can't be Knocked Off or stolen
- Psychological deterrent to status moves

### Limitations
- Requires switching (loses momentum)
- No effect while staying in
- Can't cure teammates
- Vulnerable to Pursuit/trapping
- No protection from status initially

### Counters
- Trapping abilities (Arena Trap, Shadow Tag)
- Trapping moves (Mean Look, Block)
- Pursuit (punishes switches)
- Direct damage (ignore status entirely)
- Entry hazards (punish repeated switches)

### Competitive Usage Notes
Natural Cure excels on Pokemon that naturally switch frequently. It's particularly valuable on defensive pivots that can absorb status for the team. The ability creates favorable risk-reward scenarios where opponents must decide whether inflicting status is worth giving a free cure. Best utilized on Pokemon with good defensive stats and access to pivoting moves.

### Team Building Considerations
- Pairs well with offensive teams needing status absorption
- Enables aggressive plays knowing status can be cured
- Reduces need for cleric support
- Allows more flexible item choices

### Version History
Natural Cure has remained mechanically identical since its introduction in Generation 3. The ability's simplicity and effectiveness have made it a staple defensive ability throughout all generations.