---
id: 22
name: Intimidate
status: reviewed
character_count: 90
---

# Intimidate - Ability ID 22

## In-Game Description
"Lowers foes' Atk by one stage on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, the user drops the Attack stat of all opposing Pokemon by one stage.

## Detailed Mechanical Explanation
*For Discord/reference use*

**INTIMIDATE** is an entry-based stat-lowering ability that reduces opponents' Attack stats upon switching in.

### Activation Mechanics:
- **Trigger**: Immediately upon entering battle (onEntry hook)
- **Effect**: Lowers Attack by 1 stage (-1 stage = 2/3 original Attack)
- **Targets**: All opposing Pokemon in battle
- **Repeated Use**: Activates every time the user switches in, even multiple times per battle
- **Battle Script**: Uses `BattleScript_IntimidateActivatedNew` for animation and messaging

### Technical Implementation:
```c
constexpr Ability Intimidate = {
    .onEntry = UseIntimidateClone,
};

// From gIntimidateCloneData array:
{
    .ability = ABILITY_INTIMIDATE,
    .numStatsLowered = 1,
    .statsLowered = {STAT_ATK, 0, 0},
    .targetBoth = TRUE,
    .statChange = 1,  // 1 stage reduction
}
```

### Targeting Rules:
- **Singles**: Affects the single opposing Pokemon
- **Doubles**: Affects both opposing Pokemon simultaneously
- **Multiple Opponents**: Each opponent is affected independently
- **Ally Immunity**: Never affects the user's partner in doubles

### Immunity and Interactions:
**Complete Immunity (No Effect):**
- Clear Body: "Prevents stat reduction!"
- Full Metal Body: Mega/Primal version of Clear Body
- Hyper Cutter: Specifically protects Attack and Special Attack
- Oblivious: Immune to "infatuation, Scare, Intimidate and Taunt"
- Own Tempo: Immune to "confusion, Intimidate and Scare"  
- Inner Focus: Blocks "flinch, Intimidate, Scare"
- Scrappy: Immune to "Intimidate/Scare"

**Special Interactions:**
- **Guard Dog**: Reverses effect, gains +1 Attack instead of losing it
- **Contrary**: Would reverse the stat change (loses Attack = gains Attack)
- **Defiant**: Triggers +2 Attack when Intimidated
- **Competitive**: No interaction (only triggered by Special Attack drops)

### Entry Priority:
- Intimidate activates during switch-in processing
- Multiple Intimidate users activate in speed order
- Other entry abilities (weather, hazards) may activate before or after depending on implementation

### Competitive Applications:
**Offensive Support:**
- Weakens physical attackers before they can attack
- Enables safe switches for frail teammates
- Pivoting strategy with U-turn/Volt Switch + Intimidate

**Defensive Utility:**
- Reduces damage from incoming physical attacks
- Stacks with other defensive abilities (Rocky Helmet, Rough Skin)
- Particularly effective against mono-physical threats

**Team Synergy:**
- Pairs well with U-turn/Volt Switch for repeated activation
- Supports setup sweepers by neutering physical threats
- Valuable on pivot Pokemon and lead Pokemon

### Strategic Considerations:
- **Limited to Physical**: No effect on special attackers
- **One-Time Per Switch**: Effect doesn't stack with multiple Intimidate users
- **Immunity Prevalence**: Many competitive Pokemon have Intimidate immunity
- **Substitutes**: Intimidate cannot affect Pokemon behind substitutes

### Version Notes:
- Elite Redux: Functions identically to standard Pokemon games
- Activation message: "{Pokemon}'s Intimidate cuts {target}'s attack!"
- Animation: Standard stat-down animation with intimidating visual effect