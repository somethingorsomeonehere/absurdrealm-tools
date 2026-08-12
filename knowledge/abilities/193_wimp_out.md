---
id: 193
name: Wimp Out
status: reviewed
character_count: 167
---

# Wimp Out - Ability ID 193

## In-Game Description
"At 1/2 of max HP or below, instantly switches out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the Pokemon receives damage and its HP drops to 50% or below for the first time in battle, it switches out to safety. Activates on the last hit of multihit moves.

## Detailed Mechanical Explanation

Wimp Out is a defensive ability that forces the Pokemon to automatically switch out when its HP drops to 50% or below, providing an emergency escape mechanism from dangerous situations.

### Trigger Conditions
- Pokemon's HP must drop from above 50% to 50% or below in a single turn
- Must have taken damage that turn (checked via `ShouldApplyOnHitAffect`)
- Only activatable once per battle encounter per Pokemon
- Does not trigger on multi-hit moves after the first hit

### Requirements for Activation
1. **Battle Type**: Must be a trainer battle (`BATTLE_TYPE_TRAINER`)
2. **Available Pokemon**: Must have usable party members (`CountUsablePartyMons`)
3. **Switch Ability**: Pokemon must be able to switch (`CanBattlerSwitch`)
4. **Not Arena Battle**: Cannot activate in Battle Arena (`BATTLE_TYPE_ARENA`)

### Blocking Conditions
- **Sheer Force**: Moves with the Sheer Force flag prevent activation
- **Trapping Effects**: Arena Trap, Shadow Tag, and similar effects block switching
- **Multi-Hit Moves**: Only the first hit can trigger the ability

### Implementation Details
- Uses `CheckHalfHpAbility` function to verify HP threshold crossing
- Sets `RESOURCE_FLAG_EMERGENCY_EXIT` flag for processing
- Processed during `MOVEEND_EMERGENCY_EXIT` phase of battle script
- Shows ability popup if `B_ABILITY_POP_UP` is enabled

## Strategic Usage

### Advantages
- **Emergency Escape**: Prevents KO from follow-up attacks or status damage
- **Pivot Tool**: Can force favorable switches in trainer battles  
- **Damage Mitigation**: Reduces overall damage taken by escaping dangerous situations
- **Mind Games**: Forces opponents to consider burst damage strategies

### Disadvantages
- **Loss of Control**: Cannot choose when to switch out manually
- **Predictable**: Opponents can anticipate the switch timing
- **Wild Battle Limitation**: Less useful in wild Pokemon encounters
- **One-Time Use**: Only activates once per battle per Pokemon

## Pokemon with This Ability

### Happiny Redux
- **Type**: Fighting
- **Stats**: 15/75/5/10/5/110 (BST: 220)
- **Role**: Extremely fast glass cannon with emergency escape
- **Other Abilities**: Cute Charm, Fight Spirit
- **Innates**: Vital Spirit, Long Reach, Iron Fist

### Wimpod  
- **Type**: Bug/Water
- **Stats**: 25/65/70/20/30/80 (BST: 290)  
- **Role**: Defensive pivot with decent bulk
- **Other Abilities**: Pickup, Guilt Trip
- **Innates**: Shell Armor, Coward, Looter

### Wiglett
- **Type**: Water
- **Stats**: 15/55/30/35/35/95 (BST: 265)
- **Role**: Fast but frail Water-type with escape option
- **Other Abilities**: Accelerate, Coward  
- **Innates**: Gooey, Field Explorer, Rattled

## Competitive Analysis

### AI Rating: 3/10
The AI considers Wimp Out moderately useful, rating it 3 out of 10. The AI will:
- Recognize the automatic switch potential when the Pokemon reaches half HP
- Account for the switch when planning damage calculations
- Consider the loss of momentum from forced switching

### Tier Placement
Wimp Out appears on Pokemon across different competitive tiers (Tier 3-4), suggesting its utility varies greatly depending on the Pokemon's overall stat distribution and role.

## Interactions and Edge Cases

### Related Abilities
- **Emergency Exit**: Identical effect to Wimp Out (shares same implementation)
- **Sheer Force**: Completely prevents Wimp Out activation
- **Arena Trap/Shadow Tag**: Blocks the switching component

### Battle Format Considerations
- **Singles**: Provides direct escape from bad matchups
- **Doubles**: Less reliable due to potential targeting from multiple opponents
- **Wild Battles**: Significantly less useful without guaranteed switch options

### Move Interactions
- **Multi-Hit Moves**: Only first hit can trigger, subsequent hits cannot reactivate
- **Status Moves**: Indirect damage (poison, burn) cannot trigger the ability
- **Recoil Moves**: Self-inflicted damage does not count for activation

## Coding Implementation

```cpp
constexpr Ability WimpOut = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(CheckHalfHpAbility(battler, attacker))
        CHECK_NOT(TestSheerForceFlag(attacker, gCurrentMove))
        CHECK(CanBattlerSwitch(battler) && gBattleTypeFlags & BATTLE_TYPE_TRAINER)
        CHECK_NOT(gBattleTypeFlags & BATTLE_TYPE_ARENA)
        CHECK(CountUsablePartyMons(battler));
        gBattleResources->flags->flags[battler] |= RESOURCE_FLAG_EMERGENCY_EXIT;
        return FALSE;
    },
};
```

The ability shares its exact implementation with Emergency Exit, demonstrating code reusability in the Elite Redux codebase.