---
id: 434
name: Elemental Charge
status: reviewed
character_count: 186
---

# Elemental Charge - Ability ID 434

## In-Game Description
"20% chance to BRN/FRZ/PARA with respective types."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Elemental Charge gives attacking moves a 20% chance to inflict status conditions based on move type: Electric moves cause paralysis, Fire moves cause burn, and Ice moves cause frostbite. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Elemental Charge is an offensive ability that provides a 20% chance to inflict type-based status conditions when using damaging moves of Electric, Fire, or Ice type. The ability only triggers on moves that successfully hit and deal damage to the target.

### Activation Conditions
- **Move requirement**: Must be a damaging move that hits the target
- **Type requirement**: Move must be Electric, Fire, or Ice type
- **Chance**: Exactly 20% activation rate (Random() % 100 < 20)
- **Target requirement**: Target must be susceptible to the respective status condition

### Status Effects by Type
- **Electric moves**: Inflict paralysis (if target can be paralyzed)
- **Fire moves**: Inflict burn (if target can be burned)
- **Ice moves**: Inflict frostbite (if target can get frostbite)

### Technical Implementation
```c
constexpr Ability ElementalCharge = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(Random() % 100 < 20)

        switch (moveType) {
            case TYPE_ELECTRIC:
                CHECK(CanBeParalyzed(battler, target))
                AbilityStatusEffect(MOVE_EFFECT_PARALYSIS);
                return TRUE;

            case TYPE_FIRE:
                CHECK(CanBeBurned(target))
                AbilityStatusEffect(MOVE_EFFECT_BURN);
                return TRUE;

            case TYPE_ICE:
                CHECK(CanGetFrostbite(target))
                AbilityStatusEffect(MOVE_EFFECT_FROSTBITE);
                return TRUE;
        }
        return FALSE;
    },
};
```

### Important Interactions
- **Multi-hit moves**: Each hit has an independent 20% chance to trigger
- **Substitute**: Blocked by Substitute, as it prevents direct hits
- **Type immunity**: Electric moves don't affect Ground types, etc.
- **Status immunity**: Doesn't work on targets immune to the respective status
- **Same-type moves only**: Only Electric, Fire, and Ice moves can trigger effects
- **Frostbite vs Freeze**: Ice moves inflict frostbite, not traditional freeze

### Status Condition Details
- **Paralysis**: 25% chance to be unable to move, Speed reduced by 50%
- **Burn**: Takes 1/16 max HP damage per turn, Attack reduced by 50%
- **Frostbite**: Elite Redux's version of freeze with gradual damage

### Strategic Implications
- **Mixed attackers**: Benefits Pokemon with diverse move pools across the three types
- **Status spreading**: Can cripple multiple opponents in doubles/triples
- **Revenge killer disruption**: Status effects can slow down or weaken threats
- **Type coverage synergy**: Natural fit for Pokemon with Electric/Fire/Ice coverage
- **Reliability**: 20% is significant but not overwhelming for balance

### Move Type Synergies
- **Electric moves**: Thunderbolt, Thunder, Volt Tackle, Wild Charge
- **Fire moves**: Flamethrower, Fire Blast, Flare Blitz, Fire Punch
- **Ice moves**: Ice Beam, Blizzard, Ice Punch, Icicle Crash

### Counters and Limitations
- **Status immunity**: Electric Terrain prevents paralysis, etc.
- **Type immunities**: Ground types immune to Electric moves
- **Substitute**: Blocks the ability entirely
- **Same-type restriction**: Normal, Fighting, etc. moves don't trigger
- **Multi-hit dilution**: Low chance per hit on multi-hit moves
- **Already statused**: Can't inflict status on already statused targets

### Common Users
Typically found on Pokemon with:
- Mixed offensive stats and diverse move pools
- Electric/Fire/Ice type coverage moves
- Roles as wallbreakers or revenge killers
- High attack frequency to maximize proc chances

### Competitive Usage Notes
- **Wallbreaking**: Status effects help break through defensive cores
- **Speed control**: Paralysis provides team speed control
- **Chip damage**: Burn and frostbite provide residual damage
- **Prediction reward**: Forces switches when status is threatened
- **Setup disruption**: Status can interrupt opponent setup attempts

### Ability Interactions
- **Guts**: Opponent benefits from burn (Attack boost)
- **Quick Feet**: Opponent benefits from paralysis/burn (Speed boost)
- **Magic Guard**: Opponent immune to burn/frostbite damage
- **Limber**: Opponent immune to paralysis
- **Water Veil**: Opponent immune to burn

### Team Building Considerations
- **Move diversity**: Maximize type coverage across Electric/Fire/Ice
- **Entry hazard support**: Chip damage stacks with status effects
- **Pivoting support**: U-turn/Volt Switch to maintain momentum
- **Speed tiers**: Consider paralysis for speed control needs
- **Stallbreaking**: Burn helps wear down defensive teams

### Version History
- Elite Redux exclusive ability
- Part of the expanded ability roster
- Designed to reward type diversity in movesets
- Balanced at 20% to avoid being oppressive

### Notable Interactions
- **Thunder Wave vs Elemental Charge paralysis**: Same effect, different source
- **Will-O-Wisp vs Elemental Charge burn**: Same effect, different trigger
- **Flame Orb/Toxic Orb**: Status item users unaffected by same status
- **Rest**: Can cure self-inflicted status from ability
- **Aromatherapy/Heal Bell**: Team can cure status inflicted by ability