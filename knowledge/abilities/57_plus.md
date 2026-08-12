---
id: 57
name: Plus
status: reviewed
character_count: 89
---

# Plus - Ability ID 57

## In-Game Description
"Deals double damage if an ally Pokemon has Minus or Plus."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles the Pokemon's offensive power when partnered with an ally that has Plus or Minus.

## Detailed Mechanical Explanation
*For Discord/reference use*

**PLUS** is a double-battle synergy ability that provides conditional offensive power through partner cooperation.

### Activation Mechanics:
- **Trigger**: Applied during damage calculation (onOffensiveMultiplier hook)
- **Condition**: Battle partner must be alive and have ABILITY_PLUS or ABILITY_MINUS
- **Effect**: Multiplies offensive power by 2.0x for all moves
- **Battle Format**: Only functions in double battles where partner slot exists

### Partner Requirements:
- **Partner Alive**: `IsBattlerAlive(partner)` must return true
- **Partner Ability**: Must have exactly ABILITY_PLUS (ID 57) or ABILITY_MINUS (ID 58)
- **Position**: Uses `BATTLE_PARTNER(battler)` to identify ally slot
- **Real-time Check**: Evaluated each time a move is used

### Damage Calculation:
1. **Base Move Power** (from move data)
2. **STAB, Type Effectiveness** (standard modifiers)
3. **Plus Multiplier** (x2.0 if partner condition met)
4. **Other Ability Effects** (applied after Plus)
5. **Item Effects** (Choice specs, Life Orb, etc.)

### Key Interactions:
- **vs Choice Items**: Plus doubles damage, Choice items multiply by 1.5x. Stack multiplicatively (x3.0 total)
- **vs Life Orb**: Plus effect applied first, then Life Orb's 1.3x multiplier
- **vs Critical Hits**: Critical hit multiplier applies after Plus effect
- **vs Weather/Terrain**: Environmental boosts stack with Plus multiplicatively

### Ability Relationships:
- **Minus (ID 58)**: Functionally identical ability with same code implementation
- **Shared Implementation**: `Minus.onOffensiveMultiplier = Plus.onOffensiveMultiplier`
- **Mutual Activation**: Plus activates with Minus partner and vice versa
- **Self-Activation**: Plus Pokemon activates when partnered with another Plus Pokemon

### Technical Implementation:
```c
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

### Move Synergies:
- **Gear Up (Move 637)**: Boosts Attack and Sp. Attack of Plus/Minus Pokemon by 1 stage
- **Magnetic Flux (Move 602)**: Boosts Defense and Sp. Defense of Plus/Minus Pokemon by 1 stage
- **AI Recognition**: Battle AI specifically checks for Plus/Minus when evaluating these moves

### AI Battle Rating:
- **Priority Score**: 0 (low priority for AI switching decisions)
- **Conditional Value**: AI recognizes high value when Plus/Minus partners are available
- **Team Building**: AI considers Plus/Minus pairs when constructing double battle teams

### Pokemon Distribution in Elite Redux:
- **As Innate Ability**: Multiple Electric-type Pokemon including Pichu variants
- **Notable Users**: Electric-types with high offensive stats
- **Partner Pokemon**: Several species have Minus as innate, creating natural pairs
- **Tier Usage**: Found across tiers 2-4, balanced for competitive play

### Competitive Analysis:
- **Power Level**: Extremely high in double battles (x2.0 damage multiplier)
- **Team Dependency**: Requires specific partner to function, limiting flexibility  
- **Positioning Risk**: Both Pokemon must stay alive for effect to persist
- **Setup Potential**: Works well with stat-boosting moves like Gear Up

### Strategic Applications:
1. **Double Battle Dominance**: Creates overwhelming offensive pressure with correct partner
2. **Support Move Synergy**: Gear Up and Magnetic Flux become highly valuable
3. **Lead Strategy**: Plus/Minus pairs excel as opening leads in doubles
4. **Late Game Cleaning**: High damage output can secure victories

### Counters and Limitations:
- **Single Target Removal**: Eliminating either partner disables the ability
- **Positioning Moves**: Moves that force switches or repositioning
- **Status Conditions**: Sleep, paralysis can prevent effective coordination
- **Protect/Detect**: Can disrupt synchronized offensive strategies

### Common Misconceptions:
- **Singles Usage**: Completely non-functional in single battles (no partner slot)
- **Partner Health**: Effect immediately stops when partner faints
- **Ability Suppression**: Mold Breaker and similar effects can disable Plus
- **Move Restrictions**: Works with ALL moves, no type or category limitations

### Version History:
- **Gen 3**: Introduced as signature ability of Plusle and Minun
- **Elite Redux**: Expanded distribution as innate ability on various Electric-types
- **Implementation**: Uses modern partner detection system with real-time checking

### Tactical Considerations:
- **Team Composition**: Requires building around Plus/Minus pair for maximum effectiveness
- **Speed Control**: Coordinating turn order crucial for optimal damage output
- **Protect Usage**: Strategic protection can maintain partner synergy
- **Switch Timing**: Must consider maintaining both Pokemon on field