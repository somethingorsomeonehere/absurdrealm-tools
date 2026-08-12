---
id: 199
name: Water Bubble
status: reviewed
character_count: 172
---

# Water Bubble - Ability ID 199

## In-Game Description
"Halves Fire dmg taken. Doubles Water dmg dealt. No burns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles the power of Water-type moves and reduces Fire-type damage taken by 50%. Also provides complete immunity to burns, removing existing burns upon gaining the ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

Water Bubble is a versatile defensive and offensive ability that provides three distinct benefits:

### Core Mechanics

1. **Water Move Power Boost**: Doubles the base power of all Water-type moves used by the bearer
   - Multiplicative 2.0x boost applied during damage calculation
   - Affects all Water-type moves, including special and physical attacks
   - Stacks with other damage multipliers like STAB and type effectiveness

2. **Fire Damage Resistance**: Reduces incoming Fire-type damage by 50%
   - Uses the same defensive multiplier as Heatproof ability
   - Applied as 0.5x resistance during damage calculation
   - Affects all Fire-type moves, both physical and special

3. **Burn Immunity**: Complete immunity to burn status condition
   - Prevents new burns from being inflicted
   - Automatically removes existing burn status when ability is gained
   - Uses the `removesStatusOnImmunity = TRUE` flag

### Technical Implementation

```cpp
constexpr Ability WaterBubble = {
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
        if (moveType == TYPE_WATER) MUL(2.0);
    },
    .onDefensiveMultiplier = Heatproof.onDefensiveMultiplier, // 0.5x Fire resistance
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_BURN)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Affected Moves
**Water-type moves receive 2.0x power boost:**
- All Water-type attacks (Surf, Hydro Pump, Scald, etc.)
- Both physical and special Water moves
- Multi-hit Water moves (each hit is boosted)
- Status moves are unaffected (power boost only applies to damaging moves)

### Interactions with Other Abilities/Mechanics

**Positive Synergies:**
- **STAB (Same Type Attack Bonus)**: Stacks multiplicatively for Water-types (2.0x from ability x 1.5x STAB = 3.0x total)
- **Weather effects**: Rain boosts stack with Water Bubble (Rain 1.5x x Water Bubble 2.0x = 3.0x)
- **Items**: Life Orb, Choice items, and type-boosting items stack multiplicatively
- **Abilities**: Swift Swim pairs well for Rain teams

**Ability Interactions:**
- **Mold Breaker/Turboblaze/Teravolt**: Can ignore Water Bubble's effects
- **Gastro Acid**: Removes Water Bubble and its benefits
- **Skill Swap/Role Play**: Can transfer Water Bubble to other Pokemon

**Fire Resistance Interactions:**
- Solar Power self-damage in sun is NOT reduced (not Fire-type damage)
- Burn damage over time is prevented entirely due to immunity
- Fire-type status moves (Will-O-Wisp) fail due to burn immunity

### Strategic Implications

**Offensive Usage:**
- Turns the bearer into a powerful Water-type attacker
- Allows non-Water types to function as Water specialists
- Rain team core member with doubled Water damage
- Excellent for mixed attackers using both physical and special Water moves

**Defensive Usage:**
- Natural Fire-type check with 50% damage reduction
- Burn immunity removes common status threat
- Can switch into Fire moves more safely
- Protects against burn-spreading moves

### Example Damage Calculations

**Water move with STAB and Water Bubble:**
- Base Water move: 100 BP
- STAB bonus: 100 x 1.5 = 150 BP
- Water Bubble: 150 x 2.0 = 300 effective BP

**Fire move against Water Bubble:**
- Base Fire move: 100 BP
- Water Bubble resistance: 100 x 0.5 = 50 effective BP received

### Common Users
In Elite Redux, Water Bubble is notably used by:
- Araquanid (signature Pokemon)
- Various other Pokemon through the game's expanded ability distribution
- Pokemon with access through ability-changing mechanics

### Competitive Usage Notes

**Strengths:**
- Massive Water-type damage output
- Reliable Fire resistance
- Status immunity utility
- No activation requirements
- Works immediately upon switching in

**Weaknesses:**
- Ability can be suppressed by Mold Breaker variants
- Removable through Gastro Acid
- Only affects one type offensively
- Fire resistance doesn't help against other types

### Counters
- **Mold Breaker family**: Ignores all Water Bubble effects
- **Gastro Acid**: Removes the ability entirely
- **Electric/Grass types**: Resist boosted Water moves
- **Water Absorb/Storm Drain**: Redirect/absorb boosted Water attacks
- **Dry Skin**: Takes reduced damage from boosted Water moves

### Version History
Water Bubble functions identically to its original Generation VII implementation, maintaining all three effects (Water boost, Fire resistance, burn immunity) in Elite Redux's expanded ability system.