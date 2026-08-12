---
id: 470
name: Archer
status: reviewed
character_count: 52
---

# Archer - Ability ID 470

## In-Game Description
"Boosts the power of arrow-based moves by 30%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Archer boosts the power of arrow-based moves by 30%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Archer is an offensive ability that provides a 30% power boost to all moves flagged as "arrow-based" in the game data. This ability enhances the precision and power of ranged attacks, making it ideal for Pokemon with archer-like themes.

### Activation Conditions
- **Move requirement**: The move must have the `arrowBased` flag set to true
- **Boost amount**: 30% power increase (1.3x multiplier)
- **Move types**: Works with both physical and special arrow-based moves
- **Target**: Affects single-target and multi-target arrow moves

### Arrow-Based Moves Enhanced
- **Thousand Arrows** (Ground-type, 90 BP to 117 BP)
- **Spirit Shackle** (Ghost-type, 85 BP to 110.5 BP)
- **Diamond Arrow** (Rock-type, 85 BP to 110.5 BP)
- **Blazing Arrow** (Fire-type)
- **Triple Arrows** (Fighting-type)
- Many custom Elite Redux arrow moves

### Technical Implementation
```c
constexpr Ability Archer = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].arrowBased) MUL(1.3);
        },
};
```

### Important Interactions
- **Power stacking**: Stacks multiplicatively with other power boosts
- **STAB interaction**: Works alongside Same Type Attack Bonus
- **Weather/terrain**: Combines with weather and terrain boosts
- **Choice items**: Stacks with Choice Band/Specs when applicable
- **Critical hits**: Enhanced moves can still critically hit for even more damage

### Ability Integration
- **Mythical Arrows**: Another ability that references Archer's boost mechanism
- **Mega Launcher**: Some arrow moves also have Mega Launcher boost
- **Sniper**: Common pairing for critical hit arrow moves

### Strategic Implications
- **Archer role-play**: Thematically fits Decidueye and similar Pokemon
- **Precision offense**: Makes arrow moves reliable damage dealers
- **Coverage enhancement**: Boosts unique moves not typically powered up
- **Niche movepool**: Limited to arrow-flagged moves only
- **Type diversity**: Arrow moves span multiple types

### Common Users
**Known Pokemon with Archer:**
- **Decidueye** (including Hisuian forme)
- **Decidueye Mega**
- **Ribombee Redux** (as innate ability)
- **Ribombee Redux Mega**

### Competitive Usage Notes
- Transforms niche arrow moves into viable offensive options
- Essential for Decidueye's signature Spirit Shackle viability
- Creates powerful Thousand Arrows users outside of Zygarde
- Makes Diamond Arrow a legitimate Rock-type physical option
- Pairs well with high critical hit ratio moves

### Movepool Considerations
- **Physical arrows**: Thousand Arrows, Spirit Shackle, Diamond Arrow
- **Special arrows**: Various custom elemental arrow attacks
- **Status arrows**: Some arrow moves have secondary effects
- **Multi-hit**: Triple Arrows benefits significantly
- **Priority**: Any priority arrow moves get enhanced

### Synergies
- **Sniper**: Enhanced critical hits on arrow moves
- **Scope Lens**: Increased critical hit rate
- **Choice items**: Raw power boost stacking
- **Life Orb**: Additional damage at HP cost
- **Type gems**: One-time type-specific boost

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Ghost immunity**: Normal/Fighting arrow moves
- **Type immunities**: Ground immunity affects Thousand Arrows
- **Protect variations**: Blocking arrow moves entirely
- **Intimidate**: Reduces physical arrow move damage

### Version History
- Custom Elite Redux ability (ID 470)
- Designed to enhance archer-themed Pokemon
- Part of the enhanced Decidueye line abilities
- Integrated with arrow move flagging system

### Design Philosophy
Archer represents the precision and power of skilled marksmen in Pokemon form. The ability emphasizes accuracy-based offensive gameplay while providing meaningful boosts to otherwise niche moves, creating a distinct offensive archetype focused on ranged combat excellence.