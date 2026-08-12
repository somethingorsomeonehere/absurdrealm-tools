---
id: 125
name: Sheer Force
status: reviewed
character_count: 279
---

# Sheer Force - Ability ID 125

## In-Game Description
"Exchanges added effects on its moves for 1.3x more power."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Removes most beneficial secondary effects after landing attacks in exchange for a 1.3x boost. Notably prevents Life Orb recoil when using these moves. Removable effects include reducing the target's stats, increasing the user's stats, inflicting status on a target and flinching.

## Detailed Mechanical Explanation
*For Discord/reference use*

**SHEER FORCE** is a power-boosting ability that trades secondary move effects for increased damage output.

### Activation Mechanics:
- **Trigger**: Affects moves that have the FLAG_SHEER_FORCE_BOOST flag
- **Power Boost**: 1.3x damage multiplier applied via onOffensiveMultiplier hook
- **Effect Removal**: Completely removes all secondary effects from boosted moves
- **No Announcement**: Ability works silently without battle message

### Technical Implementation:
```c
constexpr Ability SheerForce = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].flags & FLAG_SHEER_FORCE_BOOST) MUL(1.3);
        },
};
```

### Effect Removal Mechanics:
- **TestSheerForceFlag()**: Function checks if battler has Sheer Force AND move has boost flag
- **Prevention**: Blocks secondary effects in battle script commands when TestSheerForceFlag returns TRUE
- **Scope**: Removes ALL additional effects - status conditions, stat changes, healing, etc.

### Affected Move Examples:
1. **Elemental Punches**: Fire Punch (no burn), Ice Punch (no frostbite), Thunder Punch (no paralysis)
2. **Special Attacks**: Flamethrower (no burn), Ice Beam (no freeze), Thunderbolt (no paralysis)
3. **Stat-Changing Moves**: Rock Slide (no flinch), Psychic (no SpDef drop), Crunch (no Def drop)
4. **Multi-Effect Moves**: Ancient Power (no stat boosts), Silver Wind (no stat boosts)

### Moves NOT Affected:
- Moves with `no_sheer_force: true` flag (rare exceptions)
- Moves with only primary effects (no secondary effects to remove)
- Status moves without damage components

### Item Interactions:
1. **Life Orb**: 
   - **Power**: Still receives 1.3x Life Orb damage boost
   - **Recoil**: NO recoil damage taken (TestSheerForceFlag prevents it)
   - **Code**: `REQUIRE_NOT(TestSheerForceFlag(gBattlerAttacker, gCurrentMove))` in Life Orb recoil
   - **Result**: Effective 1.69x damage boost (1.3 x 1.3) with no drawbacks

2. **Other Items**: Works normally with type-boosting items, Choice items, etc.

### Competitive Applications:
- **Nidoking/Nidoqueen**: Classic Sheer Force users with wide movepool
- **Movesets**: Prioritize moves with secondary effects over those without
- **Life Orb Synergy**: Incredible damage output with no Life Orb recoil
- **Coverage Moves**: Earth Power, Sludge Wave, Ice Beam all get boosted

### Strategic Considerations:
- **Move Selection**: Choose moves with secondary effects over similar moves without
- **Item Choice**: Life Orb is often optimal for maximum damage output
- **Trade-offs**: Lose utility effects like burns/freezes for raw power
- **Wall Breaking**: Excellent for breaking through defensive Pokemon

### Notable Pokemon:
- Nidoking, Nidoqueen (classic users)
- Exploud (special attacker with wide movepool)
- Various Pokemon in Elite Redux's expanded ability system

### Version History:
- Gen 5: Introduced with 1.3x multiplier
- Elite Redux: Maintains standard 1.3x boost, expanded to more Pokemon through multi-ability system