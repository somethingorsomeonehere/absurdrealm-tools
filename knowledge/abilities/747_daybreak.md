---
id: 747
name: Daybreak
status: reviewed
character_count: 64
---

# Daybreak - Ability ID 747

## In-Game Description
"Burns the foe on contact. Also works on offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user burns the foe on contact. Works on offense and defense.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Daybreak is a unique contact-based ability that inflicts burn status on opponents through physical contact. It's one of the most reliable burn-inducing abilities in the game, working with 100% consistency rather than the typical 30% chance of similar abilities.

### Activation Conditions
- **Contact requirement**: Only activates when contact moves are used
- **Bi-directional**: Works both defensively (when opponent attacks with contact) and offensively (when user attacks with contact)
- **No random chance**: Unlike Flame Body, Static, or Poison Point, Daybreak has a 100% activation rate
- **Status immunity check**: Will not activate if target cannot be burned (Fire types, current burn status, etc.)

### Technical Implementation
```c
ON_EITHER(Daybreak) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(CanBeBurned(opponent))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))

    AbilityStatusEffectSafe(MOVE_EFFECT_BURN, battler, opponent);
    return TRUE;
}
```

### Key Differences from Similar Abilities
- **Flame Body**: 30% chance to burn on contact (defensive only)
- **Daybreak**: 100% chance to burn on contact (both offensive and defensive)
- **ON_EITHER**: This macro makes it work bidirectionally, unlike most contact abilities

### Contact Move Examples
**Physical moves that trigger Daybreak:**
- Tackle, Body Slam, Thunder Punch
- Earthquake, Stone Edge (non-contact moves do NOT trigger)
- Flame Wheel, Flare Blitz (contact Fire moves)
- U-turn, Volt Tackle

**Non-contact moves that do NOT trigger:**
- Shadow Ball, Thunderbolt, Surf
- Rock Slide, Earthquake
- Air Slash, Dragon Pulse

### Burn Status Effects
- **Damage**: 1/16 max HP per turn
- **Attack reduction**: Physical Attack reduced by 50%
- **Duration**: Until switched out, KO'd, or cured
- **Stacking**: Cannot stack with other major status conditions

### Important Interactions
- **Fire-type immunity**: Fire-type Pokemon cannot be burned
- **Guts ability**: Opponent gains Attack boost if they have Guts
- **Magic Guard**: Prevents burn damage but not the Attack reduction
- **Heatproof**: Reduces burn damage from 1/16 to 1/32 HP per turn
- **Natural Cure**: Cures burn when switching out
- **Ability suppression**: Doesn't work under Mold Breaker effects

### Multi-Hit Moves
- Each hit of multi-hit contact moves can trigger Daybreak
- First successful hit that connects will inflict burn
- Subsequent hits won't re-inflict burn (already burned)

### Strategic Implications
**Offensive advantages:**
- Guaranteed burn on contact attacks creates powerful wallbreaking potential
- Reduces opponent's physical attack by 50%
- Chip damage from burn helps secure KOs

**Defensive advantages:**
- Deters physical attackers from using contact moves
- Punishes U-turn/Volt Switch users
- Creates passive damage through burn

**Team synergy:**
- Pairs well with Pokemon that can capitalize on burned opponents
- Excellent for stall teams that benefit from residual damage
- Strong deterrent against physical setup sweepers

### Competitive Usage Notes
- **Physical walls**: Excellent on bulky Pokemon that can survive contact hits
- **Revenge killers**: Can guarantee burn when revenge killing with contact moves
- **Entry hazard synergy**: Burn + Stealth Rock creates significant residual pressure
- **Wallbreaking**: Contact attackers become incredibly dangerous with guaranteed burn

### Counters
- **Fire-type Pokemon**: Immune to burn entirely
- **Non-contact moves**: Special attacks and non-contact physical moves avoid trigger
- **Remote attackers**: Pokemon with strong special movesets
- **Ability suppression**: Mold Breaker family abilities
- **Status condition prevention**: Aromaveil, Misty Terrain protection
- **Substitute**: Blocks direct contact with the ability user

### Synergies
- **Rough Skin/Iron Barbs**: Stack contact punishment effects
- **Rocky Helmet**: Additional contact move punishment
- **Burn support moves**: Will-O-Wisp for non-contact burn spreading
- **Hex/Infernal Parade**: STAB moves that deal double damage to burned targets
- **Facade users**: Team members that benefit from status conditions

### Risk Management
**For the user:**
- Vulnerable to special attackers
- Fire-types can switch in safely
- Status moves and entry hazards still threaten

**For opponents:**
- Must rely on special attacks or non-contact physical moves
- Physical setup becomes much more difficult
- U-turn/Volt Switch strategies are heavily punished

### Version History
- Elite Redux exclusive ability
- Designed as an enhanced version of contact burn abilities
- Notable for 100% activation rate and bidirectional function
- Part of the expanded ability roster for competitive diversity