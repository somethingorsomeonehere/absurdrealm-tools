---
id: 454
name: Adrenaline Rush
status: reviewed
character_count: 90
---

# Adrenaline Rush - Ability ID 454

## In-Game Description
"KOs raise Speed by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's Speed by one stage whenever it knocks out an opponent with a direct hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Adrenaline Rush is an offensive momentum ability that provides cumulative Speed boosts for maintaining offensive pressure. Each KO grants a +1 Speed stage boost, allowing for snowball potential.

### Activation Conditions
- **KO requirement**: The Pokemon with Adrenaline Rush must directly cause an opponent to faint
- **Timing**: Speed boost applies immediately after the target faints, before the next Pokemon switches in
- **Boost amount**: +1 Speed stage per KO (maximum +6 stages total)
- **KO methods**: Works on all forms of KO:
  - Direct damage from attacks
  - Indirect damage from status conditions (if the ability user inflicted them)
  - Recoil damage from moves like Take Down
  - Multi-hit moves that cause fainting

### Technical Implementation
```c
// Adrenaline Rush uses MoxieClone function with STAT_SPEED
constexpr Ability AdrenalineRush = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int { 
        return MoxieClone(battler, STAT_SPEED); 
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};

// MoxieClone function implementation
static int MoxieClone(int battler, int stat) {
    CHECK(HasAttackerFaintedTarget())
    CHECK(ChangeStatBuffs(battler, 1, stat, MOVE_EFFECT_AFFECTS_USER | STAT_BUFF_DONT_SET_BUFFERS, NULL))
    BattleScriptCall(BattleScript_RaiseStatOnFaintingTarget);
    return TRUE;
}
```

### Speed Stage Mechanics
- **Stage 1**: 1.5x Speed (50% increase)
- **Stage 2**: 2.0x Speed (100% increase)  
- **Stage 3**: 2.5x Speed (150% increase)
- **Stage 4**: 3.0x Speed (200% increase)
- **Stage 5**: 3.5x Speed (250% increase)
- **Stage 6**: 4.0x Speed (300% increase)

### Important Interactions
- **Multi-hit moves**: Only one Speed boost per target that faints
- **Substitute**: Can activate even if attacking through Substitute
- **Faint prevention**: Doesn't activate if target survives with Focus Sash, Sturdy, etc.
- **Indirect KOs**: Works with status damage if the ability user caused the status
- **Ability suppression**: Cannot activate if ability is suppressed by Mold Breaker effects

### Strategic Applications
- **Revenge killing**: Ideal for fast revenge killers that can outspeed after a KO
- **Late-game sweeping**: Becomes increasingly dangerous as more opponents faint
- **Priority move synergy**: Works well with priority moves for guaranteed first KO
- **Choice item synergy**: Excellent with Choice Scarf or Choice Band for initial KO setup
- **Setup sweeper support**: Allows physical/special sweepers to outspeed after first KO

### Team Building Considerations
- **Fast attackers**: Best on naturally fast Pokemon (90+ base Speed)
- **Strong attackers**: Needs sufficient power to secure KOs reliably  
- **Multi-target moves**: Pokemon with Earthquake, Rock Slide benefit from potential multi-KOs
- **Priority moves**: Bullet Punch, Aqua Jet help guarantee first KO
- **Coverage moves**: Wide movepool helps secure KOs against various types

### Common Users
Adrenaline Rush is typically found on:
- Fast physical attackers with good coverage
- Revenge killers with priority moves
- Late-game cleaners and sweepers
- Pokemon that naturally learn multi-hit or spread moves

### Competitive Usage Patterns
- **Early-game**: Use as revenge killer after team member faints
- **Mid-game**: Look for opportunities to score first KO safely
- **Late-game**: Becomes win condition with multiple speed boosts accumulated
- **Switch timing**: Often best to switch in after a team member faints for revenge

### Synergistic Abilities
When paired with other abilities (in Elite Redux's multi-ability system):
- **Life Orb effect abilities**: Increased damage for more reliable KOs
- **Priority boosting abilities**: Ensures first strike capability
- **Type-changing abilities**: Provides better coverage for securing KOs
- **Stat-boosting abilities**: Compounds the sweeping potential

### Counters and Limitations
- **Sturdy/Focus Sash**: Prevents KO and ability activation
- **Ghost-type switching**: Ghost-types can switch freely from Normal/Fighting moves
- **Defensive walls**: High bulk can prevent KOs needed for activation
- **Status conditions**: Paralysis and burn can limit sweeping potential
- **Priority moves**: Opposing priority can revenge kill despite speed boost
- **Ability suppression**: Mold Breaker, Neutralizing Gas shut down the ability

### Comparison to Similar Abilities
- **Moxie**: Boosts Attack instead of Speed (ID varies)
- **Beast Boost**: Boosts highest stat instead of specific stat
- **Grim Neigh**: Boosts Special Attack instead of Speed
- **Chilling Neigh**: Also boosts Attack like Moxie

### Version History
- Introduced in Elite Redux as part of expanded ability roster
- Functions identically to standard Moxie-type abilities but with Speed focus
- Part of the momentum-based ability family for offensive team strategies

### Damage Calculation Impact
While Adrenaline Rush doesn't directly affect damage, the Speed boosts enable:
- **Outspeeding revenge killers**: Prevents common revenge kill attempts
- **Choice Scarf users**: Can eventually outspeed even scarfed opponents
- **Speed tiers**: Moves Pokemon into higher speed tiers for consistent outspeeding
- **Turn order control**: Allows user to maintain offensive pressure and momentum