---
id: 257
name: Pastel Veil
status: reviewed
character_count: 177
---

# Pastel Veil - Ability ID 257

## In-Game Description
"Casts Safeguard on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Pastel Veil automatically sets up Safeguard for the user's team when the Pokemon enters battle. Safeguard lasts for 5 turns and protects all team members from status conditions.

## Detailed Mechanical Explanation
*For Discord/reference use*

Pastel Veil is an entry ability that automatically activates Safeguard for the user's team when the Pokemon enters battle. The ability implementation:

### Core Mechanics
1. **Activation Trigger**: Activates on entry (switch-in or battle start)
2. **Condition Check**: Only activates if the user's side doesn't already have Safeguard active
3. **Duration**: Sets Safeguard for 5 turns (SCREEN_DURATION constant)
4. **Side Effect**: Affects the entire team, not just the user

### Safeguard Protection
Safeguard provides the following protections:
- **Status Immunity**: Protects against all major status conditions:
  - Burn
  - Freeze  
  - Paralysis
  - Poison (including badly poisoned)
  - Sleep
- **Coverage**: Protects all Pokemon on the user's side of the field
- **Duration**: Lasts for 5 turns after activation
- **Interaction**: Does not stack with existing Safeguard

### Technical Implementation
- **Function**: `PastelVeil` with `onEntry` trigger
- **Battle Script**: Uses `BattleScript_PastelVeilActivated`
- **Message**: "{Pokemon}'s Pastel Veil set up Safeguard!"
- **AI Scoring**: Treated as `AI_SCORE_SAFEGUARD` by battle AI

### Usage Notes
- Excellent for lead Pokemon to provide team-wide status protection
- Particularly valuable against status-heavy teams
- Can be used strategically to protect setup sweepers
- Multiple Pokemon with Pastel Veil won't stack the effect
- Works well with other entry abilities for comprehensive team support

### Pokemon Distribution
Available as both a regular ability and innate ability on various Pokemon throughout Elite Redux, often found on Fairy-type and support-oriented Pokemon.