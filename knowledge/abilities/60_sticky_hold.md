---
id: 60
name: Sticky Hold
status: reviewed
character_count: 53
---

# Sticky Hold - Ability ID 60

## In-Game Description
"Can't lose its item."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user's item cannot be forcibly removed or stolen.

## Detailed Mechanical Explanation
*For Discord/reference use*

**STICKY HOLD** is a protective ability that provides complete immunity to item removal, theft, and forced item switching.

### Core Mechanics:
- **Complete Item Protection**: Prevents all forms of item loss during battle
- **Implementation**: Uses dedicated `IsStickyHold(battler)` function in battle utilities
- **Shared Functionality**: ABILITY_SUPERSWEET_SYRUP also provides identical protection

### Protected Against:
- **Direct Theft**: Knock Off, Thief, Covet
- **Item Switching**: Trick, Switcheroo  
- **Forced Removal**: Embargo effects, item-destroying moves
- **AI Recognition**: Opponent AI avoids item-targeting moves

### Technical Implementation:
```c
AbilityEnum IsStickyHold(int battler) {
    AbilityEnum ability = BattlerHasAbility(battler, ABILITY_STICKY_HOLD, TRUE);
    if (!ability) ability = BattlerHasAbility(battler, ABILITY_SUPERSWEET_SYRUP, TRUE);
    return ability;
}
```

The ability is checked throughout battle script commands whenever item removal is attempted:
- `battle_script_commands.c`: Multiple checks prevent item removal
- Shows ability popup when protection activates
- Returns FALSE for all item-targeting effects

### Strategic Applications:
- **Item-Dependent Sets**: Protects Choice items, Life Orb, Focus Sash
- **Defensive Cores**: Enables reliable Leftovers/Rocky Helmet strategies
- **Competitive Value**: AI rates as 3/10 (situational but useful)
- **Team Support**: Prevents opponents from removing key team items

### Interactions:
- **Breakable**: Can be suppressed by Mold Breaker abilities
- **Voluntary Actions**: Does not prevent self-initiated item loss (Natural Gift, Fling)
- **Substitute**: Works independently of Substitute protection
- **Magic Guard**: Provides different protection - compatible abilities

### Common Users:
- Pokemon that rely heavily on specific items
- Defensive walls with Leftovers
- Choice item users wanting guaranteed effect
- Support Pokemon with utility items

### Competitive Usage:
- **Singles**: Moderate utility for item-dependent strategies
- **Doubles**: Higher value due to more item interaction
- **Stall Teams**: Essential for Leftovers-dependent walls
- **Anti-Meta**: Counters Knock Off-heavy environments

### Counters:
- **Mold Breaker**: Bypasses item protection completely
- **Non-Item Strategies**: Ability provides no other benefits
- **Status Moves**: No protection against status conditions
- **Type Coverage**: Doesn't affect move effectiveness

### Version History:
- Elite Redux maintains standard Sticky Hold functionality
- Enhanced with Supersweet Syrup sharing implementation
- Integrated with 4-ability system for broader utility