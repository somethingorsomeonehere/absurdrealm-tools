---
id: 58
name: Minus
status: reviewed
character_count: 89
---

# Minus - Ability ID 58

## In-Game Description
"Deals double damage if an ally Pokemon has Minus or Plus."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles the Pokemon's offensive power when partnered with an ally that has Minus or Plus.

## Detailed Mechanical Explanation
*For Discord/reference use*

**MINUS** is a damage-boosting ability that doubles offensive power when paired with specific partner abilities in multi-battle formats.

### Activation Mechanics:
- **Trigger**: During damage calculation (onOffensiveMultiplier hook)
- **Effect**: Multiplies damage by 2.0x (100% increase)
- **Partner Requirements**: Ally must have ABILITY_PLUS or ABILITY_MINUS
- **Partner State**: Partner must be alive (IsBattlerAlive check)
- **Battle Format**: Only functions in double/triple battles (requires living partner)

### Technical Implementation:
```c
constexpr Ability Minus = {
    .onOffensiveMultiplier = Plus.onOffensiveMultiplier,
};

// Shared implementation with Plus:
constexpr Ability Plus = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            int partner = BATTLE_PARTNER(battler);
            if (!IsBattlerAlive(partner)) return;
            if (BattlerHasAbility(partner, ABILITY_PLUS, FALSE) || 
                BattlerHasAbility(partner, ABILITY_MINUS, FALSE)) MUL(2.0);
        },
};
```

### Partner Detection System:
- **BATTLE_PARTNER Macro**: `(id) ^ 2` - Uses XOR to find partner slot
- **Partner Checking**: Verifies partner is alive before ability check
- **Ability Detection**: Uses `BattlerHasAbility()` with FALSE flag (ignores suppression)
- **Symmetric Effect**: Both Plus and Minus abilities trigger the boost for each other

### Battle Format Requirements:
- **Singles**: No effect (no partner exists)
- **Doubles**: Functions when partner has Plus/Minus
- **Triples**: Functions when direct partner has Plus/Minus
- **Multi-Battle**: Only checks immediate battle partner, not all allies

### Move Interactions:
- **All Moves**: Affects every offensive move that deals damage
- **Physical/Special**: Boosts both physical and special attacks equally
- **Multi-Hit**: Each hit receives the 2.0x multiplier
- **Fixed Damage**: Does not affect moves with fixed damage values
- **Status Moves**: No effect on non-damaging moves

### Synergistic Moves (AI Recognition):
**Gear Up (Move Effect):**
- AI recognizes Plus/Minus users as prime targets
- Raises Attack and Special Attack of Plus/Minus holders
- Score bonus when user or partner has ability

**Magnetic Flux (Move Effect):**
- Specifically targets Plus/Minus ability holders
- Raises Defense and Special Defense of affected Pokemon
- AI prioritizes when Plus/Minus users are present

### Elite Redux Implementation:
**Pokemon with Minus (as Innate):**
- **Plusle** (Electric/Fairy) - Tier 2
  - Abilities: Transistor, Lightning Rod, Power Spot
  - Innates: **Minus**, Defiant, Speed Boost
  - Partner to: Minun (Plus holder)

**Strategic Role:**
- Forms pairs with Plus users for maximum effectiveness
- Creates "power couple" strategies in doubles format
- Enables overwhelming offensive pressure when both abilities activate

### Damage Calculation:
```
Base Damage x Type Effectiveness x STAB x Minus Boost x Other Multipliers
Where Minus Boost = 2.0 when partner has Plus/Minus, 1.0 otherwise
```

**Example Calculations:**
- 100 BP move with partner Plus: 200 effective BP
- With STAB (1.5x): 100 x 2.0 x 1.5 = 300 effective BP
- Super effective + Minus + STAB: 100 x 2.0 x 2.0 x 1.5 = 600 effective BP

### Competitive Applications:
**Doubles Strategy:**
- Pair Minus holder with Plus holder for mutual benefit
- Both Pokemon deal double damage when together
- Creates immediate offensive pressure from turn 1
- Forces opponents to prioritize removing one partner

**Team Building:**
- Natural synergy with Plusle (Minus) + Minun-like pairs
- Requires specific team composition around ability synergy
- Vulnerable to partner removal strategies
- Best with fast, powerful attackers

### Counterplay:
**Direct Counters:**
- **Eliminate Partner**: Remove Plus/Minus partner to disable ability
- **Singles Format**: Force singles battles where ability has no effect
- **Priority Moves**: KO one partner before they can attack together
- **Redirection**: Use Follow Me/Rage Powder to isolate targets

**Defensive Options:**
- **Wide Guard**: Blocks spread moves from powered-up attackers
- **Intimidate**: Reduces physical damage even with Minus boost
- **Protect/Detect**: Stall while planning partner elimination
- **Bulk Investment**: Tank the doubled damage and retaliate

### Ability Interactions:
**Positive Synergies:**
- **Plus**: Perfect partner ability, both get 2.0x damage
- **Follow Me/Rage Powder**: Protects the partner needed for activation
- **Speed Boost**: Ensures faster activation of boosted attacks
- **Friend Guard**: Reduces damage to crucial partner

**Negative Interactions:**
- **Ability Suppression**: Gastro Acid, Core Enforcer disable the boost
- **Partner Switching**: Loses boost when partner switches out
- **Imposter**: Opponent copying ability without proper partner setup

### Version Notes:
- Elite Redux: Functions identically to mainline games
- Boost applies to all damage-dealing moves without exception
- AI recognizes and properly evaluates Plus/Minus synergies
- No activation message (passive boost during damage calculation)
- Perfect symmetry with Plus ability implementation