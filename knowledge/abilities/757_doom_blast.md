---
id: 757
name: Doom Blast
status: reviewed
character_count: 150
---

# Doom Blast - Ability ID 757

## In-Game Description
"Dark-type moves deal 1.35x damage but have 10% recoil."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Dark-type moves by 35% but causes 10% recoil damage based on damage dealt (minimum 1 HP). The recoil damage will be able to knock out the user.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Doom Blast is a high-risk, high-reward ability that significantly boosts Dark-type offensive power while inflicting recoil damage on the user.

**Damage Boost:**
- Multiplies all Dark-type move damage by 1.35x (35% increase)
- Applied after all other damage calculations
- Affects both physical and special Dark-type moves

**Recoil Mechanism:**
- Triggers after dealing damage with any Dark-type move
- Recoil damage = max(damage_dealt / 20, 1)
- This equals 5% of damage dealt, with a minimum of 1 HP
- Uses the B_MSG_RECOIL_NORMAL message format

### Technical Implementation
```cpp
constexpr Ability DoomBlast = {
    .onRecoil = +[](ON_RECOIL) -> int {
        CHECK(moveType == TYPE_DARK);
        gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_RECOIL_NORMAL;
        return max(damage / 20, 1);
    },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_DARK) MUL(1.35);
        },
};
```

### Affected Moves
All 64 Dark-type moves in the game are affected, including but not limited to:
- **Physical:** Knock Off, Crunch, Sucker Punch, Pursuit, Bite, Payback
- **Special:** Dark Pulse, Shadow Ball, Snarl, Night Daze, Hex
- **Status:** Not affected (no damage to calculate recoil from)

### Damage Calculations
**Example with 100 BP Dark Pulse:**
- Base damage: 100 BP
- With Doom Blast: 100 x 1.35 = 135 effective BP
- If deals 200 damage: Recoil = max(200/20, 1) = 10 HP recoil

**Example with weak attack dealing 15 damage:**
- Recoil would be max(15/20, 1) = max(0.75, 1) = 1 HP minimum

### Strategic Implications
**Advantages:**
- Massive 35% boost to all Dark-type moves
- Transforms moderate Dark moves into powerful attacks
- Excellent for sweeping with Dark-type coverage
- Pairs well with high Attack/Special Attack stats

**Disadvantages:**
- Constant HP drain limits longevity
- Makes the user susceptible to priority moves
- Recoil can be substantial with high-damage attacks
- Self-KO risk in extended battles

### Common Users
Currently exclusive to:
- **Morpeko (Hangry Form)** - Electric/Dark type with 101 Attack and Speed
  - Benefits from STAB on Dark moves (1.5x x 1.35x = 2.025x total multiplier)
  - High Speed allows for quick sweeping before recoil accumulates
  - Also has Electrocytes and Power Spot as alternative abilities

### Competitive Usage
**Optimal Sets:**
- Choice Band/Choice Specs for maximum damage output
- Life Orb synergy creates extreme power but accelerated HP loss
- Focus Sash for guaranteed survival of first recoil

**Team Support:**
- Wishes support to recover recoil damage
- Entry hazard removal to prevent additional chip damage
- Priority protection from teammates

### Counters and Answers
**Direct Counters:**
- Steel-types resist Dark moves (Doom Blast boost less impactful)
- Fairy-types are immune to Dark moves
- Bulky resists that can tank boosted Dark moves
- Priority users can exploit recoil damage accumulation

**Indirect Counters:**
- Entry hazards compound the HP loss problem
- Status conditions (burn, poison) accelerate KO timing
- Defensive cores that force multiple attacks

### Notable Synergies
**Abilities:**
- Does not stack with other recoil abilities (would be redundant)
- Magic Guard would negate recoil (not available on current users)
- Guts could potentially benefit from recoil damage as indirect "status"

**Items:**
- Life Orb: Extreme power but 20% total HP loss per attack (10% + 10%)
- Choice items: Maximize damage while locked into Dark moves
- Leftovers/Black Sludge: Partial recoil recovery

**Moves:**
- Rest: Full HP recovery but wastes turns
- Roost: Consistent healing option
- Drain moves: Don't exist in Dark-type movepool

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Currently version 2.6 implementation
- Unique ability exclusive to Morpeko Hangry Form
- No balance changes recorded since introduction

### Competitive Viability
**Tier Placement:** High-risk, high-reward niche ability
**Usage Rate:** Low due to single Pokemon availability
**Success Rate:** Moderate - effective in right hands but requires careful play

The ability transforms Dark-type moves into nuclear options while demanding precise positioning and game state awareness to maximize effectiveness before recoil damage becomes overwhelming.