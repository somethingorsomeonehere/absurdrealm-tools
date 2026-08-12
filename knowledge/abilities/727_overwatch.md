---
id: 727
name: Overwatch
status: reviewed
character_count: 257
---

# Overwatch - Ability ID 727

## In-Game Description
"On the Prowl + Stakeout."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All moves with priority 0 or higher gain +1 priority on the user's first turn. Negative priority moves become priority 0 instead of adding +1 priority. Deals double damage to opponents that just switched in. Only works right after they switch in for 1 turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Overwatch is a combination ability that merges the effects of On the Prowl and Stakeout into a single powerful ability. It provides both priority manipulation and switch-in punishment, making it excellent for maintaining offensive pressure.

### Component Abilities

#### On the Prowl Component
- **Priority boost**: All moves gain +1 priority on the first turn after switching in
- **Negative priority adjustment**: Moves with negative priority (like -1, -2, etc.) are set to +0 instead
- **Duration**: Only active on the very first turn after entering battle (`gVolatileStructs[battler].onTheProwl = TRUE`)
- **Turn tracking**: Uses the `onTheProwl` volatile status that gets cleared at end of turn

#### Stakeout Component  
- **Switch-in punishment**: Deals double damage (2.0x multiplier) to opponents that just switched in
- **Detection mechanism**: Triggers when `gVolatileStructs[target].isFirstTurn == 2`
- **Timing**: Works for two turns after opponent switches in (counter decrements each turn)
- **Always active**: No turn limitations like On the Prowl

### Technical Implementation
```c
// Overwatch combines both abilities
constexpr Ability Overwatch = {
    .onEntry = OnTheProwl.onEntry,           // Sets onTheProwl flag
    .onOffensiveMultiplier = Stakeout.onOffensiveMultiplier,  // 2x damage vs switch-ins
};

// Priority calculation (from battle_main.c)
if (gVolatileStructs[battlerId].onTheProwl) {
    if (gBattleMoves[move].priority >= 0)
        priority++;                          // +1 to non-negative priority
    else
        priority -= gBattleMoves[move].priority;  // Negative becomes +0
}

// Switch-in damage multiplier
if (gVolatileStructs[target].isFirstTurn == 2) MUL(2.0);
```

### Switch-in Tracking System
The `isFirstTurn` counter works as follows:
- **Value 2**: Just switched in this turn - Stakeout applies
- **Value 1**: Second turn after switch-in - Stakeout applies  
- **Value 0**: Third turn onward - Stakeout no longer applies
- **Decrement**: Reduces by 1 each turn in `RunTurnActionsFunctions()`

### Priority Mechanics Deep Dive
- **Normal moves** (priority 0): Become priority +1 on first turn
- **Quick Attack** (priority +1): Becomes priority +2 on first turn
- **Extremespeed** (priority +2): Becomes priority +3 on first turn
- **Circle Throw** (priority -6): Becomes priority +0 on first turn
- **Counter/Mirror Coat** (priority -5): Become priority +0 on first turn

### Activation Conditions
**On the Prowl effects:**
- Must be the first turn after switching in
- Applies to any move used that turn
- Clears at end of turn regardless of whether a move was used

**Stakeout effects:**
- Target must have switched in within the last 2 turns
- Applies to any offensive move
- No restrictions on move type or category

### Important Interactions
- **Entry hazards**: Stakeout damage applies even if opponent takes Stealth Rock damage
- **U-turn/Volt Switch**: Can trigger both effects - priority on your move, then Stakeout if they switch
- **Pursuit**: Gets priority boost and potentially Stakeout multiplier
- **Choice items**: Priority boost applies even when locked into a move
- **Trick Room**: Priority inversion still applies after the +1 boost

### Strategic Applications
**Lead Position:**
- Excellent as a lead Pokemon to pressure opponent's lead
- Priority ensures first move even against faster opponents
- Punishes immediate switches with double damage

**Pivot Punishment:**
- Deters opponent from making frequent switches
- Forces opponents to stay in against threats
- Creates lose-lose scenarios for opponent

**Late Game Cleaning:**
- Priority moves help clean up weakened teams
- Switch punishment prevents easy escapes
- Maintains pressure throughout battle

### Synergies
- **Choice Band/Specs**: Massive damage on switch-in punishment
- **Life Orb**: Stacks with the damage multiplier for huge damage
- **U-turn/Volt Switch**: Create switching scenarios to exploit
- **Pursuit**: Trap switching opponents for guaranteed Stakeout damage
- **Entry hazards**: Force more switches to trigger Stakeout
- **Fake Out**: Gets priority boost and can force switches

### Counters and Limitations
**On the Prowl Limitations:**
- Only works for one turn after switching
- Doesn't help with subsequent turns
- Vulnerable to Trick Room reversal
- Priority moves still lose to higher priority

**Stakeout Limitations:**
- Only affects switch-ins, not initial leads
- No boost against Pokemon that stay in
- Can be played around with bulky switch-ins
- Entry hazards may KO before Stakeout triggers

**General Counters:**
- **Prankster**: Still gets higher priority on status moves
- **Trick Room**: Reverses priority advantage
- **Bulky switch-ins**: Can tank the doubled damage
- **Protect**: Wastes the priority turn
- **Switch prediction**: Opponent can predict and stay in

### Competitive Usage
**Tier Assessment:** High-tier combination ability
- Excellent for offensive builds
- Strong in both lead and mid-game positions  
- Versatile across multiple battle formats
- High skill ceiling for optimal use

**Common Users:**
- Fast offensive Pokemon that want guaranteed first moves
- Pokemon with strong priority moves (Aqua Jet, Bullet Punch, etc.)
- Choice item users that want switch punishment
- Pokemon with good prediction moves like U-turn

**Team Roles:**
- **Lead**: Pressure opponent immediately
- **Wallbreaker**: Punish defensive switches
- **Cleaner**: Priority helps sweep weakened teams
- **Pivot**: Create advantageous switch scenarios

### Version History
- Custom Elite Redux ability combining two existing effects
- Part of the expanded ability system
- Demonstrates the power of combination abilities
- Shows how timing-based mechanics can synergize

### Meta Impact
Overwatch creates a unique threat profile that forces opponents to carefully consider their switching patterns. The combination of priority and switch punishment makes it one of the most immediately threatening abilities for offensive teams, while the limited duration of priority prevents it from being overpowered in longer battles.