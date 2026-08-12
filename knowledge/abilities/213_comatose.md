---
id: 213
name: Comatose
status: reviewed
character_count: 190
---

# Comatose - Ability ID 213

## In-Game Description
"Can move, but is always asleep. Immune to status conditions."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Comatose considers the user as asleep for moves and statuses. The Pokemon can move normally and gains immunity to all status conditions. Cannot be copied or suppressed. Rest fails when used.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- Pokemon permanently appears asleep (displays sleep status icon)
- Can act normally every turn without needing to "wake up"
- Complete immunity to all status conditions
- Status immunity is "unsuppressable" - cannot be disabled by abilities like Mold Breaker
- Automatically removes existing status conditions when ability activates

### Activation Conditions
- Always active when the Pokemon has this ability
- Announces itself with a special message on switch-in
- Cannot be suppressed or disabled by any means

### Technical Implementation
```c
constexpr Ability Comatose = {
    .onEntry = +[](ON_ENTRY) -> int {
        gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_SWITCHIN_COMATOSE;
        BattleScriptPushCursorAndCallback(BattleScript_AnnounceStatusAbility);
        return TRUE;
    },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_STATUS1)
        return TRUE;
    },
    .unsuppressable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Battle Interface Integration
```c
// Forces sleep status display in battle interface
if (BattlerHasAbility(battlerId, ABILITY_COMATOSE, TRUE))
    status = STATUS1_SLEEP;
```

### Move Interactions
- **Wake-Up Slap**: Deals double damage (120 BP instead of 60 BP)
- **Dream Eater**: Cannot be used on Comatose Pokemon (no actual sleep status)
- **Sleep Talk**: Cannot be used by Comatose Pokemon
- **Rest**: Cannot be used effectively (already immune to status)
- **Snore**: Cannot be used (requires actual sleep status)

### Ability Interactions
- **Bad Dreams**: Affects Comatose Pokemon (takes 1/8 HP damage per turn)
- **Sweet Dreams**: Heals Comatose Pokemon by 1/8 HP per turn
- **Mold Breaker/Teravolt/Turboblaze**: Cannot suppress Comatose
- **Gastro Acid**: Cannot remove Comatose
- **Simple Beam/Worry Seed**: Cannot replace Comatose

### Item Interactions
- **Dream Ball**: Has 4x catch rate modifier against Comatose Pokemon
- **Chesto Berry**: No effect (Pokemon not actually asleep)
- **Sleep healing items**: No effect on status immunity

### Strategic Implications
**Advantages:**
- Complete status immunity makes Pokemon extremely reliable
- Cannot be shut down by sleep moves, toxic, or burn
- Excellent for stallbreaking and consistent performance
- Immune to status-based strategies

**Disadvantages:**
- Takes damage from Bad Dreams
- Vulnerable to Wake-Up Slap's double damage
- Cannot benefit from sleep-based moves like Sleep Talk
- Limited to Pokemon that naturally learn this ability

### Common Users
- **Komala**: The primary user of this ability
- Various Elite Redux custom Pokemon may have access

### Competitive Usage Notes
- Excellent ability for bulky Pokemon that want guaranteed consistency
- Pairs well with recovery moves since status can't interrupt healing
- Strong against stall teams that rely on status conditions
- Must be careful around Bad Dreams users

### Counters
- **Bad Dreams**: Passive damage over time
- **Wake-Up Slap**: Deals significant damage
- **Direct damage**: Must rely on raw power since status won't work
- **Entry hazards**: Still vulnerable to Spikes, Stealth Rock, etc.

### Synergies
- **Sweet Dreams**: Provides healing instead of taking damage
- **Recovery moves**: Can use them consistently without status interruption
- **Setup moves**: Cannot be disrupted by status conditions
- **Choice items**: No risk of being locked into a move due to sleep

### Version History
- Introduced in Generation 7 as Komala's signature ability
- Maintained core functionality in Elite Redux
- Enhanced with additional interactions for dream-based abilities