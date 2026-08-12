---
id: 818
name: Tentalock (N)
status: reviewed
character_count: 294
---

# Tentalock (N) - Ability ID 818

## In-Game Description
"Grappler + Serpent Bind."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Trapping moves last 6 turns instead of 4-5 turns and increases their damage at the end of the turn to 1/6 max HP per turn. Gives attacks a 50% chance to trap the target for 6 turns, preventing escape or switching. Once trapped, their speed drops by one stage each turn they remain on the field. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Tentalock (N) is a combination innate ability that merges the effects of two distinct trapping abilities:

### Core Mechanics

**Grappler Component:**
- Extends the duration of trapping moves (Bind, Wrap, Clamp, etc.) to exactly 6 turns
- Increases trapping damage from the standard 1/8 max HP to 1/6 max HP per turn
- Stacks with Grip Claw item: 6 turns + 7 turns = 8 total turns when combined

**Serpent Bind Component:**
- Adds a 50% chance per turn to reduce the trapped opponent's Speed by one stage
- Speed reduction occurs during the end-of-turn phase while the target is trapped
- Speed drops are cumulative and can stack up to -6 stages over multiple turns

### Technical Implementation

```c
// From battle_script_commands.c - Grappler trapping duration
if (hasGrappler && hasGripClaw)
    gVolatileStructs[gEffectBattler].wrapTurns = 8;
else if (hasGrappler)
    gVolatileStructs[gEffectBattler].wrapTurns = 6;  // Tentalock uses this

// From battle_util.c - Enhanced trapping damage
if (BATTLER_HAS_ABILITY(gBattleStruct->wrappedBy[gActiveBattler], ABILITY_GRAPPLER))
    gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 6;  // 1/6 instead of 1/8
```

### Affected Moves
All trapping moves benefit from Tentalock:
- Bind
- Wrap  
- Clamp
- Fire Spin
- Whirlpool
- Sand Tomb
- Magma Storm
- Infestation
- Thunder Cage
- Snap Trap

### Damage Calculations

**Standard Trapping:** 1/8 max HP per turn (12.5%)
**With Tentalock:** 1/6 max HP per turn (~16.67%)
**Duration:** Guaranteed 6 turns (vs. 4-5 turns normally)

**Example against 300 HP target:**
- Standard: 37-38 damage x 4-5 turns = 148-190 total damage
- Tentalock: 50 damage x 6 turns = 300 total damage
- Plus potential Speed drops: -1 to -6 stages over 6 turns

### Interactions and Synergies

**Item Synergies:**
- **Grip Claw:** Extends duration to 8 turns (6 + 7 = 8 maximum)
- **Binding Band:** Damage boost applies on top of Grappler's enhancement

**Ability Interactions:**
- **Magic Guard:** Protects targets from trapping damage but not Speed drops
- **Clear Body/Full Metal Body:** Prevents Speed stat reductions
- **Shed Shell:** Allows immediate escape, negating all effects

**Move Synergies:**
- **Thunder Wave/Glare:** Paralyze before trapping for double Speed reduction
- **Sticky Web:** Entry hazard + trapping creates severe Speed control
- **Toxic Spikes:** Poison damage stacks with trapping damage

### Strategic Applications

**Defensive Utility:**
- Guaranteed 6-turn trap duration provides consistent damage output
- Speed reduction cripples fast sweepers and setup Pokemon
- Forces switches while dealing significant residual damage

**Offensive Pressure:**
- Enhanced damage (1/6 vs 1/8) makes trapping more threatening
- Speed drops enable slower teammates to outspeed trapped foes
- Creates setup opportunities for stat-boosting moves

### Common Users

**Tentagrewl** (Water/Poison):
- Stats: 100/80/90/90/130/110
- Excellent defensive bulk with 100 HP and 130 Special Defense
- Access to Clamp, Bind, and Whirlpool for trapping options
- Water/Poison typing provides good defensive coverage
- High Speed (110) allows outspeeding before trapping

### Competitive Usage

**Tier:** Specialized utility ability
**Usage Rate:** Moderate in bulky offense and stall teams
**Effectiveness:** High against setup sweepers and frail attackers

**Strengths:**
- Guaranteed extended trapping duration removes RNG
- Significant damage output over 6 turns
- Speed control disrupts opponent's game plan
- Combines well with entry hazards and status moves

**Weaknesses:**
- Relies on successfully landing trapping moves first
- Countered by Shed Shell and Ghost-types
- Setup time vulnerable to fast attackers
- Magic Guard reduces effectiveness significantly

### Counters and Counterplay

**Direct Counters:**
- **Shed Shell:** Complete immunity to trapping effects
- **Ghost-types:** Can switch out freely (Gen 6+ mechanics)
- **Magic Guard:** Blocks trapping damage entirely
- **Clear Body/Full Metal Body:** Prevents Speed reductions

**Indirect Counters:**
- **Taunt:** Prevents setup moves while trapped
- **U-turn/Volt Switch:** Pivot moves can help trapped teammates
- **Priority moves:** Bypass Speed reductions when trapped
- **Substitute:** Blocks initial trapping attempt

### Version History
- **Elite Redux 1.0:** Introduced as innate ability combination
- **Current:** Stable implementation with consistent 6-turn duration and 1/6 damage

### Competitive Notes
Tentalock represents a significant upgrade over standard trapping abilities, making it valuable for teams that want to control the battlefield through sustained pressure and Speed manipulation. The guaranteed 6-turn duration eliminates the randomness typically associated with trapping moves, while the enhanced damage and Speed reduction create meaningful win conditions against setup-heavy teams.