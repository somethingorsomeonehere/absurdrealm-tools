---
id: 328
name: Overwhelm
status: reviewed
character_count: 155
---

# Overwhelm - Ability ID 328

## In-Game Description
"Hits Fairies with Dragon moves. Immune to Intimidate and Scare."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Allows Dragon-type moves to hit Fairy-type Pokemon for normal damage instead of having no effect. Additionally, the user is immune to Intimidate and Scare.

## Mechanical Analysis

### Type Effectiveness Override
- **Target**: Dragon vs Fairy type matchup
- **Normal Interaction**: Dragon moves have 0x effectiveness (no effect) against Fairy types
- **With Overwhelm**: Dragon moves deal 1.0x effectiveness (normal damage) against Fairy types
- **Implementation**: Uses `onTypeEffectiveness` callback to modify damage calculation

### Immunity Effects
- **Taunt Immunity**: `tauntImmune = TRUE`
- **Covers**: Intimidate, Scare, and other similar stat-lowering entry abilities
- **Mechanism**: Prevents the ability from being affected by mental/intimidation-based effects

## Code Implementation

```cpp
constexpr Ability Overwhelm = {
    .onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
        CHECK(moveType == TYPE_DRAGON) 
        CHECK(defType == TYPE_FAIRY) 
        CHECK_NOT(*mod) 
        *mod = UQ_4_12(1.0);
        return TRUE;
    },
    .tauntImmune = TRUE,
};
```

## Strategic Implications

### Offensive Benefits
- Dragon-type attackers can now hit Fairy-type defenders
- Removes Fairy's immunity to Dragon moves completely
- Enables Dragon-type coverage against Fairy walls

### Defensive Benefits
- Immune to Intimidate (prevents Attack reduction)
- Immune to Scare (prevents stat reduction)
- Maintains offensive presence against intimidation tactics

### Competitive Impact
- High value against Fairy-heavy teams
- Counters common Intimidate users
- Particularly effective on Dragon-type attackers

## Notable Interactions

### Type Chart Changes
- **Hydreigon vs Clefable**: Can now hit with Dragon Pulse
- **Garchomp vs Togekiss**: Dragon Rush becomes viable
- **Salamence vs Sylveon**: Dragon Claw hits for normal damage

### Ability Counters
- Does not affect other type immunities (Ghost vs Normal, etc.)
- Only specifically targets Dragon vs Fairy interaction
- Intimidate immunity is passive and always active

## Related Abilities
- **Scrappy**: Similar concept but for Normal/Fighting vs Ghost
- **Turboblaze/Teravolt**: Ignore all abilities (broader scope)
- **Inner Focus**: Immunity to flinching (similar mental resistance theme)

## Pokemon That Learn This Ability
*Note: Check SpeciesList.textproto for current distribution*

## Battle AI Considerations
- AI should prioritize Dragon moves against Fairy types when this ability is present
- Intimidate users become less effective against this ability
- Strategic switching patterns may change in competitive play