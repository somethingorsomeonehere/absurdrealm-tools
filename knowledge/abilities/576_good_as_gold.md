---
id: 576
name: Good As Gold
status: reviewed
character_count: 162
---

# Good As Gold - Ability ID 576

## In-Game Description
"Immune to all Status moves, unless whole field is affected."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Good As Gold grants immunity to all status moves that directly target this Pokemon. Remains vulnerable to status moves that affect the entire field, such as Haze. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Primary Effect**: Complete immunity to status moves that target the Pokemon directly
- **Exception**: Field-wide status moves (that affect all Pokemon) can still affect the user
- **Targeting Check**: Uses `battler != attacker` logic to determine move targeting

### Activation Conditions
- Triggers when a status move targets this Pokemon
- Does NOT activate for moves that target the user themselves
- Does NOT activate for moves that affect the entire field

### Technical Implementation
```cpp
constexpr Ability GoodAsGold = {
    .onImmune = +[](ON_IMMUNE) -> int {
        CHECK(battler != attacker) CHECK(IS_MOVE_STATUS(move));
        *immunityScript = BattleScript_SoundproofProtected;
        return TRUE;
    },
    .breakable = TRUE,
};
```

### Move Categories Affected
**Blocked Status Moves (Examples):**
- Sleep Powder, Spore, Hypnosis
- Thunder Wave, Glare, Stun Spore
- Toxic, Poison Powder, Will-O-Wisp
- Confuse Ray, Sweet Kiss, Swagger
- Taunt, Torment, Disable
- Leech Seed, Mean Look, Spider Web

**NOT Blocked (Field-Wide Examples):**
- Haze (affects all Pokemon's stat changes)
- Aromatherapy (heals all team members)
- Heal Bell (heals all team members)
- Entry hazards like Stealth Rock (affect switching)

### Interactions with Other Abilities/Mechanics
- **Mold Breaker/Turboblaze/Teravolt**: Can bypass Good As Gold immunity
- **Magic Bounce**: If both Pokemon have status immunity abilities, interactions depend on move priority
- **Substitute**: Good As Gold protects the actual Pokemon, not the Substitute
- **Priority**: Immunity occurs before the move hits, so priority doesn't matter

### Strategic Implications
**Offensive Uses:**
- Allows setup sweepers to avoid status disruption
- Enables safe switching into predicted status moves
- Creates opportunities for free setup turns

**Defensive Applications:**
- Hard counters status-based stall strategies
- Forces opponents to use direct attacks instead of status
- Provides utility in formats with heavy status move usage

### Common Users
- Typically found on legendary or pseudo-legendary Pokemon
- Gholdengo is the most notable canonical user
- Often paired with setup moves or sweeping sets

### Competitive Usage Notes
- **Singles**: Extremely valuable for setup sweepers and anti-stall
- **Doubles**: Less impactful due to fewer targeted status moves
- **Format Impact**: Can significantly shift metagames away from status-heavy strategies

### Counters
- **Direct Damage**: Physical and special attacks work normally
- **Ability Suppressors**: Gastro Acid, Simple Beam remove the immunity
- **Mold Breaker**: Bypasses the immunity entirely
- **Field Effects**: Weather, terrain, and entry hazards still affect the user

### Synergies
- **Setup Moves**: Pairs excellently with Dragon Dance, Nasty Plot, etc.
- **Substitute**: Can set up safely behind Substitute
- **Recovery Moves**: Allows time to heal without status interruption
- **Choice Items**: Prevents status moves from forcing switches

### Version History
- Introduced in Generation IX (Pokemon Scarlet/Violet)
- Elite Redux Implementation: Uses standard immunity framework
- **Current Status**: Fully implemented with field-wide move exception noted in description

### Notes
- The ability description mentions field-wide move exception, though current code implementation may need verification for moves like Haze
- Uses the same battle script as Soundproof for immunity messages
- Marked as breakable by Mold Breaker and similar abilities