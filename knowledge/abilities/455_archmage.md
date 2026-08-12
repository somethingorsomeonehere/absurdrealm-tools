---
id: 455
name: Archmage
status: reviewed
character_count: 267
---

# Archmage - Ability ID 455

## In-Game Description
"30% chance of adding a type related effect to each move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

30% chance to add type-based effects: Poison=Toxic, Ice=Frostbite, Water=Confusion, Fire=Burn, Electric/Psychic/Fairy/Grass set terrain, Normal=Encore, Rock=Stealth Rock, Ghost=Disable, Dark=Bleed, Fighting=+SpAtk, Flying=+Speed, Dragon=-Atk, Ground=Trap, Steel=+Def.

## Detailed Mechanical Explanation

Archmage is one of the most complex abilities in Elite Redux, providing different secondary effects based on the type of move used. It triggers on successful non-status moves with a 30% chance.

### Core Mechanics
- **Hook**: `onAttacker` - triggers when the Pokemon with this ability uses a move
- **Activation conditions**:
  - Move must hit the target (`DidMoveHit()`)
  - Move cannot be a status move (`IS_MOVE_STATUS(move)`)
  - 30% random chance (`Random() % 100 < 30`)
- **Properties**: `randomizerBanned = TRUE` (cannot be randomly assigned)

### Type-Specific Effects

When Archmage triggers, it applies different effects based on the move type:

#### Status Infliction Effects
- **Poison-type moves**: Inflicts Toxic poison on target
- **Ice-type moves**: Inflicts Frostbite on target
- **Water-type moves**: Inflicts Confusion on target
- **Fire-type moves**: Inflicts Burn on target
- **Ghost-type moves**: Inflicts Disable on target
- **Dark-type moves**: Inflicts Bleed on target

#### Terrain Setting Effects
- **Electric-type moves**: Sets Electric Terrain
- **Psychic-type moves**: Sets Psychic Terrain
- **Fairy-type moves**: Sets Misty Terrain
- **Grass-type moves**: Sets Grassy Terrain (though code references Misty Terrain)

#### Special Battle Effects
- **Normal-type moves**: Inflicts Encore on target
- **Rock-type moves**: Sets Stealth Rock on target's side
- **Ground-type moves**: Prevents target from escaping (trap effect)

#### Self-Stat Boost Effects
- **Fighting-type moves**: Raises user's Special Attack by 1 stage
- **Flying-type moves**: Raises user's Speed by 1 stage
- **Steel-type moves**: Raises user's Defense by 1 stage

#### Opponent Stat Reduction Effects
- **Dragon-type moves**: Lowers target's Attack by 1 stage

#### Incomplete Implementation
- **Bug-type moves**: Currently has a TODO comment for "Set sticky web" but no implementation

### Key Implementation Notes

1. **Safety Checks**: Each effect includes appropriate checks (e.g., `CanBeBurned(target)`, `CanRaiseStat(battler, STAT_X)`)
2. **Target Validation**: Most effects check if the target is still alive before applying
3. **Battle Scripts**: Terrain effects use specific battle scripts for proper animation/messaging
4. **Status Protection**: Respects ability-based status immunities and other protective effects
5. **Terrain Duration**: Uses standard terrain duration (8 turns base, 12 with Terrain Extender)

### Strategic Value

Archmage provides incredible versatility, allowing a Pokemon to adapt its strategy based on its moveset. The 30% activation rate makes it reliable enough to influence battle tactics while not being overpowered. The variety of effects means it can:
- Apply status conditions for DoT or debuff
- Set beneficial terrain for team support
- Boost own stats for setup
- Debuff opponents for control
- Set hazards for entry damage

The randomizer ban indicates this ability is considered too powerful or complex for random distribution, likely due to its incredible versatility and potential to drastically alter battle flow.

### Similar Abilities
- **Serene Grace**: Also provides secondary effect chances, but only doubles existing move effects rather than adding new ones
- **Super Luck**: Provides consistent secondary benefits but only affects critical hit rates
- **Sheer Force**: Trades secondary effects for power, opposite philosophy to Archmage

Archmage is unique in providing completely different effects based on move type, making it one of the most adaptive abilities in the game.
