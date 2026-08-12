---
id: 337
name: Raw Wood
status: reviewed
character_count: 168
---

# Raw Wood - Ability ID 337

## In-Game Description
"Halves dmg taken by Grass moves. Boosts own Grass moves by 1.2x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from Grass-type attacks by 50% while boosting the power of the user's own Grass-type moves by 20%. Damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Raw Wood provides a **dual-type interaction** with Grass-type moves:
- **Defensive:** **0.5x damage multiplier** (50% damage reduction) against all incoming Grass-type attacks
- **Offensive:** **1.2x damage multiplier** (20% damage boost) for all outgoing Grass-type moves

This creates a unique offensive-defensive synergy that makes the Pokemon both resistant to and empowered by Grass-type moves.

### Activation Conditions
**Defensive Effect:**
- Triggers automatically against **any Grass-type move** targeting the Pokemon
- Works against both physical and special Grass attacks
- Functions regardless of the attacking Pokemon's ability or move properties

**Offensive Effect:**
- Triggers automatically when the Pokemon uses **any Grass-type move**
- Applies to both physical and special Grass attacks
- Stacks with other damage-boosting effects

### Technical Implementation
```cpp
constexpr Ability RawWood = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_GRASS) MUL(1.2);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_GRASS) RESISTANCE(.5);
        },
    .breakable = TRUE,
};
```

Location: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 3563-3573)

### Affected Move Types
**Grass-type moves** (both offensive and defensive effects):
- Energy Ball
- Leaf Storm
- Power Whip
- Seed Bomb
- Solar Beam
- Petal Dance
- Grass Knot
- Leaf Blade
- Giga Drain
- Wood Hammer

### Damage Calculation Examples
**Defensive (incoming Grass moves):**
- 100 BP Grass move to 50% damage (50 BP effective)
- 120 BP Leaf Storm to 60 BP effective damage

**Offensive (outgoing Grass moves):**
- 100 BP Energy Ball to 120 BP effective power
- 120 BP Leaf Storm to 144 BP effective power

### Interactions with Other Mechanics

**Can be bypassed by:**
- Mold Breaker and similar abilities (marked as `breakable = TRUE`)
- Abilities that ignore defensive abilities (defensive effect only)

**Does NOT affect:**
- Status effects from Grass moves (sleep from Sleep Powder, etc.)
- Indirect damage (poison, weather, entry hazards)
- Multi-type moves (only affects pure Grass-type moves)

**Stacks with:**
- Type advantages/disadvantages (0.5x Fire resistance + 0.5x Raw Wood = 0.25x vs Grass)
- STAB (Same Type Attack Bonus) - 1.2x Raw Wood + 1.5x STAB = 1.8x total boost
- Other damage-boosting abilities and items
- Critical hits and other multipliers

### Strategic Implications

**Dual-Role Synergy:**
- Exceptional for Grass-type Pokemon that both dish out and receive Grass attacks
- Creates unique positioning against Grass-heavy teams
- Enables aggressive play while maintaining defensive utility

**Offensive Value:**
- 20% damage boost makes Grass moves significantly more threatening
- Combines excellently with high-BP Grass moves like Leaf Storm
- Enhances STAB effectiveness for Grass-type users

**Defensive Value:**
- Strong switch-in potential against Grass attackers
- Reduces effectiveness of opposing Grass-type cores
- Provides insurance against Grass-type revenge killers

### Common Users in Elite Redux
**Pokemon with Raw Wood as Innate Ability:**
- **Sudowoodo** - Rock-type that gains Grass synergy despite typing
- **Bonsly** - Pre-evolution with early game defensive utility
- **Ogerpon** - Grass-type that maximizes both offensive and defensive benefits
- **Duelumber** - Likely a Grass/Rock or similar dual-type with strong synergy

**Notable Users (Regular Ability):**
- Several other species have access to Raw Wood as a changeable ability
- Particularly effective on Pokemon with strong Grass-type movepools

### Competitive Usage Notes

**Tier Impact:**
- High value in formats with prevalent Grass-type attackers
- Creates unique niches for Pokemon that wouldn't normally counter Grass types
- Enables hybrid offensive-defensive strategies

**Common Strategies:**
- Pivot switching against Grass-type special attackers
- Wallbreaking with boosted Grass moves while maintaining defensive presence
- Supporting teams weak to Grass with reliable resistances

**Team Synergy:**
- Excellent partner for Pokemon weak to Grass attacks
- Provides both offensive and defensive utility in a single ability slot
- Creates unpredictable matchups against Grass-focused teams

### Counters and Limitations

**Direct Counters:**
- Mold Breaker abilities bypass both offensive and defensive effects
- Pokemon with non-Grass coverage moves ignore the defensive utility
- Fire-types resist boosted Grass moves despite the offensive boost

**Indirect Limitations:**
- Only affects one type (Grass) unlike broader abilities
- Breakable status means common abilities can nullify the effect
- Status effects from Grass moves still apply at full strength

### Unique Characteristics

**Dual-Effect Design:**
- One of the few abilities that provides both offensive and defensive benefits for the same type
- Creates interesting strategic decisions about when to use Grass moves
- Enables Pokemon to both wall and break Grass-type threats

**Type Specialist Identity:**
- Reinforces Grass-type identity even on non-Grass Pokemon
- Creates pseudo-Grass typing through ability interaction
- Unique thematic design connecting to wood/plant materials

### Version History
- New ability created for Elite Redux
- Part of the expanded ability system with unique type interactions
- Designed to create more diverse defensive and offensive options

### Synergistic Abilities
**Works well with:**
- **Chlorophyll** - Speed boost + Grass move power creates sweep potential
- **Overgrow** - Stacks with Raw Wood for massive Grass move damage when low HP
- **Regenerator** - Enhanced longevity with Grass resistance
- **Solar Power** - Sun teams that benefit from boosted Grass moves

**Competitive Combinations:**
- Raw Wood + Grass STAB + Choice items = extremely powerful Grass attacks
- Pairs excellently with recovery moves for sustained presence
- Enhances the effectiveness of Grass-type movepool diversity

### Calculation Examples
**Full Damage Scenarios:**
- Grass-type with STAB + Raw Wood: 1.5x x 1.2x = 1.8x total boost
- Critical hit + Raw Wood: 1.5x x 1.2x = 1.8x total boost
- Choice Band + Raw Wood: 1.5x x 1.2x = 1.8x total boost

**Defensive Scenarios:**
- 2x weakness to Grass + Raw Wood: 2.0x x 0.5x = 1.0x neutral damage
- 0.5x resistance to Grass + Raw Wood: 0.5x x 0.5x = 0.25x total resistance
- Neutral typing + Raw Wood: 1.0x x 0.5x = 0.5x damage taken