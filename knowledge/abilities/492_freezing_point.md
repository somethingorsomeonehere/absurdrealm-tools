---
id: 492
name: Freezing Point
status: reviewed
character_count: 224
---

# Freezing Point - Ability ID 492

## In-Game Description
"Contact moves have 20% chance to inflict frostbite."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact with this Pokemon has a 20% chance to inflict frostbite. Non-contact has a 30% chance. Works offensively and defensively. Frostbitten Pokemon lose 1/8th of their max HP each turn and have their Special Attack halved. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Freezing Point inflicts frostbite status on contact, creating a defensive ability that punishes physical attackers with a debilitating ice-based status condition.

### Activation Conditions
- **Trigger**: When opponent makes contact with this Pokemon
- **Chance**: 30% probability per contact move
- **Contact requirement**: Move must have the contact flag
- **Target eligibility**: Opponent must be able to receive frostbite status
- **Immunity check**: Respects frostbite immunity from abilities/types

### Technical Implementation
```c
constexpr Ability FreezingPoint = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(IsMoveMakingContact(gCurrentMove))
        CHECK(Random() % 100 < 30)
        CHECK(CanGetFrostbite(attacker))
        
        SetMoveEffect(MOVE_EFFECT_FROSTBITE, FALSE);
        return TRUE;
    },
};
```

### Frostbite Status Condition
- **HP damage**: 1/8 maximum HP lost per turn at end of turn
- **Special Attack reduction**: Special Attack halved during damage calculation
- **Duration**: Permanent until cured or switched out
- **Visual indicator**: Frostbitten Pokemon show ice crystals/blue tint
- **Type interaction**: Ice-type status effect with specific curing methods

### Curing Methods
- **Fire-type moves**: Moves with FLAG_THAW_USER flag cure frostbite
- **Switching out**: Removes frostbite status naturally
- **Aromatherapy/Heal Bell**: Team-wide status cure moves
- **Lum Berry**: Instant frostbite cure
- **Natural Cure**: Cures on switch-out
- **Rest**: Sleep replaces frostbite status

### Strategic Applications
- **Special wall**: Punishes special attackers who resort to contact moves
- **Physical deterrent**: Discourages contact moves from physical attackers
- **Status spreading**: Creates field presence through status infliction
- **Defensive utility**: Provides passive protection against contact moves
- **Special Attack debuffing**: Weakens opposing special sweepers

### Contact Move Examples
**Commonly affected moves:**
- Tackle, Body Slam, Return
- Punch moves (Fire Punch, Ice Punch, Thunder Punch)
- Bite, Crunch, Hyper Fang
- Earthquake, Close Combat
- U-turn, Volt Switch (if making contact)

**Not affected:**
- Projectile moves (Thunderbolt, Flamethrower)
- Ranged attacks (Shadow Ball, Energy Ball)
- Non-contact physical moves (Rock Slide, Earthquake)

### Immunity Considerations
- **Ice-types**: May have natural frostbite immunity
- **Fire-types**: Often immune to ice-based status conditions
- **Ability immunity**: Abilities like Limber or Water Veil
- **Safeguard**: Protects team from status conditions
- **Substitute**: Blocks contact and prevents frostbite

### Competitive Usage
- **Defensive tanks**: Excellent on bulky Pokemon that can survive contact
- **Status spreaders**: Complements other status-inflicting strategies
- **Special walls**: Particularly effective against mixed attackers
- **Pivot Pokemon**: Good on defensive pivots that take hits
- **Stall teams**: Provides passive damage and debuffing

### Frostbite vs Burn Comparison
- **HP damage**: Both deal 1/8 max HP per turn
- **Stat reduction**: Frostbite halves Special Attack, burn halves Attack
- **Curing**: Frostbite cured by fire moves, burn by water/ice moves
- **Immunity**: Different type immunities and resistances
- **Strategic use**: Frostbite counters special attackers, burn counters physical

### Synergies
- **Entry hazards**: Combine with Stealth Rock for additional passive damage
- **Other status**: Stack with poison/burn for maximum status pressure
- **Healing moves**: Leftovers/recovery to outlast opponents
- **Ice-type moves**: Thematic synergy with ice-based attacks
- **Defensive items**: Rocky Helmet stacks contact punishment

### Counters
- **Long-range attackers**: Special attackers with non-contact moves
- **Fire-types**: Often immune and can cure teammates
- **Substitute**: Blocks contact and prevents frostbite
- **Status immunity**: Magic Guard, Poison Heal, etc.
- **Rapid switching**: Avoid prolonged contact with the ability user

### Version History
- Elite Redux custom status condition and ability
- Designed as Special Attack equivalent to burn status
- Part of expanded status system for enhanced strategic depth
- Provides ice-type defensive utility beyond traditional freeze