---
id: 791
name: DNA Scramble
status: reviewed
character_count: 195
---

# DNA Scramble - Ability ID 791

## In-Game Description
"Changes forms based on the the move used."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Transforms Deoxys between forms based on the move used. Damaging moves trigger Attack form, Recover triggers Defense form, other status moves trigger Speed form. Form changes occur before attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
DNA Scramble is an exclusive ability for Deoxys that automatically transforms it between its four different forms based on the type of move being used. The transformation occurs during the `onBeforeAttack` phase, meaning the form change happens before the move is executed, allowing the new form's stats to affect the attack.

### Activation Conditions
The ability triggers before any attack and evaluates the move being used to determine the target form:

1. **Attack Form Transformation**: Any move with power > 0 (damaging moves)
2. **Defense Form Transformation**: Specifically the move Recover
3. **Speed Form Transformation**: Any status move (split == SPLIT_STATUS) except Recover
4. **Base Form**: Starting form with balanced stats

### Form Statistics
```
Base Form (Normal):    HP: 50, Atk: 150, Def: 50, SpAtk: 150, SpDef: 50, Speed: 150
Attack Form:           HP: 50, Atk: 180, Def: 20, SpAtk: 180, SpDef: 20, Speed: 150
Defense Form:          HP: 50, Atk: 70,  Def: 160, SpAtk: 70, SpDef: 160, Speed: 90
Speed Form:            HP: 50, Atk: 95,  Def: 90, SpAtk: 95, SpDef: 90, Speed: 180
```

### Technical Implementation
```cpp
constexpr Ability DNAScramble = {
    .onBeforeAttack = +[](ABILITY_ON_BEFORE_ATTACK) -> int {
        SpeciesEnum newSpecies = SPECIES_NONE;
        switch (gBattleMons[battler].species) {
            case SPECIES_DEOXYS:
                if (gBattleMoves[move].power > 0)
                    newSpecies = SPECIES_DEOXYS_ATTACK;
                else if (move == MOVE_RECOVER)
                    newSpecies = SPECIES_DEOXYS_DEFENSE;
                else if (gBattleMoves[move].split == SPLIT_STATUS)
                    newSpecies = SPECIES_DEOXYS_SPEED;
                break;
            // Additional form-specific logic for each form...
        }
        
        UpdateAbilityStateIndicesForNewSpecies(battler, newSpecies);
        gBattleMons[battler].species = newSpecies;
        BattleScriptCall(BattleScript_AttackerFormChange);
        return TRUE;
    },
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
};
```

### Form Change Logic by Current Form

**From Base Form (SPECIES_DEOXYS):**
- Damaging moves to Attack Form
- Recover to Defense Form  
- Other status moves to Speed Form

**From Attack Form:**
- Recover to Defense Form
- Status moves (except Recover) to Speed Form
- Damaging moves to Stay in Attack Form

**From Defense Form:**
- Damaging moves to Attack Form
- Status moves (except Recover) to Speed Form
- Recover to Stay in Defense Form

**From Speed Form:**
- Damaging moves to Attack Form
- Recover to Defense Form
- Other status moves to Stay in Speed Form

### Ability Properties
- **Unsuppressable**: Cannot be suppressed by abilities like Neutralizing Gas
- **Randomizer Banned**: Excluded from randomizer due to species-specific nature
- **Form Change Animation**: Triggers `BattleScript_AttackerFormChange` for visual effect

### Strategic Implications

**Attack Form Usage:**
- Maximizes offensive power with 180 Attack and Special Attack
- Extremely frail with only 20 Defense and Special Defense
- Best for hit-and-run tactics or when you need maximum damage output
- Vulnerable to priority moves due to reduced bulk

**Defense Form Usage:**
- Becomes an exceptional wall with 160 Defense and Special Defense
- Significantly reduced offensive presence (70 Attack/Special Attack)
- Lower speed (90) makes it more vulnerable to setup
- Ideal for stalling strategies or when expecting powerful attacks

**Speed Form Usage:**
- Reaches maximum speed of 180, outspeeding almost everything
- Balanced offensive stats (95 Attack/Special Attack) 
- Good for status moves, setup, or revenge killing
- Can utilize status moves to maintain form

### Common Users
DNA Scramble is exclusive to Deoxys and its forms. No other Pokemon can have this ability.

### Competitive Usage Notes
- **Versatility**: Allows Deoxys to adapt its role mid-battle based on needs
- **Prediction Game**: Opponents must guess which form Deoxys will take based on predicted moves
- **Move Selection Pressure**: Forces careful consideration of move choice due to stat implications
- **Setup Synergy**: Can use status moves to enter Speed form, then use that speed for offensive moves to switch to Attack form

### Counters
- **Priority Moves**: Can revenge kill Attack form due to its poor bulk
- **Taunt**: Prevents status moves, limiting form change options
- **Multi-hit Moves**: Can break through Defense form's bulk
- **Status Conditions**: Burn reduces Attack form's physical damage significantly
- **Choice Items**: Lock Deoxys into one move type, limiting form adaptability

### Synergies
- **Life Orb**: Boosts damage in Attack form while the recoil is manageable due to form switching
- **Focus Sash**: Protects frail Attack form from one-hit KOs
- **Leftovers**: Provides consistent recovery across all forms
- **Recover**: Guarantees access to Defense form when needed for bulk
- **Status Moves**: Allow controlled switching to Speed form for positioning

### Version History
DNA Scramble is a custom ability created for Elite Redux, designed to showcase Deoxys's adaptability and alien DNA manipulation capabilities. The ability emphasizes tactical decision-making and form optimization based on battle conditions.

### Example Scenarios

**Scenario 1**: Deoxys starts in base form, uses Psycho Boost (damaging move) to transforms to Attack form with 180 SpAtk, then uses Recover to transforms to Defense form with 160 defenses.

**Scenario 2**: Deoxys in Speed form uses Thunder Wave (status move) to stays in Speed form, then uses Zen Headbutt (damaging move) to transforms to Attack form for maximum damage.

**Scenario 3**: Deoxys in Attack form faces a powerful physical attacker to uses Recover to immediately transforms to Defense form to tank the incoming attack.