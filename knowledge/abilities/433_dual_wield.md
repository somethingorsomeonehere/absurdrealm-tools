---
id: 433
name: Dual Wield
status: reviewed
character_count: 197
---

# Dual Wield - Ability ID 433

## In-Game Description
"Mega Launcher and Keen Edge moves hit twice for 70% damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mega Launcher and Keen Edge moves that hit one time normally now hit twice, with each hit dealing 70% of the move's normal damage. Secondary effects roll independently for each hit (except flinch).

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Dual Wield is an offensive ability that transforms certain moves into double-hitting attacks. When the user attempts a move that would be boosted by either Mega Launcher or Keen Edge, the ability converts it into a two-hit attack using the Parental Bond system.

### Activation Conditions
- **Move Type Requirement**: Move must have either:
  - `FLAG_MEGA_LAUNCHER_BOOST` (beam/pulse/cannon moves)
  - `FLAG_KEEN_EDGE_BOOST` (blade/cutting moves)
- **Damage Calculation**: Each hit deals 70% of the original move's power
- **Total Damage**: 140% of original damage (0.7 x 2 = 1.4)
- **Hit Mechanics**: Uses `PARENTAL_BOND_DUAL_WIELD` system

### Mega Launcher Boosted Moves (Examples)
**Beam/Pulse Moves:**
- Water Gun, Hydro Pump, Ice Beam, Psybeam
- Aurora Beam, Hyper Beam, Solar Beam, Dragon Pulse
- Aura Sphere, Dark Pulse, Focus Blast, Flash Cannon
- Charge Beam, Signal Beam, Heal Pulse, Steam Eruption
- Origin Pulse, Fleur Cannon, Prismatic Laser, Dynamax Cannon

**Projectile Moves:**
- Sludge Bomb, Octazooka, Zap Cannon, Rock Blast
- Gunk Shot, Searing Shot, Anchor Shot, Scale Shot
- Meteor Beam, Shell Side Arm, many custom moves

### Keen Edge Boosted Moves (Examples)
**Blade/Cutting Moves:**
- Karate Chop, Razor Wind, Guillotine (custom effect)
- Cut, Slash, Leaf Blade, Night Slash
- Psycho Cut, Air Cutter, Sacred Sword
- Many custom blade moves in Elite Redux

### Technical Implementation
```c
// Dual Wield ability definition
constexpr Ability DualWield = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType {
        CHECK(IsMegaLauncherBoosted(battler, move) || gBattleMoves[move].flags & FLAG_KEEN_EDGE_BOOST);
        return PARENTAL_BOND_DUAL_WIELD;
    },
};

// Damage calculation in battle_util.c
case PARENTAL_BOND_DUAL_WIELD:
    return UQ_4_12(0.7);  // 70% damage per hit
```

### Important Interactions
- **Secondary Effects**: Both hits can trigger secondary effects independently
- **Contact Moves**: Contact-based moves make contact on both hits
- **Accuracy**: Each hit is rolled for accuracy separately
- **Critical Hits**: Each hit can crit independently
- **Substitutes**: Can break substitute on first hit, damage Pokemon on second
- **Abilities**: Abilities like Sturdy, Focus Sash only block the first hit
- **Items**: Life Orb recoil applies after each hit

### Move Selection Logic
The ability works through the `IsMegaLauncherBoosted()` function which returns true if:
1. Move has `FLAG_MEGA_LAUNCHER_BOOST` flag, OR
2. Move is a status move and user has Gunman ability, OR
3. Move has `FLAG_KEEN_EDGE_BOOST` flag (direct check)

### Damage Comparison
- **Single Hit**: 100% damage
- **Dual Wield**: 70% + 70% = 140% total damage
- **Parental Bond**: 100% + 25% = 125% total damage (for comparison)
- **Skill Link Multi-Hit**: Usually 125% (5 x 25%) but varies by move

### Strategic Implications
- **Power Boost**: Effective 40% damage increase over single hits
- **Multi-Hit Benefits**: Breaks substitutes, triggers abilities multiple times
- **Status Spreading**: Doubles chance for secondary effects to trigger
- **Synergy Potential**: Excellent with abilities that trigger on hit
- **Drawbacks**: Vulnerable to Rocky Helmet, Rough Skin, Iron Barbs

### Synergistic Abilities
- **Mega Launcher**: Boosts base power by 30%, then Dual Wield doubles hits
- **Keen Edge**: Boosts base power by 30%, then Dual Wield doubles hits
- **Sheer Force**: Prevents secondary effects but boosts power
- **Life Orb**: Boosts both hits but doubles recoil damage

### Common Users
Dual Wield is particularly effective on:
- **Special Attackers**: With access to beam/pulse moves
- **Physical Attackers**: With blade/cutting moves
- **Mixed Attackers**: Who can utilize both move types
- **Pokemon with good movepool coverage**: Maximizing eligible moves

### Counters and Limitations
- **Rocky Helmet/Rough Skin**: Double damage from contact moves
- **Sturdy/Focus Sash**: Only blocks first hit, not second
- **Substitute**: Can be broken by first hit, but limits second hit
- **Protection moves**: Block both hits completely
- **Abilities**: Lightning Rod, Storm Drain, etc. only redirect first hit

### Competitive Usage Notes
- **Move Selection**: Prioritize moves with secondary effects
- **Item Synergy**: Life Orb for power, Choice items for consistency
- **Team Support**: Excellent for breaking through defensive cores
- **Late Game**: Powerful for cleaning up weakened teams
- **Coverage**: Wide movepool compatibility makes it versatile

### Version History
- New ability introduced in Elite Redux
- Uses the Parental Bond system for implementation
- Unique in affecting both Mega Launcher and Keen Edge moves
- Part of Elite Redux's expanded ability roster

### Related Abilities
- **Mega Launcher**: Base power boost for beam/pulse moves
- **Keen Edge**: Base power boost for blade/cutting moves
- **Parental Bond**: Similar double-hit mechanic with different power split
- **Skill Link**: Guarantees maximum hits for multi-hit moves