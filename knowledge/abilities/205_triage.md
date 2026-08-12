---
id: 205
name: Triage
status: reviewed
character_count: 231
---

# Triage - Ability ID 205

## In-Game Description
"Moves that have a healing effect gain +3 priority."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Triage grants +3 priority to most healing moves. Includes draining moves like Giga Drain, and delayed healing moves like Wish. Does not work with  Aqua Ring, Grassy Terrain, Ingrain, Leech Seed, Pain Split, Present, or Pollen Puff.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Priority Boost**: All moves with healing effects receive +3 priority
- **Priority Bracket**: +3 priority places healing moves in the same bracket as Fake Out and First Impression
- **Activation**: Automatic when using any move that has a healing effect

### Technical Implementation
```cpp
constexpr Ability Triage = {
    .onPriority = +[](ON_PRIORITY) -> int {
        CHECK(IsHealingMoveEffect(gBattleMoves[move].effect))
        return 3;
    },
};
```

### Complete List of Affected Move Effects
Based on `IsHealingMoveEffect()` function:
- **EFFECT_ABSORB**: Giga Drain, Mega Drain, Leech Life, Drain Punch, etc.
- **EFFECT_MORNING_SUN**: Morning Sun (weather-dependent healing)
- **EFFECT_MOONLIGHT**: Moonlight (weather-dependent healing) 
- **EFFECT_RESTORE_HP**: Recover, Slack Off, Milk Drink, Soft-Boiled
- **EFFECT_REST**: Rest (full heal + sleep)
- **EFFECT_ROOST**: Roost (heal + temporary Flying type removal)
- **EFFECT_WISH**: Wish (delayed healing)
- **EFFECT_HEALING_WISH**: Healing Wish (sacrifice for team heal)
- **EFFECT_REVIVAL_BLESSING**: Revival Blessing (revive teammate)
- **EFFECT_SOFTBOILED**: Soft-Boiled variants
- **EFFECT_SYNTHESIS**: Synthesis (weather-dependent healing)
- **EFFECT_SHORE_UP**: Shore Up (Ground/Rock terrain boost)
- **EFFECT_JUNGLE_HEALING**: Jungle Healing (team status cure)
- **EFFECT_HEAL_PULSE**: Heal Pulse (heal target)
- **EFFECT_MATCHA_GOTCHA**: Matcha Gotcha (damage + heal)
- **EFFECT_STRENGTH_SAP**: Strength Sap (heal + Attack drop)
- **EFFECT_DRAIN_BRAIN**: Custom draining move

### Priority System Context
- **+4 Priority**: Protect, Detect, other protection moves
- **+3 Priority**: Fake Out, First Impression, **Triage-boosted healing moves**
- **+2 Priority**: Extreme Speed, some priority moves
- **+1 Priority**: Quick Attack, Bullet Punch, most priority moves
- **0 Priority**: Normal moves

### Interactions with Other Abilities/Mechanics
- **Prankster**: Does not stack - Triage overrides for healing moves
- **Gale Wings**: Does not stack - each ability only affects specific move types
- **Heal Block**: Triage still grants priority, but moves will fail if blocked
- **Choice Items**: Priority boost applies even when locked into healing moves
- **Magic Bounce**: Priority boost applies before Magic Bounce reflection

### Strategic Implications
- **Defensive Pivoting**: Makes bulky Pokemon extremely hard to revenge kill
- **Stall Breaking**: High-priority recovery can outlast opposing offense
- **Support Role**: Priority Heal Pulse and team healing becomes extremely valuable
- **Revenge Prevention**: Nearly impossible to revenge kill with priority healing

### Example Damage Calculations
Priority healing with Triage can completely change battle dynamics:
- Comfey with +3 priority Draining Kiss can heal while dealing damage
- Meganium with +3 priority Giga Drain becomes nearly impossible to KO
- Audino with +3 priority Wish can guarantee healing for teammates

### Common Users in Elite Redux
- **Comfey**: Natural Triage user, excellent with Draining Kiss
- **Meganium**: As innate ability, pairs with Grassy Surge for healing synergy
- **Mega Meganium**: Enhanced bulk with priority healing
- **Audino**: Support role with priority team healing
- **Mega Audino**: Defensive wall with priority recovery
- **Blissey**: Ultimate special wall with priority healing
- **Chansey**: Eviolite tank with priority recovery
- **Dolliv/Arboliva**: Olive-themed healers with priority recovery

### Competitive Usage Notes
- **Tier Impact**: Makes defensive Pokemon significantly more viable
- **Team Synergy**: Excellent on stall and balance teams
- **Speed Control**: Eliminates need for speed investment on healers
- **Revenge Killing**: Makes revenge killing Triage users extremely difficult

### Counters
- **Taunt**: Prevents use of status healing moves
- **Heal Block**: Completely shuts down healing moves
- **Encore**: Can lock into non-healing moves
- **Strong Priority**: Higher priority attacks (though rare at +4)
- **Multi-hit Moves**: Can break through Substitute + healing strategies

### Synergies
- **Leftovers**: Passive healing complements active healing
- **Regenerator**: Additional healing when switching out
- **Magic Guard**: Prevents indirect damage while healing
- **Grassy Terrain**: Boosts Grass-type healing moves and provides passive healing
- **Substitute**: Priority healing can easily maintain Substitute

### Version History
- Introduced in Generation VII (Sun/Moon)
- Originally exclusive to Comfey
- Elite Redux: Expanded to multiple Pokemon as regular or innate ability
- Priority value consistent across all implementations (+3)