---
id: 493
name: Cryo Proficiency
status: reviewed
character_count: 281
---

# Cryo Proficiency - Ability ID 493

## In-Game Description
"Freezing Point + summons hail on contact + hail immunity."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact with this Pokemon has a 20% chance to inflict frostbite. Non-contact has a 30% chance. Works offensively and defensively. Frostbitten Pokemon lose 1/8th of their max HP each turn and have their Special Attack halved. 
Sets hail after receiving a hit. Immune to hail damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Cryo Proficiency is an enhanced version of Freezing Point that combines frostbite infliction with weather control, creating a master of ice-based battlefield manipulation.

### Triple Effect Components

#### 1. Freezing Point Inheritance
- **Contact frostbite**: 30% chance to inflict frostbite on contact moves
- **Status effect**: Frostbite deals 1/8 HP per turn and halves Special Attack
- **Defensive utility**: Punishes contact move users with debilitating status

#### 2. Hail Summoning
- **Trigger**: When the Pokemon successfully hits with a contact move
- **Condition**: Only summons hail if no hail weather is currently active
- **Duration**: Standard hail duration (8 turns in Elite Redux)
- **Control**: Creates advantageous weather conditions on demand

#### 3. Hail Immunity
- **Damage immunity**: Takes no damage from hail weather
- **Weather advantage**: Can operate freely in hail while opponents suffer
- **Synergy**: Combines perfectly with self-summoned hail

### Technical Implementation
```c
constexpr Ability CryoProficiency = {
    .onDefender = FreezingPoint.onDefender,  // 30% frostbite on contact
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(IsMoveMakingContact(gCurrentMove))
        return CryoProficiencyHail(battler);  // Summon hail if not active
    },
    .hailImmune = TRUE,  // Immune to hail damage
};
```

### Hail Weather Effects
- **Damage**: 1/16 max HP per turn to non-Ice types
- **Accuracy**: Blizzard never misses in hail
- **Move boosts**: Aurora Veil can be used
- **Duration**: 8 turns base (can be extended with items)
- **Synergy**: Works with other hail-based abilities

### Strategic Applications
- **Weather control**: Establishes favorable conditions through combat
- **Status spreading**: Combines weather damage with frostbite
- **Ice synergy**: Enables ice-type strategies and move synergies
- **Field dominance**: Controls battlefield conditions through presence
- **Defensive layering**: Multiple forms of passive damage and debuffing

### Contact Move Synergies
**Optimal contact moves:**
- Ice Punch: Thematic ice attack that can summon hail
- Body Slam: Reliable contact move for weather setup
- U-turn: Hit and switch while setting up hail for team
- Rapid Spin: Clear hazards while establishing weather
- Drain Punch: Healing while creating battlefield control

### Weather Team Applications
- **Hail setter**: Reliable weather setting without using a move slot
- **Weather maintainer**: Can re-establish hail through combat
- **Ice-type support**: Enables team strategies around hail weather
- **Blizzard accuracy**: Team can use Blizzard with perfect accuracy
- **Aurora Veil setup**: Enables defensive screen strategies

### Double Battle Considerations
- **Team protection**: Hail damages opposing team but not user
- **Weather wars**: Can contest opposing weather through combat
- **Ally synergy**: Supports ice-type partners with weather
- **Field control**: Passive damage affects multiple opponents
- **Positioning**: Contact moves need careful targeting

### Defensive Applications
- **Contact deterrent**: Multiple punishments for contact moves
- **Passive damage**: Hail + frostbite create sustained damage
- **Special attack debuff**: Frostbite weakens special attackers
- **Weather immunity**: Operates freely in self-created conditions
- **Status immunity**: Ice-types often resist ice-based status

### Limitations
- **Contact requirement**: Both effects need contact moves to trigger
- **Weather dependency**: Less effective when hail is already active
- **Ice immunity**: Ice-types resist frostbite and are hail-immune
- **Contact immunity**: Some abilities prevent contact altogether
- **Weather wars**: Opposing weather can override hail

### Counters
- **Long-range attackers**: Avoid contact completely
- **Weather control**: Override hail with other weather
- **Ice-types**: Immune to both hail and often frostbite
- **Substitute**: Blocks contact and prevents both effects
- **Cloud Nine/Air Lock**: Negates weather benefits

### Item Synergies
- **Icy Rock**: Extends hail duration for maximum field control
- **Leftovers**: Offsets hail damage for non-Ice teammates
- **Rocky Helmet**: Additional contact punishment
- **Never-Melt Ice**: Boosts ice-type moves in created hail
- **Safety Goggles**: Protects allies from hail damage

### Competitive Usage
- **Weather setter**: Alternative to Abomasnow/Alolan Ninetales
- **Defensive wall**: Multiple forms of contact punishment
- **Team enabler**: Sets up conditions for ice-type teammates
- **Field controller**: Manages battlefield conditions actively
- **Hybrid role**: Combines offense, defense, and support

### Pokemon Suitability
Ideal for Pokemon with:
- **Ice typing**: Natural synergy with hail and ice moves
- **High Defense**: Can survive contact moves to trigger effects
- **Contact moves**: Can actively summon hail through offense
- **Bulk**: Survives long enough to establish weather control
- **Support role**: Benefits team through weather and status

### Version History
- Elite Redux custom ability expanding on Freezing Point
- Designed for comprehensive ice-type battlefield control
- Part of weather manipulation ability expansion
- Combines status, weather, and immunity for unique gameplay