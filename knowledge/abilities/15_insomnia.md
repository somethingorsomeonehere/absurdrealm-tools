---
id: 15
name: Insomnia
status: reviewed
character_count: 295
---

# Insomnia - Ability ID 15

## In-Game Description
"Cannot fall asleep. Rest fails if used."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents falling asleep by any means, including sleep moves, abilities like Yawn, and other effects that cause sleep status. Rest will fail completely when used. If gained while asleep (via Worry Seed/Skill Swap), immediately wakes up. Can be bypassed by Mold Breaker and similar abilities. TEST

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Insomnia is implemented in `src/abilities.cc` (lines 461-468) with the following properties:

```c
constexpr Ability Insomnia = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_SLEEP)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Key Features

1. **Sleep Immunity**: 
   - Prevents the Pokemon from being put to sleep by any means
   - Uses the `CHECK_SLEEP` flag in the `onStatusImmune` callback
   - Returns `TRUE` when any sleep-inducing effect is attempted

2. **Rest Prevention**:
   - The move Rest will fail completely if used by a Pokemon with Insomnia
   - This is handled in the battle script system
   - Prevents self-induced sleep for recovery

3. **Wake-Up Effect**:
   - `removesStatusOnImmunity = TRUE` means if a sleeping Pokemon gains Insomnia, it immediately wakes up
   - This can occur through moves like Worry Seed that change abilities

### Ability Properties
- **breakable**: TRUE - Can be suppressed by abilities like Mold Breaker
- **removesStatusOnImmunity**: TRUE - Cures existing sleep when gained

### Sources of Sleep Blocked
- Sleep Powder, Spore, Hypnosis, Sing, Grass Whistle
- Dark Void, Lovely Kiss
- Effect Spore ability
- Yawn (prevents sleep after drowsy turn)
- Rest (move fails entirely)
- Any other sleep-inducing effect

### Interactions

1. **With Worry Seed**:
   - Worry Seed changes the target's ability to Insomnia
   - Cannot be used on Pokemon that already have Insomnia
   - Protected by Ability Shield

2. **With Other Sleep Immunity Abilities**:
   - **Vital Spirit**: Identical sleep immunity
   - **Sweet Veil**: Protects self and allies from sleep
   - **Rude Awakening**: Conditional sleep immunity
   - **Comatose**: Always acts as if asleep but immune to sleep status

3. **With Ability-Ignoring Effects**:
   - Can be bypassed by Mold Breaker and similar abilities
   - Sleep-inducing moves from Pokemon with Mold Breaker will work

### Technical Details
The ability check happens at multiple points:
- When attempting to inflict sleep status
- During move execution (for Rest)
- In AI calculations for move effectiveness
- During status cure checks

### Strategic Implications
- **Sleep Immunity**: Complete protection against sleep-based strategies
- **Rest Denial**: Cannot use Rest for recovery, limiting healing options
- **Status Absorber**: Can switch into predicted sleep moves safely
- **Lead Potential**: Good for leads that fear sleep leads like Butterfree

### Common Users
Typically found on Pokemon that are naturally alert or restless, often including nocturnal Pokemon or those with high energy levels.

### Competitive Usage Notes
- Excellent on setup sweepers that fear sleep
- Valuable on defensive Pokemon that can't afford sleep turns
- Trade-off: loses Rest as a recovery option
- Can enable safer switches into known sleep users

### Counters
- Direct damage (no defensive benefits beyond sleep immunity)
- Other status conditions still work normally
- Mold Breaker bypasses the immunity
- Pokemon with Insomnia often lack recovery without Rest

### Synergies
- Pivot Pokemon that can absorb sleep moves
- Setup sweepers that need uninterrupted setup
- Pokemon with other recovery options (Roost, Recover, etc.)
- Teams weak to sleep-based strategies

### Version History
Insomnia has remained functionally identical throughout the generations, providing consistent sleep immunity. The interaction with Rest failing has been present since its introduction.