---
id: 731
name: To The Bone
status: reviewed
character_count: 202
---

# To The Bone - Ability ID 731

## In-Game Description
"Critical hits get a 1.5x boost and inflict bleeding."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Critical hits are boosted by 50% and inflict bleeding. Bleeding causes 1/16 max HP damage per turn, prevents healing, and negates the effects of stat stages. Rock and Ghost types are immune to bleeding.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
To The Bone is a hybrid offensive ability that combines critical hit damage amplification with status infliction. It has two distinct effects that work together to create a powerful synergy.

### Critical Hit Damage Boost
- **Damage multiplier**: Critical hits deal 1.5x additional damage (stacks with base crit multiplier)
- **Calculation**: Normal crit (2x) becomes 3x damage with To The Bone
- **Type independence**: Works with all move types and categories
- **Timing**: Damage boost applies during damage calculation phase

### Bleeding Infliction
- **Trigger condition**: Only activates on critical hits
- **Status effect**: Inflicts bleeding status condition on the target
- **Damage formula**: 1/16 of target's maximum HP per turn (minimum 1 HP)
- **Timing**: Bleeding damage occurs at end of turn, after other effects
- **Duration**: Permanent until switched out, cured, or fainted

### Technical Implementation
```c
// To The Bone combines two existing ability effects:
constexpr Ability ToTheBone = {
    .onAttacker = RazorSharp.onAttacker,        // Bleeding on crit
    .onOffensiveMultiplier = Sniper.onOffensiveMultiplier,  // 1.5x crit damage
};

// RazorSharp effect - bleeding on critical hits
.onAttacker = +[](ON_ATTACKER) -> int {
    CHECK(ShouldApplyOnHitAffect(target))
    CHECK(CanBleed(target))
    CHECK(gIsCriticalHit)  // Only triggers on crits
    return AbilityStatusEffect(MOVE_EFFECT_BLEED);
}

// Sniper effect - 1.5x critical hit damage
.onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
    if (isCrit) MUL(1.5);
}
```

### Bleeding Mechanics
- **Damage calculation**: `BLEED_DAMAGE(maxHP) = maxHP / 16`
- **Minimum damage**: Always deals at least 1 HP damage
- **Status type**: Primary status condition (like burn, poison, paralysis)
- **Immunity**: Rock-type and Ghost-type Pokemon are immune to bleeding
- **Magic Guard interaction**: Bleeding damage is blocked by Magic Guard
- **Healing**: Can be cured by items, moves, or abilities that cure status conditions

### Critical Hit Synergy
The ability creates a powerful synergy loop:
1. High critical hit rate increases bleeding application frequency
2. Bleeding damage softens targets for future attacks
3. Enhanced critical damage ensures meaningful impact when crits occur
4. Status condition provides ongoing pressure even after switching

### Activation Requirements
- **Critical hit required**: Both effects only activate on critical hits
- **Target must be hittable**: Standard hit/miss calculation applies first
- **No self-infliction**: Cannot cause bleeding on the user
- **Status susceptibility**: Target must be able to receive bleeding status

### Important Interactions
- **Focus Energy/Lucky Chant**: Abilities that affect crit rates indirectly affect bleeding frequency
- **Super Luck**: Pokemon with high natural crit rates maximize this ability's potential
- **Scope Lens/Razor Claw**: Items that boost crit rate increase bleeding application
- **Multi-hit moves**: Each hit can potentially trigger bleeding if it crits
- **Substitute**: Bleeding bypasses Substitute and damages the real Pokemon
- **Taunt**: Doesn't prevent the ability from working

### Bleeding Status Details
- **End-turn timing**: Occurs during end-of-turn status damage phase
- **Stacking**: Does not stack with multiple applications
- **Priority**: Processed alongside other status conditions
- **Switch immunity**: Switching out removes bleeding status
- **Fainting**: Bleeding can cause fainting if HP drops to 0

### Strategic Applications
- **Crit-focused builds**: Excellent on Pokemon with high crit ratios or crit-boosting moves
- **Pressure builds**: Bleeding provides consistent chip damage over time
- **Switching punishment**: Forces opponents to stay in or lose HP
- **Stall breaking**: Continuous damage helps break defensive strategies
- **Setup deterrent**: Makes it risky for opponents to set up against the user

### Competitive Viability
- **High-tier ability**: Combines immediate damage boost with lasting effects
- **Meta relevance**: Strong in formats where critical hits are prominent
- **Team synergy**: Works well with hazard damage and other chip sources
- **Versatility**: Effective on both physical and special attackers

### Common Users
- Pokemon with naturally high critical hit ratios
- Users of high-crit moves (Slash, Cross Chop, Stone Edge)
- Pokemon with access to Focus Energy or similar setup moves
- Offensive Pokemon that can benefit from both immediate and sustained damage

### Counters and Limitations
- **Crit immunity**: Abilities like Battle Armor or Shell Armor negate both effects
- **Status immunity**: Pokemon immune to status conditions avoid bleeding
- **Type immunity**: Rock and Ghost types cannot be inflicted with bleeding
- **Magic Guard**: Completely negates bleeding damage
- **Healing**: Aromatherapy, Heal Bell, and similar moves cure bleeding
- **Low crit rate**: Pokemon with poor critical hit chances rarely activate the ability

### Synergistic Moves and Items
- **High-crit moves**: Slash, Psycho Cut, Cross Chop, Stone Edge
- **Crit-boosting items**: Scope Lens, Razor Claw, Lucky Punch
- **Setup moves**: Focus Energy, Laser Focus
- **Multi-hit moves**: Pin Missile, Bullet Seed (multiple crit chances)
- **Always-crit moves**: Frost Breath, Storm Throw (guaranteed activation)

### Version History
- **Elite Redux exclusive**: Custom ability not found in official games
- **Design philosophy**: Combines offensive power with status pressure
- **Balance consideration**: Requires critical hits to function, preventing overpowered consistency

### Damage Calculations
```
Normal critical hit: 2.0x damage
To The Bone critical hit: 3.0x damage (2.0 x 1.5)
Bleeding damage per turn: Target Max HP ÷ 16 (minimum 1)

Example with 400 HP target:
- Normal crit with 100 BP move: ~200 damage
- To The Bone crit: ~300 damage
- Bleeding per turn: 25 damage
```

### Notable Interactions
- **Sniper stacking**: If a Pokemon somehow has both abilities, effects would stack to 2.25x crit damage
- **Life Orb**: Bleeding damage is not boosted by Life Orb
- **Weather**: Bleeding damage is not affected by weather conditions
- **Abilities**: Can trigger other on-damage abilities when bleeding damage is taken