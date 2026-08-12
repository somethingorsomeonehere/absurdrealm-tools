---
id: 251
name: Screen Cleaner
status: reviewed
character_count: 255
---

# Screen Cleaner - Ability ID 251

## In-Game Description
"Clears screens and Aurora Veil from both sides on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Screen Cleaner removes all protective screens from both sides of the battlefield when the Pokemon enters battle. This eliminates Reflect, Light Screen, Aurora Veil, and Smokescreen from both your team and the opponent's team immediately upon switching in.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Activation:** Upon entry (when the Pokemon switches into battle)

**Effect:** Removes all of the following protective screens from both the user's side and the opponent's side:
- **Reflect** (reduces physical damage)
- **Light Screen** (reduces special damage) 
- **Aurora Veil** (reduces both physical and special damage, requires hail/snow)
- **Smokescreen** (reduces accuracy)

**Implementation Details:**
- Uses the `TryRemoveScreens()` function which checks both sides of the battlefield
- Removes the status flags and resets all associated timers to 0
- Only activates if there are actually screens present to remove
- Shows a switch-in message when screens are successfully removed
- This is an entry ability that triggers automatically upon switching in

**Strategic Applications:**
- **Screen Breaking:** Counter teams that rely on dual screens (Reflect + Light Screen)
- **Aurora Veil Counter:** Particularly effective against hail teams using Aurora Veil
- **Utility Support:** Clears both friendly and enemy screens, which can be advantageous or disadvantageous depending on the situation
- **Lead Pokemon:** Can be used as a lead to immediately clear any screens set by the opponent's lead

**Interactions:**
- Does not affect other entry hazards (Stealth Rock, Spikes, etc.)
- Does not affect stat boosts or other battle conditions
- Cannot be suppressed by abilities like Neutralizing Gas
- Works in all battle formats including singles and doubles

**Notable Considerations:**
- Removes screens from BOTH sides, so be careful not to remove your own beneficial screens
- Only activates if screens are actually present
- Cannot be blocked or prevented by other abilities
- The screen removal happens before other switch-in effects