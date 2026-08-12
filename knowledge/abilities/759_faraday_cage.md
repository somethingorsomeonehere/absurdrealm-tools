---
id: 759
name: Faraday Cage
status: reviewed
character_count: 292
---

# Faraday Cage - Ability ID 759

## In-Game Description
"Shell Armor + 50BP Thunder Cage when hit by contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Incoming damage is reduced by 20%, multiplicative with other damage reduction. Critical hits are blocked. Uses Thunder Cage when hit by contact moves, a 50 BP Electric-type Special move that traps the opponent for 4-5 turns. The target takes 1/8 max HP damage each turn and cannot switch out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics

Faraday Cage is a composite ability that combines the defensive properties of Shell Armor (which is based on Battle Armor) with an offensive retaliation effect:

**Defensive Component (Shell Armor/Battle Armor):**
- **Critical Hit Immunity**: Prevents the Pokemon from taking critical hits (NEVER_CRIT)
- **Physical Damage Reduction**: Reduces incoming physical damage by 20% (0.8x multiplier)
- **Breakable**: Can be bypassed by Mold Breaker and similar abilities

**Offensive Component (Thunder Cage Retaliation):**
```cpp
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(attacker))
    CHECK(IsMoveMakingContact(move, attacker))
    
    UseOutOfTurnAttack(battler, attacker, ability, MOVE_THUNDER_CAGE, 50);
    return FALSE;
},
```

### Activation Conditions

The Thunder Cage retaliation triggers when:
1. The Pokemon with Faraday Cage is hit by an attack
2. The attack makes contact (physical moves that can be affected by abilities like Static)
3. The hit effect should apply (not blocked by Sheer Force, etc.)

### Thunder Cage Properties

**Base Move Stats:**
- **Type**: Electric
- **Category**: Special
- **Power**: 80 (reduced to 50 when triggered by Faraday Cage)
- **Accuracy**: 90%
- **PP**: 15
- **Effect**: EFFECT_TRAP (partial trapping move)

**Trapping Mechanics:**
- Traps the target for 2-5 turns (typically 4-5 turns)
- Deals 1/8 of the target's maximum HP as damage at the end of each turn
- Prevents the target from switching out or fleeing
- Target is bound by the electric cage and takes continuous damage

### Strategic Implications

**Defensive Utility:**
- Excellent against physical attackers due to damage reduction and crit immunity
- Forces opponents to think twice about using contact moves
- Provides consistent damage output through trapping

**Offensive Potential:**
- Thunder Cage retaliation can deal significant damage over time
- Trapping effect disrupts opponent's switching strategies
- 50 BP Thunder Cage still respects type effectiveness and STAB

**Team Synergy:**
- Works well on bulky Electric-types that can tank hits
- Pairs effectively with entry hazards to maximize damage
- Good for stall teams that benefit from passive damage

### Common Users

Based on trainer data analysis, Faraday Cage is used by:
- **Stunfisk**: Bulky Ground/Electric type that benefits from physical bulk
- **Raging Bolt**: Paradox Pokemon with high HP and Special Attack
- **Tyranjoula**: Bug/Electric type that appreciates the defensive boost
- **Sandy Shocks**: Electric/Ground type with good bulk

### Competitive Usage Notes

**Strengths:**
- Deters physical attackers, especially those relying on contact moves
- Provides both immediate damage reduction and long-term damage output
- Cannot be completely negated (damage reduction always applies unless ability is suppressed)

**Counters:**
- Special attackers bypass the physical damage reduction
- Non-contact moves avoid the Thunder Cage retaliation
- Mold Breaker, Teravolt, and Turboblaze bypass the ability entirely
- Magic Guard prevents Thunder Cage's trapping damage

**Synergies:**
- **Leftovers/Black Sludge**: Enhances survivability for longer trapping
- **Electric Terrain**: Boosts Thunder Cage's power by 30%
- **Choice Specs**: If the Pokemon can somehow use Thunder Cage directly, increases damage
- **Entry Hazards**: Combines with trapping to rack up chip damage

### Example Damage Calculations

**Defensive Reduction:**
- 252+ Atk Life Orb Garchomp Earthquake: 84-99% to 67-79% (with Faraday Cage)
- 252+ Atk Choice Band Azumarill Aqua Jet: 63-74% to 50-59% (with Faraday Cage)

**Thunder Cage Retaliation:**
- 50 BP Thunder Cage from 252+ SpA Modest user about 25-30% to most neutral targets
- Additional 1/8 HP per turn for 4-5 turns = 50-62.5% total passive damage

### Version History

Faraday Cage is an Elite Redux original ability, combining defensive utility with offensive presence. The 50 BP Thunder Cage ensures the retaliation is meaningful without being overpowered, while the Shell Armor component provides consistent defensive value against physical threats.

The ability represents the concept of an electrical cage or shield that both protects the user and punishes those who make direct contact, fitting thematically with Electric-types that have defensive designs or capabilities.