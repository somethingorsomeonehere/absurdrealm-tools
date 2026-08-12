---
id: 461
name: Monkey Business
status: reviewed
character_count: 145
---

# Monkey Business - Ability ID 461

## In-Game Description
"Uses Tickle on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Monkey Business automatically uses Tickle upon switching into battle, lowering the opposing Pokemon's Attack and Defense stats by one stage each. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Monkey Business is an entry ability that automatically uses the move Tickle when the Pokemon switches into battle. This provides immediate battlefield control by weakening the opponent's physical capabilities.

### Activation Conditions
- **Trigger**: Activates immediately when the Pokemon switches into battle
- **Target**: Automatically targets the opposing Pokemon
- **Bypass**: Cannot be blocked by Substitute
- **Accuracy**: Uses Tickle's 100% accuracy, so it cannot miss

### Move Details - Tickle
- **Type**: Normal-type status move
- **Effect**: Lowers opponent's Attack and Defense by 1 stage each
- **Accuracy**: 100% (cannot miss)
- **PP**: 20 (though irrelevant for ability usage)
- **Protection**: Can be blocked by Protect, Detect, and similar moves
- **Redirection**: Affected by move redirection abilities like Lightning Rod

### Technical Implementation
```c
constexpr Ability MonkeyBusiness = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_TICKLE, 0); 
    },
};
```

The ability uses the `UseEntryMove` function which:
- Executes the move immediately upon entry
- Uses the standard move mechanics and interactions
- Triggers appropriate battle messages and animations
- Respects move immunities and protections

### Important Interactions
- **Substitute**: Tickle bypasses Substitute and directly affects the opponent
- **Protect/Detect**: Entry move can be blocked by protection moves if opponent used them
- **Magic Coat**: Tickle can be reflected back to the user
- **Contrary**: If opponent has Contrary, the stat changes become boosts instead
- **Clear Body/White Smoke**: These abilities prevent the stat reductions
- **Mold Breaker variants**: Do not affect this ability as it's not a stat-changing ability itself

### Stat Stage Changes
- **Attack**: Reduced by 1 stage (-33% physical damage)
- **Defense**: Reduced by 1 stage (-33% physical defense)
- **Stacking**: Can stack with other stat reductions
- **Maximum**: Cannot reduce stats below -6 stages

### Strategic Implications
- **Lead disruption**: Excellent on lead Pokemon to immediately weaken physical threats
- **Pivot utility**: Great for defensive pivots that want to debuff while switching
- **Setup disruption**: Interrupts physical setup sweepers immediately
- **Doubles synergy**: Can debuff both opponents in doubles format
- **Anti-physical**: Specifically counters physical attackers and contact moves

### Synergies
- **Intimidate**: Stacks with Intimidate for -2 Attack total
- **Defensive pivots**: Pairs well with U-turn, Volt Switch, or Teleport users
- **Support movesets**: Complements other debuffing moves like Will-O-Wisp
- **Bulky attackers**: Good on Pokemon that can tank hits after debuffing
- **Prankster**: If paired with Prankster, follow-up status moves gain priority

### Counters and Limitations
- **Magic Coat**: Reflects Tickle back to the user
- **Protect/Detect**: Can block the entry move if predicted
- **Taunt**: Doesn't affect the entry move, but limits follow-up status moves
- **Clear Body/White Smoke**: Prevents stat reductions entirely
- **Contrary**: Turns debuffs into buffs for the opponent
- **Special attackers**: Less effective against special-based teams

### Common Users
This ability would typically be found on:
- Primate Pokemon (thematic fit)
- Support-oriented Pokemon
- Defensive pivots
- Anti-physical specialists
- Pokemon with naturally high bulk to survive after debuffing

### Competitive Usage Notes
- **Entry hazard synergy**: Combines well with Stealth Rock damage
- **Momentum control**: Provides immediate battlefield presence
- **Team support**: Benefits the entire team by weakening physical threats
- **Prediction reward**: Switching in on predicted physical moves maximizes value
- **Multi-battle utility**: Useful in both singles and doubles formats

### Version History
- Custom ability in Elite Redux
- Uses standard Tickle move mechanics
- Part of the expanded ability roster for enhanced gameplay variety

### Similar Abilities
- **Intimidate**: Also lowers Attack on entry, but doesn't affect Defense
- **Moxie**: Opposite effect (boosts stats instead of lowering)
- **Download**: Analyzes and potentially boosts stats instead of lowering opponent's