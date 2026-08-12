---
id: 289
name: Growing Tooth
status: reviewed
character_count: 102
---

# Growing Tooth - Ability ID 289

## In-Game Description
"Raises Attack by one stage after using a biting move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Growing Tooth boosts the user's Attack by one stage whenever they successfully hit with a biting move. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Growing Tooth activates whenever the user successfully uses a move with the `FLAG_STRONG_JAW_BOOST` flag. Upon successful use, it raises the user's Attack stat by one stage (+50% Attack).

### Activation Conditions
- Must successfully use a biting move (move must have `FLAG_STRONG_JAW_BOOST`)
- Triggers only when `ShouldApplyOnHitAffect` returns true
- Activates after damage calculation but before the move fully resolves
- The stat boost must be possible (not already at +6 Attack)

### Technical Implementation
```cpp
constexpr Ability GrowingTooth = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)
        CHECK(ChangeStatBuffs(battler, 1, STAT_ATK, MOVE_EFFECT_AFFECTS_USER, NULL))

        gBattleScripting.battler = battler;
        BattleScriptCall(BattleScript_AttackBoostActivates);
        return TRUE;
    },
};
```

### Complete List of Affected Moves
**Basic Biting Moves:**
- Bite
- Hyper Fang
- Super Fang
- Crunch

**Elemental Fang Moves:**
- Thunder Fang
- Ice Fang 
- Fire Fang
- Poison Fang

**Specialized Biting Moves:**
- Aqua Fang
- Bug Bite
- Psychic Fangs
- Jaw Lock
- Pluck
- Leech Life

**Elite Redux Custom Moves:**
- Bolt Beak
- Deathroll
- Draconic Fangs
- Fertile Fangs
- Fishious Rend
- Iron Fangs
- Jagged Fangs
- Kilobite
- Lovely Bite
- Rip and Tear
- Shadow Fangs
- Snap Trap
- Tectonic Fangs
- Terror Charge

### Interactions with Other Abilities/Mechanics
- **Strong Jaw**: Stacks multiplicatively - Strong Jaw boosts damage, Growing Tooth boosts future Attack
- **Sheer Force**: If user has Sheer Force, moves lose secondary effects but Growing Tooth still activates
- **Moxie**: Both abilities can trigger from the same KO, providing +2 Attack total
- **Choice Items**: Growing Tooth can still activate while locked into a Choice item
- **Substitute**: Activates even when attacking through Substitute

### Strategic Implications
- **Snowball Potential**: Each successful biting move makes subsequent attacks stronger
- **Early Game Setup**: Weak biting moves like Bite become setup tools
- **Late Game Power**: Strong moves like Crunch become even more devastating after boosts
- **Multi-hit Consideration**: Each hit of multi-hit biting moves can potentially trigger (though most biting moves are single-hit)

### Example Damage Calculations
Assuming 100 base Attack, neutral nature, level 50:
- **Base Attack**: 120 (no boosts)
- **After 1 Growing Tooth**: 180 (+50%)
- **After 2 Growing Tooth**: 240 (+100%)
- **After 3 Growing Tooth**: 300 (+150%)

### Common Users
**Natural Learners** (Pokemon that learn multiple biting moves):
- Mightyena line (Bite, Crunch, Thunder/Ice/Fire Fang)
- Crobat line (Bite, Crunch, Leech Life)
- Sharpedo line (Bite, Crunch, Aqua Fang)
- Tyranitar line (Bite, Crunch)

**Synergistic Pokemon**:
- Physical attackers with diverse movepools
- Pokemon with access to setup moves + biting moves
- Fast sweepers that can capitalize on Attack boosts

### Competitive Usage Notes
- **Tier Placement**: Strong on physical attackers with good Speed
- **Team Role**: Physical sweeper/wallbreaker
- **Preferred Formats**: Singles > Doubles (easier to get multiple boosts)
- **Item Synergy**: Life Orb, Choice Band, Muscle Band

### Counters
- **Intimidate**: Reduces Attack boosts' effectiveness
- **Burn**: Halves physical damage output
- **Physical Walls**: Resist boosted attacks
- **Priority Moves**: Revenge kill before setup complete
- **Taunt**: Prevents setup if relying on non-attacking moves first

### Synergies  
- **Strong Jaw**: Perfect partner ability for maximum biting move effectiveness
- **Technician**: Boosts weak biting moves used for setup
- **Speed Boost**: Ensures ability to capitalize on Attack boosts
- **Adaptability**: Enhances STAB biting moves further

### Version History
- **Elite Redux**: Custom ability implementation
- **Mechanic**: Based on Strong Jaw's move flagging system
- **Balance**: Moderate power level - requires successful hits to build up