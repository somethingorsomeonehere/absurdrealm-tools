---
id: 18
name: Flash Fire
status: reviewed
character_count: 190
---

# Flash Fire - Ability ID 18

## In-Game Description
"When hit by a Fire move, Fire power is boosted."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Flash Fire grants complete immunity to Fire-type moves. When hit by Fire attacks, powers up the user's Fire moves by 50% until switching out. The boost doesn't stack from multiple Fire hits.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Flash Fire provides Fire-type immunity while boosting the user's Fire-type offense. Implementation in `src/abilities.cc`:

```cpp
constexpr Ability FlashFire = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_FIRE)
        return ABSORB_RESULT_FLASH_FIRE;
    },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE && gBattleResources->flags->flags[battler] & RESOURCE_FLAG_FLASH_FIRE) 
                MUL(1.5);
        },
    .breakable = TRUE,
};
```

### Key Features

1. **Fire Absorption**:
   - Completely absorbs Fire-type moves (no damage taken)
   - Returns `ABSORB_RESULT_FLASH_FIRE` to trigger boost
   - Works on all Fire moves including status moves like Will-O-Wisp

2. **Power Boost**:
   - Fire-type moves gain 1.5x power after absorbing a Fire attack
   - Uses `RESOURCE_FLAG_FLASH_FIRE` (0x1) to track activation
   - Boost persists until the Pokemon switches out
   - Does NOT stack - multiple Fire hits don't increase the multiplier

3. **Battle Messages**:
   - First activation: "Pokemon's Fire power was raised with Flash Fire!"
   - Subsequent absorptions: "Pokemon's Flash Fire made the move ineffective!"

### Damage Calculations
With Flash Fire boost active:
- Base Fire move: 1.5x power
- Fire move with STAB: 1.5x x 1.5x = 2.25x power
- Fire move with STAB + Sun: 1.5x x 1.5x x 1.5x = 3.375x power
- Fire move with STAB + Choice Specs: 1.5x x 1.5x x 1.5x = 3.375x power

### Strategic Implications

**Defensive Value**:
- Complete Fire immunity enables safe switches
- Counters Fire-type attackers effectively  
- Blocks Will-O-Wisp and Fire status moves

**Offensive Value**:
- Turns defense into offense with 1.5x boost
- Creates mind games - opponents hesitate to use Fire moves
- Enables Fire-type sweeps after activation

**Switching Dynamics**:
- Boost resets on switch, encouraging staying in
- Opponents may try to force switches to reset boost
- Pivot moves maintain momentum while keeping boost

### AI Behavior
The AI is programmed to avoid using Fire-type moves against Flash Fire users unless:
- The partner already has Flash Fire boost activated
- No better options are available

This is implemented in `battle_ai_main.c` with specific checks for Flash Fire activation state.

### Pokemon with Flash Fire
Typically found on Fire-types and Pokemon associated with heat/volcanic environments. The ability provides both defensive utility and offensive potential.

### Interactions

1. **With Mold Breaker**:
   - Flash Fire is breakable, so Mold Breaker bypasses it
   - Fire moves will hit normally and not trigger boost

2. **With Weather**:
   - Sun further boosts Fire moves to massive damage
   - Rain reduces Fire damage but Flash Fire still absorbs

3. **With Other Abilities**:
   - **Elemental Vortex**: Combines Flash Fire + Water Absorb
   - Standard Flash Fire mechanics apply for the Fire portion

### Competitive Usage Notes
- Excellent on Fire-types for mirror matchups
- Valuable on Pokemon weak to Fire (Grass, Bug, Steel, Ice)
- Creates safe switch-ins to predicted Fire moves
- Can enable Fire-type lures with coverage moves

### Counters
- Mold Breaker ignores Flash Fire entirely
- Non-Fire offensive moves unaffected
- Forced switches reset the power boost
- Stealth Rock and other hazards

### Synergies
- Pokemon with Fire-type coverage moves
- Sun teams for maximum Fire damage
- Defensive cores needing Fire immunity
- U-turn/Volt Switch to maintain boost while pivoting

### Version History
Flash Fire has remained consistent:
- Provides Fire immunity
- Grants 1.5x Fire-type power boost
- Boost doesn't stack with multiple activations
- Elite Redux maintains standard Flash Fire mechanics