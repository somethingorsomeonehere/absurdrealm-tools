---
id: 80
name: Steadfast
status: reviewed
character_count: 43
---

# Steadfast - Ability ID 80

## In-Game Description
"Raises Speed by one stage if this Pokemon flinches."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Getting flinched raises Speed by one stage.

## Detailed Mechanical Explanation
*For Discord/reference use*

**STEADFAST** is a reactive ability that converts flinching from a disadvantage into a Speed boost opportunity.

### Activation Mechanics:
- **Trigger**: When the Pokemon flinches due to any move effect
- **Effect**: Raises Speed by one stage (+50% Speed)
- **Timing**: Activates immediately after the flinch prevents the move
- **Script**: Displays ability name and "Speed rose!" message

### Flinch Interaction:
1. **Flinch Occurs**: Pokemon takes damage and becomes unable to move
2. **Steadfast Triggers**: Speed +1 stage boost applied
3. **Turn Continues**: Other Pokemon can still act normally
4. **Next Turn**: Boosted Speed potentially allows first move

### Technical Implementation:
The ability is handled in the battle script system when flinching occurs:

```assembly
BattleScript_MoveUsedFlinched::
    printstring STRINGID_PKMNFLINCHED
    waitmessage B_WAIT_TIME_LONG
    setstatchanger STAT_SPEED, 1, FALSE
    callifability BS_ATTACKER, ABILITY_RATTLED, BattleScript_AttackerAbilityStatRaiseAndDoStatBuff
BattleScript_MoveUsedFlinched_CheckSteadfast:
    callifability BS_ATTACKER ABILITY_STEADFAST BattleScript_AttackerAbilityStatRaiseAndDoStatBuff
```

### Moves That Trigger Steadfast:
**Common Flinch Moves:**
- Fake Out (100% flinch, priority +3)
- Air Slash (30% flinch)
- Iron Head (30% flinch)
- Rock Slide (30% flinch)
- Bite (30% flinch)
- Headbutt (30% flinch)
- Twister (20% flinch)
- Stomp (30% flinch)
- Astonish (30% flinch)
- Zen Headbutt (20% flinch)

**High-Flinch Moves:**
- Fake Out: Guaranteed flinch on first turn
- King's Rock/Razor Fang: 10% flinch chance on any damaging move
- Serene Grace: Doubles flinch chances (e.g., Air Slash becomes 60%)

### Flinch Prevention:
The following abilities prevent flinching entirely, making Steadfast irrelevant:
- **Inner Focus**: Prevents flinching completely
- **Enlightened**: Custom ability that prevents flinching
- **Unlocked Potential**: Custom ability that prevents flinching
- **Way of Precision**: Custom ability that prevents flinching

### Ability Synergies:
1. **Rattled Combo**: Both abilities can trigger from the same flinch
   - Rattled boosts Speed when hit by Bug, Dark, Ghost moves
   - If such moves also cause flinch, both abilities activate
   - Result: Speed +2 stages total

2. **King's Rock/Razor Fang**: Held items add 10% flinch chance to moves
   - Increases opportunities for Steadfast activation
   - Particularly effective on multi-hit moves

3. **Serene Grace Users**: Facing Pokemon with Serene Grace doubles flinch chances
   - Air Slash becomes 60% flinch chance
   - More opportunities for Speed boosts

### Strategic Applications:
1. **Fake Out Counter**: Steadfast users can benefit from common Fake Out leads
2. **Speed Control**: Converts opponent's flinch strategies into Speed boosts
3. **Momentum Shifts**: Can turn defensive situations into offensive opportunities
4. **Anti-Flinch Tech**: Provides benefit where flinch immunity provides none

### Common Users:
- **Machamp**: Steadfast as regular ability (Machamp family)
- **Riolu/Lucario**: Steadfast as regular ability option
- **Meditite/Medicham**: Steadfast as regular ability option
- **Gallade**: Steadfast as regular ability option
- Various custom Pokemon in Elite Redux

### Competitive Considerations:
**Advantages:**
- Turns opponent's flinch strategies against them
- Can create unexpected Speed tiers after boost
- Combines well with other Speed-boosting effects
- Provides utility even when taking damage

**Disadvantages:**
- Requires taking damage to activate
- Opponent can avoid using flinch moves
- Situational activation makes it unreliable
- Competing with other powerful abilities

### Counters:
- Avoid using flinch-inducing moves against Steadfast users
- Use Inner Focus or other flinch immunity abilities
- Focus on non-flinching damage moves
- Priority moves can still outspeed even after boost

### Version History:
- **Gen 4**: Introduction of Steadfast ability
- **Elite Redux**: Maintained original functionality
- **Elite Redux**: Added to various custom Pokemon as regular or innate ability

### Edge Cases:
- If Pokemon is already at +6 Speed, Steadfast still attempts to activate but shows "won't go higher"
- Multiple sources of flinching in one turn only trigger Steadfast once
- Flinching from moves like Fake Out on switch-in can provide immediate Speed boost for subsequent turns