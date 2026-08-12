---
id: 730
name: Razor Sharp
status: reviewed
character_count: 190
---

# Razor Sharp - Ability ID 730

## In-Game Description
"Critical hits also inflict bleeding."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Inflict bleed when landing a critical hit. Bleeding causes 1/16 max HP damage per turn, prevents healing, and negates the effects of stat stages. Rock and Ghost types are immune to bleeding.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Razor Sharp is an offensive ability that applies the bleeding status condition to opponents when the user lands a critical hit. Bleeding is a damaging status condition that deals consistent damage over time and prevents recovery.

### Activation Conditions
- **Critical hit requirement**: The attack must be a critical hit
- **Target requirements**: Target must be able to receive status conditions
- **Damage requirement**: The attack must successfully hit and deal damage
- **Status immunity**: Respects all normal status immunity rules

### Status Effect Details
- **Bleeding damage**: Deals 1/16 of the target's maximum HP per turn
- **Timing**: Damage occurs during the end-of-turn status damage phase
- **Healing prevention**: Prevents all forms of healing while active
- **Stat buffs**: Prevents stat increases while bleeding
- **Duration**: Lasts until cured by normal status-curing methods

### Technical Implementation
```c
constexpr Ability RazorSharp = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBleed(target))
        CHECK(gIsCriticalHit)

        return AbilityStatusEffect(MOVE_EFFECT_BLEED);
    },
};
```

### Bleeding Status Mechanics
- **Damage calculation**: `BLEED_DAMAGE(hp) = hp / 16`
- **Type immunities**: Rock and Ghost types cannot be inflicted with bleeding
- **Minimum damage**: Always deals at least 1 HP damage per turn
- **Magic Guard**: Blocked by Magic Guard ability
- **Status priority**: Cannot be applied if target already has a major status condition

### Important Interactions
- **Critical hit synergy**: Works with any move that can critical hit
- **Multi-hit moves**: Each hit can potentially trigger if it crits
- **Contact moves**: No contact requirement, works with all move types
- **Substitute**: Cannot inflict bleeding on substitute users
- **Focus Sash/Sturdy**: Bleeding damage can break these on subsequent turns

### Status Cure Methods
- **Natural healing**: Pecha Berry, Aromatherapy, Heal Bell
- **Switching**: Does not cure by switching (unlike poison in some games)
- **Items**: Full Heal, Status cure items
- **Moves**: Refresh, Rest (clears all status)
- **Abilities**: Natural Cure (on switch), Shed Skin (chance each turn)

### Strategic Implications
- **Crit-focused builds**: Synergizes with high critical hit ratio moves
- **Scope Lens/Razor Claw**: Items that boost crit rate enhance ability
- **Super Luck**: Ability that increases crit rate pairs well
- **Pressure application**: Forces opponents to cure status or suffer damage
- **Anti-recovery**: Shuts down healing strategies effectively

### Common Users
- Pokemon with naturally high critical hit ratios
- Physical attackers with access to high-crit moves
- Pokemon with Super Luck or similar abilities
- Fast Pokemon that can apply pressure quickly

### Competitive Usage Notes
- **Crit rate importance**: Ability effectiveness scales with critical hit frequency
- **Move selection**: Favor moves with high critical hit ratios
- **Item synergy**: Critical hit boosting items maximize ability value
- **Team support**: Benefits from crit rate support from teammates
- **Matchup dependent**: Most effective against bulky, defensive teams

### Counters
- **Type immunities**: Rock and Ghost types completely immune
- **Status immunity**: Abilities like Limber, Water Veil (if they block bleeding)
- **Clerics**: Pokemon with Aromatherapy/Heal Bell
- **Natural Cure**: Ability that removes status on switch
- **Lum Berry**: Auto-cures bleeding status
- **Magic Guard**: Prevents bleeding damage

### Synergies
- **Super Luck**: Doubles critical hit rate
- **Scope Lens/Razor Claw**: Boosts critical hit rate
- **Focus Energy**: Increases critical hit stage
- **High crit moves**: Slash, Psycho Cut, Stone Edge
- **Speed control**: Helps land critical hits before opponent can heal

### Comparison to Similar Abilities
- **To The Bone**: Also inflicts bleeding on crits but adds 1.5x crit damage
- **Poison Point**: Inflicts poison on contact (30% chance)
- **Static**: Inflicts paralysis on contact (30% chance)
- **Flame Body**: Inflicts burn on contact (30% chance)

### Version History
- Elite Redux exclusive ability
- Part of the expanded status condition system
- Bleeding status introduced alongside this ability
- Designed to reward critical hit focused gameplay

### Meta Impact
- Encourages critical hit rate investment in competitive play
- Provides alternative win condition through status damage
- Creates tension between offensive and defensive strategies
- Adds complexity to healing and recovery management