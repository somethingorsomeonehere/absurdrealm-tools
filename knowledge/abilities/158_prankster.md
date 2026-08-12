---
id: 158
name: Prankster
status: reviewed
character_count: 100
---

# Prankster - Ability ID 158

## In-Game Description
"Status moves have +1 priority but fail on opposing Dark-types."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Status moves gain +1 priority. Status moves fail when directly targeting opposing Dark-type Pokemon. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Prankster grants +1 priority to all status moves (moves with `SPLIT_STATUS`), making them execute earlier in the turn order. The priority boost applies during move selection and affects the speed calculation bracket.

**Priority System:**
- Normal status moves: Priority 0
- Prankster status moves: Priority +1
- Still slower than moves with naturally higher priority (Quick Attack +1, Extreme Speed +2)

### Implementation Details

**Priority Boost Logic:**
```cpp
constexpr Ability Prankster = {
    .onPriority = +[](ON_PRIORITY) -> int {
        CHECK(IS_MOVE_STATUS(move))
        return 1;
    },
};
```

**Dark-Type Immunity Logic:**
```cpp
bool32 BlocksPrankster(MoveEnum move, u8 battlerPrankster, u8 battlerDef, bool32 checkTarget) {
    // Only blocks status moves from Prankster users
    if (!IS_MOVE_STATUS(move)) return FALSE;
    if (!BattlerHasAbility(battlerPrankster, ABILITY_PRANKSTER, FALSE)) return FALSE;
    
    // Only blocks opposing team
    if (GetBattlerSide(battlerPrankster) == GetBattlerSide(battlerDef)) return FALSE;
    
    // Target must be Dark-type and not semi-invulnerable
    if (!IS_BATTLER_OF_TYPE(battlerDef, TYPE_DARK)) return FALSE;
    if (gStatuses3[battlerDef] & STATUS3_SEMI_INVULNERABLE) return FALSE;
    
    return TRUE;
}
```

### Affected Moves (Status Moves Only)
**Stat Boosters:** Swords Dance, Nasty Plot, Calm Mind, Dragon Dance, Quiver Dance, Shell Smash
**Debuffs:** Thunder Wave, Spore, Sleep Powder, Taunt, Toxic, Will-O-Wisp, Glare
**Field Effects:** Stealth Rock, Spikes, Toxic Spikes, Light Screen, Reflect
**Utility:** Substitute, Recovery moves, Roost, Recover
**Multi-target:** Spore (hits all), Perish Song, Aromatherapy

### Dark-Type Interaction
- **Complete Immunity:** Dark-types are completely immune to Prankster-boosted status moves
- **Applies to opposing team only:** Can still use status moves on Dark-type allies
- **Multi-target protection:** In moves like Perish Song, Dark-types are unaffected while others take effect
- **Magic Coat interaction:** If a Dark-type uses Magic Coat to reflect a Prankster status move, the reflected move fails against the original Dark-type user

### Strategic Applications

**Offensive Sets:**
- Thunder Wave to setup sweeper activation
- Taunt to shuts down opposing setup/recovery
- Toxic to pressure stall tactics
- Will-O-Wisp to physical attacker neutering

**Support Sets:**
- Priority recovery with Roost
- Priority hazards (Stealth Rock, Spikes)
- Priority screens (Light Screen, Reflect)
- Priority Substitute for protection

**Speed Control:**
- Bypasses Trick Room reversal
- Outspeeds Choice Scarf users with status moves
- Guarantees first-turn setup disruption

### Competitive Usage
**Tier Placement:** Excellent utility ability, common in OU and competitive formats
**Common Users:** Sableye, Klefki, Thundurus, Tornadus, Whimsicott, Meowstic
**Team Roles:** Utility support, lead disruptor, stall support, hazard setter

**Synergistic Strategies:**
- **Focus Sash + Prankster:** Guaranteed priority status move even when frail
- **Prankster + Lagging Tail:** Ensures status moves go first, attacking moves go last
- **Prankster + Mental Herb:** Protection from Taunt while setting up

### Counters and Limitations

**Direct Counters:**
- **Dark-types:** Complete immunity to all Prankster status moves
- **Magic Bounce:** Reflects status moves back to user
- **Taunt:** Prevents status move usage (though Prankster Taunt can outspeed)

**Ability Counters:**
- **Psychic Terrain:** Blocks priority moves that target grounded Pokemon
- **Queenly Majesty/Dazzling:** Blocks all priority moves
- **Magic Bounce:** Redirects status moves

**Item Counters:**
- **Mental Herb:** One-time protection from status conditions
- **Lum Berry:** Cures status conditions immediately
- **Safety Goggles:** Blocks powder moves like Spore

### Version History and Notable Changes
- **Generation V Introduction:** Original implementation with Dark-type immunity
- **Generation VI:** Expanded to include more status moves
- **Elite Redux:** Enhanced priority system integration, improved multi-target handling

### Example Calculations

**Priority Brackets (fastest to slowest):**
1. Priority +2: Extreme Speed
2. Priority +1: Quick Attack, **Prankster status moves**
3. Priority 0: Normal moves, non-Prankster status moves
4. Priority -1: Vital Throw

**Speed Ties:**
- Two Prankster users with same speed: Determined by normal speed tie rules
- Prankster status vs naturally +1 priority: Both at +1, speed determines order
- Prankster in Trick Room: Status moves still get +1 priority despite speed reversal