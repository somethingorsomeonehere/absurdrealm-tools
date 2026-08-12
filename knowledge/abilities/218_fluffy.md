---
id: 218
name: Fluffy
status: reviewed
character_count: 152
---

# Fluffy - Ability ID 218

## In-Game Description
"Takes 1/2 dmg from contact moves but Fire moves hurt it 2x more."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Fluffy reduces damage from contact moves by 50%. Fire-type moves to deal double damage to the user. Multiplicative with other forms of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Contact Move Reduction**: All moves that make physical contact deal 0.5x damage (50% reduction)
- **Fire Vulnerability**: Fire-type moves deal 2.0x damage (100% increase)
- **Breakable**: Can be suppressed by abilities like Mold Breaker, Teravolt, Turboblaze

### Activation Conditions
- Contact move reduction triggers when the Pokemon is hit by any move with the contact flag
- Fire vulnerability applies to all Fire-type moves regardless of contact status
- Both effects are passive and automatic

### Technical Implementation
```cpp
constexpr Ability Fluffy = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE) RESISTANCE(2.0);
            if (IsMoveMakingContact(move, attacker)) MUL(0.5);
        },
    .breakable = TRUE,
};
```

### Contact Moves (Examples)
**Affected moves include:**
- Physical attacks: Tackle, Scratch, Pound, Quick Attack, Body Slam
- Punching moves: Punch, Fire Punch, Ice Punch, Thunder Punch
- Slashing moves: Slash, Night Slash, Psycho Cut
- Biting moves: Bite, Crunch, Fire Fang
- Multi-hit contact moves: Fury Swipes, Double Slap, Bullet Seed (if contact)

**NOT affected:**
- Projectile moves: Hyper Beam, Flamethrower, Thunderbolt
- Ranged physical moves: Rock Slide, Earthquake, Stone Edge
- Status moves: Thunder Wave, Toxic, Spore

### Interactions with Other Abilities/Mechanics
- **Suppression**: Mold Breaker, Teravolt, Turboblaze ignore both benefits and drawbacks
- **Ability Shield**: Protects from ability suppression
- **Type effectiveness**: Fire weakness stacks with natural Fire weakness
- **Critical hits**: Contact reduction applies to critical hits
- **Multi-hit moves**: Each hit affected individually

### Strategic Implications
**Strengths:**
- Excellent physical wall against contact-based attackers
- Forces opponents to use special moves or non-contact physical moves
- Synergizes well with high HP and Defense stats

**Weaknesses:**
- Severe Fire weakness creates exploitable matchups
- Vulnerable to special attackers and ranged physical moves
- Ability suppression removes all benefits while keeping Fire weakness

### Example Damage Calculations
Against a Pokemon with Fluffy:
- **Tackle (contact)**: 100 base damage to 50 damage (50% reduction)
- **Flamethrower (Fire, non-contact)**: 90 base damage to 180 damage (2x Fire weakness)
- **Fire Punch (Fire + contact)**: 75 base damage to 150 damage (Fire weakness applied, contact reduction ignored for Fire moves)
- **Earthquake (non-contact)**: 100 base damage to 100 damage (no modifier)

### Common Users
- **Stufful line**: Stufful and Bewear are the primary users in mainline games
- **Defensive Pokemon**: Works best on bulky Pokemon that can capitalize on the contact reduction
- **Mixed walls**: Particularly effective on Pokemon with good special bulk to compensate for Fire weakness

### Competitive Usage Notes
- **Team building**: Requires Fire-type switch-ins or resists
- **Movepool synergy**: Benefits from non-contact physical moves for offense
- **Weather**: Sun doubles Fire damage, making the weakness even more severe
- **Item synergy**: Leftovers or other recovery items help maintain bulk

### Counters
- **Fire-type moves**: Exploit the 2x weakness
- **Special attackers**: Bypass the contact reduction entirely
- **Mold Breaker variants**: Ignore the ability completely
- **Non-contact physical moves**: Earthquake, Rock Slide, Stone Edge
- **Status moves**: Toxic, Will-O-Wisp for indirect damage

### Synergies
- **Assault Vest**: Boosts special bulk to cover Fire weakness
- **Rocky Helmet**: Stacks damage with contact-based counter-attacks
- **Recovery moves**: Roost, Recover to maintain defensive presence
- **Intimidate support**: Further reduces physical damage

### Version History
- Introduced in Generation VII (Sun/Moon)
- Implemented in Elite Redux with identical mechanics
- Ability ID 218 in Elite Redux's ability system
- Classified as breakable ability in current implementation