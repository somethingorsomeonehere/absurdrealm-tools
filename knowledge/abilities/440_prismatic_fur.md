---
id: 440
name: Prismatic Fur
status: reviewed
character_count: 206
---

# Prismatic Fur - Ability ID 440

## In-Game Description
"Color Change + Protean + Fur Coat + Ice Scales."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Changes type to resist attacks before getting hit, changes type to match moves before landing a hit, halves physical damage, and halves special damage. Damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Prismatic Fur is an extremely powerful hybrid ability that combines the effects of four separate abilities into one comprehensive defensive package. It provides both defensive multipliers and type-changing mechanics.

### Component Abilities Analysis

#### 1. Color Change Component
- **Trigger**: When the Pokemon is targeted by an attack
- **Effect**: Changes the Pokemon's type to the one that resists the incoming move most effectively
- **Timing**: Before the attack hits
- **Limitation**: Once per turn activation

#### 2. Protean Component  
- **Trigger**: When the Pokemon uses an attack
- **Effect**: Changes the Pokemon's type to match the move being used
- **Timing**: Before the attack is executed
- **Limitation**: Once per turn activation
- **Benefit**: Provides STAB (Same Type Attack Bonus) on all moves

#### 3. Fur Coat Component
- **Effect**: Halves all physical damage taken (0.5x multiplier)
- **Coverage**: Affects all contact and non-contact physical moves
- **Interaction**: Stacks multiplicatively with type resistances

#### 4. Ice Scales Component
- **Effect**: Halves all special damage taken (0.5x multiplier)  
- **Coverage**: Affects all special moves
- **Interaction**: Stacks multiplicatively with type resistances

### Technical Implementation
```cpp
constexpr Ability PrismaticFur = {
    // Ice Scales + Fur Coat effect - halves ALL damage
    .onDefensiveMultiplier = +[](ON_DEFENSIVE_MULTIPLIER) { MUL(.5); },
    
    // Combined Protean + Color Change logic
    .onBeforeAttack = +[](ABILITY_ON_BEFORE_ATTACK) -> int {
        // Protean activates when attacking
        if (battler == attacker && Protean.onBeforeAttack(DELEGATE_ON_BEFORE_ATTACK)) 
            return TRUE;
        // Color Change activates when being attacked
        return ColorChange.onBeforeAttack(DELEGATE_ON_BEFORE_ATTACK);
    },
    .onBeforeAttackFor = APPLY_ON_ATTACKER_OR_TARGET,
};
```

### Activation Priority
1. **Defensive multiplier**: Always applies first (0.5x damage)
2. **Type changes**: Processed before damage calculation
3. **Protean**: Takes priority when the Pokemon is attacking
4. **Color Change**: Activates when being targeted

### Mathematical Damage Reduction
With the 0.5x multiplier from both physical and special defense:
- **Neutral effectiveness**: 0.5x damage (50% reduction)
- **Not very effective (0.5x)**: 0.25x damage (75% reduction)
- **Super effective (2x)**: 1.0x damage (normal damage)
- **4x super effective**: 2.0x damage (still only double)

### Strategic Implications

#### Offensive Benefits
- **STAB on all moves**: Protean component provides 1.5x damage on every attack
- **Unpredictable typing**: Opponents can't predict your type from team preview
- **Coverage optimization**: Can adapt type for optimal damage output

#### Defensive Benefits
- **Universal damage reduction**: Resists both physical and special attacks
- **Type adaptation**: Can become resistant to predicted threats
- **Status move immunity**: Can change to types immune to certain status moves
- **Entry hazard resistance**: Can adapt to resist Stealth Rock and spikes

#### Unique Interactions
- **Multi-hit moves**: Each hit triggers separate type evaluation
- **Priority moves**: Type changes occur before damage calculation
- **Weather immunity**: Can adapt to become immune to weather damage
- **Status immunity**: Can change to types immune to certain status conditions

### Counterplay and Limitations

#### Direct Counters
- **Mold Breaker**: Ignores the ability entirely
- **Neutralizing Gas**: Suppresses all ability effects
- **Ability suppression moves**: Role Play, Skill Swap, etc.

