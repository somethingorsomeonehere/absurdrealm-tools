---
id: 86
name: Simple
status: reviewed
character_count: 69
---

# Simple - Ability ID 86

## In-Game Description
"Doubles all stat changes on this Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles all stat stage changes on user, whether positive or negative. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**SIMPLE** is a stat-modifying ability that doubles the magnitude of all stat stage changes applied to the Pokemon.

### Activation Mechanics:
- **Trigger**: Automatically applies whenever the Pokemon receives a stat stage change
- **Timing**: Applied after Contrary reversal but before protection checks
- **Code Location**: `battle_script_commands.c` line 9625: `if (BattlerHasAbility(battler, ABILITY_SIMPLE, FALSE)) statValue *= 2;`

### Stat Change Doubling:
1. **Positive Boosts**:
   - Swords Dance: +4 Attack instead of +2
   - Calm Mind: +2 SpA/SpD instead of +1 each
   - Dragon Dance: +2 Attack/Speed instead of +1 each
   - Shell Smash: +4 Attack/SpA/Speed, -2 Defense/SpD instead of +2/-1

2. **Negative Drops**:
   - Intimidate: -2 Attack instead of -1
   - Sticky Web: -2 Speed instead of -1
   - All stat-dropping moves doubled in effect

3. **Special Interactions**:
   - **Order of Operations**: Contrary to Simple to Protection checks
   - **Move Effects**: All stat-changing move effects are doubled
   - **Self-Inflicted**: Applies to both beneficial and detrimental self-stat changes

### Stored Power Synergy:
- **Normal**: 20 + (stat increases x 20) base power
- **With Simple**: Each +1 boost = +2 stages for Simple user
- **Practical Example**: 
  - Calm Mind once = +2 SpA/SpD stages to Stored Power = 100 base power
  - Two Calm Minds = +4 SpA/SpD stages to Stored Power = 180 base power
  - **Mathematical Advantage**: Reaches maximum power much faster

### Setup Sweeping Potential:
1. **Speed of Setup**:
   - One setup move = equivalent of two for normal Pokemon
   - Reaches +6 stats in 3 moves instead of 6
   - Critical for time-limited battles

2. **Power Scaling**:
   - Stored Power caps at theoretical 860 base power with maxed stats
   - Simple reaches 540 base power in just 3 Calm Minds
   - Shell Smash once = +4/+4/+4/-2/-2 stat changes

### Interaction Rules:
- **vs Contrary**: Applied AFTER Contrary reversal
- **vs Clear Body**: Clear Body prevents the stat drop entirely, so Simple never applies
- **vs Unaware**: Unaware ignores stat stages, making Simple's boosts ineffective offensively/defensively
- **vs Simple Beam**: Can overwrite Simple ability, removing the doubling effect
- **vs Mist**: Mist prevents stat drops, so Simple's doubled negative effects are blocked

### Competitive Applications:
1. **Stored Power Sweepers**:
   - Cosmic Power + Stored Power sets become extremely potent
   - Reaches sweeping power much faster than normal
   - Psychic-types with access to both moves become setup threats

2. **Mixed Setup**:
   - Shell Smash users become incredibly dangerous
   - One Shell Smash = +4/+4/+4 offenses with manageable -2/-2 defense drops
   - Risk/reward calculation heavily favors Simple users

3. **Defensive Considerations**:
   - Vulnerability to stat drops is doubled
   - Intimidate becomes -2 Attack drop
   - Must be more careful around stat-dropping moves and abilities

### Technical Implementation:
```c
s8 ChangeStatBuffs(u8 battler, s8 statValue, u32 statId, u32 flags, const u8* BS_ptr) {
    // Handle Contrary first
    if (BATTLER_HAS_ABILITY(battler, ABILITY_CONTRARY)) {
        statValue *= -1;
    }
    
    // Simple doubles the stat change
    if (BattlerHasAbility(battler, ABILITY_SIMPLE, FALSE)) statValue *= 2;
    
    // Continue with protection checks and actual stat changes...
}
```

### Edge Cases and Limitations:
1. **Protection Bypass**: Simple calculates before protection checks, but won't apply if the stat change is ultimately blocked
2. **Cap Interactions**: Still limited by ±6 stat stage caps
3. **Z-Move Boosts**: Z-move stat boosts are also doubled
4. **Baton Pass**: Doubled stat stages are passed along normally
5. **Transform/Imposter**: Copies Simple but not the current stat stages

### Version History:
- **Gen 4**: Introduction - doubled stat stage changes
- **Gen 5+**: No mechanical changes
- **Elite Redux**: Maintains standard Simple mechanics with expanded movepools for setup strategies