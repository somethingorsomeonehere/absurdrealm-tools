---
id: 266
name: As One Ice Rider
status: reviewed
character_count: 141
---

# As One Ice Rider - Ability ID 266

## In-Game Description
"Unnerve + Chilling Neigh."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all opposing Pokemon from consuming held items. Raise Attack by one stage when the user knocks out an opponent with a direct attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

As One (Ice Rider) is a legendary signature ability that combines the effects of two separate abilities: Unnerve and Chilling Neigh. This creates a unique dual-effect ability that provides both defensive utility and offensive momentum.

### Core Components

#### Unnerve Component
- **Effect**: Prevents all opposing Pokemon from consuming their held items during battle
- **Scope**: Affects all enemies on the field simultaneously  
- **Items Blocked**: All consumable items including berries, herbs, seeds, Focus Sash, Eject Button
- **Duration**: Active as long as the Pokemon remains on the field

#### Chilling Neigh Component  
- **Effect**: Raises Attack by one stage (+50%) when knocking out an opponent
- **Trigger**: Must directly defeat an enemy with an attacking move
- **Stacking**: Multiple KOs provide cumulative Attack boosts (up to +6 maximum)
- **Timing**: Activates immediately after target faints

### Implementation Details

The ability is implemented as a unified effect in `src/abilities.cc`:

```cpp
constexpr Ability AsOneIceRider = {
    .onEntry = +[](ON_ENTRY) -> int { return SwitchInAnnounce(B_MSG_SWITCHIN_ASONE); },
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK(ChillingNeigh.onBattlerFaints(DELEGATE_BATTLER_FAINTS))
        gBattleScripting.abilityPopupOverwrite = ABILITY_CHILLING_NEIGH;
        BattleScriptCall(BattleScript_AbilityPopUpStack);
        return NO_ANNOUNCE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
    .unnerve = TRUE,
};
```

### Special Properties
- **Unsuppressable**: Cannot be disabled by abilities like Neutralizing Gas
- **Randomizer Banned**: Excluded from random ability assignment
- **Special Announcement**: Custom switch-in message when entering battle
- **Ability Popup Override**: Shows "Chilling Neigh" popup when the Attack boost triggers

### Strategic Applications

#### Offensive Benefits
- **Snowball Potential**: Each KO makes subsequent KOs easier with higher Attack
- **Late-Game Cleanup**: Excels at sweeping weakened teams
- **Choice Item Synergy**: Works well with Choice Band for initial KO power
- **Multi-KO Scenarios**: Particularly powerful against multiple weak opponents

#### Defensive Benefits  
- **Item Denial**: Prevents defensive berries from saving opponents
- **Focus Sash Nullification**: Ensures clean OHKOs on frail setup sweepers
- **Setup Prevention**: Blocks stat-boosting berries during opponent setup
- **Double Battle Control**: Affects both opponents simultaneously

### Competitive Interactions

#### Synergistic Elements
- **Physical Movesets**: Maximizes the Attack boost value
- **High Base Attack**: Amplifies the percentage increase from stat boosts  
- **Priority Moves**: Helps secure KOs to trigger the ability
- **Coverage Moves**: Ensures ability to hit diverse opponent types

#### Counters and Limitations
- **Status Moves**: Cannot trigger Attack boost from indirect damage
- **Substitute**: Blocks the KO effect if opponent uses Substitute
- **Defensive Walls**: High-HP opponents may survive even with Attack boosts
- **Speed Control**: Slower speed may prevent multiple KO opportunities

### Related Abilities
- **As One (Shadow Rider)**: Sister ability combining Unnerve + Grim Neigh (Special Attack boost)
- **Crowned King**: Combines all three effects (Unnerve + both Neigh abilities)
- **Individual Components**: Can be compared to standalone Unnerve (#127) and Chilling Neigh (#264)

### Pokemon Association
As One (Ice Rider) is typically associated with Calyrex's Ice Rider form in official games, representing the fusion of the King of Bountiful Harvests with Glastrier, the Wild Horse Pokemon. The combination reflects both the regal intimidation (Unnerve) and the fierce charging power (Chilling Neigh) of this legendary fusion.

### Code Location
- Defined in `src/abilities.cc` as `constexpr Ability AsOneIceRider`
- Listed in ability mapping at ID 266 (ABILITY_AS_ONE_ICE_RIDER)  
- Description stored in `proto/AbilityList.textproto`
- Switch-in message defined as `B_MSG_SWITCHIN_ASONE`