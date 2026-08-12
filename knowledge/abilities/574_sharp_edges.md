---
id: 574
name: Sharp Edges
status: reviewed
character_count: 109
---

# Sharp Edges - Ability ID 574

## In-Game Description
"1/6 HP damage when touched."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Damages attackers using contact moves for 1/6 of their max HP. Activates on every hit for multihitting moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

Sharp Edges is an enhanced version of Iron Barbs that deals more retaliation damage to physical attackers. While Iron Barbs and Rough Skin deal 1/8 maximum HP damage, Sharp Edges deals 1/6 maximum HP damage, making it significantly more punishing.

### Core Mechanics
- **Trigger Condition**: Activates when the Sharp Edges user is hit by a move that makes contact
- **Damage Calculation**: Deals exactly 1/6 of the attacker's maximum HP as damage (compared to 1/8 for Iron Barbs)
- **Minimum Damage**: Always deals at least 1 HP damage, even if 1/6 calculation rounds to 0
- **Damage Type**: The retaliation damage is treated as ability damage, not move damage

### Implementation Details
```cpp
constexpr Ability DoubleIronBarbs = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK_NOT(IsMagicGuardProtected(attacker))  // Magic Guard blocks damage
        CHECK(IsMoveMakingContact(move, attacker))  // Only contact moves trigger
        
        gBattleMoveDamage = gBattleMons[attacker].maxHP / 6;  // 1/6 max HP (vs 1/8 for Iron Barbs)
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;    // Minimum 1 damage
        PREPARE_ABILITY_BUFFER(gBattleTextBuff1, ability);
        BattleScriptCall(BattleScript_IronBarbsActivates);  // Uses same battle script as Iron Barbs
        return TRUE;
    },
};
```

### Contact Moves That Trigger Sharp Edges
Sharp Edges triggers on any move with the contact flag, including but not limited to:
- **Physical attacks**: Tackle, Body Slam, Close Combat, Flare Blitz, Dragon Claw
- **Status moves**: Thunder Wave (when making contact), Nuzzle
- **Multi-hit moves**: Each hit triggers Sharp Edges separately for devastating retaliation
- **Priority moves**: Quick Attack, Mach Punch, Bullet Punch
- **Recoil moves**: Double-Edge, Take Down, Flare Blitz

### Moves That Do NOT Trigger Sharp Edges
- **Projectile moves**: Shadow Ball, Flamethrower, Thunderbolt, Ice Beam
- **Long-range attacks**: Surf, Earthquake, Air Slash, Rock Slide
- **Status moves without contact**: Toxic, Will-O-Wisp, Thunder Wave (non-contact)
- **Special moves**: Most special attacks don't make contact

### Damage Comparison with Similar Abilities

**Sharp Edges vs Iron Barbs/Rough Skin**:
- **Sharp Edges**: 1/6 max HP damage (about16.67% max HP)
- **Iron Barbs/Rough Skin**: 1/8 max HP damage (12.5% max HP)
- **Difference**: Sharp Edges deals 33% more retaliation damage

### Interactions with Other Abilities and Effects

**Magic Guard Interaction**:
- Magic Guard completely prevents Sharp Edges damage
- The attacker takes no retaliation damage if they have Magic Guard
- This is explicitly checked in the code with `CHECK_NOT(IsMagicGuardProtected(attacker))`

**Rocky Helmet Interaction**:
- Sharp Edges and Rocky Helmet stack for massive retaliation damage
- Combined damage: 1/6 (Sharp Edges) + 1/6 (Rocky Helmet) = 1/3 max HP total
- This is significantly more punishing than Iron Barbs + Rocky Helmet (1/8 + 1/6 = 7/24 about 29.2%)

**Substitute Interaction**:
- Sharp Edges activates even if the attack hits a Substitute
- The attacker still takes retaliation damage

**Multi-Hit Moves**:
- Each individual hit of multi-hit moves triggers Sharp Edges
- A 5-hit move would trigger Sharp Edges 5 times, dealing 5/6 max HP damage total
- This makes multi-hit moves extremely dangerous to use against Sharp Edges users

### Damage Calculation Examples

**Example 1**: Garchomp (404 max HP) uses Dragon Claw against Sharp Edges user
- **Sharp Edges**: 404 / 6 = 67.33 to 67 HP damage to Garchomp
- **Iron Barbs**: 404 / 8 = 50.5 to 50 HP damage to Garchomp
- **Difference**: Sharp Edges deals 17 more damage (34% increase)

**Example 2**: Shedinja (1 max HP) uses Shadow Sneak against Sharp Edges user
- Calculation: 1 / 6 = 0.167 to rounds to 0, but minimum is 1
- Shedinja takes 1 HP damage and faints (same as Iron Barbs)

