---
id: 614
name: Balloon Bomber
status: reviewed
character_count: 296
---

# Balloon Bomber - Ability ID 614

## In-Game Description
"Combines Aftermath and Inflatable effects."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses a 100 BP Explosion or Outburst (whichever is higher) when knocked out. Using explosion moves will always Flinch the target. When hit by any Fire or Flying moves, boost Defense and Special Defense by one stage each. Activates on each hit of a multihit move. Boost applies after the hit lands.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Balloon Bomber is a hybrid ability that combines two distinct effects:
1. **Inflatable Component**: When hit by Fire or Flying-type moves, raises Defense and Special Defense by +1 stage each
2. **Aftermath Component**: When fainting from contact moves, deals 25% of attacker's max HP as damage

### Component Ability Analysis

#### Inflatable Effect
- **Trigger**: Hit by any Fire-type or Flying-type move
- **Effect**: +1 Defense and +1 Special Defense
- **Timing**: Activates after damage calculation
- **Conditions**: Must not be blocked by Substitute; at least one defensive stat must be below +6

#### Aftermath Effect  
- **Trigger**: Pokemon faints from a contact move
- **Effect**: Deals damage equal to 25% of attacker's max HP (minimum 1 HP)
- **Conditions**: Attacker must not have Magic Guard; move must make contact; must actually faint

### Technical Implementation
```cpp
constexpr Ability BalloonBomber = {
    .onDefender = +[](ON_DEFENDER) -> int { 
        return Aftermath.onDefender(DELEGATE_DEFENDER) || Inflatable.onDefender(DELEGATE_DEFENDER); 
    },
};
```

The ability uses a logical OR to check both component abilities, meaning either effect can trigger independently.

### Activation Scenarios

#### Inflatable Activation
- **Fire-type moves**: Flamethrower, Fire Blast, Overheat, Will-O-Wisp, etc.
- **Flying-type moves**: Wing Attack, Hurricane, Air Slash, Roost, etc.
- **Result**: Immediate +1 Defense and +1 Special Defense after taking damage

#### Aftermath Activation
- **Contact moves**: Tackle, Body Slam, Earthquake, Thunder Punch, etc.
- **Must cause fainting**: Only triggers when the move reduces HP to 0
- **Result**: Attacker takes 25% max HP damage (ignores type resistances)

### Strategic Applications

#### Defensive Pivot Strategy
- Switch into predicted Fire/Flying attacks to gain defensive boosts
- Use boosted bulk to set up or provide team support
- Threaten revenge damage if opponent uses contact moves to finish

#### Explosion Deterrent
- Opponents must consider using non-contact moves to finish off the Pokemon
- Creates mind games around finishing moves
- Particularly effective against physical attackers who rely on contact moves

#### Mega Wigglytuff Synergy
- Fire/Fairy typing benefits from Fire-type resistance (no damage from Inflatable trigger on Fire moves)
- High HP stat (120 base) makes Aftermath damage more threatening
- Balanced defensive stats benefit significantly from Inflatable boosts

### Interactions and Counters

#### Interactions
- **Magic Guard**: Prevents Aftermath damage to the attacker
- **Substitute**: Blocks Inflatable activation but not Aftermath
- **Multi-hit moves**: Inflatable activates once per turn, Aftermath only on fainting hit
- **Rocky Helmet**: Stacks with Aftermath for massive contact move punishment

#### Counters
- **Non-contact moves**: Avoid Aftermath trigger (Psychic, Thunderbolt, etc.)
- **Non-Fire/Flying attacks**: Avoid Inflatable trigger
- **Status moves**: Neither effect triggers from status moves like Toxic
- **Magic Guard users**: Immune to Aftermath damage

### Competitive Usage

#### Best Users
- **Mega Wigglytuff**: Currently the only known user in Elite Redux
- **Ideal for**: Bulky Pokemon that can survive initial hits and capitalize on boosts

#### Team Synergy
- **Entry hazard support**: Inflatable boosts help survive longer to set hazards
- **Pivot strategies**: Use defensive boosts to safely switch teammates
- **Revenge killing**: Aftermath punishes reckless contact move usage

#### Damage Calculations
Example with Mega Wigglytuff (120 HP):
- **Before Inflatable**: 252+ Atk Talonflame Flare Blitz = ~40-50% damage
- **After Inflatable (+1 Def)**: Same attack = ~25-35% damage (significant reduction)
- **Aftermath revenge**: If Talonflame's Flare Blitz faints Mega Wigglytuff, Talonflame takes 25% max HP damage

### Common Matchup Scenarios

#### vs Fire/Flying Attackers
1. Switch in on predicted Fire/Flying move
2. Take reduced damage and gain +1/+1 defensive boosts
3. Either set up further or pivot to appropriate teammate
4. Threaten Aftermath if opponent tries contact moves

#### vs Physical Attackers
1. Use as a late-game revenge threat
2. Force opponent to choose between contact moves (Aftermath risk) or non-contact moves
3. Create favorable positioning through explosion threat

### Version History
- Introduced in Elite Redux as a hybrid ability combining defensive utility with offensive threat
- Unique to Mega Wigglytuff as an innate ability
- Part of the expanded 4-ability system design philosophy