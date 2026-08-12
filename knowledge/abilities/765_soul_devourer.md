---
id: 765
name: Soul Devourer
status: reviewed
character_count: 224
---

# Soul Devourer - Ability ID 765

## In-Game Description
"Soul Eater + Phantom Pain"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user knocks out an opponent with a direct hit, it immediately recovers 25% of its maximum HP. Removes Normal-type immunity to Ghost-type moves, allowing Ghost attacks to hit Normal-type Pokemon for 1x effectiveness. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Soul Devourer is a hybrid ability that grants two distinct effects by combining Soul Eater and Phantom Pain mechanics:

### Core Mechanics

**Soul Eater Component:**
- **Healing Effect**: When this Pokemon knocks out an opponent with any damaging move, it recovers 25% of its maximum HP
- **Trigger Condition**: Must directly cause the opponent to faint with an attack
- **Healing Requirements**: Must not be at full HP and must be able to heal (not affected by Heal Block)
- **Battle Script**: Uses `BattleScript_HandleSoulEaterEffect` which calls `tryhealpercenthealth BS_STACK_1, 25`

**Phantom Pain Component:**
- **Type Effectiveness Modification**: Ghost-type moves can hit Normal-type Pokemon
- **Effectiveness Value**: Changes Ghost vs Normal from 0x (no effect) to 1x (normal effectiveness)
- **Scope**: Only affects Ghost-type moves against Normal-type Pokemon

### Technical Implementation

```cpp
// Location: src/abilities.cc
constexpr Ability SoulDevourer = {
    .onBattlerFaints = SoulEater.onBattlerFaints,
    .onTypeEffectiveness = PhantomPain.onTypeEffectiveness,
    .onBattlerFaintsFor = SoulEater.onBattlerFaintsFor,
};
```

**Soul Eater Implementation:**
```cpp
constexpr Ability SoulEater = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler));
        CHECK(CanBattlerHeal(battler));
        BattleScriptCall(BattleScript_HandleSoulEaterEffect);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

**Phantom Pain Implementation:**
```cpp
constexpr Ability PhantomPain = {
    .onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
        CHECK(moveType == TYPE_GHOST)
        CHECK(defType == TYPE_NORMAL)
        CHECK_NOT(*mod)
        *mod = UQ_4_12(1.0);
        return TRUE;
    },
};
```

### Battle Script Details

```assembly
BattleScript_HandleSoulEaterEffect::
    tryhealpercenthealth BS_STACK_1, 25, BattleScript_Return
BattleScript_HandleSoulEaterEffect_AfterHeal:
    orword gHitMarker, HITMARKER_IGNORE_SUBSTITUTE
    healthbarupdate BS_STACK_1
    datahpupdate BS_STACK_1
    printstring STRINGID_STACKREGAINEDHEALTH
    waitmessage B_WAIT_TIME_LONG
    return
```

### Activation Conditions

**Healing Trigger:**
- Must defeat an opponent with a damaging move
- Cannot be at maximum HP
- Must not be affected by Heal Block
- Works with any damaging move type
- Applies to the attacking Pokemon only

**Type Effectiveness Trigger:**
- Only affects Ghost-type moves
- Only modifies effectiveness against Normal-type Pokemon
- Changes 0x effectiveness to 1x effectiveness
- Does not affect other type matchups

### Numerical Values

- **Healing Amount**: 25% of maximum HP (same as Soul Eater)
- **Type Effectiveness**: Changes Ghost vs Normal from 0x to 1x
- **Trigger Rate**: 100% on qualifying events

### Strategic Implications

**Offensive Advantages:**
- Enables Ghost-type moves to hit Normal-type Pokemon, removing a key immunity
- Provides sustain for sweep scenarios through healing on KO
- Excellent for prolonged battles and consecutive matchups
- Allows Ghost-type Pokemon to threaten Normal-types directly

**Competitive Usage:**
- Ideal for bulky offensive Pokemon that can secure KOs
- Synergizes well with multi-target moves in doubles
- Provides both offensive utility and defensive sustain
- Particularly valuable against Normal-type walls

### Common Users

**Mega Hisuian Typhlosion:**
- Type: Fire/Ghost
- Stats: 93/89/101/145/108/99
- Innate Abilities: Hellblaze, Early Grave, Vengeful Spirit
- Perfect synergy with Ghost-type STAB moves

### Interactions with Other Abilities

**Synergies:**
- **Hellblaze**: Innate ability that boosts Fire-type moves
- **Early Grave**: Innate ability that provides additional battle effects
- **Vengeful Spirit**: Innate ability that enhances Ghost-type utility

**Limitations:**
- Healing blocked by Heal Block
- Type effectiveness change doesn't affect other immunities
- Requires securing KOs to activate healing component
- Phantom Pain component only affects one specific type matchup

### Counters

**Healing Prevention:**
- Heal Block prevents the healing component
- Abilities that prevent healing (e.g., some custom abilities)
- Keeping the user at full HP negates healing trigger

**Type Effectiveness Counters:**
- Dark-type Pokemon resist Ghost moves regardless
- Steel-type Pokemon resist Ghost moves
- Other Ghost-type Pokemon are immune to Ghost moves (unaffected by Phantom Pain)

### Example Damage Calculations

**Ghost vs Normal with Soul Devourer:**
- Base damage x 1.0 (instead of x 0.0)
- Example: Shadow Ball vs Blissey becomes neutral damage instead of no effect
- Allows Ghost-type Pokemon to threaten Normal-type walls

**Healing Calculation:**
- Example: Pokemon with 400 max HP recovers 100 HP on each KO
- Minimum healing: 1 HP (if max HP <= 4)
- Maximum healing: 25% of max HP up to practical HP limits

### Competitive Viability

**Tier Assessment:** High - Combination of offensive utility and sustain
**Best Formats:** Singles and Doubles where securing KOs is feasible
**Team Synergy:** Excellent with offensive teams that can facilitate KOs
**Meta Relevance:** Strong against Normal-type cores and in sweep scenarios

### Version History

- **Elite Redux**: Introduced as a combination ability for Mega Hisuian Typhlosion
- **Implementation**: Part of the advanced ability system combining multiple effects
- **Balance**: Provides both offensive and defensive utility without being overpowered