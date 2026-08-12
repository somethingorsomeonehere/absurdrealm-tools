---
id: 796
name: Embody Aspect (Hearthflame)
status: reviewed
character_count: 73
---

# Embody Aspect (Hearthflame) - Ability ID 796

## In-Game Description
"+1 Attack on Entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises the Pokemon's Attack stat by one stage when switching into battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Embody Aspect (Hearthflame) is one of four variants of the Embody Aspect ability exclusive to Ogerpon forms. This variant provides an immediate Attack stat boost when the Pokemon enters battle, making it excellent for physical sweeping strategies.

### Activation Conditions
- **Entry trigger**: Activates when the Pokemon switches into battle
- **Battle start**: Also activates when sent out at the beginning of battle  
- **Timing**: Occurs before any other switch-in effects or abilities
- **Stat boost**: Raises Attack by exactly 1 stage (+50% physical damage)
- **Permanence**: The boost remains until the Pokemon switches out or faints

### Technical Implementation
```c
// Embody Aspect (Hearthflame) uses IntrepidSword's entry effect
constexpr Ability EmbodyAspectHearthflame = {
    .onEntry = IntrepidSword.onEntry,
};

// IntrepidSword implementation
constexpr Ability IntrepidSword = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, STAT_ATK))
        
        SetStatChanger(STAT_ATK, 1);
        BattleScriptPushCursorAndCallback(BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
        return TRUE;
    },
};
```

### Stat Calculation Details
- **Stage +1**: Multiplies Attack by 1.5x (150% of base Attack)
- **Damage formula**: Base damage x 1.5 for all physical moves
- **Stacking**: Can stack with other Attack boosts (items, moves, etc.)
- **Maximum**: Cannot boost beyond +6 stages (+400% total)

### Important Interactions
- **Priority**: Activates before Intimidate and other switch-in abilities
- **Failure conditions**: Cannot activate if Attack is already at +6 stages
- **Ability prevention**: Blocked by Clear Body, White Smoke, Hyper Cutter
- **Stat reset**: Boost is lost when switching out or using moves like Baton Pass
- **Mold Breaker synergy**: Ogerpon's innate Mold Breaker ignores defensive abilities

### Embody Aspect Variants
- **Embody Aspect (Base)**: +1 Speed on entry
- **Embody Aspect (Hearthflame)**: +1 Attack on entry  
- **Embody Aspect (Cornerstone)**: +1 Defense on entry
- **Embody Aspect (Wellspring)**: +1 Special Defense on entry

### Strategic Implications
- **Immediate threat**: Creates instant pressure on switch-in
- **Wallbreaking**: Turns Ogerpon into an immediate physical threat
- **Pivoting power**: Excellent for aggressive switching strategies
- **Setup alternative**: Provides free setup without using a turn
- **Lead potential**: Strong choice for battle openers
- **Late-game finisher**: Can secure KOs with the Attack boost

### Example Damage Calculations
```
Ogerpon-Hearthflame-Mega @ Hearthflame Mask
120 base Attack to 180 effective Attack with Embody Aspect
Ivy Cudgel (Base Power 100, STAB 1.5x, Grass/Fire type):
- Against 252 HP / 0 Def Garchomp: 85-100% (guaranteed 2HKO)
- Against 252 HP / 252+ Def Toxapex: 45-53% (2HKO after Stealth Rock)
```

### Common Users
- **Ogerpon Hearthflame Mega**: The only known user of this ability
  - Base stats: 80/135/104/110/96/125 (with Mega Evolution)
  - Additional innate abilities: Mold Breaker, Hellblaze
  - Signature move: Ivy Cudgel (changes type based on form)

### Competitive Usage Notes
- **Entry timing**: Best used on predicted switches or as a lead
- **Immediate impact**: No setup time required unlike Swords Dance
- **Type coverage**: Pairs well with Ogerpon's Grass/Fire typing
- **Hellblaze synergy**: Innate Hellblaze boosts Fire-type Ivy Cudgel further
- **Mold Breaker utility**: Bypasses abilities like Sturdy and Multiscale
- **Hearthflame Mask**: Required item enables Mega Evolution and boosts power

### Counters
- **Physical walls**: Defensive Pokemon can still tank boosted attacks
- **Intimidate**: Reduces the Attack boost if it activates after entry
- **Burns**: Status condition halves Attack, negating the boost
- **Priority moves**: Fast priority can revenge kill before it attacks
- **Stat resets**: Moves like Clear Smog, Haze remove stat changes
- **Switch-forcing moves**: Dragon Tail, Whirlwind remove stat boosts

### Synergies
- **Hearthflame Mask**: Required for Mega Evolution, provides power boost
- **Life Orb**: Stacks with Attack boost for maximum damage
- **Choice Band**: Double boost (though locks into one move)
- **Ivy Cudgel**: Signature STAB move becomes Grass/Fire type
- **Physical coverage**: Stone Edge, U-turn, Power Whip
- **Speed control**: Tailwind or Thunder Wave support
- **Entry hazard removal**: Rapid Spin or Defog support

### Team Building Considerations
- **Fire-type core**: Pairs well with other Fire types for coverage
- **Sun team synergy**: Fire moves boosted in harsh sunlight
- **Physical attacker role**: Fills wallbreaker position on teams
- **Lead potential**: Strong opening presence with immediate threat
- **Late-game cleaner**: Can sweep weakened teams with Attack boost

### Version History
- **Elite Redux exclusive**: Custom ability for Ogerpon Hearthflame form
- **Implementation**: Based on Intrepid Sword from official games
- **Balance**: Part of Ogerpon's multi-ability system (3 innates + 1 changeable)
- **Hearthflame form**: Fire/Grass typing with unique ability set