---
id: 707
name: Gleam Eyes
status: reviewed
character_count: 242
---

# Gleam Eyes - Ability ID 707

## In-Game Description
"Frisk + Scare."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, reveals the opponents' items and prevents them from working for 2 turns; and the user drops the Special Attack stat of all opposing Pokemon by one stage. Does not prevent Mega Stones and other similar items from working. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Gleam Eyes is a combination ability that triggers two separate effects when the Pokemon enters battle:
1. **Frisk Effect**: Reveals and disables opposing Pokemon's held items
2. **Scare Effect**: Lowers opposing Pokemon's Special Attack by one stage

### Activation Conditions
- **Trigger**: Activates automatically when the Pokemon switches into battle
- **Targets**: Affects all opposing Pokemon on the field
- **Priority**: Both effects trigger simultaneously on entry

### Frisk Component
- **Item Detection**: Reveals what items the opposing Pokemon are holding
- **Item Disable**: Disables the effects of opposing Pokemon's held items for 2 turns
- **Scope**: Affects all opposing Pokemon currently on the field
- **Message**: Displays item information to the player

### Scare Component  
- **Stat Reduction**: Lowers opposing Pokemon's Special Attack by one stage
- **Implementation**: Uses the same mechanism as Intimidate but targets Sp. Attack instead of Attack
- **Resistance**: Can be blocked by abilities that prevent stat reduction (Clear Body, White Smoke, etc.)
- **Immunities**: Inner Focus, Own Tempo, Oblivious, Scrappy, and Overwhelm provide immunity

### Technical Implementation
```c
// Gleam Eyes combines UseIntimidateClone (Scare) + Frisk on entry
constexpr Ability GleamEyes = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseIntimidateClone(ability, battler) | Frisk.onEntry(DELEGATE_ENTRY); 
    },
};
```

### Important Interactions
- **Item Disable Duration**: 2 turns from activation, not affected by switching
- **Stat Stage Limits**: Cannot lower Sp. Attack below -6 stages
- **Multi-Battle**: Effects reset between battles
- **Substitutes**: Stat reduction blocked by Substitute, but Frisk still works
- **Trace/Role Play**: Can copy the ability but won't trigger entry effect until next switch

### Immunities and Resistances
**Scare Effect Blocked By:**
- Clear Body, White Smoke (stat change immunity)
- Inner Focus, Own Tempo, Oblivious (intimidation immunity)  
- Scrappy, Overwhelm (specifically immune to Scare/Intimidate)
- Hyper Cutter (if it protected Sp. Attack, but it doesn't in vanilla)

**Frisk Effect Blocked By:**
- No direct immunities, but some items may be unaffectable
- Still reveals items even if they can't be disabled

### Strategic Applications
- **Special Wall Counter**: Weakens special attackers before they can set up
- **Item Disruption**: Disables key items like Leftovers, Choice items, and berries
- **Lead Pokemon**: Excellent for leading to cripple opposing team setup
- **Pivot Support**: Great for switching in to disrupt opposing strategies
- **Doubles/Triples**: Affects multiple opponents simultaneously

### Team Building Synergies
- **Physical Attackers**: Pairs well with physical attackers who appreciate weakened special walls
- **Hazard Setters**: Works well with entry hazard users to stack pressure
- **Momentum Builders**: Good for maintaining offensive pressure
- **Status Users**: Creates openings for status moves against weakened foes

### Common Counters
- **Stat Immunity**: Clear Body family abilities
- **Intimidation Immunity**: Inner Focus, Own Tempo, Oblivious
- **Rapid Switching**: Switching out removes stat drops (but not item disable)
- **Special Physical Attackers**: Unaffected by Sp. Attack reduction
- **Mold Breaker**: Can ignore ability entirely

### Competitive Usage Notes
- **Entry Hazards**: Consider Stealth Rock damage when switching in frequently
- **Prediction Required**: Best used when opponent likely to stay in
- **Late Game**: Less effective when items already consumed
- **Speed Control**: Pair with faster Pokemon to capitalize on weakened foes

### Version History
- Custom ability in Elite Redux
- Combines existing Frisk and Scare mechanics
- Part of the expanded ability system for enhanced strategic depth

### Related Abilities
- **Intimidate** (lowers Attack instead of Sp. Attack)
- **Frisk** (reveals items but doesn't disable in vanilla)
- **Scare** (standalone Sp. Attack reduction)
- **Fearmonger** (Intimidate + Scare + contact paralysis)
- **Yuki Onna** (Scare + Intimidate + contact infatuation)