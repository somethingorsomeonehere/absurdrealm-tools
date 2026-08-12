---
id: 814
name: Strategic Pause
status: reviewed
character_count: 100
---

# Strategic Pause - Ability ID 814

## In-Game Description
"+2 crit rate when moving last + Analytic."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user moves after the target, boosts critical hit ratio by 2 stages and attack power by 30%.

## Detailed Mechanical Explanation
*For Discord/reference use*

Strategic Pause is a combination ability that merges the effects of Analytic with a powerful critical hit enhancement when the user moves last in battle.

### Core Mechanics

**Analytic Component:**
- Provides a 1.3x (30%) damage multiplier when the user moves after the target
- Calculated during the offensive multiplier phase of damage calculation
- Applies to all damaging moves except Future Sight

**Critical Hit Component:**
- Adds +2 to the critical hit stage when moving after the target
- This is a significant boost - normal critical hit stages are 0, 1, or 2
- Stage 2 critical hits have much higher chance than stage 0 (base) critical hits

### Activation Conditions

1. **Turn Order Requirement:** The user must move after the target in the same turn
   - Determined by comparing `GetBattlerTurnOrderNum(target) < gCurrentTurnActionNumber`
   - This means the target has already taken their action this turn

2. **Move Exclusions:** Future Sight and similar delayed moves do not trigger either effect

### Technical Implementation

```cpp
constexpr Ability StrategicPause = {
    .onOffensiveMultiplier = Analytic.onOffensiveMultiplier,
    .onCrit = +[](ON_CRIT) -> int {
        CHECK(GetBattlerTurnOrderNum(target) < gCurrentTurnActionNumber)
        CHECK(gBattleMoves[move].effect != EFFECT_FUTURE_SIGHT)
        return 2;
    },
};
```

### Critical Hit Stage Mechanics

Critical hit stages in Elite Redux work as follows:
- Stage 0 (normal): ~6.25% chance
- Stage 1: ~12.5% chance  
- Stage 2: ~25% chance
- Stage 3 (ALWAYS_CRIT): 100% chance

Strategic Pause provides Stage 2 critical hits when conditions are met, making critical hits occur roughly 1 in 4 attacks.

### Damage Calculation

When both effects activate:
1. Base damage is calculated
2. Analytic multiplier applies: `damage x 1.3`
3. Critical hit check occurs with +2 stage bonus
4. If critical hit occurs: `damage x 1.5` (or 2.25x for Super Luck users)

### Strategic Implications

**Ideal Users:**
- Slow, powerful attackers (Trick Room teams)
- Pokemon with naturally low Speed stats
- Mixed attackers who can capitalize on both physical and special critical hits

**Synergies:**
- **Trick Room:** Makes the user naturally move last
- **Super Luck:** Increases critical hit damage from 1.5x to 2.25x
- **Scope Lens/Razor Claw:** Further increases critical hit chance
- **Slow pivot moves:** U-turn/Volt Switch for guaranteed last move

**Team Building:**
- Pair with Trick Room setters
- Use on naturally slow powerhouses
- Consider Choice Scarf as anti-synergy (makes user move first)

### Common Users

Pokemon that naturally benefit from Strategic Pause:
- Slow special attackers (Slowking, Reuniclus)
- Bulky physical attackers (Conkeldurr, Machamp)
- Mixed attackers with good offensive stats

### Competitive Usage

**Advantages:**
- Massive damage output when activated (1.3x x potential 1.5x crit)
- Reliable activation in Trick Room
- Punishes faster opponents
- Works on both physical and special moves

**Counters:**
- Priority moves (bypass turn order)
- Abilities that prevent critical hits (Battle Armor, Shell Armor)
- Switching to maintain turn order advantage
- Speed control (Tailwind, Choice Scarf)

### Interactions with Other Mechanics

**Move Interactions:**
- Works with all damaging moves except Future Sight
- Applies to multi-hit moves (each hit gets both bonuses)
- Compatible with contact and non-contact moves

**Ability Interactions:**
- Stacks with other damage-boosting abilities if the Pokemon somehow has multiple
- Blocked by critical hit immunity abilities on the target
- Unaffected by Pressure or similar PP-draining abilities

**Item Interactions:**
- Scope Lens/Razor Claw: Further increases critical hit rate
- Life Orb: Stacks with Analytic boost for extreme damage
- Choice items: May prevent strategic positioning

### Version History

Strategic Pause was introduced in Elite Redux as part of the expanded ability system, designed to give slow Pokemon a powerful niche in competitive play while maintaining the risk/reward dynamic of turn order manipulation.

The ability represents a tactical approach to battle - by allowing opponents to move first, the user gains significant offensive advantages, embodying the "strategic pause" concept of calculated patience leading to devastating strikes.