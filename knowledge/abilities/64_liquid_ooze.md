---
id: 64
name: Liquid Ooze
status: reviewed
character_count: 278
---

# Liquid Ooze - Ability ID 64

## In-Game Description
"Draining causes harm to enemies instead of healing them."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Liquid Ooze reverses all healing effects from drain moves, causing the attacker to take damage instead. Affects Absorb, Drain Punch, Giga Drain, Leech Life, and similar draining attacks. The damage equals what would have been healed. Perfect counter to healing-based strategies.

## Detailed Mechanical Explanation
*For Discord/reference use*

**LIQUID OOZE** is a defensive counter-ability that punishes opponents for attempting to drain HP from this Pokemon.

### Core Mechanics:
- **Drain Reversal**: All HP-draining moves deal damage to the attacker instead of healing
- **Damage Calculation**: Damage equals the HP that would have been absorbed
- **Message Display**: "It sucked up the Liquid Ooze!" appears when triggered
- **Move Coverage**: Affects all moves with draining/absorbing effects

### Affected Moves:
**Direct Drain Moves:**
- Absorb, Mega Drain, Giga Drain
- Drain Punch, Draining Kiss
- Leech Life, Horn Leech
- Dream Eater (if target is asleep)

**Indirect Drain Effects:**
- Leech Seed (if implemented)
- Big Root enhancement reversal
- Any move with HP-draining secondary effects

### Technical Implementation:
Based on AI behavior and message systems:
- AI heavily penalizes drain moves against Liquid Ooze users (-6 score)
- Special battle messages (B_MSG_ABSORB_OOZE, B_MSG_LEECH_SEED_OOZE)
- Likely uses `onAbsorb` hook returning damage instead of healing

### Damage Mechanics:
- **Standard Absorption**: 50% of damage to 50% damage to attacker
- **Big Root**: Enhanced absorption to Enhanced damage to attacker  
- **Minimum Damage**: At least 1 HP damage guaranteed
- **Maximum Damage**: Proportional to original drain amount

### Strategic Applications:
- **Anti-Drain**: Hard counters drain-based strategies
- **Passive Deterrent**: AI avoids using drain moves
- **Team Support**: Protects team from Leech Seed/drain spam
- **Defensive Wall**: Punishes attempts to sustain against bulky Pokemon

### Elite Redux Context:
- **AI Integration**: Battle AI specifically recognizes and avoids triggering
- **Message System**: Dedicated battle messages for different drain types
- **Move Interactions**: Works with expanded movepool of drain attacks
- **4-Ability System**: Can be combined with other defensive abilities

### Interactions:
- **Magic Guard**: May protect attackers from Liquid Ooze damage
- **Substitute**: Unclear interaction - may bypass or affect differently
- **Healing Moves**: Only affects drain moves, not self-healing
- **Mold Breaker**: Likely bypasses Liquid Ooze protection

### Common Users:
- **Tentacruel**: Classic Liquid Ooze user with high HP
- **Gulpin/Swalot**: Poison-types immune to Toxic damage
- **Pokemon with drain vulnerability**: Those weak to Life Orb + drain combos

### Competitive Usage:
- **Defensive Core**: Protects against sustain strategies
- **Stall Teams**: Prevents opponent recovery through draining
- **Anti-Meta**: Counters drain-heavy movesets
- **Surprise Factor**: Forces opponents to reconsider move choices

### Counters:
- **Non-Drain Attacks**: Ability provides no protection against normal damage
- **Status Moves**: No effect on status-based strategies
- **Indirect Damage**: Entry hazards, weather, poison unaffected
- **Mold Breaker**: Bypasses the drain reversal effect

### AI Behavior:
The AI recognizes Liquid Ooze and will:
- Heavily penalize drain moves (-6 score for EFFECT_ABSORB)
- Avoid Leech Seed on Liquid Ooze users (-3 score)
- Prefer alternative recovery methods
- Switch to non-draining attack strategies

### Version History:
- Elite Redux maintains classic drain reversal concept
- Enhanced AI recognition for strategic avoidance
- Integrated message system for clear feedback
- Expanded to work with newer drain moves

### Implementation Notes:
*Based on code analysis, Liquid Ooze appears to be partially implemented with AI recognition and message systems, but may need full onAbsorb hook implementation in abilities.cc for complete functionality.*