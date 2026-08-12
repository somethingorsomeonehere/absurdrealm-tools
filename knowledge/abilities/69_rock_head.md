---
id: 69
name: Rock Head
status: reviewed
character_count: 174
---

# Rock Head - Ability ID 69

## In-Game Description
"Immune to recoil damage, but not immune to Explosion/crash dmg."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all recoil damage from the user's moves and abilities. Also grants immunity to enrage recoil damage. Does not prevent crash damage or Explosion/Self-Destruct damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

**ROCK HEAD** is a defensive ability that provides both recoil damage immunity and confusion status immunity.

### Recoil Protection:
- **Coverage**: Prevents recoil damage from all recoil moves
- **Protected Moves**: Take Down, Double-Edge, Flare Blitz, Head Smash, Wild Charge, Brave Bird, Wood Hammer, and all other moves with EFFECT_RECOIL variants
- **Mechanism**: The `noRecoil = TRUE` flag prevents recoil damage calculation entirely

### Confusion Immunity:
- **Trigger**: Blocks confusion status from all sources (moves, abilities, items)
- **Script**: Shows standard immunity message
- **Removal**: Automatically removes existing confusion when ability activates (`removesStatusOnImmunity = TRUE`)

### Important Limitations:
1. **Crash Damage**: Still takes damage from missed Jump Kick/High Jump Kick (EFFECT_RECOIL_IF_MISS)
2. **Self-Destruction**: Not immune to Explosion/Self-Destruct damage - these aren't recoil
3. **Indirect Damage**: Doesn't protect against Life Orb, Struggle, or other non-recoil self-damage

### Interaction Rules:
- **vs Mold Breaker**: Rock Head can be suppressed (`breakable = TRUE`)
- **vs Skill Swap/Role Play**: Can be copied or replaced by other abilities
- **vs Entrainment**: Can be overwritten by Entrainment
- **Multiple Effects**: Both recoil immunity and confusion immunity work simultaneously

### Technical Implementation:
```c
constexpr Ability RockHead = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_CONFUSION)
        return TRUE;
    },
    .breakable = TRUE,
    .noRecoil = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Move Synergy:
**Excellent with**:
- Head Smash (150 BP, normally 50% recoil)
- Double-Edge (120 BP, normally 33% recoil)
- Flare Blitz (120 BP, normally 33% recoil)
- Brave Bird (120 BP, normally 33% recoil)

**Still risky with**:
- Jump Kick/High Jump Kick (crash damage on miss)
- Explosion/Self-Destruct (self-KO moves)

### Competitive Notes:
- Transforms high-power recoil moves into safe STAB options
- Particularly valuable on Pokemon with access to Head Smash
- Confusion immunity is a nice bonus but rarely the primary reason to use the ability
- Often preferred over other abilities on physical attackers with good recoil move access

### Related Abilities:
- **Reckless**: Boosts recoil move power but keeps the recoil (opposite philosophy)
- **Magic Guard**: Broader protection including Life Orb, but no confusion immunity
- **Brute Force**: Combination of Rock Head + Reckless effects (custom Elite Redux ability)

### Version History:
- Gen 3-8: Recoil immunity only
- Elite Redux: Added confusion immunity and cleaner implementation