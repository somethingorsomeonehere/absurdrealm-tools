---
id: 728
name: Wind Rage
status: reviewed
character_count: 190
---

# Wind Rage - Ability ID 728

## In-Game Description
"Uses Defog on switch-in. Air-based moves get a 1.3x boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Defog on switch in. Lowers the opponent's evasion by one stage and clears all entry hazards, screens, Safeguard, and Mist. Additionally, all air-based moves receive a 1.3x damage boost.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Wind Rage is a dual-purpose ability that combines hazard control with offensive enhancement. It provides automatic Defog usage upon entry and boosts air-based moves by 30%.

### Entry Effect - Automatic Defog
- **Timing**: Activates immediately when the Pokemon switches into battle
- **Effect**: Automatically uses Defog with 0 BP (non-damaging version)
- **Targets cleared**:
  - All entry hazards on both sides (Spikes, Toxic Spikes, Stealth Rock, Sticky Web)
  - Light Screen and Reflect on opponent's side
  - Aurora Veil on opponent's side
  - Mist on opponent's side
- **Accuracy**: 100% success rate (cannot miss)
- **PP consumption**: Does not consume PP from Defog move

### Offensive Boost - Air-Based Moves
- **Multiplier**: 1.3x damage boost (30% increase)
- **Move criteria**: Any move with the `gBattleMoves[move].airBased` flag set to TRUE
- **Common air-based moves**:
  - Most Flying-type attacks (Air Slash, Brave Bird, Hurricane, etc.)
  - Some non-Flying moves like Gust, Twister
  - Wind-based moves regardless of type
- **Stacking**: Multiplies with other damage modifiers (STAB, type effectiveness, etc.)

### Technical Implementation
```c
constexpr Ability WindRage = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_DEFOG, 0); 
    },
    .onOffensiveMultiplier = GiantWings.onOffensiveMultiplier,
};

// GiantWings implementation (shared code):
constexpr Ability GiantWings = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].airBased) MUL(1.3);
        },
};
```

### Important Interactions
- **Entry hazard immunity**: Clears hazards before taking damage from them
- **Screen disruption**: Removes opponent's defensive screens
- **Multi-hit moves**: Each hit gets the 1.3x boost if air-based
- **Choice items**: Entry Defog doesn't lock into Defog move
- **Taunt immunity**: Entry Defog bypasses Taunt restrictions
- **Magic Bounce/Mirror Armor**: Entry Defog cannot be reflected
- **Substitute**: Entry Defog bypasses Substitute

### Air-Based Move List
Wind Rage boosts any move flagged as air-based in the battle engine:
- **Flying-type**: Air Cutter, Air Slash, Aeroblast, Brave Bird, Drill Peck, Fly, Hurricane, Peck, Sky Attack, Wing Attack, etc.
- **Wind moves**: Gust, Twister, Icy Wind (if flagged)
- **Signature moves**: Depends on individual move flags in battle data

### Strategic Applications

#### Hazard Control
- **Lead utility**: Excellent lead Pokemon for hazard-heavy metas
- **Pivot support**: Safe switching while clearing hazards
- **Anti-setup**: Removes screens that protect setup sweepers
- **Entry advantage**: Ensures clean entry for teammates

#### Offensive Enhancement
- **Flying-type synergy**: Natural boost for Flying-type attackers
- **Choice item users**: Boosted air moves with item multipliers
- **Mixed attackers**: Benefits both physical and special air moves
- **Priority moves**: Boosts priority air-based attacks

### Common Users
- Flying-type Pokemon with diverse movepools
- Pokemon with access to Hurricane, Air Slash, or Brave Bird
- Lead Pokemon on teams vulnerable to hazards
- Pivot Pokemon that need hazard control utility

### Competitive Usage Notes
- **Entry timing**: Best used early in battle for maximum hazard control
- **Team support**: Provides utility while maintaining offensive presence
- **Meta dependent**: More valuable in hazard-heavy environments
- **Move selection**: Prioritize air-based moves in moveset
- **Coverage options**: Air moves often provide good neutral coverage

### Counters
- **Rapid Spin/Defog users**: Can reset hazards after Wind Rage clears them
- **Hazard immunity**: Pokemon immune to hazards reduce entry value
- **Non-air movesets**: Ability provides no boost to non-air attacks
- **Priority moves**: Fast attacks before Wind Rage user can utilize boosts
- **Status moves**: Entry Defog doesn't prevent status infliction

### Synergies
- **Heavy-Duty Boots**: Combined hazard protection and clearing
- **Flying Gem**: One-time massive boost to Flying-type moves
- **Life Orb**: Stacks with air move boost for high damage
- **Choice items**: Powerful boosted air moves with speed/choice
- **Weather support**: Hurricane accuracy in rain, Solar Beam charge reduction

### Team Building Considerations
- **Hazard weak teammates**: Protects Pokemon vulnerable to Stealth Rock
- **Screen reliant opponents**: Disrupts defensive setups
- **Air move coverage**: Build around boosted air-based attacks
- **Entry timing**: Plan switches to maximize hazard clearing value
- **Backup hazard control**: Still valuable to have secondary removal

### Version History
- Custom Elite Redux ability (ID 728)
- Combines utility and offense in single ability
- Based on GiantWings offensive multiplier code
- Uses UseEntryMove framework for automatic Defog

### Related Abilities
- **GiantWings**: Same air move boost without hazard control
- **HugeWings**: Air boost + Levitate combination
- **LuckyWings**: Air boost + Serene Grace combination
- **Defiant/Competitive**: Stat boosts when stats are lowered by Defog