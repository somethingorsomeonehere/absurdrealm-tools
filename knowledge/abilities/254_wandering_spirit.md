---
id: 254
name: Wandering Spirit
status: reviewed
character_count: 218
---

# Wandering Spirit - Ability ID 254

## In-Game Description
"Trades ability with attacker on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by a contact move, Wandering Spirit swaps abilities with the attacker. Both Pokemon regain their original ability upon switching out. Cannot swap with abilities that are also unable to be copied or suppressed.

## Detailed Mechanical Explanation
*For Discord/reference use*

Wandering Spirit is a unique defensive ability that creates strategic ability-swapping dynamics in battle:

### Activation Conditions
- **Trigger**: When the Pokemon with Wandering Spirit is hit by a contact move
- **Contact Requirement**: Only physical moves that make contact (like Tackle, Punch moves) trigger the effect
- **One-way Activation**: The defender must have Wandering Spirit; attackers with Wandering Spirit don't trigger swaps when attacking

### Restrictions and Immunities
The ability swap is blocked by several protective measures:
- **Ability Shield**: Held item that prevents ability changes
- **Persistent Abilities**: Abilities marked as persistent in the code cannot be swapped away
- **Unsuppressable Abilities**: Abilities like Neutralizing Gas that cannot be suppressed or changed
- **Same Ability**: If both Pokemon already have Wandering Spirit, no swap occurs

### Swap Mechanics
1. **Bidirectional Exchange**: Both Pokemon permanently exchange abilities
2. **Battle Duration**: The swap lasts for the entire battle, even through switches
3. **State Updates**: The game properly updates ability state indices for both Pokemon
4. **Multiple Activations**: If the new ability holder gets hit by contact again, another swap can occur

### Strategic Applications
- **Defensive Counter**: Steal powerful offensive abilities from physical attackers
- **Ability Denial**: Remove threatening abilities from opponents
- **Setup Prevention**: Disrupt opponents relying on specific abilities for their strategy
- **Risk/Reward**: Your opponent gains your ability, creating complex decision-making

### Notable Interactions
- Works with multi-hit contact moves (triggers on first hit)
- Can be activated by moves like U-turn or Volt Switch (contact + switching)
- Does not activate against special moves, even if they have contact-like animations
- Pairs well with abilities that are less useful to physical attackers (like Special Attack boosters)

### Comparison to Similar Abilities
- **Mummy**: Only spreads to attacker, doesn't swap
- **Trace**: Copies ability on entry, not on contact
- **Role Play**: Voluntary ability copying via move

Wandering Spirit represents one of the most disruptive defensive abilities in the game, capable of completely shifting battle dynamics through forced ability exchanges.