---
id: 386
name: Spectral Shroud
status: reviewed
character_count: 208
---

# Spectral Shroud - Ability ID 386

## In-Game Description
"Spectralize + 30% chance to badly poison the foe."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Ghost-type moves and grants STAB for Ghost-type moves, regardless of the user's typing. All Ghost-type moves have a 30% chance to badly poison targets after dealing damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Spectral Shroud combines two distinct effects implemented in `abilities.cc` (lines 3987-3999):

```c
constexpr Ability SpectralShroud = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBePoisoned(battler, target, MOVE_NONE))
        CHECK(gBattleStruct->ateBoost[battler])
        CHECK(moveType == TYPE_GHOST)
        CHECK(Random() % 100 < 30)

        return AbilityStatusEffect(MOVE_EFFECT_TOXIC);
    },
    .onOffensiveMultiplier = Spectralize.onOffensiveMultiplier,
    .onMoveType = Spectralize.onMoveType,
};
```

The ability inherits from Spectralize (lines 3983-3985), which uses the ATE_ABILITY macro:

```c
constexpr Ability Spectralize = {
    ATE_ABILITY(TYPE_GHOST),
};
```

### Type Conversion Effect (Spectralize Component)
- **Normal-to-Ghost Conversion**: All Normal-type moves become Ghost-type
- **STAB Bonus**: Converted moves gain 1.5x damage multiplier when used by Ghost-types (standard STAB)
- **ATE Boost**: Converted moves likely receive additional 1.1x power boost (based on other ATE abilities)
- **Cumulative Effect**: Total ~1.65x power for Ghost-types using converted Normal moves (1.5 x 1.1)

### Poison Effect
- **Trigger Condition**: Only activates on Ghost-type moves (including converted Normal moves)
- **Activation Rate**: 30% chance after dealing damage
- **Status Applied**: Badly Poison (increasing damage each turn: 1/16, 2/16, 3/16, etc.)
- **Requirements**: 
  - Move must hit and deal damage
  - Target must be poisonable
  - Target must not be immune to poison

### Battle Effects
**Move Conversions with Poison Chance:**
- **Return/Frustration**: Normal to Ghost, potential badly poison
- **Body Slam**: Normal to Ghost with paralysis chance + potential badly poison  
- **Double-Edge**: Normal to Ghost with recoil + potential badly poison
- **Hyper Beam**: Normal to Ghost + potential badly poison
- **Quick Attack**: Normal to Ghost priority + potential badly poison

**Natural Ghost Moves with Poison:**
- **Shadow Ball**: 30% chance to badly poison
- **Shadow Claw**: 30% chance to badly poison
- **Hex**: 30% chance to badly poison (increased damage vs already poisoned targets)
- **Phantom Force**: 30% chance to badly poison

### Pokemon with Spectral Shroud

#### As a Changeable Ability:
1. **Spiritomb (Redux Form)** - Psychic/Poison
   - Type: Psychic/Poison (gains STAB from converted Ghost moves)
   - Other Abilities: Toxic Surge, Headstrong
   - Innates: Scare, Poison Puppeteer, Cosmic Daze
   - Stats: 77/60/108/117/120/35 (bulky special attacker)

#### As an Innate Ability:
1. **Mega Crobat** - Poison/Flying
   - Has Spectral Shroud as innate along with Ominous Shroud and Nosferatu
   - Other Abilities: Amplifier, Low Visibility, Tinted Lens
   - Stats: 85/140/70/120/70/160 (fast mixed attacker)

### Strategic Implications

#### Offensive Potential
- **Type Coverage**: Normal moves become Ghost-type, hitting Fighting and Psychic for super effective damage
- **STAB Abuse**: Ghost-types gain significant power boost on converted Normal moves
- **Status Pressure**: 30% badly poison chance creates constant threat
- **Mixed Viability**: Works with both physical and special Normal moves

#### Status Strategy
- **Poison Stacking**: Badly poison compounds with other poison sources
- **Hex Synergy**: Ghost moves that inflict poison set up Hex for massive damage
- **Chip Damage**: Badly poison provides escalating residual damage
- **Stall Breaking**: Forces switches due to poison pressure

### Common Users

#### Spiritomb (Redux Form)
- **Role**: Bulky special attacker with poison support
- **Key Moves**: Shadow Ball, Psychic, Nasty Plot, Pain Split
- **Strategy**: Use bulk to set up Nasty Plot, then sweep with powered-up Ghost moves
- **Poison Synergy**: Badly poison punishes switches and supports stall

#### Mega Crobat
- **Role**: Fast mixed attacker with status utility
- **Key Moves**: U-turn, Brave Bird, Shadow Ball, Toxic
- **Strategy**: Hit-and-run tactics with poison chip damage
- **Speed Advantage**: Outspeeds most threats to land poison consistently

### Competitive Usage Notes
- **Tier Rating**: High - Combines offense with status utility
- **Team Role**: Mixed attacker/status spreader
- **Synergy**: Excellent with Hex users and poison cores
- **Versatility**: Adapts to both offensive and defensive team styles

### Counters
- **Poison Immunity**: Steel and Poison types immune to badly poison
- **Magic Bounce**: Reflects status moves (but not the on-hit effect)
- **Substitute**: Blocks the poison effect
- **Heal Bell/Aromatherapy**: Removes badly poison from team
- **Natural Cure**: Auto-heals poison on switch

### Anti-Counters
- **Steel Coverage**: Use Fire or Fighting moves against Steel types
- **Poison Breaking**: Fighting and Ground moves hit Poison types super effectively
- **Sub Breaking**: Multi-hit moves or strong attacks break Substitute
- **Priority**: Fast poison application before healing moves

### Synergies
- **Hex Users**: Teammates that can capitalize on poisoned targets
- **Poison Spikes**: Entry hazards compound poison pressure
- **Toxic**: Direct poison moves ensure status even if ability fails
- **Venoshock**: Increased damage against poisoned targets
- **Black Sludge**: Poison-types gain healing from held item

### Notable Combinations
- **Spectral Shroud + Hex**: Convert Normal moves to Ghost, poison with them, then use Hex for 130 BP
- **Spectral Shroud + Venoshock**: Poison with Ghost moves, then hit with 130 BP Venoshock
- **Spectral Shroud + Substitute**: Use Sub to safely fish for poison procs
- **Spectral Shroud + Choice Items**: Powerful Ghost moves with poison utility

### Version History
Spectral Shroud is an Elite Redux original ability that combines the established Spectralize effect with a unique poison application mechanic. It represents the pinnacle of offensive status abilities, providing immediate damage enhancement while building long-term pressure through badly poison.

### Implementation Details
- **File Location**: `src/abilities.cc` lines 3987-3999
- **Dependencies**: Uses Spectralize implementation and ATE_ABILITY macro
- **Random Check**: Uses Random() % 100 < 30 for poison activation
- **Status Function**: Calls AbilityStatusEffect(MOVE_EFFECT_TOXIC) for badly poison
- **Type Check**: Only triggers on Ghost-type moves (including converted ones)