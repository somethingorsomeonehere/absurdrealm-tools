---
id: 288
name: Perfectionist
status: reviewed
character_count: 126
---

# Perfectionist - Ability ID 288

## In-Game Description
"Move BP < 51 BP: +1 to crit rate. Move BP < 26 BP: +1 priority too."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Attacks with 50 BP or less raise their critical hit ratio by one stage, and attacks with 25 BP or lower also gain +1 priority.

## Detailed Mechanical Explanation
*For Discord/reference use*

**PERFECTIONIST** is a specialized ability that enhances weak moves with critical hit boosts and priority, creating unique offensive opportunities.

### Effect Mechanics:
1. **Critical Hit Boost**:
   - Condition: Move base power <= 50
   - Effect: +1 critical hit stage
   - Affected moves: 139 total moves
   - Stacks with other crit modifiers

2. **Priority Boost**:
   - Condition: Move base power <= 25
   - Effect: +1 priority
   - Affected moves: 63 total moves
   - Both effects apply to <=25 BP moves

### Technical Implementation:
```cpp
constexpr Ability Perfectionist = {
    .onPriority = +[](ON_PRIORITY) -> int {
        CHECK(gBattleMoves[move].power <= 25)
        CHECK(gBattleMoves[move].power);
        return 1;
    },
    .onCrit = +[](ON_CRIT) -> int {
        CHECK(gBattleMoves[move].power <= 50)
        CHECK(gBattleMoves[move].power)
        return 1;
    },
};
```

### Key Details:
- CHECK ensures move has power (excludes 0 BP status moves)
- Both lambdas can trigger on same move
- Returns +1 to increase stage by 1

### Notable Move Interactions:

**Priority + Crit (<=25 BP)**:
- Fury Swipes (20 BP, 2-5 hits)
- Triple Kick (20 BP, 3 hits guaranteed)
- Fury Cutter (20 BP, doubles each hit)
- Bullet Seed (25 BP, 2-5 hits)
- Nuzzle (20 BP, 100% paralysis)
- Dragon Breath (20 BP, 30% paralysis)

**Crit Only (26-50 BP)**:
- Bite (30 BP, 30% flinch)
- Quick Attack (40 BP, already priority)
- Aqua Jet (40 BP, already priority)
- Mach Punch (40 BP, already priority)
- Power-Up Punch (40 BP, +1 Attack)

### Pokemon with Perfectionist:

**As Changeable Ability**:
- Persian (Normal)
- Scyther (Bug/Flying)
- Minccino (Normal)
- Cinccino (Normal)

**As Innate Ability**:
- Meowth (Normal)
- Rattata forms (Normal)
- Raticate forms (Normal)
- Parasect (Bug/Grass)
- Kricketot (Bug)
- Kricketune (Bug)
- Kabutops (Rock/Water - tertiary)
- Greninja (Water/Dark)

### Competitive Applications:

1. **Multi-Hit Abuse**:
   - Each hit can crit independently
   - Priority on all hits
   - Breaks Focus Sash/Sturdy
   - Penetrates Substitute

2. **Revenge Killing**:
   - Priority physical coverage
   - Outspeeds Scarfers with priority
   - Punishes weakened opponents
   - Cleans late-game

3. **Status + Priority**:
   - Nuzzle: Priority paralysis
   - Dragon Breath: Priority with para chance
   - Bite: Priority with flinch chance

### Synergistic Elements:

**Abilities**:
- Technician: 1.5x on <=60 BP moves
- Skill Link: Max hits on multi-hit
- Sniper: 2.25x crit damage
- Super Luck: Higher crit chance

**Items**:
- Scope Lens: +1 crit stage
- Razor Claw: +1 crit stage
- Life Orb: 1.3x damage
- King's Rock: Flinch on multi-hits

**Moves**:
- Focus Energy: +2 crit stages
- Tailwind: Speed support
- Sticky Web: Speed control

### Sample Sets:

**Cinccino @ Life Orb**
- Tail Slap (25 BP x 5)
- Bullet Seed (25 BP x 5)
- Rock Blast (25 BP x 5)
- U-turn

**Persian @ Scope Lens**
- Fury Swipes (20 BP x 5)
- Bite (30 BP)
- U-turn
- Taunt

### Strategic Considerations:
- Low base power limits total damage
- Priority blocked by Armor Tail/Queenly Majesty
- Requires specific movepool
- Best vs weakened teams
- Struggles vs bulky Pokemon

### Damage Calculations:
With Technician + Life Orb:
- 20 BP move: 20 x 1.5 x 1.3 = 39 BP with priority
- 25 BP move: 25 x 1.5 x 1.3 = 48.75 BP with priority
- Multi-hit: Potentially 195-244 BP total

### Version Notes:
- Elite Redux exclusive ability
- Unique BP thresholds (25/50)
- Designed for weak move optimization