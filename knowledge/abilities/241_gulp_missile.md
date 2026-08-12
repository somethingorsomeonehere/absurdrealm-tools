---
id: 241
name: Gulp Missile
status: reviewed
character_count: 300
---

# Gulp Missile - Ability ID 241

## In-Game Description
"Gulps a prey after Dive/Surf. If hit, shoots prey at enemy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When Cramorant uses Surf, Triple Dive or Dive, it catches prey: Gulping form if HP >50% or Gorging form if HP <=50%. When hit in either form, spits prey dealing 25% max HP damage to attacker and returns to base. Gulping Form also lowers Defense by 1; Gorging Form paralyzes. Cannot be suppressed etc. 

## Detailed Mechanical Explanation

### Form Change Trigger
Gulp Missile activates when Cramorant uses one of three specific moves:
- **Surf**
- **Triple Dive** 
- **Dive** (including accelerated two-turn variant)

The ability checks if:
1. The Pokemon is not transformed (e.g., not Ditto)
2. The Pokemon is specifically Cramorant (base form)
3. One of the trigger moves was used AND dealt damage OR the Pokemon is underwater (Dive's first turn)

### Form Determination
When triggered:
- **HP > 50%**: Changes to Cramorant-Gulping (caught a regular fish)
- **HP <= 50%**: Changes to Cramorant-Gorging (caught a Pikachu)

### Counterattack Mechanics
When Cramorant in Gulping or Gorging form is hit by any damaging move:
1. **Damage**: Deals exactly 25% of the attacker's maximum HP as damage
   - Minimum 1 damage if calculation rounds to 0
   - Ignores Magic Guard on the attacker
   - Bypasses Substitute (HITMARKER_IGNORE_SUBSTITUTE)
   - Classified as passive damage
2. **Form Reversion**: Always returns to base Cramorant form
3. **Additional Effects**:
   - **Gulping Form**: Lowers attacker's Defense by 1 stage (unless blocked by Clear Body, Full Metal Body, Clear Amulet, or Flower Veil)
   - **Gorging Form**: Attempts to paralyze the attacker

### Special Properties
- **Unsuppressable**: Cannot be suppressed by abilities like Neutralizing Gas
- **Randomizer Banned**: Not available in randomizer modes
- **Form Change Priority**: Updates ability state indices when changing forms
- **Battle Script Integration**: Uses dedicated battle scripts for each form's counterattack

### Key Code References
- Implementation: `src/abilities.cc` lines 2615-2641
- Battle Scripts: `data/battle_scripts_1.s` lines 8239-8318
- Ability Definition: `proto/AbilityList.textproto` entry for ABILITY_GULP_MISSILE

### Interactions and Edge Cases
1. The counterattack only triggers if `ShouldApplyOnHitAffect()` returns true
2. Magic Guard does NOT protect against the 25% HP recoil damage
3. The form change happens immediately during the move execution
4. Triple Dive was added as a trigger move in Elite Redux (not in vanilla)
5. The ability remains active even at 1 HP - form is based purely on HP percentage