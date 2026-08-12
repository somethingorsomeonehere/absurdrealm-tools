---
id: 148
name: Analytic
status: reviewed
character_count: 65
---

# Analytic - Ability ID 148

## In-Game Description
"Attacks get a 1.3x power boost if it moves last."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user moves after the target, boosts attack power by 30%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Power Boost**: 1.3x damage multiplier (30% increase)
- **Activation Condition**: When `GetBattlerTurnOrderNum(target) < gCurrentTurnActionNumber`
- **Move Restriction**: Does not affect Future Sight or Doom Desire (`gBattleMoves[move].effect != EFFECT_FUTURE_SIGHT`)

### Technical Implementation
```cpp
constexpr Ability Analytic = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (GetBattlerTurnOrderNum(target) < gCurrentTurnActionNumber && gBattleMoves[move].effect != EFFECT_FUTURE_SIGHT) MUL(1.3);
        },
};
```

### Turn Order Mechanics
The ability determines activation by comparing:
1. **Target's Turn Position**: `GetBattlerTurnOrderNum(target)` - when the target is scheduled to move
2. **Current Action Number**: `gCurrentTurnActionNumber` - how many Pokemon have already acted

If the target has already moved (target's position < current action), Analytic activates.

### Future Sight Exception
Future Sight and Doom Desire are specifically excluded because:
- They strike 3 turns in the future, not during the current turn
- The original user might not even be on the field when they hit
- Turn order context doesn't apply to delayed attacks

### Activation Examples

**Scenario 1: Speed-based turns**
- Turn order: Fast Pokemon (1) to Slow Pokemon with Analytic (2)
- Fast Pokemon attacks first
- Slow Pokemon's Analytic activates (1 < 2) ✓

**Scenario 2: Priority moves**
- Turn order: Priority user (1) to Analytic user (2)
- Priority move goes first
- Analytic activates on response (1 < 2) ✓

**Scenario 3: Same priority, different speeds**
- Fast attacker moves before slow Analytic user
- Analytic activates ✓

### Strategic Implications

#### Optimal Users
Analytic excels on:
- **Slow, powerful attackers** - Naturally move last to trigger boost
- **Trick Room sweepers** - Turn order reversal guarantees activation
- **Choice Band/Specs users** - Stacks with damage-boosting items
- **Wall breakers** - 30% boost helps break through defenses

#### Team Synergy
- **Trick Room**: Reverses speed tiers, making slow Analytic users move first (ironically reducing effectiveness in TR)
- **Speed control**: Using moves like Icy Wind to ensure moving last
- **Pivoting**: Slow U-turn/Volt Switch users can revenge kill with boosted attacks

### Move Interactions

#### Boosted Moves
- All physical and special attacks (except Future Sight/Doom Desire)
- Multi-hit moves get the boost on each hit
- Variable power moves (e.g., Gyro Ball, Payback)
- Status moves that deal damage (e.g., Thunder Wave variants)

#### Unboosted Moves
- Future Sight and Doom Desire specifically
- Pure status moves (don't deal damage)
- Self-targeting moves

### Damage Calculations

**Example**: Analytic Machamp using Close Combat
- Base Attack: 300 (after stat boosts)
- Close Combat Base Power: 120
- Analytic Boost: 1.3x
- **Total**: 300 x 120 x 1.3 = 46,800 damage calculation base

Compare to no boost: 300 x 120 = 36,000
**Effective increase**: 30% more damage

### Interactions with Other Abilities

#### Synergistic Combinations
**Strategic Pause (Analytic + Crit boost)**:
- 30% damage boost when moving last
- +2 critical hit ratio when moving last
- Devastating combination for slow sweepers

**Haste Makes Waste (Analytic + Stall)**:
- 30% damage boost when moving last  
- 30% damage reduction when being attacked first
- Perfect for slow bulky attackers

**Calculative (Analytic + Neuroforce)**:
- 30% boost when moving last
- Additional boost on super-effective moves
- Creates extremely powerful coverage attackers

#### Counters and Limitations
- **Speed control**: Paralysis, Tailwind can disrupt activation
- **Priority abuse**: Prankster, Gale Wings bypass turn order
- **Fast pivoting**: Quick U-turn/Volt Switch before Analytic user acts
- **Trick Room**: Can backfire by making Analytic user move first

### Common Users in Elite Redux

Based on the species data, Analytic appears on:
- **Porygon line** (Porygon-Z): Special attackers with diverse movepool
- **Slowking variants**: Bulky special attackers
- **Steel types**: Defensive pivots with powerful attacks  
- **Various moths/bugs**: Often paired with other analytical abilities
- **Psychic types**: Mixed attackers benefiting from turn prediction

### Competitive Analysis

#### Strengths
- Consistent 30% damage boost for slow Pokemon
- No setup required - passive benefit
- Stacks with all other damage modifiers
- Excellent for revenge killing faster threats

#### Weaknesses  
- Completely dependent on turn order
- No benefit when moving first
- Future Sight immunity reduces some niche strategies
- Can be manipulated by priority moves

#### Usage Tips
1. **EV Spreads**: Minimize Speed investment to ensure moving last
2. **Item Choices**: Life Orb, Choice items stack multiplicatively  
3. **Move Selection**: Powerful STAB moves benefit most from the boost
4. **Prediction**: Works best when you can predict opponent's actions
5. **Team Support**: Pair with entry hazards to secure KOs with boosted attacks

## Conclusion

Analytic transforms slow Pokemon from potential liabilities into powerful revenge killers and wall breakers. The 30% damage boost is substantial enough to change many damage calculations, turning 2HKOs into OHKOs. While situational, it rewards patient play and good prediction skills. In Elite Redux's multi-ability system, Analytic combines excellently with other tactical abilities to create unique strategic profiles that balance offense and defense around turn order manipulation.