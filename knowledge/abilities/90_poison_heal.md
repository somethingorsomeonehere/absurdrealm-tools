---
id: 90
name: Poison Heal
status: reviewed
character_count: 158
---

# Poison Heal - Ability ID 90

## In-Game Description
"Restores 1/8 of max HP after each turn if poisoned."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Restores 1/8 max HP per turn instead of taking damage when poisoned. Works with both regular poison and toxic poison. Also prevents damage from Toxic terrain.

## Detailed Mechanical Explanation
*For Discord/reference use*

**POISON HEAL** is a unique ability that transforms the poison status from a detriment into a powerful healing mechanism.

### Activation Mechanics:
- **Trigger**: End of turn phase (ENDTURN_POISON and ENDTURN_TOXIC)
- **Condition**: Pokemon must have poison or toxic poison status
- **Effect**: Heals 1/8 (12.5%) of max HP instead of taking damage
- **Minimum Heal**: Always heals at least 1 HP (prevents rounding to 0)

### Poison Interaction Details:
1. **Regular Poison**: Normally deals 1/8 max HP damage to Heals 1/8 max HP instead
2. **Toxic Poison**: Normally deals incremental damage (1/16, 2/16, 3/16...) to Still heals flat 1/8 max HP per turn
3. **Field Poison**: Immune to overworld poison damage (checked in field_poison.c)
4. **Toxic Waste Terrain**: Heals from toxic waste hazards instead of taking damage

### Technical Implementation:
```c
// In battle_util.c
case ENDTURN_POISON:
case ENDTURN_TOXIC:
    if (BattlerHasAbility(gActiveBattler, ABILITY_POISON_HEAL, FALSE)) {
        REQUIRE_NOT(BATTLER_MAX_HP(gActiveBattler))
        REQUIRE(CanBattlerHeal(gActiveBattler))
        
        gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 8;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        
        BattleScriptExecute(BattleScript_PoisonHealActivates);
    }
```

### Key Mechanical Interactions:
1. **Status Immunity**: Does NOT prevent getting poisoned - the ability requires poison to function
2. **Heal Block**: Healing can be prevented by Heal Block
3. **Full HP**: No healing occurs if already at max HP
4. **Toxic Counter**: Toxic's damage counter still increases, but is ignored for healing calculation
5. **Status Moves**: Pokemon can be poisoned by Toxic, Poison Powder, Toxic Spikes, etc.

### Synergistic Strategies:
1. **Toxic Orb**: Core item - automatically inflicts poison for guaranteed healing
2. **Facade**: Doubles power when poisoned (140 BP)
3. **Guts**: Can be combined for 1.5x Attack boost + healing
4. **Rest**: Poison status prevents sleep, making Rest less viable
5. **Trick/Switcheroo**: Pass Toxic Orb to opponents after activation

### Field Effects:
In the overworld, Poison Heal prevents HP loss from poison when walking. The ability is specifically checked alongside other protective abilities:
- Magic Guard
- Toxic Boost
- Impenetrable
- Apple Enlightenment

### Competitive Applications:
1. **Defensive Pivot**: Reliable 12.5% HP recovery each turn
2. **Status Absorber**: Immune to other status conditions once poisoned
3. **Stall Breaker**: Consistent healing outlasts many defensive cores
4. **Setup Sweeper**: Free turns to set up with guaranteed recovery

### Notable Users:
- Breloom: Physical attacker with Spore access
- Gliscor: Defensive pivot with Ground/Flying typing
- Elite Redux may have additional or modified Poison Heal users

### Strategic Counters:
1. **Knock Off**: Remove Toxic Orb to stop self-poisoning
2. **Taunt**: Prevent Protect stalling
3. **High Damage**: Outpace the 12.5% healing
4. **Steel/Poison Types**: Cannot be poisoned
5. **Substitute**: Blocks status moves

### Calculation Examples:
- 400 max HP to Heals 50 HP per turn
- 300 max HP to Heals 37 HP per turn
- 100 max HP to Heals 12 HP per turn
- 8 max HP to Heals 1 HP per turn (minimum)

### Version History:
- Gen 4: Introduced with Shroomish/Breloom
- Gen 5+: Expanded to Gliscor
- Elite Redux: Maintained core mechanics, integrated with expanded status system