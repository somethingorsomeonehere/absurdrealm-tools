---
id: 486
name: Prim and Proper
status: reviewed
character_count: 298
---

# Prim and Proper - Ability ID 486

## In-Game Description
"Cute Charm + Fort Knox."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by making contact (offensively or defensively), has a 50% chance to infatuate the attacker (cuts their Attack and Special Attack in half). Only works on Pokemon of the opposite gender. Immune to all damage boosting ability effects from opponents, other than Parental Bond and Multi Headed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Prim and Proper combines romantic charm with absolute defensive composure, creating a Pokemon that both enchants attackers and remains unaffected by their offensive abilities.

### Dual Effect Components

#### Cute Charm Component
- **Trigger**: When hit by contact moves
- **Chance**: 50% probability per contact hit
- **Effect**: Inflicts Attract status on the attacker
- **Gender requirement**: Only works on opposite-gender attackers
- **Contact requirement**: Move must have the contact flag

#### Fort Knox Component
- **Protection**: Complete immunity to offensive ability multipliers
- **Scope**: Blocks all opponent offensive abilities when being attacked
- **Examples blocked**: Huge Power, Pure Power, Guts, Iron Fist, etc.
- **Mechanism**: fortKnox = TRUE flag provides total offensive ability immunity

### Technical Implementation
```c
constexpr Ability PrimAndProper = {
    .onDefender = CuteCharm.onDefender,  // 50% attract on contact
    .fortKnox = TRUE,                    // Immune to offensive abilities
};

// Cute Charm mechanics
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(IsMoveMakingContact(gCurrentMove))
    CHECK(ShouldApplyOnHitAffect(battler))
    CHECK(Random() % 100 < 50)
    CHECK(CanInfatuate(attacker, battler))
    
    SetMoveEffect(MOVE_EFFECT_ATTRACT, FALSE);
    return TRUE;
}
```

### Attract Status Mechanics
- **Duration**: Permanent until cured or target switches out
- **Effect**: 50% chance per turn to be unable to attack due to infatuation
- **Gender dependency**: Requires opposite genders to work
- **Message**: "X fell in love with Y!"
- **Curing**: Mental Herb, switching out, or certain abilities

### Fort Knox Protection
**Blocked offensive abilities:**
- Huge Power/Pure Power (2x attack multipliers)
- Guts (1.5x attack when statused)
- Iron Fist (1.3x punch move boost)
- Technician (1.5x boost for weak moves)
- Sheer Force (1.3x boost for effect moves)
- Type-boosting abilities (Blaze, Torrent, etc.)

### Strategic Applications
- **Contact deterrent**: Punishes physical attackers with infatuation
- **Ability immunity**: Negates common offensive ability strategies
- **Defensive wall**: Enhanced bulk through ability blocking
- **Gender strategy**: Most effective against opposite-gender teams
- **Physical counter**: Specifically targets contact move users

### Contact Move Examples
**Commonly affected moves:**
- Physical attacks: Tackle, Body Slam, Return
- Punch moves: Fire Punch, Ice Punch, Thunder Punch
- Bite moves: Bite, Crunch, Hyper Fang
- Fighting moves: Close Combat, Drain Punch

**Not affected:**
- Ranged attacks: Thunderbolt, Flamethrower
- Projectile moves: Shadow Ball, Energy Ball
- Non-contact physical: Rock Slide, Earthquake

### Competitive Usage
- **Defensive tank**: Excellent bulk through ability immunity
- **Contact wall**: Specializes in stopping physical contact users
- **Anti-ability**: Hard counters ability-dependent attackers
- **Gender dynamics**: Team building consideration for gender ratios
- **Stall teams**: Provides passive disruption and protection

### Gender Interactions
**Maximum effectiveness:**
- Against opposite-gender physical attackers
- Mixed teams with gender variety
- Contact-heavy physical strategies

**Reduced effectiveness:**
- Same-gender opponents (no attract)
- Genderless Pokemon (no attract)
- Special attackers (no contact)

### Synergies
**Team support:**
- Leftovers: Sustain while providing passive effects
- Rocky Helmet: Stack contact punishment
- Mental Herb: Ironically protects user from attract

**Move synergies:**
- Protect: Stall while opponents deal with attract
- Substitute: Additional protection layer
- Recovery moves: Sustain defensive presence

### Counters
- **Same-gender attackers**: Immune to attract effect
- **Genderless Pokemon**: Cannot be attracted
- **Long-range attackers**: Avoid contact entirely
- **Substitute**: Blocks contact and prevents attract
- **Mental Herb**: Cures attract immediately
- **Ability suppression**: Mold Breaker bypasses both effects

### Double Battle Applications
- **Partner protection**: Fort Knox protects against spread moves
- **Field control**: Attract affects single target
- **Support utility**: Defensive presence for team
- **Gender coordination**: Team building around gender ratios

### Limitations
- **Gender dependency**: Attract only works on opposite genders
- **Contact requirement**: No effect against ranged attackers
- **Single infatuation**: Can only attract one target at a time
- **Cure availability**: Mental Herb and switching cure attract
- **Special attackers**: Less effective against special-based strategies

### Item Interactions
**User items:**
- Leftovers: Passive healing for sustained presence
- Rocky Helmet: Additional contact punishment
- Chople Berry: Survive Fighting moves to trigger effects

**Opponent items:**
- Mental Herb: Cures attract status
- Choice items: Struggle when attracted and locked
- Lum Berry: One-time attract cure

### Team Building Considerations
- **Gender balance**: Consider team gender distribution
- **Physical walls**: Excellent against contact-heavy teams
- **Ability teams**: Counters ability-dependent strategies
- **Stall cores**: Provides passive disruption
- **Switch pivots**: Safe switching with defensive utility

### Version History
- Elite Redux custom ability combining charm and defense
- Designed to create unique defensive archetype
- Part of expanded defensive ability system
- Represents refined, untouchable elegance in battle