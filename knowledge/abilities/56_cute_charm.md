---
id: 56
name: Cute Charm
status: reviewed
character_count: 198
---

# Cute Charm - Ability ID 56

## In-Game Description
"50% chance to attract on contact. Also works on offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by making contact (offensively or defensively), has a 50% chance to infatuate the attacker (cuts their Attack and Special Attack in half). This only works on Pokemon of the opposite gender.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Cute Charm in Elite Redux provides bidirectional attraction with contact moves:

1. **Contact-Based Attraction (50%)**
   - Triggers on both offensive and defensive contact moves
   - 50% activation rate when all conditions are met
   - Causes infatuation status (MOVE_EFFECT_ATTRACT)
   - Works on both physical attacks and special contact moves

2. **Gender Requirements**
   - Requires attacker and defender to have different genders
   - Cannot affect genderless Pokemon (except with special abilities)
   - Normal gender compatibility rules apply

### Technical Implementation

**Code Structure** (`src/abilities.cc`):
```cpp
ON_EITHER(CuteCharm) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))
    CHECK(CanInfatuate(battler, opponent))
    CHECK(Random() % 100 < 50)

    AbilityStatusEffectSafe(MOVE_EFFECT_ATTRACT, battler, opponent);
    return TRUE;
}
constexpr Ability CuteCharm = {
    ON_EITHER_ABILITY(CuteCharm),
};
```

**Key Helper Functions**:
- `ShouldApplyOnHitAffect()`: Checks if on-hit effects can apply
- `IsMoveMakingContact()`: Verifies the move makes physical contact
- `CanInfatuate()`: Validates gender compatibility and status immunity
- `AbilityStatusEffectSafe()`: Applies attraction status safely

### Activation Conditions
1. **Move must make contact**: Physical moves, some special moves like Petal Dance
2. **Target must be able to be infatuated**: Different gender, not already infatuated
3. **On-hit effects must be applicable**: Target not protected by abilities/items
4. **50% random chance**: Must pass Random() % 100 < 50 check

### What CanInfatuate Checks
From `src/battle_util.c`:
- Target not already infatuated
- Battlers are different (not self-targeting)
- Attacker is alive
- Target not protected by Oblivious, Aroma Veil, etc.
- Compatible genders (different and not genderless)
- Special abilities override (Pure Love, Mycelium Might)

### Bidirectional Nature
Unlike most contact abilities, Cute Charm uses `ON_EITHER_ABILITY` macro:
- **As Attacker**: Can infatuate defending Pokemon when using contact moves
- **As Defender**: Can infatuate attacking Pokemon when they use contact moves

### Abilities Using Cute Charm's Effect
Several Elite Redux abilities share this functionality:
- **Prim and Proper**: `.onDefender = CuteCharm.onDefender` + Fort Knox immunity
- **Hydro Circuit**: Includes Cute Charm's defender effect + healing from infatuated foes
- **Tender Affection**: Full Cute Charm effect + Fairy-type STAB

### Strategic Implications

1. **Defensive Utility**
   - Punishes physical attackers with potential infatuation
   - Creates setup opportunities when opponents are infatuated
   - Provides passive disruption without turn investment

2. **Offensive Application**
   - Enables aggressive infatuation strategies
   - Works with contact special moves (rare but exists)
   - Combines with other status effects for layered disruption

3. **Gender-Based Strategy**
   - More effective in metas with diverse gender distributions
   - Completely shut down by same-gender or genderless teams
   - Synergizes with gender-based move selection

### Battle Scenarios

**Defensive Scenario**:
```
Opponent uses Earthquake (contact) to 50% chance to infatuate
If triggered: Opponent becomes infatuated, may skip turns
```

**Offensive Scenario**:
```
User with Cute Charm uses Thunder Punch to 50% chance to infatuate target
Creates potential setup opportunity or disruption
```

### Interactions with Other Mechanics

**Status Immunities**:
- **Oblivious**: Complete immunity to infatuation
- **Aroma Veil**: Team-wide protection (if ally has it)
- **Shield Dust**: Prevents secondary effects including attraction
- **Substitute**: Blocks contact and thus Cute Charm activation

**Status Amplifiers**:
- **Serene Grace**: Does NOT affect Cute Charm's 50% rate (ability-based, not move effect)

**Contact Modifiers**:
- **Long Reach**: Prevents contact, disabling Cute Charm
- **Protective Pads**: User doesn't make contact, no Cute Charm trigger

### Common Contact Moves
**Physical Moves**: Tackle, Body Slam, Earthquake, Fire Punch, Ice Punch, Thunder Punch, etc.
**Special Contact**: Petal Dance, Grass Knot (some variants)

### Competitive Usage Notes
- C+ tier ability providing moderate utility
- Best on Pokemon that frequently make or receive contact
- More valuable in singles than doubles (higher contact frequency)
- Gender distribution in meta heavily affects viability
- AI rating: 4/10 (decent but situational)

### Example Calculations
**Infatuation Success Rate**: 50% base chance
**With Oblivious Target**: 0% (complete immunity)
**Against Same Gender**: 0% (cannot infatuate)
**Against Substitute**: 0% (no contact made)

### Common Cute Charm Users
Based on `base_stats.h` analysis:
- **Jigglypuff/Wigglytuff**: Classic users with defensive bulk
- **Clefairy/Clefable**: Versatile Fairy-types with support options
- **Skitty/Delcatty**: Offensive Normal-types
- **Lopunny**: Fast physical attacker
- Various Pokemon as innate or selectable ability

### Counters
- **Same Gender Team**: Complete immunity through gender matching
- **Genderless Pokemon**: Natural immunity (except vs special abilities)
- **Oblivious**: Direct ability counter
- **Aroma Veil Ally**: Team protection
- **Long Reach/Protective Pads**: Prevents contact
- **Shield Dust**: Blocks secondary effects
- **Substitute**: Physical barrier preventing contact

### Synergies
- **Thunder Wave**: Paraflinch-style disruption with paralysis + infatuation
- **Attract Support**: Stacking infatuation sources
- **Setup Moves**: Use infatuation turns to boost stats
- **Healing Moves**: Recover while opponent skips turns
- **Contact Moves**: Maximize activation opportunities
- **Gender-based Strategies**: Partner with Rivalry, etc.

### Related Abilities
- **Pure Love (508)**: Can infatuate any gender/genderless
- **Beautiful Music (622)**: Sound move-based attraction with `canInfatuateAny`
- **Hydro Circuit**: Healing + Cute Charm defensive effect
- **Tender Affection**: Cute Charm + Fairy STAB

### Version History
- **Generation III**: Introduced as defensive-only contact ability
- **Generation IV-V**: 30% activation rate, contact moves only
- **Generation VI+**: Maintained basic functionality
- **Elite Redux**: Enhanced to 50% rate + bidirectional activation + special ability variants

### Technical Notes
- Uses `AbilityStatusEffectSafe` for safe status application
- Respects Safeguard and other protective effects
- Triggers ability popup when activated
- Handles edge cases like Mold Breaker interaction (breakable)