#### Strategic Counters
- **Mixed attackers**: Force adaptation between physical/special
- **Multi-type moves**: Harder to optimally resist
- **Status moves**: Some cannot be resisted by type changes
- **Entry hazards**: Set up before type adaptation

#### Timing Limitations
- **Once per turn**: Both type changes have turn limitations
- **Prediction dependent**: Color Change requires knowing incoming moves
- **Switch vulnerability**: Type resets on switching out

### Competitive Viability

#### Tier Assessment
- **Extremely high**: One of the most powerful defensive abilities
- **Format defining**: Likely to be banned in many competitive formats
- **Versatility**: Works on any Pokemon regardless of base stats

#### Team Synergy
- **Pivot Pokemon**: Excellent for switching into threats
- **Defensive core**: Provides unparalleled mixed bulk
- **Stall teams**: Nearly unbreakable defensive presence
- **Balance teams**: Provides both offensive and defensive utility

#### Common Applications
- **Physical walls**: Enhanced by Ice Scales coverage
- **Special walls**: Enhanced by Fur Coat coverage  
- **Mixed walls**: Covers both attack types perfectly
- **Utility Pokemon**: Can adapt to any role needed

### Notable Interactions

#### Type Change Mechanics
- **Dual typing**: Retains dual typing when applicable
- **Form changes**: Interacts with form-changing abilities
- **Illusion**: Can reveal Zoroark through type changes
- **Forecast**: Conflicts with weather-based type changes

#### Damage Calculation
- **Berry reduction**: Stacks with damage-reducing berries
- **Reflect/Light Screen**: Multiplicative stacking with screens
- **Burn**: Physical damage reduction stacks with burn
- **Sand/Hail**: Can adapt to become immune to weather damage

#### Status Interactions
- **Poison immunity**: Can change to Steel/Poison types
- **Burn immunity**: Can change to Fire type
- **Paralysis immunity**: Can change to Electric type (Limber separate)
- **Sleep immunity**: Limited type-based sleep immunity

### Ability Comparison

#### vs Individual Components
- **Protean alone**: Provides offense but no defense
- **Color Change alone**: Provides adaptation but no guaranteed reduction
- **Fur Coat alone**: Only covers physical attacks
- **Ice Scales alone**: Only covers special attacks

#### vs Other Defensive Abilities
- **Wonder Guard**: More restrictive but can achieve immunity
- **Magic Guard**: Different protection profile (indirect damage)
- **Multiscale**: Conditional but potentially stronger
- **Filter/Solid Rock**: Less damage reduction but no restrictions

### Usage Recommendations

#### Pokemon Selection
- **High HP**: Maximizes effective bulk from damage reduction
- **Balanced stats**: Benefits from both physical and special reduction
- **Good movepool**: Takes advantage of Protean STAB on all moves
- **Utility moves**: Can adapt typing for optimal support

#### Move Selection
- **Coverage moves**: Each gains STAB through Protean
- **Status moves**: Can adapt typing for immunity/resistance
- **Recovery moves**: Essential for maintaining defensive presence
- **Setup moves**: Can adapt to resist common revenge killers

#### Item Pairing
- **Leftovers**: Provides consistent recovery
- **Assault Vest**: Stacks with Ice Scales for special bulk
- **Rocky Helmet**: Punishes contact moves on physical attacks
- **Heavy-Duty Boots**: Prevents entry hazard damage

### Version History
- **Elite Redux exclusive**: Not present in official Pokemon games
- **Hybrid ability**: Represents pinnacle of ability combination design
- **Balance consideration**: May require restriction in competitive play
- **Implementation**: Uses advanced ability delegation system

### Development Notes
The ability showcases Elite Redux's innovative approach to ability design, combining multiple existing abilities into a cohesive new ability. The implementation uses the game's delegation system to call the original abilities' functions while adding the unified defensive multiplier.

This ability represents one of the most comprehensive defensive tools available in the game, providing both immediate damage reduction and adaptive type coverage. Its inclusion demonstrates Elite Redux's commitment to creating unique and powerful ability combinations that expand strategic possibilities.