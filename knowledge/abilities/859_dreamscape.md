---
id: 859
name: Dreamscape
status: reviewed
character_count: 299
---

# Dreamscape - Ability ID 859

## In-Game Description
"Comatose + Dreamcatcher + Deal 20% more damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Considers the user as asleep for moves and statuses. User can act normally and gains immunity to status conditions. Doubles the power of moves when any active Pokemon is asleep. Attacks hit sleeping foes who are switching out for 1x power instead, damaging them before leaving. Boosts damage by 20%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Dreamscape is a combination ability that merges three distinct effects:
1. **Comatose component**: Permanent sleep-like state with full functionality and status immunity
2. **Dreamcatcher component**: Double move power when any Pokemon on field is asleep
3. **Additional boost**: Extra 20% damage multiplier on top of other effects

**Total Damage Calculation:**
- Base move power x 2.0 (Dreamcatcher) x 1.2 (additional boost) = **2.4x total multiplier**
- This represents a 140% damage increase over normal move power

### Activation Conditions
- **Always active** - cannot be suppressed or disabled
- Permanent sleep status ensures Dreamcatcher is always triggered
- Status immunity is unsuppressable (survives Mold Breaker, etc.)
- Announces itself on switch-in

### Technical Implementation
```cpp
constexpr Ability Dreamscape = {
    .onEntry = Comatose.onEntry,  // Announces switch-in, shows sleep status
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            Dreamcatcher.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);  // 2.0x
            MUL(1.2);  // Additional 20% boost
        },
    .onStatusImmune = Comatose.onStatusImmune,  // Complete status immunity
    .unsuppressable = TRUE,  // Cannot be disabled
    .removesStatusOnImmunity = TRUE,  // Clears existing status on switch-in
};
```

### Component Analysis

**From Comatose (ID 213):**
- Permanent sleep-like appearance and functionality
- Complete immunity to all status conditions (poison, burn, paralysis, freeze, sleep)
- Unsuppressable - cannot be disabled by any ability or move
- Automatically removes existing status conditions on activation
- Can act normally every turn without "waking up"

**From Dreamcatcher (ID 305):**
- Doubles move power when any battler on field has sleep status
- Since this Pokemon has permanent sleep (via Comatose), Dreamcatcher is always active
- Applies to all damage-dealing moves of any type
- Checks global battlefield state for sleep status

**Additional Enhancement:**
- Extra 1.2x damage multiplier applied after Dreamcatcher
- This stacks multiplicatively: Base x 2.0 x 1.2 = 2.4x total

### Move Interactions
- **All Damage Moves**: Receive the full 2.4x power boost (Dreamcatcher + bonus)
- **Wake-Up Slap**: Deals 4x damage due to sleep status (120 BP to 480 BP with Dreamscape)
- **Dream Eater**: Cannot be used on this Pokemon (no actual sleep, just sleep status)
- **Sleep Talk**: Cannot be used (Comatose prevents selection)
- **Rest**: Has no effect (already immune to status conditions)
- **Snore**: Cannot be used (requires true sleep state)

### Ability Interactions
- **Bad Dreams**: Takes 1/8 HP damage per turn (recognizes sleep status)
- **Sweet Dreams**: Heals 1/8 HP per turn instead of taking damage
- **Mold Breaker/Teravolt/Turboblaze**: Cannot suppress any component of Dreamscape
- **Gastro Acid**: Cannot remove Dreamscape
- **Simple Beam/Worry Seed**: Cannot replace Dreamscape
- **Insomnia/Vital Spirit on allies**: Don't affect Dreamscape since user provides the sleep status

### Strategic Applications

**Offensive Powerhouse:**
- Guaranteed 2.4x damage multiplier makes even weak moves threatening
- 60 BP move becomes 144 BP effective power
- 100 BP move becomes 240 BP effective power
- Combines raw power with complete status immunity

**Versatile Coverage:**
- Boost applies to all move types and categories
- Physical, special, and even some status moves benefit
- Priority moves, multi-hit moves, all receive the boost

**Team Support:**
- Acts as permanent sleep status for teammates with sleep-dependent abilities
- Cannot be status locked or shut down by opponent strategies
- Reliable damage output regardless of opponent's strategy

### Damage Calculations
**Example with 100 BP move:**
- Base: 100 power
- With Dreamscape: 100 x 2.0 x 1.2 = 240 power
- With STAB: 240 x 1.5 = 360 power
- With Life Orb: 360 x 1.3 = 468 power
- With super effective: 468 x 2.0 = 936 effective power

**Example with Wake-Up Slap (60 BP):**
- Base against sleeper: 60 x 2 = 120 power
- With Dreamscape: 120 x 2.0 x 1.2 = 288 power
- Essentially a 480 BP move against sleeping targets

### Common Users
- **Highly Restricted**: Dreamscape is typically reserved for legendary or pseudo-legendary Pokemon
- **Elite Redux Special Events**: May appear on event-exclusive Pokemon
- **Custom Designs**: Used on powerful Elite Redux original species
- **Late-Game Encounters**: Found on challenging post-game boss Pokemon

### Competitive Analysis
**Strengths:**
- Unparalleled offensive power with 140% damage increase
- Complete immunity to all status conditions
- Cannot be suppressed, disabled, or counteracted
- Consistent performance - no setup required
- Excellent against stall teams and status-based strategies

**Weaknesses:**
- Vulnerable to Bad Dreams passive damage
- Takes 4x damage from Wake-Up Slap
- Cannot benefit from sleep-based utility moves
- Extremely rare - difficult to obtain
- May be banned in certain competitive formats

**Threat Assessment:**
- **Tier Impact**: Game-changing ability that warrants immediate respect
- **Usage Restriction**: Likely limited to special formats or events
- **Counter-Play**: Focus on raw damage, entry hazards, and Bad Dreams
- **Team Building**: Requires specific strategies to handle effectively

### Counters and Limitations
**Direct Counters:**
- **Bad Dreams users**: Passive damage can wear down over time
- **Wake-Up Slap users**: Deal massive damage (4x effectiveness)
- **Priority moves**: Can potentially KO before it can act
- **Entry hazards**: Still vulnerable to Spikes, Stealth Rock, Toxic Spikes

**Strategic Limitations:**
- Cannot use sleep-based utility moves effectively
- Vulnerable to moves that specifically target sleeping Pokemon
- High power may lead to quick battles, reducing strategic depth
- Extremely rare availability limits practical use

### Synergistic Elements
**Beneficial Abilities (on teammates):**
- **Sweet Dreams**: Heals the Dreamscape user instead of damaging it
- **Healing abilities**: Help offset Bad Dreams damage
- **Entry hazard removal**: Protects the valuable Dreamscape user

**Beneficial Items:**
- **Life Orb**: Stacks for even more devastating damage (3.12x total)
- **Choice items**: Lock into one move but with incredible power
- **Leftovers**: Helps offset Bad Dreams damage over time
- **Dream Ball**: 4x catch rate if encountered in wild

### Version History and Balance
- **Elite Redux Addition**: Custom ability representing ultimate sleep mastery
- **Power Level**: Intentionally overpowered for special encounters or events
- **Design Philosophy**: Combines two existing abilities with additional boost for unique effect
- **Balance Considerations**: Extreme rarity balances extreme power
- **Future Updates**: May receive adjustments based on competitive impact

This ability represents the pinnacle of sleep-based combat mastery, combining status immunity, guaranteed activation conditions, and overwhelming offensive power into a single, devastatingly effective package.