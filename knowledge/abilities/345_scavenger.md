---
id: 345
name: Scavenger
status: reviewed
character_count: 102
---

# Scavenger - Ability ID 345

## In-Game Description
"Dealing a KO heals 1/4 of this Pokemon's max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When this Pokemon defeats an opponent with a direct hit, it immediately regains 25% of its maximum HP. 

## Detailed Mechanical Explanation

### Basic Information
- **Name**: Scavenger
- **ID**: 345 (ABILITY_SCAVENGER)

### Mechanical Analysis

### Implementation Details
- **Trigger**: `onBattlerFaints` with `APPLY_ON_ATTACKER`
- **Condition**: Activates when the Pokemon with Scavenger knocks out an opponent
- **Effect**: Heals 25% of the user's maximum HP
- **Battle Script**: `BattleScript_HandleSoulEaterEffect`
- **Shared Implementation**: Uses `SoulEater.onBattlerFaints`

### Code Implementation
```cpp
// Location: src/abilities.cc, line 3652
constexpr Ability Scavenger = {
    .onBattlerFaints = SoulEater.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

The Scavenger ability shares its implementation with Soul Eater (#331), using the same healing function:

```cpp
// Soul Eater implementation (referenced by Scavenger)
constexpr Ability SoulEater = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler));
        CHECK(CanBattlerHeal(battler));
        BattleScriptCall(BattleScript_HandleSoulEaterEffect);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

### Battle Script
```assembly
// Location: data/battle_scripts_1.s, line 11846
BattleScript_HandleSoulEaterEffect::
    tryhealpercenthealth BS_STACK_1, 25, BattleScript_Return
BattleScript_HandleSoulEaterEffect_AfterHeal:
    orword gHitMarker, HITMARKER_IGNORE_SUBSTITUTE
    healthbarupdate BS_STACK_1
    datahpupdate BS_STACK_1
    printstring STRINGID_STACKREGAINEDHEALTH
    waitmessage B_WAIT_TIME_LONG
    return
```

## Strategic Analysis

### Strengths
- **Sustainable Sweeping**: Provides excellent longevity for offensive Pokemon
- **Momentum Building**: Each victory makes subsequent battles easier
- **Reliable Trigger**: Activates on any knockout, regardless of move type
- **Significant Recovery**: 25% HP healing is substantial and often decisive
- **Multi-Battle Advantage**: Excels in scenarios with multiple opponents

### Limitations
- **KO Dependency**: Requires securing knockouts to provide any benefit
- **Full HP Restriction**: Cannot heal beyond maximum HP
- **No Defensive Value**: Provides no protection against being KO'd
- **Single Battle Limitation**: Less valuable in 1v1 scenarios

### Tactical Applications
- **Offensive Sweepers**: Ideal for fast, powerful Pokemon designed to eliminate multiple opponents
- **Late-Game Dominance**: Becomes increasingly powerful as battles progress
- **Endurance Strategies**: Excellent for prolonged battles and battle facilities
- **Multi-Battle Formats**: Particularly effective in Double, Triple, and Rotation battles
- **Revenge Killing**: Helps secure follow-up KOs after trading with an opponent

## Pokemon with Scavenger
Based on the codebase analysis, Scavenger appears as both a regular ability and an innate ability on various Pokemon. The ability is distributed across different species, often fitting thematically with scavenging or predatory Pokemon.

## Related Abilities
Scavenger shares its implementation with several other healing-on-KO abilities:

### Direct Siblings (Same Implementation)
- **Soul Eater (#331)**: Identical effect and implementation
- **Hunter's Horn (#464)**: Also uses `SoulEater.onBattlerFaints`
- **Jaws of Carnage (#438)**: Uses similar healing mechanism but with 50% HP recovery

### Thematic Relatives
- **Moxie (#153)**: Gains Attack boost on KO instead of healing
- **Beast Boost (#224)**: Raises highest stat on KO
- **Grim Neigh (#265)**: Raises Special Attack on KO

## Competitive Analysis

### Tier Placement
Scavenger is a **high-tier** ability for offensive Pokemon, particularly those with:
- High offensive stats
- Good Speed or priority moves
- Adequate bulk to survive hits
- Wide movepool coverage

### Synergistic Strategies
- **Life Orb**: Compensates for recoil damage through healing
- **Choice Items**: Maintains effectiveness across multiple KOs
- **Entry Hazards**: Helps secure more KOs for healing opportunities
- **Status Moves**: Sleep Powder, Thunder Wave to guarantee KOs

### Counters and Limitations
- **Sturdy/Focus Sash**: Prevents KOs and denies healing
- **Revenge Killers**: Fast Pokemon that can KO before Scavenger can heal
- **Priority Moves**: Bypass Speed advantage and potentially KO
- **Residual Damage**: Sandstorm, Spikes, etc. can wear down despite healing

## Technical Notes
- The ability uses `tryhealpercenthealth` with a 25% value in battle scripts
- Healing is subject to standard battle conditions (CanBattlerHeal check)
- The effect bypasses Substitute due to `HITMARKER_IGNORE_SUBSTITUTE`
- Displays the standard "Pokemon regained health!" message after healing
- Shared implementation means any changes to Soul Eater also affect Scavenger
- The ability is properly registered in the ability lookup table at line 9190 of abilities.cc

## Conclusion
Scavenger is a powerful sustain ability that rewards aggressive play and successful KOs. Its ability to maintain health through consecutive victories makes it particularly valuable for sweeping strategies and extended battles. The shared implementation with Soul Eater ensures consistent behavior across similar abilities, while the thematic name fits well with scavenging or predatory Pokemon that benefit from defeating their prey.