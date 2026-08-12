---
id: 31
name: Lightning Rod
status: reviewed
character_count: 158
---

# Lightning Rod - Ability ID 31

## In-Game Description
"Redirects Electric moves. Absorbs them, ups highest Atk."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user draws in Electric-type moves and gains immunity to them. Additionally, Electric-type moves boost the highest attacking stat of the user by one stage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Lightning Rod combines move redirection with absorption and stat boosting. It fundamentally changes Electric-type targeting in battle.

### Technical Implementation
From `/src/abilities.cc`:
```cpp
constexpr Ability LightningRod = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_ELECTRIC);
        *statId = GetHighestAttackingStatId(battler, TRUE);
        return ABSORB_RESULT_STAT;
    },
    .redirectType = TYPE_ELECTRIC,
    .breakable = TRUE,
};
```

### Key Mechanics

1. **Move Redirection**:
   - All Electric-type moves target the Lightning Rod user
   - Works in both singles and doubles
   - Overrides original target selection
   - Even draws Electric moves aimed at partner

2. **Absorption Effect**:
   - Electric moves deal 0 damage to Lightning Rod user
   - Triggers stat boost instead of damage
   - Works regardless of user's type

3. **Stat Boost Mechanism**:
   - Uses `GetHighestAttackingStatId(battler, TRUE)`
   - Compares Attack vs Special Attack (including modifiers)
   - Boosts the higher stat by +1 stage
   - Maximum boost is +6 stages

### Ability Properties
- **Breakable**: Can be suppressed by Mold Breaker
- **Type-specific**: Only affects Electric-type moves
- **Absorption-based**: Completely negates damage

### Move Interactions

**Redirected and absorbed:**
- Thunder, Thunderbolt, Thunder Shock
- Wild Charge, Volt Tackle
- Thunder Wave (absorbed, no paralysis)
- All Electric-type attacks

**NOT affected:**
- Non-Electric moves with paralysis chance
- Electric Terrain (field effect)
- Galvanize-boosted Normal moves (become Electric)

### Pokemon with Lightning Rod

**Changeable ability:**
- Rhyhorn/Rhydon/Rhyperior line
- Goldeen/Seaking
- Blitzle/Zebstrika
- Cubone/Marowak (Alolan)
- Various Electric-immune Pokemon

**Innate ability:**
- Goldeen/Seaking (also changeable)
- Morpekyll
- Several Elite Redux additions

### Strategic Applications

**Singles:**
- Complete Electric immunity
- Setup opportunity from Electric attacks
- Deters Electric move usage
- Stat boosting without setup moves

**Doubles/VGC:**
- Protects partner from Electric moves
- Enables Electric-weak partners
- Discharge becomes safe to use
- Creates targeting dilemmas

### Stat Boost Details
- Boosts Attack if Attack ≥ Special Attack
- Boosts Special Attack if Special Attack > Attack
- Considers stat stages in calculation
- +1 boost per absorbed Electric move
- Can reach +6 maximum

### Synergies
- **Ground-types**: Already immune, gain free boosts
- **Water/Flying types**: Cover Electric weakness
- **Mixed attackers**: Benefit from either stat boost
- **Discharge teams**: Safe Electric spread moves
- **Rain teams**: Counter to Thunder spam

### Advantages
- Immunity plus stat boost
- Partner protection in doubles
- Discourages Electric moves entirely
- No damage from redirected moves
- Works on status moves (Thunder Wave)

### Counters
- Mold Breaker abilities
- Non-Electric coverage moves
- Gastro Acid/Worry Seed
- Physical vs special targeting
- Setup punishment (Haze, Clear Smog)

### Competitive Usage Notes
Lightning Rod excels on Pokemon that:
1. Appreciate Electric immunity
2. Can utilize mixed offenses
3. Serve as doubles support
4. Already resist/immune to Electric

The ability transforms Electric attacks from threats into setup opportunities. In doubles, it enables powerful Electric-weak Pokemon like Gyarados or Pelipper to function safely. The dynamic stat boost choice rewards balanced offensive stats.

### Comparison to Similar Abilities
- **Storm Drain**: Water-type equivalent
- **Sap Sipper**: Grass-type equivalent  
- **Flash Fire**: Fire immunity + Fire boost
- **Motor Drive**: Electric immunity + Speed boost

### Notable Interactions
- Rhyperior: Ground/Rock with Lightning Rod creates double Electric immunity
- Seaking: Water-type gains Electric immunity, covering weakness
- Partner Gyarados: Enables safe Gyarados usage in doubles

### Version History
- Gen 3-4: Only redirected moves, no stat boost
- Gen 5+: Added immunity and Special Attack boost
- Elite Redux: Boosts highest attacking stat instead of just Special Attack