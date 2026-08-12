---
id: 7
name: Limber
status: reviewed
character_count: 281
---

# Limber - Ability ID 7

## In-Game Description
"Immune to paralysis. Takes 50% less recoil damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All recoil damage to the user is halved; this includes moves with scaling recoil damage like Brave Bird, moves with crash damage like Jump Kick, or moves with fixed recoil like Steel Beam. Paralysis also cannot affect the user, and if they gain Limber, existing paralysis is cured.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Limber provides two distinct defensive benefits:

1. **Paralysis Immunity**
   - Complete immunity to paralysis status
   - Removes existing paralysis when gained
   - Prevents paralysis from all sources (Thunder Wave, Static, Body Slam, etc.)
   - Shows ability popup when paralysis is attempted

2. **Recoil Reduction (50%)**
   - All recoil damage is halved
   - Applies to move recoil (Double-Edge, Brave Bird, etc.)
   - Applies to crash damage (High Jump Kick miss)
   - Applies to Mind Blown and Steel Beam self-damage

### Technical Implementation

**Code Structure** (`src/abilities.cc`):
```cpp
constexpr Ability Limber = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_PARALYSIS)
        return TRUE;
    },
    .breakable = TRUE,
    .halfRecoil = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Key Properties
- **Breakable**: Can be suppressed by Mold Breaker, Gastro Acid, etc.
- **Status Removal**: Cures paralysis if gained while paralyzed
- **Half Recoil Flag**: Reduces all forms of recoil by 50%

### Recoil Calculation Examples
For a Pokemon using Brave Bird (120 BP, 33% recoil):
- Normal: Deals 120 damage, takes 40 recoil
- With Limber: Deals 120 damage, takes **20 recoil**

For High Jump Kick miss:
- Normal: Loses 50% max HP
- With Limber: Loses **25% max HP**

### Interactions with Other Abilities/Mechanics
- **Reckless**: Boosts recoil move damage, Limber reduces the recoil
- **Rock Head**: Complete recoil immunity vs Limber's 50% reduction
- **Magic Guard**: Also provides recoil immunity
- **Sheer Force**: Removes recoil entirely for affected moves
- **Thunder Wave**: Completely blocked by Limber

### Strategic Implications
1. **Physical Sweeper**: Safely use powerful recoil moves
2. **Speed Tier Maintenance**: No paralysis speed drops
3. **Pivot**: Switch into predicted Thunder Wave
4. **Recoil Attacker**: Brave Bird, Double-Edge become more spammable
5. **Risk Mitigation**: High Jump Kick less punishing on miss

### Common Strategies
- **Recoil Spam**: Use high-power recoil moves repeatedly
- **Paralysis Bait**: Switch into obvious Thunder Wave attempts
- **Life Orb Synergy**: Already taking chip damage, recoil reduction helps
- **Choice Band**: Maximum power with reduced drawback

### Competitive Usage Notes
- High-tier ability for physical attackers
- Enables recoil move spam strategies
- Excellent on fast, frail attackers
- Paralysis immunity maintains offensive pressure
- Particularly valuable in paralysis-heavy metagames

### Affected Moves (Recoil Reduction)
**Recoil Moves**: Brave Bird, Double-Edge, Flare Blitz, Head Smash, Submission, Take Down, Volt Tackle, Wild Charge, Wood Hammer

**Crash Moves**: High Jump Kick, Jump Kick

**Other**: Mind Blown, Steel Beam, Shadow End, Light of Ruin

### Common Users
- Persian (original user)
- Hitmonlee (benefits from HJK safety)
- Various Normal-types with Double-Edge
- Physical attackers with recoil moves

### Counters
- **Burn**: Alternative speed/damage reduction
- **Intimidate**: Reduces physical damage output
- **Static/Flame Body**: Contact punishments still work
- **Priority moves**: Bypass speed advantage
- **Gastro Acid**: Removes the ability

### Synergies
- **Swords Dance**: Set up then spam recoil moves
- **Healing support**: Offset remaining recoil
- **Tailwind**: Stack speed control
- **Healing Wish**: Full restore after recoil accumulation
- **Choice items**: Maximum damage output

### Version History
- **Original**: Only paralysis immunity
- **Elite Redux**: Added 50% recoil reduction for offensive utility