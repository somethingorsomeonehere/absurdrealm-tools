---
id: 77
name: Tangled Feet
status: reviewed
character_count: 175
---

# Tangled Feet - Ability ID 77

## In-Game Description
"Doubles Evasion when confused."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user is confused or enraged, the Pokemon uses its Speed stat instead of Defense or Special Defense for damage calculations. Choice Scarf does not affect this ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

**TANGLED FEET** is a defensive ability that reduces incoming accuracy while the user is confused.

### Core Mechanics:
- **Trigger**: Only when this Pokemon has the confused status (STATUS2_CONFUSION)
- **Effect**: Halves the accuracy of moves targeting this Pokemon (*accuracy /= 2)
- **Application**: Applied during accuracy calculation phase with ACCURACY_MULTIPLICATIVE priority
- **Target Requirement**: Uses onAccuracyFor = APPLY_ON_TARGET (affects moves targeting this Pokemon)

### Activation Conditions:
1. **Status Check**: Pokemon must have STATUS2_CONFUSION bit set
2. **Target Validation**: Only applies when this Pokemon is the target of a move
3. **Move Coverage**: Affects all moves (attacking, status, etc.) that target this Pokemon
4. **Duration**: Active for entire duration of confusion status

### Technical Implementation:
```c
constexpr Ability TangledFeet = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(gBattleMons[target].status2 & STATUS2_CONFUSION);
        *accuracy /= 2;
        return ACCURACY_MULTIPLICATIVE;
    },
    .onAccuracyFor = APPLY_ON_TARGET,
    .breakable = TRUE,
};
```

### Numerical Values:
- **Accuracy Modifier**: 0.5x (50% of original accuracy)
- **Examples**:
  - Thunder Bolt (100% accuracy) to 50% accuracy
  - Thunder (70% accuracy) to 35% accuracy
  - Fire Blast (85% accuracy) to 42.5% accuracy
  - Focus Blast (70% accuracy) to 35% accuracy

### Interactions with Other Abilities/Mechanics:
1. **Ability Interactions**:
   - Overridden by **No Guard** (both user and opponent)
   - Stacks with **Sand Veil/Snow Cloak** evasion boosts
   - Works alongside **Wonder Skin** for status moves
   - Bypassed by **Keen Eye** users attacking this Pokemon

2. **Move Interactions**:
   - Affects **never-miss moves** like Swift and Aerial Ace (they still hit)
   - Reduces accuracy of **OHKO moves** (already low accuracy)
   - Applies to **status moves** targeting this Pokemon
   - Stacks multiplicatively with accuracy drops from moves like Sand Attack

3. **Status Synergy**:
   - **Own Tempo** prevents confusion, negating this ability
   - **Lum Berry/Mental Herb** cure confusion, ending the effect
   - Confusion from **Swagger** activates this ability
   - **Persim Berry** cures confusion after eating

### Strategic Implications:
1. **Defensive Strategy**:
   - Intentionally getting confused can provide evasion
   - Pairs well with Swagger users for setup
   - Creates mind games around confusion curing

2. **Risk vs Reward**:
   - Confusion deals self-damage 33% of the time
   - 50% accuracy reduction vs 33% self-harm chance
   - Becomes less effective as battle progresses due to confusion timer

3. **Team Support**:
   - Teammates can use Swagger to activate ability
   - Heal Bell/Aromatherapy can remove confusion when needed
   - Trick/Switcheroo with Persim Berry for timing control

### Common Users:
- **Original Games**: Spinda (signature ability), Doduo/Dodrio line
- **Elite Redux**: Currently appears in commented trainer parties but not actively used
- **AI Evaluation**: Rated 2/10 by battle AI (low priority ability)

### Competitive Usage Notes:
1. **Niche Applications**:
   - Anti-revenge kill tool (confusion + evasion)
   - Stall tactics in specific matchups
   - Surprise factor in casual play

2. **Limitations**:
   - Requires negative status to function
   - Confusion timer limits duration
   - Many Pokemon have access to never-miss moves
   - Self-damage risk often outweighs benefits

### Counters:
1. **Direct Counters**:
   - **No Guard** ability ignores accuracy modifiers
   - **Keen Eye** prevents accuracy reduction (when attacking)
   - Never-miss moves (Swift, Aerial Ace, etc.)
   - **Lock-On/Mind Reader** guarantees next move hits

2. **Indirect Counters**:
   - Status cleansing moves (Heal Bell, Aromatherapy)
   - Phazing moves (Roar, Whirlwind) to force switches
   - Multi-hit moves (more chances to hit)
   - Priority moves for guaranteed damage

### Synergies:
1. **Team Support**:
   - **Swagger** users to intentionally confuse
   - **Prankster** status spreaders
   - **Aromatic Veil** teammates for confusion immunity backup

2. **Item Synergies**:
   - **Leftovers** to offset confusion damage
   - **Mental Herb** for emergency confusion cure
   - **Persim Berry** for automatic confusion removal

3. **Move Synergies**:
   - **Rest** can cure confusion while healing
   - **Substitute** protects from confusion damage
   - **Facade** benefits from confusion status

### Version History:
- **Gen 4**: Introduced as Spinda's signature ability
- **Gen 5+**: Also given to Doduo/Dodrio line
- **Elite Redux**: Standard implementation, currently unused in active trainer parties

### Notes:
- One of the few abilities that requires a negative status to function
- The ability is breakable by Mold Breaker and similar effects
- Despite its unique concept, rarely sees competitive play due to inherent risks
- More effective against physical attackers due to confusion's physical damage component