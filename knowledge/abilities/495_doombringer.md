---
id: 495
name: Doombringer
status: reviewed
character_count: 264
---

# Doombringer - Ability ID 495

## In-Game Description
"Uses Doom Desire on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Doom Desire on entry. Doom Desire is a Steel-type 140 base power and strikes the target two turns later, bypassing substitutes and other protections. The attack cannot miss once initiated and ignores accuracy checks. This cannot target the same Pokemon twice.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Doombringer automatically initiates a devastating delayed attack when entering battle, creating inevitable future damage that cannot be easily avoided or blocked.

### Activation Conditions
- **Trigger**: Activates immediately upon switching into battle
- **Target**: Automatically targets the first available opposing Pokemon
- **Move used**: Doom Desire (Steel-type, 140 base power)
- **Delay**: Attack lands exactly 2 turns after activation
- **Guarantee**: Cannot miss once the countdown begins

### Technical Implementation
```c
constexpr Ability Doombringer = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_DOOM_DESIRE, 0); 
    },
};
```

### Doom Desire Move Properties
- **Type**: Steel
- **Category**: Special
- **Base Power**: 140
- **Accuracy**: 100% (but irrelevant after activation)
- **Effect**: EFFECT_FUTURE_SIGHT (delayed attack)
- **Target**: Selected opponent
- **PP**: 5 (not relevant for ability usage)

### Future Sight Mechanics
- **Turn 1**: Doom Desire is activated, target is marked
- **Turn 2**: Countdown continues, no damage
- **Turn 3**: Doom Desire hits the originally targeted position
- **Persistence**: Attack lands even if user faints or switches out
- **Inevitability**: Cannot be stopped once countdown starts

### Strategic Applications
- **Entry pressure**: Immediate threat upon switching in
- **Delayed punishment**: Forces opponent into difficult positions
- **Switch-in safety**: Threatens revenge even if user is KO'd
- **Field control**: Creates ongoing battlefield pressure
- **Steel coverage**: Provides Steel-type attacks for non-Steel users

### Defensive Interactions
**Cannot be blocked by:**
- Protect/Detect (delayed attacks bypass protection)
- Substitute (Future Sight effect ignores substitutes)
- Switching out (attack follows the battlefield position)
- Type immunity (Steel-type interactions still apply)

**Can be avoided by:**
- Switching the targeted Pokemon out (if done before attack lands)
- Wonder Guard (if Steel isn't super-effective)
- Magic Guard (prevents Future Sight damage)

### Timing Considerations
- **Switch-in Turn**: Doom Desire activates
- **Opponent Turn 1**: Can react/switch with 2 turns of warning
- **User Turn 2**: Can follow up or switch out safely
- **Opponent Turn 2**: Last chance to avoid by switching
- **Turn 3**: Doom Desire hits regardless of user status

### Double Battle Applications
- **Position targeting**: Targets specific battlefield position
- **Ally protection**: Attack can hit even if user is KO'd
- **Field pressure**: Forces opponent positioning decisions
- **Steel coverage**: Provides team Steel-type damage

### Competitive Usage
- **Entry hazard**: Creates immediate battlefield pressure
- **Revenge tool**: Guarantees damage even if user faints
- **Steel utility**: Non-Steel types gain powerful Steel attack
- **Prediction tool**: Forces opponent into suboptimal plays
- **Late-game finisher**: High power delayed damage

### Synergies
**Team support:**
- Entry hazards: Stack damage with Stealth Rock/Spikes
- Pivot moves: U-turn/Volt Switch after setting up doom
- Taunt users: Prevent defensive moves before doom hits
- Trappers: Prevent switching to avoid the delayed attack

**Item synergies:**
- Choice items: Can lock into setup then switch
- Leftovers: Sustain while doom countdown proceeds
- Focus Sash: Survive to ensure doom activation

### Counters
- **Fast KO**: Eliminate user before they can switch
- **Strategic switching**: Move targeted Pokemon to safety
- **Magic Guard**: Prevents Future Sight damage entirely
- **Wonder Guard**: If Steel isn't super-effective
- **Pressure**: Quickly eliminate to prevent follow-up

### Limitations
- **One activation**: Only triggers once per switch-in
- **Delayed damage**: No immediate impact
- **Switch dependency**: Opponent can avoid by switching
- **Predictable**: Opponent knows doom is coming
- **Position-based**: Targets battlefield position, not specific Pokemon

### Version History
- Elite Redux custom ability for delayed battlefield control
- Based on Jirachi's signature move Doom Desire
- Designed to create inevitable pressure and strategic depth
- Part of expanded entry ability system