---
id: 88
name: Download
status: reviewed
character_count: 172
---

# Download - Ability ID 88

## In-Game Description
"Raises Atk/Sp. Atk by one stage depending on opponent."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When switching in, if the foe's Defense is higher than Special Defense, raise Special Attack by one stage. If Special Defense is higher or equal, raise Attack by one stage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**DOWNLOAD** is an entry ability that provides an adaptive offensive boost based on the opponent's defensive stats.

### Activation Mechanics:
- **Trigger**: On entry to battle (onEntry hook)
- **Target Analysis**: Examines the opposing Pokemon's Defense vs Special Defense
- **Stat Comparison**: Uses actual stat values including stat stage modifiers
- **Boost Applied**: +1 stage to either Attack or Special Attack

### Stat Comparison Logic:
1. **Target Selection**:
   - Primary: Direct opponent across from the user
   - Fallback: If primary target is fainted, checks partner's opponent
   - Fails if no valid target exists

2. **Defense Calculation**:
   - Compares Defense vs Special Defense including stat stages
   - Uses `GetHighestDefendingStatId` function with stat stages included
   - If Defense > Special Defense to Raises Special Attack
   - If Special Defense ≥ Defense to Raises Attack

3. **Boost Application**:
   - Standard +1 stat stage increase
   - Subject to normal stat stage limits (+6 maximum)
   - Triggers ability notification animation

### Technical Implementation:
```c
constexpr Ability Download = {
    .onEntry = +[](ON_ENTRY) -> int {
        gBattlerTarget = BATTLE_OPPOSITE(battler);
        if (!IsBattlerAlive(battler)) gBattlerTarget = BATTLE_PARTNER(gBattlerTarget);
        CHECK(IsBattlerAlive(battler))

        int stat = GetHighestDefendingStatId(gBattlerTarget, TRUE) == STAT_DEF ? STAT_SPATK : STAT_ATK;
        CHECK(ChangeStatBuffs(battler, 1, stat, MOVE_EFFECT_AFFECTS_USER, NULL))
        BattleScriptPushCursorAndCallback(BattleScript_AttackerAbilityStatRaiseEnd3);
        return TRUE;
    },
};
```

### Strategic Analysis Algorithm:
The ability performs a simple but effective analysis:
- **Mixed Attackers**: Download users typically have balanced offensive stats to utilize either boost
- **Counterintuitive Logic**: Targets with high Defense get hit by special attacks, and vice versa
- **Stat Stage Awareness**: Considers opponent's stat boosts/drops in calculation

### Interaction Rules:
- **Multiple Opponents**: In doubles, only analyzes the direct opponent, not both foes
- **Substitute**: Ignores substitutes and analyzes the actual Pokemon's stats
- **Transform/Illusion**: Analyzes the apparent Pokemon's stats (what's visible)
- **Clear Body/White Smoke**: Download's boost to the user is not prevented by opponent's abilities

### Common Download Users:
1. **Porygon Line**: 
   - Porygon2: Often uses Download as an innate ability
   - Porygon-Z: Traditional Download user with high mixed offenses

2. **Genesect**: 
   - Legendary Bug/Steel type with Download
   - Can run mixed sets effectively
   - Often paired with Techno Blast for coverage

### Competitive Applications:
1. **Lead Strategies**: Immediate offensive pressure with correct coverage
2. **Mixed Attackers**: Flexibility to hit from either offensive stat
3. **Pivot Roles**: Gain momentum with U-turn/Volt Switch after boost
4. **Setup Prevention**: Forces opponents to respect both offensive stats

### Synergistic Elements:
- **Items**: Life Orb, Choice Specs/Band (locks into one attack type)
- **Moves**: Mixed coverage moves, setup moves to further boost
- **Abilities**: In Elite Redux, pairs well with offensive innate abilities

### Counterplay:
- **Balanced Defenses**: Pokemon with equal Defense/Special Defense minimize Download's effectiveness
- **Priority Moves**: Strike before Download user can utilize their boost
- **Intimidate**: Neutralizes Attack boost if Download chooses physical
- **Weather/Terrain**: Environmental damage can pressure before attacks

### Version History:
- Gen 4: Introduced with Porygon-Z
- Gen 5: Given to Genesect
- Elite Redux: Available on various Pokemon as regular or innate ability