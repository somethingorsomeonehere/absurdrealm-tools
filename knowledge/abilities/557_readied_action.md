---
id: 557
name: Readied Action
status: reviewed
character_count: 123
---

# Readied Action - Ability ID 557

## In-Game Description
"Doubles attack on first turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the user's Attack stat by 2x for one turn. Multiplicative with other damage boosts. Reapplies after switching in.


## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Activation**: Triggers automatically upon switch-in
- **Effect**: Doubles the Pokemon's Attack stat (multiplies by 2.0x) for the first turn only
- **Duration**: One turn after switch-in, then the effect disappears
- **Stat Affected**: Physical Attack stat only (not Special Attack)

### Technical Implementation
The ability works by setting two flags in the battle engine:
```c
gVolatileStructs[battler].readiedAction = TRUE;
gVolatileStructs[battler].started.readiedAction = TRUE;
```

The attack doubling occurs in the stat calculation:
```c
// In battle_util.c line 7016
if (gVolatileStructs[battler].readiedAction) statBase *= 2;
```

The flag is cleared after one turn unless it was set during switch-in:
```c
CLEAR_ONE_TURN(readiedAction)
```

### Affected Moves
- **All physical moves** (Attack stat-based moves)
- **Does NOT affect** Special Attack-based moves
- **Does NOT affect** status moves

### Interactions with Other Mechanics
- **Stacks multiplicatively** with other Attack boosts (stat stages, items, etc.)
- **Works with** Choice Band, Life Orb, and other damage-boosting items
- **Compatible with** other abilities that boost Attack (though the Pokemon can only have one main ability)
- **Burn status** still halves Attack after the Readied Action boost is applied
- **Intimidate** and other Attack-lowering effects apply after the doubling

### Strategic Implications
- **Immediate threat**: Forces opponents to respect first-turn damage potential
- **Switch-in pressure**: Makes the Pokemon dangerous immediately upon entry
- **One-time use**: Must be used wisely as the effect only lasts one turn
- **Prediction reward**: Benefits from correctly predicting opponent's moves/switches

### Example Damage Calculations
Assuming a Pokemon with 100 base Attack using a 100 BP physical move:
- **Normal**: ~200 damage (approximate)
- **With Readied Action**: ~400 damage (approximate)
- **With Readied Action + Choice Band**: ~600 damage (approximate)

### Common Users
Based on the ability implementation, this would typically be found on:
- Physical attackers that benefit from immediate pressure
- Pokemon with good switch-in opportunities
- Wallbreakers that need the extra power to break through defensive cores

### Competitive Usage Notes
- **Lead potential**: Strong on leads for immediate pressure
- **Revenge killing**: Excellent for coming in after a teammate faints
- **Wallbreaking**: Can break through physically defensive Pokemon
- **Momentum control**: Creates immediate threats that force switches

### Counters
- **Physical walls**: High Defense Pokemon can still tank the boosted attack
- **Intimidate users**: Reduce the Attack boost (though it's still doubled from the reduced amount)
- **Priority moves**: Can bypass the need to tank the first-turn attack
- **Status moves**: Sleep, paralysis, or other status can waste the boost turn

### Synergies
- **Choice items**: Stacks with Choice Band for massive damage
- **Life Orb**: Additional damage boost for even more power
- **Type-boosting items**: Plates, expert belts, etc. for type-specific damage
- **High Attack stats**: Pokemon with naturally high Attack benefit most

### Version History
- **Elite Redux**: Custom ability implementation
- **Unique mechanic**: First-turn Attack doubling provides immediate offensive presence

### Related Abilities
- **Huge Power**: Permanent Attack doubling vs. one-turn boost
- **Pure Power**: Similar permanent Attack boost
- **Guts**: Attack boost when statused vs. first-turn boost