---
id: 710
name: Dream Whimsy
status: reviewed
character_count: 193
---

# Dream Whimsy - Ability ID 710

## In-Game Description
"Uses Yawn on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Yawn on switch in, targeting the opposing Pokemon. Yawn causes drowsiness that makes the target fall asleep at the end of the next turn. The sleep effect can be prevented by switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Dream Whimsy is an entry-based ability that automatically executes Yawn when the Pokemon enters battle. This creates immediate pressure on the opponent by setting up a delayed sleep status.

### Activation Conditions
- **Trigger**: Activates when the Pokemon switches into battle
- **Target**: Automatically targets the opposing Pokemon (if alive)
- **Priority**: Uses the UseEntryMove function with MOVE_YAWN and 0 power
- **Move data**: Yawn is a Normal-type status move with 10 PP and 100% accuracy

### Technical Implementation
```c
constexpr Ability DreamWhimsy = {
    .onEntry = +[](ON_ENTRY) -> int { return UseEntryMove(battler, ability, MOVE_YAWN, 0); },
};
```

The UseEntryMove function:
- Finds the first alive opposing Pokemon as target
- Queues Yawn as an extra attack with the ability's power override (0)
- Uses the standard battle system to execute the move

### Yawn Move Mechanics
- **Effect**: EFFECT_YAWN (ID 187) - causes drowsiness status
- **Timing**: Target falls asleep at the end of the turn AFTER Yawn hits
- **Type**: Normal-type status move
- **Accuracy**: 100% (cannot miss under normal circumstances)
- **PP**: 10 (irrelevant for ability use)
- **Flags**: Affected by Protect, Magic Coat, Mirror Move

### Important Interactions
- **Sleep immunity**: Pokemon with abilities like Insomnia, Vital Spirit are immune
- **Type immunity**: Does not affect Grass-types (if they have immunity)
- **Protect effects**: Can be blocked by Protect, Detect, King's Shield, etc.
- **Magic Coat**: Can be reflected back to the user
- **Substitute**: Blocked by Substitute
- **Switching**: Target can switch out to avoid falling asleep
- **Sleep Talk**: Sleeping Pokemon can still use Sleep Talk

### Sleep Status Details
- **Duration**: 1-3 turns when asleep (standard sleep mechanics)
- **Wake-up chance**: 33% each turn after the first
- **Sleep Talk**: Can use Sleep Talk while asleep
- **Dream Eater**: Makes target vulnerable to Dream Eater attacks

### Strategic Implications
- **Entry pressure**: Forces immediate decision-making from opponent
- **Switch forcing**: Opponent may switch to avoid sleep
- **Tempo control**: Gains momentum by potentially removing threat for 2-4 turns
- **Pivot synergy**: Excellent on pivoting Pokemon (U-turn, Volt Switch users)
- **Support role**: Sets up for teammates to capitalize on sleeping foes

### Counters and Limitations
- **Sleep immunity**: Hard countered by Insomnia, Vital Spirit, Comatose
- **Protection moves**: Protect, Detect completely block the effect
- **Magic Coat**: Reflects Yawn back to user
- **Substitute**: Blocks Yawn entirely
- **Switching**: Opponent can switch out before sleep occurs
- **Faster threats**: Fast opponents can attack before sleep takes effect
- **One-time use**: Only activates on switch-in, not mid-battle

### Synergies
- **U-turn/Volt Switch**: Allows repeated entry activations
- **Pivot moves**: Creates switching loops for repeated Yawn pressure
- **Dream Eater users**: Teammates can exploit sleeping targets
- **Nightmare**: Can set up Nightmare on sleeping foes
- **Setup moves**: Team can use sleep turns for Swords Dance, etc.
- **Hazard setters**: Sleep provides free turns for Stealth Rock, Spikes

### Competitive Usage Notes
- **Entry hazard support**: Pairs well with hazard setters
- **Pivot team core**: Essential for pivoting strategies
- **Anti-setup**: Prevents opponent setup by forcing sleep
- **Tempo advantage**: Gains 1-2 free turns minimum
- **Mind games**: Creates psychological pressure on opponent switches

### Double Battle Considerations
- **Single target**: Only affects one opponent in doubles
- **Positioning**: May target less threatening opponent
- **Partner synergy**: Teammate can capitalize on sleeping foe
- **Spread moves**: Partner can hit sleeping target with spread moves

### Common Users
- Pokemon designed for support and disruption roles
- Pivoting Pokemon with U-turn or Volt Switch
- Bulky Pokemon that can afford to use a turn for status
- Lead Pokemon designed to set early game tempo

### Version History
- New ability in Elite Redux
- Uses standard Yawn mechanics with entry trigger
- Part of the expanded ability roster for strategic diversity

### Ability ID and Classification
- **ID**: 710
- **Category**: Entry-based status ability  
- **Rarity**: Rare (specialized disruption ability)
- **Power Level**: Medium-High (strong utility effect)