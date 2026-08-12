---
id: 763
name: Conjourer of Deceit
status: reviewed
character_count: 287
---

# Conjourer of Deceit - Ability ID 763

## In-Game Description
"Magic Guard + Magic Bounce"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants immunity to all non-attack damage sources including entry hazards, weather damage, status conditions, and recoil. Reflects most status moves back to the user before they can take effect. Reflected moves target the original user. Does not reflect moves that were already reflected.

## Detailed Mechanical Explanation
*For Discord/reference use*

Conjourer of Deceit is an incredibly powerful defensive ability that combines two of the most protective abilities in the game: Magic Guard and Magic Bounce. This creates a nearly impenetrable defensive wall against indirect damage and status manipulation.

### Magic Guard Component
The Magic Guard component prevents ALL indirect damage, protecting the Pokemon from:

**Status Condition Damage:**
- Burn damage (normally 1/16 HP per turn)
- Poison damage (1/8 HP per turn for regular poison, 1/16 for badly poisoned first turn)
- Frostbite damage (1/16 HP per turn)
- Bleed damage (1/8 HP per turn)
- Curse damage (1/4 HP per turn)
- Nightmare damage (1/4 HP per turn while asleep)

**Weather Damage:**
- Sandstorm damage (1/16 HP per turn)
- Hail damage (1/16 HP per turn)

**Entry Hazard Damage:**
- Spikes damage (1/8, 1/6, or 1/4 HP depending on layers)
- Stealth Rock damage (varies by type effectiveness)
- Toxic Spikes damage (applies poison without damage)

**Item-Related Damage:**
- Life Orb recoil (1/10 HP per attack)
- Black Sludge damage for non-Poison types (1/8 HP per turn)
- Sticky Barb damage (1/8 HP per turn)
- Rocky Helmet damage (1/6 HP when making contact)
- Jaboca Berry damage (1/8 HP after physical contact)
- Rowap Berry damage (1/8 HP after special contact)

**Move Recoil and Self-Damage:**
- Recoil from moves like Double-Edge, Flare Blitz
- Self-damage from moves like Mind Blown, Steel Beam
- Powder self-damage when using Fire moves

### Magic Bounce Component
The Magic Bounce component reflects status moves and entry hazards back to the user:

**Reflected Status Moves:**
```c
// Moves with FLAG_MAGIC_COAT_AFFECTED are bounced
- Thunder Wave, Will-O-Wisp, Toxic
- Sleep Powder, Spore, Hypnosis
- Leech Seed, Taunt, Encore
- Stat-lowering moves like Growl, Leer
- Entry hazards like Spikes, Stealth Rock, Toxic Spikes
```

**Implementation Details:**
```c
constexpr Ability ConjurerOfDeceit = {
    .breakable = TRUE,      // Can be suppressed by Mold Breaker-type abilities
    .magicGuard = TRUE,     // Activates Magic Guard protection
    .magicBounce = TRUE,    // Activates Magic Bounce reflection
};
```

### Strategic Implications

**Offensive Advantages:**
- Can safely use Life Orb without recoil damage
- Immune to status conditions that would otherwise cripple setup sweepers
- Cannot be worn down by passive damage

**Defensive Advantages:**
- Complete immunity to hazard control and status spreading
- Forces opponents to rely purely on direct attacks
- Bounces entry hazards back, potentially setting up opponent's own team

**Synergies:**
- **Life Orb**: No recoil damage while gaining 30% power boost
- **Substitute**: Can safely use without fear of being broken by status moves
- **Setup Moves**: Cannot be disrupted by status moves or Taunt
- **Leftovers/Recovery**: Healing is more effective without passive damage

### Counters and Limitations

**Direct Counters:**
- **Mold Breaker-type abilities**: Teravolt, Turboblaze, Mold Breaker bypass the ability entirely
- **Infiltrator**: Can bypass Magic Bounce with status moves
- **Direct attacks**: Physical and special moves are unaffected

**Strategic Counters:**
- **Mixed attackers**: Focus purely on damage-dealing moves
- **Prankster users**: Dark-type immunity to Prankster can still work if the Pokemon isn't Dark-type
- **Contact punishment**: Rocky Helmet, Static, Flame Body still work on contact

### Common Users
- **Mega Meowscarada**: The signature user with stats of 81/140/70/121/70/153
  - Grass/Dark typing provides excellent offensive coverage
  - High Speed and Attack stats make it a formidable physical attacker
  - Access to priority moves and setup options

### Competitive Usage Notes

**In Singles:**
- Excellent setup sweeper with immunity to status disruption
- Can wall status-reliant defensive cores
- Forces opponents into aggressive playstyles

**In Doubles:**
- Protects partner from redirected status moves
- Immune to Spore and other spread status moves
- Can safely use self-damaging spread moves

### Example Damage Calculations
With Magic Guard active:
- Life Orb Leaf Storm: Full damage with no 10% HP recoil
- Burn status: 0 damage per turn instead of 1/16 HP
- 3-layer Spikes: 0 damage on switch-in instead of 1/4 HP

With Magic Bounce active:
- Opponent's Thunder Wave to Bounced back to paralyze the user
- Opponent's Stealth Rock to Reflected to their side of the field
- Opponent's Taunt to Bounced back to prevent their own status moves

### Version History
- Introduced in Elite Redux as Mega Meowscarada's signature ability
- Combines two existing ability effects for unprecedented defensive utility
- Considered one of the most powerful defensive abilities in the game