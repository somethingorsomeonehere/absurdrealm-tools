---
id: 27
name: Effect Spore
status: reviewed
character_count: 95
---

# Effect Spore - Ability ID 27

## In-Game Description
"30% chance to inflict SLP, PARA or PSN if hit by a contact move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by a contact move, 30% chance to inflict sleep, paralysis, or poison. Chosen randomly. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Effect Spore is a defensive ability that has a 30% chance to inflict one of three status conditions when the user is hit by a contact move. When triggered, it randomly selects between Sleep, Paralysis, or Poison with equal probability (33.33% each).

### Technical Implementation
```cpp
constexpr Ability EffectSpore = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK_NOT(IsPowderImmune(attacker, FALSE))
        CHECK(Random() % 100 < 30)

        switch (Random() % 3) {
            case 0: // Poison
            case 1: // Paralysis  
            case 2: // Sleep
        }
    },
    .breakable = TRUE,
    .powderImmune = TRUE,
};
```

### Activation Requirements
1. **Contact move**: Only physical moves that make contact
2. **On-hit effects apply**: Standard battle conditions
3. **30% trigger chance**: Checked before status selection
4. **No powder immunity**: Target must not be immune to powder effects

### Status Distribution
When Effect Spore triggers:
- **33.33%** chance for Poison
- **33.33%** chance for Paralysis
- **33.33%** chance for Sleep

### Immunities and Protections
**Complete immunity from:**
- Grass-type Pokemon (powder immunity)
- Overcoat ability
- Safety Goggles item

**Status-specific immunities:**
- Electric-types can't be paralyzed
- Poison/Steel-types can't be poisoned
- Pokemon with Insomnia/Vital Spirit can't be put to sleep
- Already statused Pokemon can't receive a second status

### Ability Properties
- **Breakable**: Can be suppressed by Mold Breaker
- **Powder-based**: Treated as a powder effect for immunity purposes
- **AI Rating**: 4/10 (moderate defensive value)

### Pokemon with Effect Spore
**Common users:**
- Paras/Parasect (mushroom theme)
- Shroomish/Breloom  
- Foongus/Amoonguss
- Morelull/Shiinotic
- Other mushroom/spore themed Pokemon

**Also available to:**
- Cutiefly/Ribombee (innate ability)
- Gossifleur/Eldegoss (cotton spores)
- Various Pokemon through Elite Redux's expanded ability system

### Strategic Implications
- **Physical deterrent**: Discourages contact moves
- **RNG protection**: Unreliable but potentially game-changing
- **Multi-hit vulnerability**: Each hit has separate 30% chance
- **Status roulette**: Opponent can't predict which status they'll receive

### Synergies
- **Defensive builds**: Works well on bulky Pokemon that take multiple hits
- **Substitute**: Effect Spore still triggers when Substitute is hit
- **Rocky Helmet**: Stacks chip damage with status chance
- **Regenerator**: Can switch out and heal while opponent deals with status

### Counters
- Special attackers (no contact)
- Grass-type attackers (immune)
- Overcoat ability users
- Safety Goggles holders
- Long Reach ability
- Non-contact physical moves
- Protective Pads item

### Competitive Usage Notes
Effect Spore provides decent defensive utility but suffers from unreliability. The 30% activation rate and random status selection make it difficult to build strategies around. However, it can swing matches when it activates at crucial moments, particularly landing sleep. Best used on Pokemon that naturally want to absorb physical hits and can capitalize on any of the three status conditions.

### AI Behavior
The AI considers Effect Spore when deciding whether to use contact moves, applying a small penalty (10% adjusted chance) to account for potential status. It weighs all three possible statuses equally when making decisions.

### Version History
Effect Spore has remained mechanically consistent throughout generations. The main changes have been clarifications on its powder-based nature and interactions with new items/abilities that provide powder immunity.