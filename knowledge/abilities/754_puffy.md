---
id: 754
name: Puffy
status: reviewed
character_count: 145
---

# Puffy - Ability ID 754

## In-Game Description
"Takes 1/2 dmg from contact moves but Fire moves hurt it 2x more."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from contact moves by 50%. Fire-type moves to deal double damage to the user. Multiplicative with other forms of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Puffy provides a defensive multiplier that affects incoming damage based on move properties and types:

1. **Contact Move Reduction**: All moves that make contact deal 50% damage (0.5x multiplier)
2. **Fire Vulnerability**: Fire-type moves deal 200% damage (2.0x resistance value = double damage)

### Implementation Details
```cpp
constexpr Ability Puffy = {
    .onDefensiveMultiplier = Fluffy.onDefensiveMultiplier,
    .breakable = TRUE,
};

// Referenced from Fluffy:
.onDefensiveMultiplier =
    +[](ON_DEFENSIVE_MULTIPLIER) {
        if (moveType == TYPE_FIRE) RESISTANCE(2.0);  // 2x damage from Fire
        if (IsMoveMakingContact(move, attacker)) MUL(0.5);  // 0.5x from contact
    },
```

### Contact Move Determination
Uses `IsMoveMakingContact(move, attacker)` which checks:
- Move's natural contact flag in move data
- Abilities that can modify contact (Long Reach negates contact)
- Items that affect contact mechanics

### Affected Moves
**Contact moves reduced by 50%:**
- Most physical moves: Tackle, Body Slam, Thunder Punch, etc.
- Some special moves: Grass Knot, Petal Dance (if contact flagged)
- Multi-hit contact moves: each hit is reduced

**Not affected by contact reduction:**
- Non-contact physical moves: Earthquake, Rock Slide, Bullet Seed
- All special moves (unless specifically flagged as contact)
- Status moves

**Fire moves dealing double damage:**
- All Fire-type moves regardless of contact status
- Includes: Flamethrower, Fire Blast, Fire Punch, Flare Blitz, etc.

### Interactions with Other Mechanics

**Ability Interactions:**
- **Breakable**: Can be suppressed by Mold Breaker, Turboblaze, Teravolt
- **Long Reach**: Negates the contact reduction component
- **Iron Fist/Tough Claws**: Contact boosting abilities stack with Puffy's reduction

**Item Interactions:**
- **Protective Pads**: Prevents contact effects but Puffy still reduces damage
- **Rocky Helmet**: Contact attackers still take recoil despite reduced damage

**Type Effectiveness Stacking:**
- Fire vulnerability stacks with type effectiveness
- Fire vs Grass (Popcorm): 2x (type) x 2x (Puffy) = 4x total damage
- Contact reduction applies after type effectiveness calculation

### Damage Calculation Example
**Contact Physical Move vs Puffy user:**
- Base damage: 100
- Type effectiveness: 1.0x (neutral)
- Puffy reduction: 0.5x
- Final damage: 50

**Fire-type move vs Popcorm (Grass/Fire) with Puffy:**
- Base damage: 100
- Type effectiveness vs Grass: 2.0x
- Puffy Fire vulnerability: 2.0x
- Final damage: 400 (extremely vulnerable)

### Strategic Implications

**Strengths:**
- Excellent physical wall against contact-based attackers
- Forces opponents to use non-contact moves or special attacks
- Provides reliable damage reduction in physical matchups

**Weaknesses:**
- Extreme Fire vulnerability makes Fire moves devastating
- Non-contact physical moves bypass the protection entirely
- Special attackers can exploit the lack of special defense boost

**Team Building Considerations:**
- Pair with Pokemon that resist Fire moves
- Use in teams with good Fire-type switch-ins
- Consider dual screens or other defensive support

### Common Users
- **Popcorm** (Grass/Fire): Ironic typing makes Fire weakness even more severe
- **Popcorm-Mega** (Grass/Fire): Higher stats but same vulnerabilities

### Competitive Usage
**Niche Applications:**
- Anti-physical specialist in specific matchups
- Situational defensive pivot against contact-heavy teams
- Surprise factor in lower tiers

**Major Limitations:**
- Fire weakness severely limits viability
- Grass/Fire typing on current users compounds Fire vulnerability
- Better defensive abilities available for most roles

### Counters
**Direct Counters:**
- Any Fire-type attacker (devastating damage)
- Non-contact physical attackers (Earthquake users, etc.)
- Special attackers (bypass protection entirely)
- Mold Breaker users (ignore ability completely)

**Indirect Counters:**
- Status moves (not affected by damage reduction)
- Entry hazards (bypass ability)
- Weather damage (not affected)

### Synergies
**Ability Synergies:**
- **Aerodynamics** (innate on Popcorm): Speed boost helps with pivoting
- **Levitate** (innate on Popcorm): Immunity to Ground moves
- **Skill Link** (innate on Popcorm): Multi-hit moves all benefit from contact reduction

**Item Synergies:**
- **Leftovers**: Reliable recovery to maintain bulk
- **Assault Vest**: Special bulk to complement physical protection
- **Heat Rock/Flash Fire redirect**: Team support for Fire weakness

### Version History
- Introduced in Elite Redux as ability ID 754
- Shares implementation with Fluffy (original Pokemon ability)
- Currently exclusive to Popcorm line (Grass/Fire types)
- Part of Elite Redux's expanded ability roster

### Design Notes
Puffy represents a high-risk, high-reward defensive ability that provides substantial protection against a common attack category while creating a glaring weakness. The Fire vulnerability is particularly punishing on Grass-type users, creating interesting teambuilding challenges and strategic depth.