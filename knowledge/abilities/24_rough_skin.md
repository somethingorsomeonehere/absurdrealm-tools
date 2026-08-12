---
id: 24
name: Rough Skin
status: reviewed
character_count: 109
---

# Rough Skin - Ability ID 24

## In-Game Description
"Enemies lose 1/8 of max HP if they use a contact move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Damages attackers using contact moves for 1/8 of their max HP. Activates on every hit for multihitting moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Rough Skin inflicts damage on any opponent that hits the ability holder with a contact move. The damage is calculated as 1/8 (12.5%) of the attacker's maximum HP, with a minimum of 1 HP damage.

### Technical Implementation
```cpp
constexpr Ability RoughSkin = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK_NOT(IsMagicGuardProtected(attacker))
        CHECK(IsMoveMakingContact(move, attacker))
        gBattleMoveDamage = gBattleMons[attacker].maxHP / 8;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        PREPARE_ABILITY_BUFFER(gBattleTextBuff1, ability);
        BattleScriptCall(BattleScript_IronBarbsActivates);
        return TRUE;
    },
};
```

### Activation Conditions
1. **Contact requirement**: Only triggers on moves flagged as making contact
2. **On-hit effects must apply**: Certain conditions can prevent activation
3. **Defender must survive**: No activation if knocked out by the attack

### Protection and Immunities
- **Magic Guard**: Completely prevents Rough Skin damage
- **Long Reach**: Allows contact moves without triggering Rough Skin
- **Protective Pads**: Item that prevents contact ability effects

### Related Abilities
- **Iron Barbs**: Identical functionality (`.onDefender = RoughSkin.onDefender`)
- **Poison Quills**: Combines Rough Skin damage with Poison Point's poison chance

### Damage Calculation Examples
- 100 HP attacker: Takes 12 damage
- 300 HP attacker: Takes 37 damage  
- 400 HP attacker: Takes 50 damage
- 7 HP attacker: Takes 1 damage (minimum)

### Strategic Implications
- **Anti-physical**: Deters physical attackers and contact move users
- **Chip damage**: Accumulates significant damage over multiple hits
- **Multi-hit punishment**: Each hit of a multi-hit move triggers separately
- **No accuracy check**: Damage is guaranteed if conditions are met

### Common Users
- Galarian Meowth (changeable ability option)
- Various shark and rough-skinned Pokemon
- Often found on defensive Pokemon as innate ability

### Synergies
- **Rocky Helmet**: Stacks for 1/6 total damage (18.75%)
- **Substitute**: Sub takes hit but Rough Skin still activates
- **Counter/Mirror Coat**: Can use both for massive retaliation
- **Defensive stats**: High defense encourages more contact attempts

### Counters
- Special attackers (no contact)
- Magic Guard ability
- Long Reach ability  
- Protective Pads item
- Non-contact physical moves (Earthquake, Rock Slide)

### Competitive Usage Notes
Rough Skin excels on bulky physical walls that can take multiple hits. The guaranteed damage adds up quickly, especially against Pokemon that rely on weaker multi-hit moves or U-turn for momentum. It's particularly effective in formats where physical attackers are common.

### Version History
Rough Skin has maintained consistent mechanics since its introduction, always dealing 1/8 max HP damage to contact move users. The addition of items and abilities that interact with contact moves has created more counterplay options over time.