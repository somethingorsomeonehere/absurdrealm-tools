---
id: 233
name: Neuroforce
status: reviewed
character_count: 43
---

# Neuroforce - Ability ID 233

## In-Game Description
"Grants an additional 1.35x boost to Super-effective moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Super effective attacks are boosted by 35%.


## Detailed Mechanical Explanation
*For Discord/reference use*

**NEUROFORCE** is an offensive ability that provides additional damage amplification specifically for super-effective attacks.

### Core Mechanics:
- **Activation Condition**: Triggers when type effectiveness multiplier is 2.0x or higher
- **Damage Boost**: Applies 1.35x multiplier to super-effective moves
- **Stacking Calculation**: Multiplies with type effectiveness (2x becomes 2.7x, 4x becomes 5.4x)
- **No Announcement**: Ability works silently without battle message

### Technical Implementation:
```c
constexpr Ability Neuroforce = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (typeEffectivenessMultiplier >= UQ_4_12(2.0)) MUL(1.35);
        },
};
```

### Numerical Values:
- **2x Super Effective**: 2.0 x 1.35 = **2.7x total damage**
- **4x Double Super Effective**: 4.0 x 1.35 = **5.4x total damage**
- **Neutral/Resisted**: No boost applied (1x and 0.5x moves unchanged)

### Complete List of Affected Moves:
**All moves that deal super-effective damage receive the boost**, including:
- STAB moves hitting for super-effective damage
- Coverage moves with type advantage
- Multi-type moves like Flying Press (if super-effective)
- Moves with changed effectiveness due to abilities (e.g., Scrappy making Normal/Fighting hit Ghost)

### Interactions with Other Abilities/Mechanics:
1. **Type-Changing Abilities**: 
   - Protean/Libero: Neuroforce applies if the new type creates super-effective matchup
   - Normalize: Removes type effectiveness, so Neuroforce won't activate

2. **Effectiveness-Modifying Abilities**:
   - Scrappy: If Normal/Fighting becomes super-effective vs Ghost, Neuroforce applies
   - Tinted Lens: Works independently (Tinted Lens affects resisted moves, Neuroforce affects super-effective)

3. **Other Damage Multipliers**:
   - **STAB**: 1.5x x 2x (type) x 1.35x (Neuroforce) = 4.05x total
   - **Life Orb**: 1.3x x 2x (type) x 1.35x (Neuroforce) = 3.51x total
   - **Choice Items**: 1.5x x 2x (type) x 1.35x (Neuroforce) = 4.05x total

### Strategic Implications:
- **Wallbreaking**: Turns moderate super-effective hits into devastating attacks
- **Coverage Priority**: Rewards diverse movesets with good type coverage
- **Switch Punishment**: Makes switching into super-effective moves extremely risky
- **Synergy with Mixed Attackers**: Benefits both physical and special super-effective moves

### Example Damage Calculations:
**Scenario**: Neuroforce Pokemon with 100 Attack using 80 BP move
- **Against Normal Effectiveness**: 80 BP x 1.0 = 80 effective BP
- **Against Super Effective**: 80 BP x 2.0 x 1.35 = 216 effective BP
- **Against Double Super Effective**: 80 BP x 4.0 x 1.35 = 432 effective BP

### Common Users in Elite Redux:
Based on the species analysis, notable Neuroforce users include:
- **Tentacruel**: Fast special attacker with diverse coverage
- **Crobat**: High-speed physical attacker
- **Kingdra**: Mixed attacker with good movepool
- **Mewtwo variants**: Legendary with incredible offensive stats
- **Ultra Necrozma**: Psychic/Steel type with powerful moves
- **Blastoise variants**: Bulky attacker with Mega Launcher synergy

### Competitive Usage Notes:
- **Team Role**: Excellent on wallbreakers and late-game sweepers
- **Movepool Importance**: More valuable on Pokemon with diverse type coverage
- **Speed Considerations**: Most effective on fast Pokemon that can outspeed and OHKO
- **Item Synergy**: Works well with Life Orb, Choice items, and Z-Moves (if implemented)

### Counters and Defensive Strategies:
- **Resist Super-Effective Moves**: Use Pokemon that resist the user's main STAB
- **Bulk Up**: Extremely bulky Pokemon can still survive boosted super-effective hits
- **Priority Moves**: Revenge kill with priority before the Neuroforce user can attack
- **Status Conditions**: Burn halves physical attack power, negating much of the boost

### Synergies:
1. **Speed Control**: Tailwind, Trick Room, or Speed Boost to ensure attacks land first
2. **Entry Hazards**: Stealth Rock weakens switch-ins, making Neuroforce OHKOs more likely
3. **Dual Screens**: Helps the user survive long enough to fire off super-effective attacks
4. **Setup Moves**: Nasty Plot, Dragon Dance, etc. to further amplify the boosted damage

### Ability Combinations in Multi-Ability System:
- **Neuroforce + Analytic**: Calculative ability (slower but more powerful)
- **Neuroforce + Beast Boost**: Snowball effect after securing KOs
- **Neuroforce + Levitate**: Immunity to Ground moves while boosting super-effective attacks

### Version History:
- **Gen 7**: Introduced as Necrozma's signature ability with 1.25x multiplier
- **Elite Redux**: Enhanced to 1.35x multiplier and distributed to multiple Pokemon through the expanded ability system
- **Current**: Maintains 1.35x boost, available as both regular and innate ability on various species