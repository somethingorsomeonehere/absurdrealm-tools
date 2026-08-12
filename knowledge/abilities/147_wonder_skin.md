---
id: 147
name: Wonder Skin
status: reviewed
character_count: 104
---

# Wonder Skin - Ability ID 147

## In-Game Description
"Blocks most damage boosting and multihit abilities."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to all damage boosting ability effects from opponents, other than Parental Bond and Multi Headed.

## Detailed Mechanical Explanation
**Wonder Skin** is functionally **identical** to Fort Knox, providing comprehensive protection against offensive ability modifiers.

### Core Mechanics
Wonder Skin operates identically to Fort Knox:
- Set with the `fortKnox = TRUE` property
- Implemented with exactly the same code: `constexpr Ability WonderSkin = { .fortKnox = TRUE, };`
- Has the same description: "Blocks most damage boosting and multihit abilities"

### What Wonder Skin Blocks

#### Damage Boosting Abilities
Wonder Skin blocks **offensive multiplier abilities** by preventing them from activating against the Wonder Skin user:

**Major Damage Boosters:**
- Hustle (+40% physical damage)
- Flash Fire (+50% Fire damage when activated)
- Guts (+50% physical damage when statused)
- Plus/Minus (doubles damage with partner)
- Rivalry (+25% damage vs same gender)
- Swarm abilities (Overgrow, Blaze, Torrent, Swarm - +50% at low HP)
- Levitate (+25% Flying damage)
- And many other custom abilities with `onOffensiveMultiplier`

**Type-Based Boosts:**
- All -ate abilities (Pixilate, Refrigerate, etc.)
- Weather-specific damage boosts
- Terrain-based multipliers

#### Multihit Abilities
Blocks abilities using `onParentalBond` hook:
- Parental Bond (makes moves hit twice)
- Hyper Aggressive (makes moves hit twice)
- Multi Headed (2-3 hits based on heads)
- Primal Maw (double hit for bite moves)
- Dual Wield (double hit for certain moves)
- Raging Boxer (double hit for punch moves)
- And other abilities with `onParentalBond`

### "Blocking" Mechanics
When Wonder Skin "blocks" an ability:
- **Damage boosting**: The multiplier effect doesn't apply - no bonus damage is dealt
- **Multihit abilities**: The move only hits once instead of multiple times

The blocking occurs in the damage calculation phase (`CalculateAbilityMultipliers`) where the code checks `if (!hasFortKnox)` before applying offensive multipliers.

### Critical Exception
**Some abilities resist Fort Knox** with `resistsFortKnox = TRUE`:
- Parental Bond itself resists Fort Knox
- Multi Headed resists Fort Knox
- These can bypass Wonder Skin's protection

### Relationship to Fort Knox
Wonder Skin is **completely identical** to Fort Knox mechanically:
- Same internal implementation (`fortKnox = TRUE`)
- Same description and functionality
- Different names for thematic variety

This appears to be a design choice to give different Pokemon the same protective effect under different thematic names.

### Pokemon Distribution
Wonder Skin appears on defensive Pokemon like:
- Paldean Wooper
- Mega Swalot
- Furfrou Star Trim
- Terapagos Stellar
- Mega Clodsire

### Strategic Implications
Wonder Skin creates a powerful defensive wall against:
- Offensive ability strategies (Huge Power, Hustle, etc.)
- Multihit movesets (Parental Bond, Multi Headed, etc.)
- Weather-based attackers relying on ability boosts

This makes it particularly valuable in competitive play against setup sweepers and multihit attackers, forcing opponents to rely purely on base stats and move power rather than ability enhancements.
