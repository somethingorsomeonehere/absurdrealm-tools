---
id: 858
name: Breezy Neigh
status: reviewed
character_count: 97
---

# Breezy Neigh - Ability ID 858

## In-Game Description
KOs raise Speed by one stage.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the Pokemon's Speed by one stage when it causes an opponent to faint with a direct attack.

## Detailed Mechanical Explanation

### Technical Implementation

**File**: `src/abilities.cc`
**Mechanism**: Uses the `MoxieClone` function with `STAT_SPEED` parameter
**Trigger**: `onBattlerFaints` with `APPLY_ON_ATTACKER`

```cpp
constexpr Ability BreezyNeigh = {
    .onBattlerFaints = AdrenalineRush.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};

constexpr Ability AdrenalineRush = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int { return MoxieClone(battler, STAT_SPEED); },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

## Key Mechanics

1. **Activation Condition**: Only activates when the Pokemon with Breezy Neigh directly causes a knockout
2. **Stat Boost**: Raises Speed by exactly one stage (+50% of base Speed stat)
3. **Timing**: Speed boost occurs immediately after the target faints
4. **Stacking**: Multiple knockouts result in multiple Speed boosts (up to +6 stages maximum)
5. **Battle Script**: Uses `BattleScript_RaiseStatOnFaintingTarget` for the animation and message

## Related Abilities
- **Moxie**: Raises Attack on KO (same mechanism, different stat)
- **Grim Neigh**: Raises Special Attack on KO  
- **Chilling Neigh**: Raises Attack on KO (from official games)
- **Adrenaline Rush** (ID: 454): Identical effect, shares the same implementation

## Battle Applications
- Excellent for sweeping teams after securing the first knockout
- Synergizes well with Choice Scarf or other speed-boosting items
- Particularly effective on Pokemon with good offensive stats but moderate base Speed
- Can turn slow, powerful attackers into late-game threats