---
id: 497
name: Yuki Onna
status: reviewed
character_count: 275
---

# Yuki Onna - Ability ID 497

## In-Game Description
"Intimidate variant + 30% attract on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Lowers both Attack and Special Attack of opposing Pokemon upon entry by one stage. Additionally provides a 30% chance to infatuate (cuts their Attack and Special Attack in half) the target on contact. Works offensively and defensively. This only works on the opposite gender.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Yuki Onna combines battlefield intimidation with enchanting contact effects, representing the dual nature of the legendary Japanese snow spirit who is both terrifying and beautiful.

### Entry Effect: Dual Intimidation
- **Trigger**: Activates immediately upon switching into battle
- **Stats lowered**: Both Attack and Special Attack by 1 stage each
- **Targets**: All opposing Pokemon on the field
- **Scope**: Affects both opponents in double battles
- **Message**: Uses intimidate activation battle script

### Contact Effect: Infatuation
- **Trigger**: When Yuki Onna makes contact with an opponent
- **Chance**: 30% probability per contact move
- **Status**: Attract (infatuation)
- **Requirement**: Target must be capable of infatuation
- **Success condition**: Move must successfully hit and affect target

### Technical Implementation
```c
constexpr Ability YukiOnna = {
    .onEntry = +[](ON_ENTRY) -> int {
        return UseIntimidateClone(battler, ability);
    },
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(IsMoveMakingContact(gCurrentMove))
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(Random() % 100 < 30)
        CHECK(CanInfatuate(battler, target))
        
        SetMoveEffect(MOVE_EFFECT_ATTRACT, FALSE);
        return TRUE;
    },
};
```

### Intimidate Clone System
```c
// Custom intimidate variant that lowers both offensive stats
.targetBoth = TRUE,        // Affects both opponents
.statLower = {
    [STAT_ATK] = 1,       // Lower Attack by 1 stage
    [STAT_SPATK] = 1,     // Lower Special Attack by 1 stage
},
```

### Infatuation Mechanics
- **Effect**: Target falls in love and may not attack 50% of the time
- **Duration**: Permanent until cured or target switches out
- **Gender requirement**: Typically requires opposite genders
- **Immunity**: Same-gender Pokemon or genderless often immune
- **Curing**: Mental Herb, switching out, or certain abilities

### Strategic Applications
- **Dual stat reduction**: Weakens both physical and special attackers
- **Contact deterrent**: Punishes physical attackers with infatuation
- **Entry control**: Immediate battlefield impact upon switching
- **Mixed utility**: Both offensive and defensive applications
- **Psychological warfare**: Forces cautious play from opponents

### Folklore Connection
**Japanese Yuki-onna legend:**
- **Beautiful but deadly**: Snow woman who appears on winter nights
- **Dual nature**: Both alluring and terrifying to travelers
- **Fatal attraction**: Men become entranced by her beauty before freezing
- **Intimidating presence**: Her appearance fills witnesses with dread

### Contact Move Interactions
**Commonly affected moves:**
- Physical attacks: Tackle, Body Slam, Return
- Punch moves: Fire Punch, Ice Punch, Thunder Punch
- Bite moves: Bite, Crunch, Hyper Fang
- Fighting moves: Close Combat, Drain Punch

**Not affected:**
- Ranged attacks: Flamethrower, Thunderbolt
- Non-contact physical: Rock Slide, Earthquake
- Special moves: Most special attacks

### Double Battle Applications
- **Team debuffing**: Weakens both opposing Pokemon simultaneously
- **Contact punishment**: Deters physical attackers from both sides
- **Field presence**: Creates immediate impact across entire field
- **Support utility**: Helps entire team by weakening opponents

### Competitive Usage
- **Lead Pokemon**: Excellent for immediate battlefield control
- **Defensive walls**: Reduces incoming damage while punishing contact
- **Support role**: Weakens opponents for teammates
- **Pivot Pokemon**: Entry effect helps team, contact effect aids staying power
- **Stall teams**: Disrupts offensive pressure through stat reduction

### Synergies
**Stat reduction synergy:**
- Rocky Helmet: Additional contact punishment
- Leftovers: Sustain while opponents deal reduced damage
- Eviolite: Enhanced bulk while debuffing opponents

**Team support:**
- Entry hazards: Stack passive damage with stat reduction
- Status spreaders: Combine with other disruptive effects
- Defensive cores: Create safe switching opportunities

### Counters
- **Clear Body/White Smoke**: Immune to stat reduction
- **Defiant/Competitive**: Turn stat drops into boosts
- **Substitute**: Blocks contact and prevents infatuation
- **Long-range attackers**: Avoid contact entirely
- **Same-gender teams**: Resist infatuation effects

### Limitations
- **One-time entry**: Stat reduction only on switch-in
- **Contact requirement**: Infatuation needs physical contact
- **Gender dependency**: Infatuation often requires opposite genders
- **Mental immunity**: Some abilities prevent infatuation
- **Stat immunity**: Some abilities prevent stat reduction

### Item Interactions
**Beneficial items:**
- Mental Herb: Opponent item that cures infatuation
- Lum Berry: Opponent item that cures attract status
- Ability Shield: Prevents intimidate-like effects

**User items:**
- Rocky Helmet: Stack contact punishment
- Leftovers: Sustain through prolonged battles
- Choice items: Hit hard after debuffing opponents

### Version History
- Elite Redux custom ability inspired by Japanese folklore
- Combines intimidation with attraction for thematic accuracy
- Designed to capture the dual nature of the Yuki-onna legend
- Part of expanded cultural mythology ability system