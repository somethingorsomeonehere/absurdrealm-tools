---
id: 629
name: Recurring Nightmare
status: reviewed
character_count: 187
---

# Recurring Nightmare - Ability ID 629

## In-Game Description
"Revives at 25% HP once after fainting in fog."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After fainting while fog is active, the user revives at 25% max Hp when sending out your next party member. This still activates when the user faints on the last turn of fog being active.

## Detailed Mechanical Explanation

**In-Game Name**: Shallow Grave

### Core Mechanics
- **Trigger Condition**: User must faint while fog weather is active (WEATHER_FOG_ANY)
- **Revival HP**: Returns with exactly 25% of maximum HP
- **Usage Limit**: Only triggers once per battle (persistent ability flag)
- **Weather Dependency**: Completely inactive without fog conditions
- **Battle Message**: "{Pokemon name} fades back into the fog!"

### Implementation Details
- **Ability Type**: Persistent (.persistent = TRUE)
- **Battle Script**: BattleScript_RecurringNightmare
- **String ID**: STRINGID_RECURRING_NIGHTMARE
- **In-Game Name**: "Shallow Grave"
- **Original Description**: "Revives at 25% HP once after fainting in fog."

### Strategic Applications
- **Fog Synergy**: Pairs perfectly with fog-summoning moves and abilities
- **Surprise Factor**: Opponents may not expect the revival mechanic
- **Extended Pressure**: Allows continued battle participation after apparent defeat
- **Weather Control**: Incentivizes maintaining fog conditions throughout battle
- **Defensive Utility**: Provides safety net for risky offensive strategies

### Technical Notes
- Persistent abilities remain active even when the Pokemon faints
- Revival occurs immediately after the fainting animation
- Does not stack with other revival effects
- Weather must be active at the moment of fainting
- One-time use restriction prevents infinite revival loops