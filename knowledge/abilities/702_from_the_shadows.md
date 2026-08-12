---
id: 702
name: From the Shadows
status: reviewed
character_count: 215
---

# From the Shadows - Ability ID 702

## In-Game Description
"Attacks trap and have a 20% flinch chance when moving first."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user moves first in a turn, attacks gain a 20% chance to flinch and trap the target on hit. The trap effect applies regardless of flinch success. Flinch chance only works on the first hit of multihit moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
From the Shadows is an offensive ability that combines trapping mechanics with conditional flinch chance. It has two distinct effects that trigger on successful attacks.

### Primary Effect: Trapping
- **Always active**: Every successful attack traps the target
- **Escape prevention**: Target cannot switch out or flee
- **Similar to moves**: Block, Mean Look, Spider Web
- **Persistent**: Effect remains until the user switches out or faints
- **Override protection**: Bypasses most switching abilities and items

### Secondary Effect: Flinch Chance
- **Speed dependent**: Only triggers when moving first in turn order
- **20% chance**: Applied to eligible moves when speed condition is met
- **Move restrictions**: Only works on moves that can normally cause flinch
- **Turn order check**: Compares battler turn positions, not raw speed stats

### Activation Conditions
- **Attack requirement**: Must successfully hit the target
- **Move eligibility**: For flinch, move must be able to have extra flinch chance
- **Speed priority**: For flinch, user must act before target in turn order
- **No immunities**: Target must not be immune to the specific effects

### Technical Implementation
```c
// From the Shadows implementation
constexpr Ability FromTheShadows = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(GetBattlerTurnOrderNum(target) >= gCurrentTurnActionNumber)

        // 20% flinch chance when moving first
        if (CanMoveHaveExtraFlinchChance(move) && Random() % 100 < 20) {
            AbilityStatusEffectDirect(MOVE_EFFECT_FLINCH);
        }

        // Always trap the target
        CHECK_NOT(gBattleMons[target].status2 & STATUS2_ESCAPE_PREVENTION)
        gBattleMons[target].status2 |= STATUS2_ESCAPE_PREVENTION;
        gVolatileStructs[target].battlerPreventingEscape = battler;
        BattleScriptCall(BattleScript_AnnounceTargetTrapped);
        return TRUE;
    },
};
```

### Turn Order Mechanics
- **Priority moves**: User with higher priority moves first regardless of speed
- **Speed ties**: Determined by actual speed stats and random factors
- **Trick Room**: Slower Pokemon move first, affecting flinch activation
- **Action timing**: Checks position in turn queue, not raw speed values

### Important Interactions
- **Multi-hit moves**: Each hit can potentially flinch and trap applies once
- **Substitute**: Trapping effect works through Substitute
- **Ghost types**: Cannot be trapped by normal means, but this ability bypasses immunity
- **Arena Trap immunity**: Flying types and Levitate are still trapped
- **Magnet Rise**: Doesn't prevent trapping from this ability

### Flinch Mechanics Detail
- **Move compatibility**: Only works on moves that can normally have flinch chance
- **Status moves**: Generally don't qualify for extra flinch chance
- **Already flinching moves**: Stacks with natural flinch chance
- **Flinch immunity**: Inner Focus and similar abilities prevent the flinch
- **Same turn**: Flinch only affects the next turn, not current action

### Strategic Applications
- **Speed control**: Encourages investment in speed for flinch consistency
- **Trapping utility**: Guarantees targets can't escape prediction
- **Revenge killing**: Excellent for revenge scenarios with speed advantage
- **Setup prevention**: Traps setup sweepers and forces confrontation
- **Pivot denial**: Prevents opponents from switching momentum

### Counters and Limitations
- **Speed control**: Slower opponents avoid flinch chance
- **Priority moves**: Can bypass speed-based flinch activation
- **Flinch immunity**: Inner Focus, Shield Dust block flinch component
- **Ghost immunity**: Ghost types cannot be trapped (traditional rules)
- **U-turn/Volt Switch**: May allow escape before trap applies
- **Fainting**: User fainting releases all trapped targets

### Team Synergies
- **Speed support**: Tailwind, Agility support maximizes flinch chance
- **Priority moves**: Ensures first move advantage for activation
- **Choice items**: Speed boost items increase flinch reliability
- **Trick Room teams**: Can work as anti-setup in reverse speed scenarios
- **Entry hazards**: Trapped opponents take guaranteed damage

### Competitive Usage Notes
- **Role compression**: Combines speed-based offense with trapping utility
- **Prediction tool**: Forces opponents into specific play patterns
- **Anti-switching**: Excellent against momentum-based strategies
- **Setup counter**: Traps and potentially flinches setup attempts
- **Speed tier important**: Effectiveness tied to speed investment and team support

### Move Compatibility
Flinch chance works with moves that can normally have enhanced flinch rates:
- **Physical attacks**: Most contact and non-contact physical moves
- **Special attacks**: Most damaging special moves
- **Multi-hit moves**: Each hit can trigger flinch independently
- **Status moves**: Generally excluded from flinch enhancement

### Version History
- Custom ability in Elite Redux
- Part of the expanded ability roster
- Designed for speed-based offensive pressure
- Combines classic trapping with modern flinch mechanics

### Thematic Design
From the Shadows represents an ambush predator that strikes from concealment, trapping prey while using speed and surprise to create openings. The ability rewards aggressive, fast-paced play while providing utility through escape denial.