---
id: 610
name: Poison Puppeteer
status: reviewed
character_count: 93
---

# Poison Puppeteer - Ability ID 610

## In-Game Description
"When any Pokemon becomes poisoned, all opponents that can be confused become confused."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user applies poison, they also apply confusion. Does not activate from Toxic Spikes.

## Detailed Mechanical Explanation

### Implementation Details

### Code Location
- **Definition**: `src/abilities.cc` line 6423-6434
- **Battle Script**: `BattleScript_PoisonPuppeteer` in `data/battle_scripts_1.s`
- **Trigger**: `MOVE_EFFECT_POISON` via `setStateOnEffect`

### Mechanical Behavior
- Uses `PoisonPuppeteerClone` function to iterate through all battlers
- Triggers on the `onReactive` hook when poison status is applied
- Calls `CanBeConfused(target)` to validate confusion eligibility
- Ignores Substitute, Safeguard, and passive damage flags
- Only affects opponents who aren't already confused and lack confusion immunity

### Strategic Applications
**Offensive Synergy**: Pairs excellently with poison-spreading moves like Toxic Spikes, Poison Gas, or abilities like Toxic Chain. Multi-target poison effects create widespread confusion.

**Defensive Utility**: Punishes contact moves that trigger Poison Point or abilities that inflict poison on switch-in, creating immediate battlefield control.

**Counter-Strategy**: Opponents using Poison-type moves or abilities become vulnerable to mass confusion, turning their offensive strategy against them.

### Pokemon with This Ability

### Spiritomb Redux (Psychic/Poison)
- **Role**: Innate ability alongside Scare and Cosmic Daze
- **Stats**: 77/60/108/117/120/35 - Defensive special attacker
- **Synergy**: Can learn poison moves to trigger its own ability

### Pecharunt (Poison/Ghost)
- **Role**: Innate ability alongside Levitate and Toxic Chain  
- **Stats**: 88/88/160/88/88/88 - Balanced defensive pivot
- **Synergy**: Toxic Chain provides 30% poison chance, triggering Poison Puppeteer

### Related Abilities
- **Toxic Chain**: Creates poison opportunities for Poison Puppeteer
- **Parasitic Spores**: Another poison-based ability that spreads status
- **Entrance**: Uses same `PoisonPuppeteerClone` framework for attraction

### Battle Applications
1. **Status Spreading**: Combine with Toxic Spikes or Poison Gas for mass confusion
2. **Revenge Punishment**: Punish opponent's poison strategies with confusion
3. **Control Setup**: Use confusion to disrupt opponent's offensive momentum
4. **Synergy Chains**: Stack with other status abilities for overwhelming pressure