---
id: 9
name: Static
status: reviewed
character_count: 99
---

# Static - Ability ID 9

## In-Game Description
"30% chance to paralyze on contact. Also works on offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact with this Pokemon has a 30% chance to inflict paralysis. Works offensively and defensively.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Static has been enhanced in Elite Redux to work bidirectionally:

1. **Defensive Trigger** (Original)
   - 30% chance when hit by a contact move
   - Paralyzes the attacker

2. **Offensive Trigger** (Elite Redux Enhancement)
   - 30% chance when using a contact move
   - Paralyzes the defender
   - Makes physical Electric-types much more threatening

### Technical Implementation

**Code Implementation** (`src/abilities.cc`):
```cpp
ON_EITHER(Static) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(CanBeParalyzed(battler, opponent))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))
    CHECK(Random() % 100 < 30)
    
    AbilityStatusEffectSafe(MOVE_EFFECT_PARALYSIS, battler, opponent);
    return TRUE;
}
```

The `ON_EITHER` macro enables both offensive and defensive activation.

### Paralysis Effects
When Static triggers, the target:
- Has Speed reduced to 50% (25% in older gens)
- Has 25% chance to be fully paralyzed each turn
- Cannot be paralyzed if Electric-type or already statused

### Activation Requirements
1. Move must make contact
2. Target must be able to be paralyzed
3. 30% random chance must succeed
4. Standard on-hit conditions must be met

### Strategic Implications

**Offensive Benefits**:
- Wild Charge becomes a paralysis spreader
- Spark gains additional utility
- Physical Electric coverage more valuable
- Speed control through offense

**Defensive Benefits**:
- Punishes physical attackers
- Discourages U-turn/Fake Out
- Speed control through defense
- Contact move deterrent

### Overworld Effect
When a Pokemon with Static leads the party:
- 50% chance to encounter Electric-type Pokemon
- Stacks with other encounter rate modifiers
- Only works in areas with Electric-types

### Interactions with Other Abilities/Mechanics
- **Limber/Shield Dust**: Prevents paralysis
- **Guts**: Turns paralysis into Attack boost
- **Quick Feet**: Turns paralysis into Speed boost
- **Synchronize**: Bounces paralysis back
- **Mold Breaker**: Bypasses Static entirely

### Example Battle Scenarios

**Offensive**: Pikachu uses Wild Charge
- Deals damage + 30% chance to paralyze
- Recoil damage still applies
- Can cripple faster threats

**Defensive**: Pikachu is hit by Close Combat
- Takes damage + 30% chance to paralyze attacker
- Can punish physical sweepers

### Common Static Users
- **Pikachu**: Has Static as innate ability
- **Ampharos**: Defensive Electric-type
- **Manectric**: Fast special attacker
- **Emolga**: Flying/Electric with contact moves
- Various Electric-types as ability option

### Competitive Usage Notes
- A-tier ability with offensive enhancement
- Excellent speed control option
- Synergizes with physical Electric moves
- Can single-handedly swing momentum
- More valuable than Flame Body/Poison Point due to paralysis benefits

### Mathematical Analysis
Per battle with contact moves:
- 1 contact: 30% paralysis chance
- 2 contacts: 51% paralysis chance
- 3 contacts: 65.7% paralysis chance
- 4 contacts: 76% paralysis chance

### Counters
- **Electric-types**: Immune to paralysis
- **Limber**: Complete paralysis immunity
- **Non-contact moves**: Earthquake, special attacks
- **Taunt**: Prevent Thunder Wave follow-up
- **Lum Berry/Cheri Berry**: One-time cure

### Synergies
- **Thunder Wave**: Guaranteed paralysis option
- **Volt Switch**: Safe pivot after paralysis
- **Fake Out**: Extra contact chance turn 1
- **Speed control**: Tailwind, Sticky Web
- **Hex/Venoshock**: Boost damage vs status

### Related Abilities
- **Flame Body**: 30% burn on contact
- **Poison Point**: 30% poison on contact
- **Effect Spore**: 30% random status on contact
- **White Noise**: Includes Static effect plus healing

### Version History
- **Gen III+**: 30% defensive paralysis chance
- **Elite Redux**: Added offensive paralysis chance