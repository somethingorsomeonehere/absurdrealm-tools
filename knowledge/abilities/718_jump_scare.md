---
id: 718
name: Jump Scare
status: reviewed
character_count: 124
---

# Jump Scare - Ability ID 718

## In-Game Description
"Attacks with Astonish on first switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Astonish on switch in, a 40 BP Ghost-type Physical move with +3 priority that always causes flinching. Once per battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Jump Scare is an entry hazard ability that automatically uses the move Astonish when switching into battle. The ability has a one-time restriction per battle to prevent abuse through repeated switching.

### Activation Conditions
- **Entry timing**: Triggers immediately upon switching into battle
- **One-time use**: Only activates on the first switch-in per battle
- **Persistent tracking**: Uses single-use ability counter system
- **No restrictions**: Works regardless of opponent's type or abilities

### Move Properties (Astonish)
- **Type**: Ghost-type physical move
- **Power**: 40 base power
- **Accuracy**: 100% accuracy
- **Effect**: 100% chance to cause flinching
- **Priority**: +3 (moves before most other moves)
- **PP**: 10 (though irrelevant for ability use)
- **Contact**: Yes, triggers contact-based abilities

### Technical Implementation
```c
constexpr Ability JumpScare = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(GetSingleUseAbilityCounter(battler, ability)) 
        SetSingleUseAbilityCounter(battler, ability, TRUE);
        return UseEntryMove(battler, ability, MOVE_ASTONISH, 0);
    },
    .persistent = TRUE,
};
```

### Important Interactions
- **Flinch mechanics**: Target cannot move that turn if they haven't acted yet
- **Priority system**: +3 priority means it goes before most moves
- **Contact move**: Triggers abilities like Static, Rough Skin, etc.
- **Ghost typing**: Cannot affect Normal or Fighting types
- **One-time counter**: Persists through the entire battle
- **Switch timing**: Activates before opponent can act

### Strategic Implications
- **Surprise factor**: Catches opponents off-guard on first switch
- **Momentum control**: High priority flinch can disrupt opponent's setup
- **Entry threat**: Forces opponents to consider switch-in timing
- **Limited use**: Cannot be spammed through repeated switching
- **Type coverage**: Ghost-type attack provides unique damage typing

### Battle Timing
1. Pokemon switches into battle
2. Jump Scare checks if already used this battle
3. If not used, sets counter and uses Astonish
4. Astonish targets opposing Pokemon with +3 priority
5. 40 damage dealt (if not immune) and 100% flinch applied

### Competitive Usage
- **Lead potential**: Strong on lead Pokemon for immediate pressure
- **Pivot abuse**: One-time strong switch-in option
- **Setup disruption**: Can interrupt opponent's setup attempts
- **Psychological pressure**: Opponents must respect the threat
- **Limited utility**: Effectiveness decreases after first use

### Counters and Limitations
- **Type immunity**: Normal and Fighting types are immune
- **Ghost-type resistance**: Ghost types resist the damage
- **One-time only**: Cannot be used again in the same battle
- **Contact drawbacks**: User takes contact-based damage/effects
- **Protect/Detect**: Can be blocked by protection moves
- **Substitute**: Doesn't break through Substitute

### Synergies
- **Intimidate**: Combines well with attack-lowering entry
- **Choice items**: Doesn't lock into Astonish, preserves item flexibility
- **Pivot moves**: U-turn/Volt Switch after using the ability
- **Setup moves**: Can flinch opponent before they boost
- **Entry hazards**: Combines with Stealth Rock for chip damage

### Pokemon Distribution
- Found as innate ability on certain Ghost-type Pokemon
- Typically on Pokemon with mischievous or startling themes
- Complements naturally bulky or support-oriented Pokemon
- Often paired with other entry abilities or intimidation effects

### Version History
- Custom ability in Elite Redux
- Designed to provide entry pressure without being overpowered
- One-time restriction prevents switch abuse
- Uses existing Astonish move for consistency