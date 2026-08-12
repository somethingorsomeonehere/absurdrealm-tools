---
id: 124
name: Pickpocket
status: reviewed
character_count: 144
---

# Pickpocket - Ability ID 124

## In-Game Description
"Steals the foe's held item on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user steals the target's held item on contact if they are currently holding no item. Does not work with Mega Stones and other similar items.

## Detailed Mechanical Explanation

### Activation Conditions
- Triggers when the Pokemon with Pickpocket is hit by a **contact move**
- The Pokemon must take damage from the attack
- The move must not have "no effect" (type immunity, etc.)
- Activates during the MOVEEND phase after damage calculation

### Success Requirements
1. **Holder must have no item** - Cannot steal if already holding something
2. **Target must have a stealable item** - Some items cannot be stolen
3. **Target cannot have protective abilities**:
   - Sticky Hold prevents item theft
   - Supersweet Syrup prevents item theft
4. **Item must be removable** - Mega Stones, Z-Crystals, etc. cannot be stolen

### Special Interactions
- **Works through Substitute** - Unlike many abilities, Pickpocket bypasses substitutes
- **Priority System** - If multiple Pokemon could trigger Pickpocket, one is randomly selected
- **Immediate Effect** - Stolen items take effect immediately (e.g., Choice items, Leftovers)
- **Ability Popup** - Shows ability activation animation when successful
- **Sheer Force** - Does not activate if attacker has Sheer Force and uses a boosted move

### Battle Flow
1. Opponent uses contact move
2. Damage is dealt to Pickpocket holder
3. Game checks if Pickpocket can activate
4. If successful, item is transferred
5. Ability popup appears
6. Stolen item effects activate immediately

## Competitive Analysis

### Strengths
- **Item Disruption** - Removes crucial items like Choice items, Leftovers, or Life Orb
- **Resource Gain** - Can acquire beneficial items mid-battle
- **No Turn Cost** - Activates passively without using a move
- **Substitute Bypass** - Works even through protective substitutes

### Weaknesses
- **Requires Empty Slot** - Must not be holding an item to function
- **Contact Dependency** - Useless against special attackers or status moves
- **One-Time Use** - Once an item is stolen, ability becomes inactive
- **Predictable** - Opponents can play around it by avoiding contact moves

### Strategy Tips
- **Lead Position** - Effective on leads to disrupt opponent's initial strategy
- **Knock Off Synergy** - Pair with Knock Off users to create item-stealing opportunities
- **Defensive Builds** - Works well on bulky Pokemon that can take multiple hits
- **Anti-Choice** - Particularly effective against Choice item users who get locked into contact moves

## Known Pokemon with Pickpocket
Several Pokemon lines have access to Pickpocket, often as a secondary ability option:
- Dark-type trickster Pokemon (fitting the thief theme)
- Pokemon with deceptive or mischievous characteristics
- Often paired with other disruption-based abilities

## History and Trivia
- Introduced in Generation V (Black/White)
- One of several "theft" abilities alongside Magician
- Thematically represents opportunistic theft during close combat
- Animation shows a quick "snatch" effect when activating

## See Also
- **Magician** - Similar effect but triggers when using attacks
- **Sticky Hold** - Direct counter to Pickpocket
- **Knock Off** - Move that removes items
- **Thief/Covet** - Moves that steal items