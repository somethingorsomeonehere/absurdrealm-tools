---
id: 244
name: Punk Rock
status: reviewed
character_count: 151
---

# Punk Rock - Ability ID 244

## In-Game Description
"Sound moves deal 1.3x more dmg. Takes -50% dmg from sound moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Punk Rock amplifies the user's sound moves by 30% and reduces incoming sound move damage by 50%. Damage reduction is multiplicative with other sources. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Punk Rock is a dual-purpose ability that affects both offensive and defensive sound move interactions:

**Offensive Effects:**
- Increases damage of all sound moves used by the Pokemon by 30% (1.3x multiplier)
- Applies to any move with the FLAG_SOUND property
- Stacks multiplicatively with other damage modifiers (STAB, type effectiveness, items, etc.)

**Defensive Effects:**
- Reduces damage taken from sound moves by 50% (0.5x multiplier)
- Provides protection against all incoming sound-based attacks
- Acts as a defensive multiplier applied after other calculations

**Sound Move Classification:**
Sound moves are determined by the FLAG_SOUND property and include:
- Offensive: Hyper Voice (95 BP), Boomburst (140 BP), Round (60 BP), Sonic Boom
- Status: Roar, Sing, Supersonic, Grass Whistle, Disable
- Special cases: Normal-type moves become sound moves when used by Pokemon with Reverbate ability

**Technical Details:**
- Uses onOffensiveMultiplier and onDefensiveMultiplier callbacks
- Breakable by Mold Breaker, Teravolt, and Turboblaze abilities
- Cannot be suppressed by Neutralizing Gas
- Works in both singles and doubles battles
- Multipliers apply before final damage calculation

**Strategic Applications:**
- Excellent on sound-based attackers like Exploud, Chatot, or Noivern
- Provides both offensive power and defensive utility
- Counters opposing sound-based strategies
- Synergizes well with Choice items for massive sound move damage
- Useful in doubles for spread move damage enhancement

**Interactions:**
- Does not stack with multiple instances of the same ability
- Works independently of Soundproof (which grants immunity)
- Compatible with sound-enhancing items and abilities
- Multipliers calculated separately from critical hits and weather effects