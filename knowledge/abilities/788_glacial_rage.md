---
id: 788
name: Glacial Rage
status: reviewed
character_count: 150
---

# Glacial Rage - Ability ID 788

## In-Game Description
"Triggers 50 BP Blizzard after using a Ice-type move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After using an Ice-type move, the user follows up with a 50 BP Blizzard (Ice, 85% accuracy, hits both opponents, 20% frostbite chance. Weather-based). 

## Detailed Mechanical Explanation
*For Discord/reference use*

Glacial Rage is an offensive ability that triggers after the user successfully uses any Ice-type move. The ability follows the "rage" pattern established by similar abilities like Volcano Rage (Fire-type -> Eruption) and High Tide (Water-type -> Surf).

**Mechanical Details:**
- **Trigger Condition**: Successfully using any Ice-type move (moveType == TYPE_ICE)
- **Follow-up Move**: Blizzard with 50 BP (overriding the normal 110 BP)
- **Target**: Both opponents in double battles (BOTH target type)
- **Accuracy**: 85% (standard Blizzard accuracy)
- **Additional Effects**: 20% frostbite chance from Blizzard's natural effect
- **Weather Interaction**: Blizzard has perfect accuracy in hail/snow weather

**Strategic Applications:**
1. **Multi-Hit Potential**: Every Ice move becomes a potential 2-hit combo
2. **Coverage Enhancement**: Provides consistent Ice-type pressure after any Ice attack
3. **Status Pressure**: Each follow-up Blizzard has a 20% chance to inflict frostbite
4. **Double Battle Dominance**: Can hit both opponents with the follow-up attack
5. **Weather Synergy**: Devastating in hail/snow conditions with perfect accuracy

**Notable Interactions:**
- Works with any Ice-type move, including status moves like Haze (if they're Ice-type)
- The follow-up Blizzard can trigger abilities like Ice Body on opponents
- In hail/snow weather, the follow-up Blizzard has 100% accuracy
- The reduced 50 BP still benefits from STAB and other damage modifiers
- Can potentially trigger multiple times in one turn with multi-hit Ice moves

**Found On:**
- Mega Glalie (Innate Ability)

This ability transforms Ice-type attackers into consistent offensive threats, making every Ice move potentially devastating through the guaranteed follow-up attack and frostbite pressure.