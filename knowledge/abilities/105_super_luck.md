---
id: 105
name: Super Luck
status: reviewed
character_count: 70
---

# Super Luck - Ability ID 105

## In-Game Description
"Raises critical-hit ratio of own moves by +1."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Adds +1 to the critical hit stage of all the Pokemon's damaging moves.

## Detailed Mechanical Explanation

Super Luck is a passive ability that enhances the critical hit ratio of all damaging moves used by the Pokemon with this ability. Here's how it works:

### Core Mechanics
- Adds +1 to the critical hit stage calculation for all damaging moves
- This bonus is applied before the move is executed
- Works with all damaging moves, regardless of type or category (physical/special)

### Critical Hit Stage System
The critical hit system in Pokemon uses stages:
- Stage 0: 1/16 chance (6.25%)
- Stage 1: 1/8 chance (12.5%)
- Stage 2: 1/2 chance (50%)
- Stage 3+: Guaranteed critical hit (100%)

With Super Luck:
- Normal moves start at Stage 1 instead of Stage 0
- High-crit moves (like Slash) go from Stage 1 to Stage 2
- Moves with +2 crit ratio go from Stage 2 to Stage 3 (guaranteed crit)

### Stacking with Other Effects
Super Luck stacks additively with:
- High critical-hit ratio moves (Slash, Leaf Blade, etc.): +1 stage
- Scope Lens/Razor Claw held items: +1 stage
- Focus Energy status: +2 stages
- Z-Move critical hit boosts
- Any other critical hit stage modifiers

### Example Combinations
1. **Super Luck + Normal Move**: 1/8 chance (12.5%)
2. **Super Luck + Slash**: 1/2 chance (50%)
3. **Super Luck + Slash + Scope Lens**: Guaranteed critical hit
4. **Super Luck + Focus Energy + Normal Move**: Guaranteed critical hit

### Implementation Details
From the code in `abilities.cc`:
```c
constexpr Ability SuperLuck = {
    .onCrit = +[](ON_CRIT) -> int { return 1; },
};
```

The implementation is straightforward - it returns 1 when calculating critical hit stages, adding exactly one stage to the critical hit calculation. This is checked during damage calculation for all damaging moves.

### Strategic Implications
- Excellent on Pokemon with access to high-crit moves
- Pairs well with Scope Lens for reliable critical hits
- Benefits from critical hit damage being 1.5x in modern generations
- Particularly effective on Pokemon with high Attack/Special Attack stats
- Can bypass defensive stat boosts since critical hits ignore them

### Notable Users
Super Luck is particularly effective on Pokemon that can learn multiple high-critical-hit-ratio moves, allowing them to achieve guaranteed critical hits with proper setup.