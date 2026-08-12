---
id: 428
name: Cheap Tactics
status: reviewed
character_count: 111
---

# Cheap Tactics - Ability ID 428

## In-Game Description
"Attacks with Scratch on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Cheap Tactics uses Scratch (40 BP Normal physical move) targeting a random opponent when switching into battle. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Cheap Tactics is an aggressive entry ability that immediately forces the Pokemon to use Scratch upon switching into battle. This provides instant damage output and can catch opponents off guard with unexpected early damage.

### Activation Conditions
- **Switch-in trigger**: Activates whenever the Pokemon enters battle
  - Normal switch-ins
  - After fainting of previous Pokemon
  - U-turn/Volt Switch entries
  - Red Card forced switches
- **Target selection**: Automatically targets an alive opponent
  - Prioritizes the opposing battler in front
  - Falls back to any alive opponent if primary target fainted
- **Move execution**: Uses Scratch with standard properties

### Technical Implementation
```c
// Cheap Tactics uses UseEntryMove to execute Scratch on entry
constexpr Ability CheapTactics = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_SCRATCH, 0); 
    },
};
```

The ability leverages the `UseEntryMove` function which:
1. Finds a valid target (alive opponent)
2. Checks if the extra move can be used
3. Queues the move for execution using the standard battle system

### Move Properties (Scratch)
- **Base Power**: 40 (not modified by the 0 movePower parameter)
- **Type**: Normal (no STAB unless user is Normal-type)
- **Accuracy**: 100% (cannot miss under normal conditions)
- **Category**: Physical (uses Attack stat and opponent's Defense)
- **Contact**: Yes (triggers contact-based abilities and items)
- **PP**: Not consumed (entry moves don't use PP)

### Important Interactions
- **Type effectiveness**: Follows standard type chart (resisted by Rock/Steel, immune to Ghost)
- **Contact abilities**: Triggers Rough Skin, Static, Flame Body, etc.
- **Defensive abilities**: Can trigger abilities like Sturdy, Effect Spore, Cute Charm
- **Items**: Can trigger Rocky Helmet, Red Card, Weakness Policy
- **STAB**: Gets Same Type Attack Bonus if user is Normal-type
- **Critical hits**: Can land critical hits normally
- **Stat modifications**: Affected by Attack/Defense boosts and drops

### Priority and Timing
- **Entry priority**: Executes immediately upon switch-in
- **Queue system**: Added to attack queue for proper battle flow
- **Multiple entries**: If multiple Pokemon have entry moves, they execute in speed order
- **Protection bypass**: Cannot be blocked by Protect, Detect, or similar moves
- **Substitute interaction**: Hits through Substitute normally

### Strategic Implications
- **Immediate pressure**: Deals damage before opponent can act
- **Chip damage**: Provides consistent damage output on every switch
- **Contact synergy**: Pairs well with other contact-based effects
- **Revenge killing**: Can potentially finish off weakened opponents
- **Switching costs**: Makes switching more risky for both players
- **Entry hazard synergy**: Combines with Stealth Rock for significant entry damage

### Counters and Limitations
- **Ghost-type immunity**: Normal-type moves cannot hit Ghost types
- **Rock/Steel resistance**: Heavily resisted by these types
- **Contact punishment**: Vulnerable to contact-based retaliation
- **Low base power**: 40 BP is relatively weak late game
- **No choice**: Cannot choose targets or opt out of attacking
- **Ability suppression**: Disabled by Mold Breaker effects on opponents

### Synergies
- **Contact abilities**: Rocky Helmet, Rough Skin users take damage
- **Normal-type STAB**: 60 effective BP with Same Type Attack Bonus
- **Attack boosts**: Choice Band, Life Orb boost the entry damage
- **Sheer Force**: Boosts power if Scratch had secondary effects (it doesn't)
- **Technician**: Boosts moves with 60 or less base power to 60 BP

### Competitive Usage Notes
- **Lead potential**: Excellent on lead Pokemon for immediate damage
- **Pivot synergy**: Combines well with U-turn/Volt Switch strategies
- **Hazard support**: Works alongside entry hazards for maximum switch punishment
- **Fast attackers**: Best on fast Pokemon that can follow up the entry damage
- **Fragile sweepers**: Provides utility even if the user faints quickly

### Common Users
Pokemon that benefit from Cheap Tactics typically have:
- High Attack stats to maximize Scratch damage
- Fast speed to potentially finish off damaged opponents
- Frail defenses making immediate offense valuable
- Normal typing for STAB bonus
- Roles as leads or frequent switch-ins

### Comparison to Similar Abilities
- **Low Blow (ID 384)**: Uses Feint Attack (Dark-type, can't KO at 1 HP)
- **Cheap Tactics (ID 428)**: Uses Scratch (Normal-type, can KO normally)
- **Jump Scare**: Uses Astonish with potential flinch
- **Assassin's Tools**: Uses Spectral Thief with stat stealing

### Version History
- Custom Elite Redux ability (ID 428)
- Uses the established UseEntryMove framework
- Part of the aggressive entry ability family
- Scratch move properties unchanged from base game standards