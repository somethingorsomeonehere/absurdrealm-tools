---
id: 194
name: Emergency Exit
status: reviewed
character_count: 167
---

# Emergency Exit - Ability ID 194

## In-Game Description
"At 1/2 of max HP or below, instantly switches out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the Pokemon receives damage and its HP drops to 50% or below for the first time in battle, it switches out to safety. Activates on the last hit of multihit moves.

## Detailed Mechanical Explanation

### Implementation Details
Emergency Exit is implemented identically to Wimp Out - they share the same `onDefender` function that:

1. **Trigger Check**: `CheckHalfHpAbility(battler, attacker)` verifies:
   - Pokemon was above 50% HP before the attack
   - Pokemon is now at or below 50% HP after the attack
   - Not during multi-hit moves (only triggers on final hit)

2. **Battle Context Checks**:
   - Must be a trainer battle (`BATTLE_TYPE_TRAINER`)
   - Cannot be Arena battle format
   - Must have usable party members available
   - Must be able to switch (not trapped)

3. **Activation**: Sets `RESOURCE_FLAG_EMERGENCY_EXIT` flag for processing during move end phase

### Activation Conditions
- **HP Threshold**: Exactly 50% max HP or below
- **Damage Source**: Must be from an opponent's attack
- **Battle Type**: Trainer battles only (not wild battles)
- **Party Status**: Must have switchable Pokemon available
- **Timing**: Only on the final hit of multi-hit moves
- **Status**: Cannot be prevented by trapping moves/abilities

### Priority and Interactions
- **When**: After damage calculation, during move end effects
- **Priority**: Processed in `MOVEEND_EMERGENCY_EXIT` phase
- **Sheer Force**: Blocked by Sheer Force on the attacking move
- **Multi-hit**: Only triggers after the final hit connects
- **Trapping**: Blocked by abilities like Arena Trap or moves like Mean Look

### Strategic Applications

**Defensive Utility**:
- **Damage Pivot**: Safely exit after taking significant damage
- **Status Avoidance**: Escape before secondary effects apply
- **Momentum Control**: Force switches at crucial moments
- **Team Preview**: Reveals when opponent reaches damage thresholds

**Offensive Applications**:
- **Hit-and-Run**: Attack then automatically switch out
- **Surprise Factor**: Unexpected switches can disrupt opponent's strategy
- **Entry Hazard Setup**: Switch to hazard setters after triggering

**Synergistic Combinations**:
- **Regenerator**: Heal while switched out
- **U-turn/Volt Switch**: Manual switching before the threshold
- **Focus Sash**: Survive to exactly 1 HP and trigger
- **Healing Items**: Sitrus Berry can interfere with timing

### Pokemon Distribution
Found on several Pokemon as both regular and innate abilities:
- Speed-oriented Pokemon (Deoxys forms)
- Defensive support Pokemon (Audino variants)
- Mixed offensive/defensive roles

### Battle Scenarios

**Scenario 1: Damage Threshold**
- Pokemon at 60% HP takes 25% damage to Triggers (now at 35%)
- Pokemon at 45% HP takes damage to Does not trigger (already below threshold)

**Scenario 2: Multi-hit Moves**
- Double Kick: First hit brings to 45%, second hit to 20% to Triggers after second hit
- Triple Kick: Only checks after final hit regardless of intermediate HP

**Scenario 3: Battle Format**
- Trainer Battle: Functions normally
- Wild Battle: Does not activate
- Arena Battle: Blocked entirely

### Counterplay Strategies
- **Trapping**: Use Arena Trap, Shadow Tag, or Mean Look
- **Sheer Force**: Abilities that add Sheer Force prevent activation
- **Exact Damage**: Calculate to avoid triggering the threshold
- **Status Effects**: Apply before reaching 50% HP threshold
- **Multi-hit Moves**: Only the final hit matters for activation

## Mechanical Differences from Similar Abilities
- **Wimp Out**: Identical functionality (same code implementation)
- **Eject Button**: Item-based, single use, any damage threshold
- **Red Card**: Triggered when hit by contact moves specifically
- **Teleport**: Manual switching move, not automatic

## Coding Notes
- Uses shared `CheckHalfHpAbility` function with other half-HP triggered abilities
- Flag-based delayed activation system prevents mid-battle conflicts
- Battle script handles both trainer and wild battle contexts separately
- No ability state tracking needed (stateless activation)