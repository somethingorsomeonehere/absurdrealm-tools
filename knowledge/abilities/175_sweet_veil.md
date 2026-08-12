---
id: 175
name: Sweet Veil
status: reviewed
character_count: 74
---

# Sweet Veil - Ability ID 175

## In-Game Description
"This Pokemon and its ally are immune to sleep."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Provides sleep immunity to both the user and their ally in double battles. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Sweet Veil is a sleep immunity ability that works for both the user and their ally in doubles battles. Here's how it functions mechanically:

### Core Functionality
- **Status Immunity**: Provides immunity to all sleep-inducing effects (CHECK_SLEEP status flag)
- **Ally Protection**: Uses `.onStatusImmuneFor = APPLY_ON_ALLY` to extend protection to allied Pokemon
- **Breakable**: Can be disabled by abilities like Mold Breaker, Turboblaze, or Teravolt
- **No Status Removal**: Unlike some immunity abilities, it doesn't automatically cure existing sleep

### Technical Implementation
```cpp
constexpr Ability SweetVeil = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_SLEEP)
        return TRUE;
    },
    .onStatusImmuneFor = APPLY_ON_ALLY,
    .breakable = TRUE,
};
```

### Sleep Sources Protected Against
- Direct sleep moves (Sleep Powder, Hypnosis, Spore, etc.)
- Sleep from abilities (Effect Spore when it rolls sleep)
- Sleep from items or other battle effects
- Rest is still usable (as it's self-induced and bypasses immunity)

### Battle Format Differences
- **Singles**: Only protects the user
- **Doubles/Multi**: Protects both the user and their ally
- **Ally dies**: Protection is lost for remaining Pokemon if Sweet Veil user faints

### Interaction Notes
- Does not prevent self-induced sleep (Rest)
- Can be bypassed by mold breaker-type abilities
- Works even if the ally has a different ability
- Functions similar to Aroma Veil but specifically for sleep immunity
- The ally gets the protection regardless of their position or ability

### Comparison with Similar Abilities
- **Insomnia/Vital Spirit**: Only protects the user, but also removes existing sleep
- **Aroma Veil**: Protects from multiple status conditions but not sleep specifically
- **Sweet Veil**: Unique in providing sleep immunity to both user and ally