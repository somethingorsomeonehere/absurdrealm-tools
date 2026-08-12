---
id: 170
name: Magician
status: reviewed
character_count: 165
---

# Magician - Ability ID 170

## In-Game Description
"Steals the foe's held item after using a non-contact move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user steals the target's held item when landing a non-contact move if they are currently holding no item. Does not work with Mega Stones and other similar items.

## Detailed Mechanical Explanation

Magician is a non-contact move-triggered ability that allows the holder to steal the opponent's held item when using non-contact moves. This theft mechanic provides strategic item disruption and acquisition, making it particularly valuable for special attackers and status move users.

### Activation Conditions
- Triggers when the Pokemon with Magician uses a **non-contact move**
- The target must take damage from the attack
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
- **Works through Substitute** - Unlike many abilities, Magician bypasses substitutes
- **Priority System** - If multiple Pokemon could trigger item theft, one is randomly selected
- **Immediate Effect** - Stolen items take effect immediately (e.g., Choice items, Leftovers)
- **Ability Popup** - Shows ability activation animation when successful
- **Sheer Force** - Does not activate if holder has Sheer Force and uses a boosted move

### Key Difference from Pickpocket
- **Pickpocket** triggers when hit by contact moves (defensive theft)
- **Magician** triggers when using non-contact moves (offensive theft)
- Same underlying mechanics, but opposite activation conditions

### Battle Flow
1. Pokemon with Magician uses non-contact move
2. Damage is dealt to target
3. Game checks if Magician can activate
4. If successful, item is transferred
5. Ability popup appears
6. Stolen item effects activate immediately

## Competitive Analysis

### Strengths
- **Item Disruption** - Removes crucial items like Choice items, Leftovers, or Life Orb
- **Resource Gain** - Can acquire beneficial items mid-battle
- **Offensive Control** - Player chooses when to trigger via move selection
- **Special Attacker Synergy** - Perfect for non-contact special moves
- **Substitute Bypass** - Works even through protective substitutes

### Weaknesses
- **Requires Empty Slot** - Must not be holding an item to function
- **Non-Contact Dependency** - Useless if relying on contact moves
- **One-Time Use** - Once an item is stolen, ability becomes inactive
- **Predictable** - Opponents can prepare for item theft attempts

### Strategy Tips
- **Special Attacker Focus** - Ideal for Pokemon with strong special movesets
- **Status Move Synergy** - Works with damaging status moves if they don't make contact
- **Choice Item Counter** - Excellent against Choice-locked opponents
- **Utility Theft** - Can steal utility items like Leftovers, Rocky Helmet, etc.

## Known Pokemon with Magician
Three Pokemon currently have access to Magician in Elite Redux:

### Klefki
- **Type:** Steel/Fairy
- **Role:** Support/Utility
- **Stats:** 57/80/91/80/87/75
- **Other Abilities:** Magic Guard, Friend Guard
- **Strategy:** Perfect defensive utility Pokemon with item disruption capability

### Hoopa Unbound
- **Type:** Psychic/Dark  
- **Role:** Offensive Powerhouse
- **Stats:** 80/170/60/160/130/80
- **Other Abilities:** Intimidate, Long Reach
- **Strategy:** Devastating mixed attacker that can steal items while dealing massive damage

### Meowscarada
- **Type:** Grass/Dark
- **Role:** Fast Physical/Special Hybrid
- **Stats:** 81/110/70/81/70/123
- **Other Abilities:** Magic Bounce, Magic Guard
- **Category:** Literally the "Magician Pokemon"
- **Strategy:** High-speed attacker with excellent type coverage and utility

## History and Trivia
- Introduced in Generation VI (X/Y)
- Originally associated with the Fennekin evolution line
- Represents the classic "magician's trick" of making items disappear
- Thematically opposite to Pickpocket - active vs passive theft
- Meowscarada is categorized as the "Magician Pokemon" species

## See Also
- **Pickpocket** - Complementary ability that triggers on contact moves
- **Sticky Hold** - Direct counter to Magician
- **Knock Off** - Move that removes items
- **Thief/Covet** - Moves that steal items
- **Magic Guard** - Often paired with Magician on the same Pokemon