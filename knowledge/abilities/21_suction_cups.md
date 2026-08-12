---
id: 21
name: Suction Cups
status: reviewed
character_count: 50
---

# Suction Cups - Ability ID 21

## In-Game Description
"Cannot be forced to switch out by an enemy's move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents forced switching from moves and Red Card.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Suction Cups is a simple but effective ability that prevents forced switching. Implementation in `src/abilities.cc`:

```cpp
constexpr Ability SuctionCups = {
    .breakable = TRUE,
};
```

### Key Features

1. **Forced Switch Prevention**:
   - Blocks moves that force the target to switch out
   - Prevention handled in battle system's switch checks
   - Similar mechanism to Guard Dog ability

2. **Affected Moves**:
   - **Roar**: Sound-based forced switch
   - **Whirlwind**: Wind-based forced switch  
   - **Dragon Tail**: Damage + forced switch
   - **Circle Throw**: Damage + forced switch

3. **NOT Affected**:
   - Voluntary switches by the player/trainer
   - Self-switching moves (U-turn, Volt Switch, Flip Turn)
   - Parting Shot (user switches, not target)
   - Baton Pass, Teleport (self-switching)
   - Red Card item effect

### AI Behavior
The AI is programmed to recognize Suction Cups and adjust strategy accordingly:

```c
case EFFECT_ROAR:
    if (CountUsablePartyMons(battlerDef) == 0)
        score -= 10;
    else if (BattlerHasAbility(battlerDef, ABILITY_SUCTION_CUPS, TRUE))
        score -= 10;
```

- AI reduces score by 10 for using Roar-like moves against Suction Cups
- AI treats it similarly to having no available switch targets
- AI Rating: 2 (moderate defensive value)

### Ability Properties
- **breakable = TRUE**: Can be suppressed by Mold Breaker and similar abilities
- When suppressed, forced switches work normally
- No additional properties or effects

### Strategic Implications

**Defensive Value**:
- Maintains field position against phazing teams
- Protects setup sweepers from being forced out
- Counters Roar/Whirlwind stall strategies
- Preserves stat boosts and field setup

**Team Support**:
- Enables safer setup strategies
- Protects hazard setters from phazing
- Maintains weather/terrain setters on field
- Counters defensive phazing cores

### Limitations
- Only prevents forced switches, not damage
- Dragon Tail/Circle Throw still deal damage
- Mold Breaker bypasses protection
- No offensive benefits

### Pokemon with Suction Cups
Typically found on Pokemon with suction cup-like appendages or those that anchor themselves in place. Often appears on defensive Water-types and setup sweepers.

### Competitive Usage Notes

**Setup Sweepers**:
- Protects Swords Dance/Nasty Plot boosts
- Maintains Substitute against phazing
- Enables multiple setup turns

**Defensive Roles**:
- Hazard setters stay on field
- Walls resist phazing strategies
- Weather setters maintain presence

### Counters
- Mold Breaker abilities bypass Suction Cups
- Gastro Acid and ability suppression
- Direct offensive pressure
- Status conditions and Taunt
- Perish Song (different switch mechanic)

### Synergies
- Setup moves benefit from switch protection
- Substitute users maintain their sub
- Baton Pass chains stay intact
- Hazard stacking teams

### Interactions

1. **With Mold Breaker**:
   - Teravolt, Turboblaze also bypass
   - Forced switches work normally

2. **With Ingrain**:
   - Stack for double switch prevention
   - Ingrain adds HP recovery

3. **In Doubles**:
   - Protects from both opponents' phazing
   - Maintains Trick Room/Tailwind setter

### Version History
Suction Cups has maintained consistent functionality:
- Prevents forced switching from opponent's moves
- Can be bypassed by Mold Breaker
- Does not affect self-switching or voluntary switches

Elite Redux maintains the standard implementation while ensuring AI recognition for strategic play.