**Example 3**: Skill Link Cloyster uses Icicle Spear (5 hits) against Sharp Edges user
- Each hit: 251 / 6 = 41.83 to 41 HP damage per hit
- Total damage: 41 x 5 = 205 HP damage to Cloyster
- Cloyster effectively takes 205/251 = 81.7% of its max HP in retaliation

**Example 4**: Magic Guard Alakazam uses Psycho Cut against Sharp Edges user
- Magic Guard blocks the retaliation damage
- Alakazam takes 0 damage despite Psycho Cut making contact

### Strategic Implications

**Offensive Usage**:
- Extremely punishing to physical attackers
- Devastating against multi-hit move users
- Can single-handedly shut down contact-based physical sweepers
- More likely to KO attackers than Iron Barbs due to higher damage

**Defensive Synergies**:
- **Rocky Helmet**: Creates a 1/3 max HP retaliation combo
- **Spiky Shield**: Combines blocking with additional retaliation
- **High Defense**: Survive the initial attack to ensure retaliation triggers
- **Rough Skin**: Would theoretically stack for 1/6 + 1/8 = 7/24 max HP damage

**Team Support**:
- Entry hazards make switching even more costly for physical attackers
- Wish support helps the Sharp Edges user stay healthy to continue retaliating
- Paralysis support slows down contact-based sweepers

### Current Users in Elite Redux

Based on the codebase analysis, Sharp Edges appears as an innate ability on several Pokemon:
- **Defensive Steel-types**: Likely used on heavily armored Pokemon
- **Spiky/Thorny Pokemon**: Fitting thematically with sharp, dangerous exteriors
- **High-tier competitive Pokemon**: Often appears alongside other powerful innate abilities

Common ability combinations include:
- Sharp Edges + Self Repair (healing to offset damage taken)
- Sharp Edges + Quark Drive (stat boosts)
- Sharp Edges + Dual Wield (offensive pressure)

### Competitive Considerations

**Strengths**:
- **Highest retaliation damage**: 33% more than Iron Barbs
- **Passive damage without investment**: No need for moves or items
- **Deters physical attackers**: Makes contact moves much riskier
- **Excellent on defensive walls**: Punishes common physical threats
- **Multi-hit deterrent**: Completely shuts down multi-hit strategies

**Counters**:
- **Magic Guard users**: Complete immunity to retaliation (Alakazam, Clefable)
- **Special attackers**: Most special moves don't make contact
- **Long-range physical moves**: Earthquake, Rock Slide, Stone Edge
- **Healing moves**: Can recover the retaliation damage, though at significant cost
- **Status moves**: Non-contact status moves bypass retaliation

**Risk vs Reward**:
- Sharp Edges creates a much higher risk for using contact moves
- Physical attackers must consider whether the attack is worth potentially losing 16.67% max HP
- Multi-hit moves become nearly suicidal against Sharp Edges users

### Comparison to Other Retaliation Abilities

**Sharp Edges vs Iron Barbs**:
- **Damage**: 1/6 vs 1/8 max HP (33% more damage)
- **Usage**: Sharp Edges is rarer and more punishing
- **Strategic value**: Sharp Edges is significantly more deterrent

**Sharp Edges vs Rocky Helmet**:
- **Sharp Edges**: Ability-based, 1/6 max HP damage
- **Rocky Helmet**: Item-based, 1/6 max HP damage
- **Combined**: 1/3 max HP total retaliation damage

**Sharp Edges vs Aftermath**:
- **Sharp Edges**: Per-hit retaliation while alive
- **Aftermath**: One-time damage when KO'd (1/4 max HP)
- **Strategic role**: Different defensive strategies

### Version History

Sharp Edges (internally called "Double Iron Barbs") is an Elite Redux custom ability that enhances the Iron Barbs concept. It represents the logical evolution of contact punishment abilities, providing more meaningful retaliation against physical attackers.

The ability fills a specific niche in the Elite Redux metagame where physical attackers are extremely powerful, providing a strong defensive tool that can actually threaten offensive Pokemon. Its higher damage output makes it a genuine consideration for team building, both as a defensive tool and as something to play around when using physical attackers.

### Conclusion

Sharp Edges represents the pinnacle of contact punishment abilities in Elite Redux. Its 1/6 max HP retaliation damage makes it significantly more threatening than Iron Barbs, creating meaningful decision points for physical attackers. When combined with Rocky Helmet, it creates one of the most punishing defensive combinations in the game, dealing 33% max HP damage per contact move.

The ability is particularly effective in the Elite Redux environment where multi-hit moves and physical sweepers are common, providing a strong defensive answer to these strategies. However, it maintains clear counterplay through Magic Guard, special attacks, and non-contact moves, ensuring it remains balanced despite its power.