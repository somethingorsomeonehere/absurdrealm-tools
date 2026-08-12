---
id: 41
name: Water Veil
status: reviewed
character_count: 123
---

# Water Veil - Ability ID 41

## In-Game Description
"Burn-immune. Casts Aqua Ring on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Aqua Ring on entry, which restores 1/16 HP each turn. Grants immunity to burn status and removes burn on switching in.

## Detailed Mechanical Explanation
*For Discord/reference use*

**WATER VEIL** is a protective ability that provides burn immunity and automatic Aqua Ring recovery.

### Activation Mechanics:
- **Burn Immunity**: Completely prevents burn status via onStatusImmune hook
- **Auto Aqua Ring**: Automatically applies STATUS3_AQUA_RING on switch-in
- **Entry Message**: "{Pokemon} enveloped itself in a veil made of water."
- **Requirement**: Only activates if the Pokemon doesn't already have Aqua Ring status

### Burn Immunity:
1. **Complete Protection**: Cannot be burned by any move, ability, or item
2. **Status Removal**: If burned before gaining this ability, burn is immediately cured
3. **Immunity Override**: Cannot be bypassed by moves like Corrosive or abilities like Mold Breaker
4. **Message**: Shows standard "It doesn't affect [Pokemon]!" when burn is attempted

### Aqua Ring Mechanics:
1. **Healing Amount**: Restores 1/16 (6.25%) of max HP each turn
2. **Big Root Boost**: Healing increased to 1/16 x 1.5 = 9.375% max HP with Big Root held
3. **Absorbant Synergy**: Healing increased by additional 50% if Pokemon also has Absorbant ability
4. **Turn Priority**: Heals during end-of-turn phase, specifically during ENDTURN_AQUA_RING step
5. **Conditions**: Only heals if Pokemon is not at full HP, can heal, and is still conscious

### Interaction Rules:
- **vs Other Recovery**: Stacks with Leftovers, Rain Dish, Ice Body, and other healing effects
- **vs Heal Block**: Aqua Ring healing is blocked by Heal Block status
- **vs Magic Guard**: Pokemon with Magic Guard still receive Aqua Ring healing
- **Switching**: Aqua Ring status is lost when the Pokemon switches out
- **Taunt/Encore**: Cannot be prevented since it's an automatic ability effect

### Technical Implementation:
```c
constexpr Ability WaterVeil = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gStatuses3[battler] & STATUS3_AQUA_RING)
        
        gStatuses3[battler] |= STATUS3_AQUA_RING;
        BattleScriptPushCursorAndCallback(BattleScript_BattlerEnvelopedItselfInAVeil);
        return TRUE;
    },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_BURN)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Competitive Notes:
- Provides excellent longevity with consistent healing
- Hard counters Will-O-Wisp and other burn strategies
- Synergizes well with defensive sets and stall tactics
- Big Root is a strong held item choice to maximize healing
- Can be Skill Swapped, Role Played, or Traced for strategic value
- Vulnerable to Gastro Acid, Worry Seed, and other ability-suppressing effects

### Comparison to Similar Abilities:
- **vs Magma Armor**: Identical burn immunity, but Magma Armor doesn't provide Aqua Ring
- **vs Heatproof**: Water Veil provides immunity, Heatproof only reduces Fire damage and burn damage
- **vs Water Absorb**: Different defensive niche - immunity vs healing from attacks
- **vs Aqua Ring (move)**: Automatic activation vs manual setup, but same healing effect

### Version History:
- Gen 3-4: Burn immunity only
- Elite Redux: Enhanced with automatic Aqua Ring effect on switch-in