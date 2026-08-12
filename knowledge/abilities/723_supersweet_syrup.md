---
id: 723
name: Supersweet Syrup
status: reviewed
character_count: 119
---

# Supersweet Syrup - Ability ID 723

## In-Game Description
"Sticky Hold + Disables foe's item for 2 turns on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user's item cannot be forcibly removed or stolen. When making contact, the opponent's item is disabled for 2 turns.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Supersweet Syrup is a combination defensive/disruptive ability that provides dual item-related effects:
1. **Sticky Hold component**: Protects the user's item from removal
2. **Contact-based item disable**: Disables attacker's item for 2 turns when hit by contact moves

### Activation Conditions
**Sticky Hold Effect (Passive)**:
- Always active while ability is not suppressed
- Prevents item removal by moves like Knock Off, Thief, Trick, Switcheroo
- Protects from abilities that steal or remove items

**Item Disable Effect (Reactive)**:
- Triggers when hit by contact moves
- Attacker must have an item to be affected
- Sets Embargo status on attacker for 2 turns
- Only works if the ability user survives the contact move

### Technical Implementation
```c
constexpr Ability SupersweetSyrup = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK_NOT(gStatuses3[attacker] & STATUS3_EMBARGO)
        CHECK(gBattleMons[attacker].item)

        gVolatileStructs[attacker].embargoTimer = 2;
        gStatuses3[attacker] |= STATUS3_EMBARGO;
        gLastUsedItem = gBattleMons[attacker].item;
        BattleScriptCall(BattleScript_AnnounceAttackerItemDisabled);
        return TRUE;
    },
    .breakable = TRUE,
};
```

### Embargo Status Effect
When an opponent is affected by the item disable:
- **Duration**: 2 turns, decremented at end of turn
- **Effect**: Completely negates item effects during battle
- **Includes**: Held item effects, berries, type-boosting items, status-curing items
- **Visual**: Shows status message when applied and when it ends

### Item Protection (Sticky Hold Component)
The Sticky Hold aspect works through the `IsStickyHold()` function:
```c
AbilityEnum IsStickyHold(int battler) {
    AbilityEnum ability = BattlerHasAbility(battler, ABILITY_STICKY_HOLD, TRUE);
    if (!ability) ability = BattlerHasAbility(battler, ABILITY_SUPERSWEET_SYRUP, TRUE);
    return ability;
}
```

This means Supersweet Syrup provides identical item protection to pure Sticky Hold.

### Important Interactions
- **Contact moves only**: Only physical moves that make contact trigger the disable
- **Substitute bypass**: Contact through Substitute won't trigger the effect
- **Multi-hit moves**: Each hit can potentially trigger, but Embargo prevents multiple applications
- **Already embargoed**: Won't trigger if attacker is already under Embargo
- **Mold Breaker**: Can bypass the ability entirely
- **Item already gone**: Won't trigger if attacker has no item

### Sticky Hold Interactions
- **Knock Off**: Prevents item removal but still takes super-effective damage if Dark move
- **Thief/Covet**: Prevents item theft
- **Trick/Switcheroo**: Prevents item swapping
- **Magic Room**: Item protection still works during Magic Room
- **Fling**: User can still use their own Fling (not prevented by Sticky Hold)

### Strategic Applications
**Defensive Use**:
- Protects valuable items like Leftovers, Life Orb, Choice items
- Punishes contact attackers by removing their item benefits
- Excellent on bulky physical walls that expect contact moves

**Offensive Use**:
- Secure choice item effects without fear of Knock Off
- Maintain type-boosting plates or gems
- Keep utility items like Focus Sash protected

### Synergies
- **Rocky Helmet/Iron Barbs**: Combines with contact damage for double punishment
- **Flame Body/Static**: Additional contact-based status alongside item disable
- **Recovery items**: Leftovers, Black Sludge stay protected
- **Choice items**: Maintain power/speed boosts safely
- **Assault Vest**: Keep special bulk without removal risk

### Counters
- **Non-contact moves**: Special attacks, projectiles avoid item disable
- **Mold Breaker variants**: Bypass ability entirely
- **Already no item**: Attackers with no items aren't affected
- **Long-range attackers**: Pokemon that don't rely on contact moves
- **Ability suppression**: Neutralizing Gas, Core Enforcer

### Common Users
This is a unique signature ability in Elite Redux, typically found on:
- Defensive Pokemon that expect contact moves
- Pokemon with valuable items to protect
- Support Pokemon that want to maintain utility items
- Sticky/syrup-themed Pokemon (thematically appropriate)

### Competitive Viability
**Strengths**:
- Dual utility provides both protection and disruption
- Punishes common physical attackers
- Excellent for maintaining item-dependent strategies
- Can swing momentum by disabling key items

**Weaknesses**:
- Only affects contact moves
- No protection against special attackers
- Ability can be suppressed or bypassed
- Requires surviving the contact move to trigger

### Comparison to Similar Abilities
- **Pure Sticky Hold**: Same item protection but no offensive disruption
- **Rough Skin/Iron Barbs**: Contact damage instead of item disable
- **Effect Spore**: Contact-based status instead of item disable
- **Embargo (move)**: Similar effect but as an active move choice

### Version History
- New ability introduced in Elite Redux
- Combination of existing Sticky Hold mechanics with new Embargo application
- Part of the expanded ability roster for enhanced strategic depth