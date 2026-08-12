---
id: 160
name: Iron Barbs
status: reviewed
character_count: 109
---

# Iron Barbs - Ability ID 160

## In-Game Description
"Enemies lose 1/8 of max HP if they use a contact move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Damages attackers using contact moves for 1/8 of their max HP. Activates on every hit for multihitting moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

Iron Barbs is a defensive ability that punishes physical attackers who use contact moves. It functions identically to Rough Skin, sharing the same implementation code.

### Core Mechanics
- **Trigger Condition**: Activates when the Iron Barbs user is hit by a move that makes contact
- **Damage Calculation**: Deals exactly 1/8 of the attacker's maximum HP as damage
- **Minimum Damage**: Always deals at least 1 HP damage, even if 1/8 calculation rounds to 0
- **Damage Type**: The retaliation damage is treated as ability damage, not move damage

### Implementation Details
```cpp
constexpr Ability IronBarbs = {
    .onDefender = RoughSkin.onDefender,  // Uses identical implementation to Rough Skin
};

// RoughSkin implementation (shared with Iron Barbs):
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(attacker))
    CHECK_NOT(IsMagicGuardProtected(attacker))  // Magic Guard blocks damage
    CHECK(IsMoveMakingContact(move, attacker))  // Only contact moves trigger
    gBattleMoveDamage = gBattleMons[attacker].maxHP / 8;  // 1/8 max HP
    if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;    // Minimum 1 damage
    PREPARE_ABILITY_BUFFER(gBattleTextBuff1, ability);
    BattleScriptCall(BattleScript_IronBarbsActivates);
    return TRUE;
},
```

### Contact Moves That Trigger Iron Barbs
Iron Barbs triggers on any move with the contact flag, including but not limited to:
- **Physical attacks**: Tackle, Body Slam, Earthquake, Close Combat, Flare Blitz
- **Status moves**: Thunder Wave (when making contact), Nuzzle
- **Multi-hit moves**: Each hit triggers Iron Barbs separately
- **Priority moves**: Quick Attack, Mach Punch, Bullet Punch
- **Recoil moves**: Double-Edge, Take Down, Flare Blitz

### Moves That Do NOT Trigger Iron Barbs
- **Projectile moves**: Shadow Ball, Flamethrower, Thunderbolt
- **Punching moves**: Fire Punch, Ice Punch, Thunder Punch (these DO make contact)
- **Long-range attacks**: Surf, Earthquake, Air Slash
- **Status moves without contact**: Toxic, Will-O-Wisp, Thunder Wave (non-contact)

### Interactions with Other Abilities and Effects

**Magic Guard Interaction**:
- Magic Guard completely prevents Iron Barbs damage
- The attacker takes no retaliation damage if they have Magic Guard
- This is explicitly checked in the code with `CHECK_NOT(IsMagicGuardProtected(attacker))`

**Rocky Helmet Interaction**:
- Iron Barbs and Rocky Helmet stack for 1/4 max HP total damage (1/8 + 1/6)
- Both activate separately and independently

**Substitute Interaction**:
- Iron Barbs activates even if the attack hits a Substitute
- The attacker still takes retaliation damage

**Multi-Hit Moves**:
- Each individual hit of multi-hit moves triggers Iron Barbs
- A 5-hit move would trigger Iron Barbs 5 times for massive retaliation damage

### Damage Calculation Examples

**Example 1**: Garchomp (404 max HP) uses Earthquake against Iron Barbs user
- Calculation: 404 ÷ 8 = 50.5 to 50 HP damage to Garchomp
- Note: Earthquake doesn't make contact, so Iron Barbs wouldn't actually trigger

**Example 2**: Garchomp uses Dragon Claw against Iron Barbs user
- Calculation: 404 ÷ 8 = 50.5 to 50 HP damage to Garchomp
- Dragon Claw makes contact, so Iron Barbs triggers

**Example 3**: Shedinja (1 max HP) uses Shadow Sneak against Iron Barbs user
- Calculation: 1 ÷ 8 = 0.125 to rounds to 0, but minimum is 1
- Shedinja takes 1 HP damage and faints

**Example 4**: Magic Guard Alakazam uses Psycho Cut against Iron Barbs user
- Magic Guard blocks the retaliation damage
- Alakazam takes 0 damage despite Psycho Cut making contact

### Strategic Implications

**Offensive Usage**:
- Punishes physical attackers heavily
- Particularly effective against multi-hit move users
- Can KO low-HP attackers with retaliation damage

**Defensive Synergies**:
- **Rocky Helmet**: Stack for maximum retaliation (1/4 max HP total)
- **Spiky Shield**: Combines blocking with additional retaliation
- **High Defense**: Survive the initial attack to ensure retaliation triggers

**Common Users in Elite Redux**:
Iron Barbs appears on many defensive Steel-types and spiky Pokemon:
- Forretress, Ferrothorn, Chesnaught
- Various custom Steel/Ground and Steel/Grass types
- Often paired with other defensive abilities as innate abilities

### Competitive Considerations

**Strengths**:
- Passive damage without investment
- Deters physical attackers
- Excellent on defensive pivots and walls
- Can revenge-kill weakened opponents

**Counters**:
- **Magic Guard users**: Complete immunity to retaliation
- **Special attackers**: Most special moves don't make contact
- **Long-range physical moves**: Earthquake, Rock Slide, etc.
- **Healing moves**: Can recover the retaliation damage

**Team Support**:
- Entry hazards amplify the punishment for switching
- Wish support helps the Iron Barbs user stay healthy
- Paralysis support slows down physical attackers

### Version History
Iron Barbs was introduced in Generation V and has remained largely unchanged. In Elite Redux, it maintains its original mechanics while being distributed to additional Pokemon as both a regular and innate ability, making it more prevalent in competitive play.

The ability is considered one of the most reliable forms of passive damage in the game, with its guaranteed minimum damage ensuring it's never completely useless.