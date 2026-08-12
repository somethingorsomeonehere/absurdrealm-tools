---
id: 210
name: Battle Bond
status: reviewed
character_count: 131
---

# Battle Bond - Ability ID 210

## In-Game Description
"Transforms into Battle Bond form after dealing a KO."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Battle Bond immediately triggers a form change when this Pokemon deals the finishing blow to an opposing Pokemon. Cannot be copied.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Battle Bond is an ability that triggers a permanent form change when the Pokemon with this ability deals a knockout blow to an opponent. The transformation occurs immediately after the target faints and cannot be reversed during battle.

### Activation Conditions
- The Pokemon must deliver the finishing blow that causes an opponent to faint
- Works on any knockout (direct damage, status effects, etc.) as long as this Pokemon is the attacker
- Triggers once per battle - subsequent KOs do not cause additional transformations
- Cannot be suppressed or negated by abilities like Mold Breaker

### Form Transformations and Stat Changes

**Greninja to Ash-Greninja:**
- Base: 72/100/67/103/71/122 (BST: 535)
- Transformed: 72/150/67/153/71/132 (BST: 645)
- Changes: +50 Attack, +50 Special Attack, +10 Speed

**Chesnaught to Clemont Form:**
- Base: 88/107/122/74/80/64 (BST: 535)  
- Transformed: 88/128/152/98/92/87 (BST: 645)
- Changes: +21 Attack, +30 Defense, +24 Special Attack, +12 Special Defense, +23 Speed

**Delphox to Serena Form:**
- Base: 75/69/72/114/100/105 (BST: 535)
- Transformed: 75/96/95/134/120/125 (BST: 645)
- Changes: +27 Attack, +23 Defense, +20 Special Attack, +20 Special Defense, +20 Speed

### Technical Implementation
```cpp
constexpr Ability BattleBond = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        SpeciesEnum newSpecies = SPECIES_NONE;
        switch (gBattleMons[battler].species) {
            case SPECIES_GRENINJA_BATTLE_BOND:
                newSpecies = SPECIES_GRENINJA_ASH;
                break;
            case SPECIES_CHESNAUGHT_BATTLE_BOND:
                newSpecies = SPECIES_CHESNAUGHT_CLEMONT;
                break;
            case SPECIES_DELPHOX_BATTLE_BOND:
                newSpecies = SPECIES_DELPHOX_SERENA;
                break;
            case SPECIES_DARMANITAN_REDUX_BOND:
                newSpecies = SPECIES_DARMANITAN_REDUX_BLUNDER;
                break;
        }
        // Updates species and triggers transformation animation
        UpdateAbilityStateIndicesForNewSpecies(battler, newSpecies);
        gBattleMons[battler].species = newSpecies;
        BattleScriptCall(BattleScript_BattleBondActivatesOnMoveEndAttacker);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
};
```

### Interactions with Other Mechanics
- **Transform/Imposter**: Cannot be copied or transformed into
- **Skill Swap/Role Play**: Cannot be transferred to other Pokemon
- **Gastro Acid/Neutralizing Gas**: Cannot be suppressed (unsuppressable = TRUE)
- **Randomizer**: Excluded from random ability assignment (randomizerBanned = TRUE)
- **Switching Out**: Transformation persists for the remainder of the battle
- **Status Conditions**: Transformation is not affected by sleep, paralysis, etc.

### Strategic Implications
- **Sweeping Potential**: The stat boosts make these Pokemon excellent late-game sweepers
- **Momentum Building**: Getting the first KO becomes crucial for unlocking full potential
- **Team Support**: Benefits from entry hazards and chip damage to secure KOs
- **Risk/Reward**: Must survive long enough to get a KO to activate the transformation

### Example Damage Calculations
**Greninja-Ash vs Toxapex (252 HP/252+ Def):**
- Pre-transformation: 103 SpA Water Shuriken = 35-42% (4HKO)
- Post-transformation: 153 SpA Water Shuriken = 52-61% (2HKO)

**Chesnaught-Clemont vs Landorus-T (252 HP/0 Atk):**
- Pre-transformation: 107 Atk Wood Hammer = 45-53% (2HKO)
- Post-transformation: 128 Atk Wood Hammer = 54-63% (2HKO, guaranteed with Stealth Rock)

### Common Users
- **Greninja-Battle Bond**: Most popular due to balanced offensive boosts
- **Chesnaught-Battle Bond**: Defensive pivot that becomes a mixed threat
- **Delphox-Battle Bond**: Balanced special attacker with improved bulk
- **Darmanitan-Redux Bond**: Elite Redux exclusive variant

### Competitive Usage Notes
- **Tier Placement**: Often restricted to higher tiers due to transformation potential
- **Set Diversity**: Can run mixed offensive or setup sets pre-transformation
- **Team Synergy**: Pairs well with hazard setters and pivot Pokemon
- **Meta Influence**: Forces opponents to play around potential transformations

### Counters
- **Priority Moves**: Can revenge kill before transformation benefits are utilized
- **Bulky Walls**: Can tank hits even after transformation
- **Status Effects**: Burn halves physical Attack boosts, paralysis reduces Speed
- **Entry Hazards**: Chip damage can limit switching opportunities

### Synergies
- **Stealth Rock**: Helps secure KOs for transformation
- **Healing Wish/Lunar Dance**: Can reset HP while keeping transformation
- **Speed Control**: Tailwind/Trick Room depending on form and strategy
- **Pivot Support**: U-turn/Volt Switch brings in safely for KO opportunities

### Version History
- **Elite Redux**: Expanded to include Kalos starters beyond just Greninja
- **Original**: Only Greninja had access in mainline games
- **Balance Changes**: Stat distributions carefully tuned for competitive balance