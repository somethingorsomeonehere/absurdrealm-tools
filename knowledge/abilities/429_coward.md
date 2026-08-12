---
id: 429
name: Coward
status: reviewed
character_count: 71
---

# Coward - Ability ID 429

## In-Game Description
"Sets up Protect on switch-in. Only works once."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Coward automatically activates Protect on entry. Works once per battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Coward is a single-use defensive ability that automatically activates Protect when the Pokemon switches into battle. This provides complete protection for one turn, but the effect can only be used once per battle entry.

### Activation Conditions
- **Trigger**: Automatically activates when the Pokemon switches into battle
- **Single-use**: Only works once per battle entry (tracked by single-use counter)
- **Persistent**: The ability remains active throughout the battle for tracking purposes
- **Timing**: Activates during switch-in, before any other actions

### Protection Effects
- **Complete immunity**: Blocks all direct attacks, status moves, and damage
- **Status immunity**: Prevents all status conditions during the protected turn
- **Multi-hit protection**: Blocks all hits from multi-hit moves
- **Indirect damage**: Does not protect against entry hazards, weather, or residual damage

### Technical Implementation
```c
// Coward ability implementation
constexpr Ability Coward = {
    .onEntry = +[](ON_ENTRY) -> int {
        // Check if ability has already been used
        CHECK_NOT(GetSingleUseAbilityCounter(battler, ability))
        
        // Mark ability as used for this battle entry
        SetSingleUseAbilityCounter(battler, ability, TRUE);
        
        // Activate protection for this turn
        gRoundStructs[battler].protectedThisTurn = TRUE;
        
        // Trigger protection message
        BattleScriptPushCursorAndCallback(BattleScript_BattlerIsProtectedForThisTurn);
        return TRUE;
    },
    .persistent = TRUE,  // Keep tracking throughout battle
};
```

### Single-Use Counter System
- **GetSingleUseAbilityCounter**: Checks if the ability has been used this battle entry
- **SetSingleUseAbilityCounter**: Marks the ability as used (TRUE = used, FALSE = available)
- **Battle entry**: Counter resets when Pokemon is withdrawn and sent back out
- **Persistent flag**: Ensures the ability remains active for counter tracking

### Important Interactions
- **Entry hazards**: Coward activates after entry hazard damage is taken
- **Weather damage**: Protection doesn't affect weather damage during the turn
- **Priority moves**: Blocked by Coward's protection like normal Protect
- **Multi-turn moves**: Protects for the full duration if opponent is locked in
- **Switching**: Withdrawing and re-entering resets the single-use counter

### Strategic Applications
- **Frail sweepers**: Guarantees safe setup turn for Glass Cannon Pokemon
- **Pivot protection**: Safe switching option for momentum control
- **Scout opponent**: Forces opponent to reveal their intended move
- **Stall breaking**: Wastes opponent's turn while setting up your strategy
- **Revenge killing**: Protects against revenge attempts on switch-in

### Limitations
- **One-time use**: Cannot be used again until Pokemon is withdrawn and re-entered
- **Residual damage**: Entry hazards, weather, and status still affect the Pokemon
- **Prediction dependent**: Opponent may switch or use setup moves
- **Passive ability**: No offensive benefit, purely defensive
- **Timing specific**: Only works on switch-in, not mid-battle

### Synergies
- **Glass Cannon builds**: Paired with high-damage, low-defense Pokemon
- **Setup moves**: Guarantees one free turn of setup (Swords Dance, Calm Mind, etc.)
- **Choice items**: Allows safe switching with Choice-locked Pokemon
- **Momentum control**: Enables safe pivoting in competitive play
- **Revenge prevention**: Protects against common revenge killing attempts

### Counters
- **Multi-turn commitment**: Opponent can use setup moves or switch
- **Residual damage**: Entry hazards chip away at health despite protection
- **Prediction**: Experienced players may anticipate and adapt their strategy
- **Passive play**: Doesn't contribute to offensive pressure
- **One-time limitation**: Becomes predictable after first use

### Competitive Usage Notes
- **High-level play**: Extremely valuable for guaranteeing setup opportunities
- **Team building**: Excellent on hyper-offensive teams needing safe setup
- **Momentum shifts**: Can dramatically alter battle flow when used correctly
- **Prediction meta**: Changes how opponents approach the battle
- **Risk/reward**: High reward but limited usage requires careful timing

### Common Users
- **Fragile sweepers**: Pokemon with high attack but low defenses
- **Setup sweepers**: Pokemon that need one turn to become threatening
- **Glass Cannon builds**: Maximum offensive investment with minimal bulk
- **Pivot Pokemon**: Safe switching options for team momentum
- **Revenge killers**: Protection against counter-revenge attempts

### Version History
- **Elite Redux exclusive**: Custom ability not found in official games
- **Single-use system**: Utilizes Elite Redux's ability counter mechanics
- **Persistent tracking**: Remains active throughout battle for proper function
- **Balance consideration**: One-time use prevents it from being overpowered