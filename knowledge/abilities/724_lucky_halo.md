---
id: 724
name: Lucky Halo
status: reviewed
character_count: 136
---

# Lucky Halo - Ability ID 724

## In-Game Description
"Negates self stat drops. Endures the a single KO."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents self-inflicted stat drops on the user and allows them to survive an attack that would KO them one time, leaving them with 1 HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Lucky Halo is a defensive ability that combines two protective effects: stat drop immunity and a once-per-battle endure effect. It provides consistent protection against stat manipulation while offering a safety net against KO moves.

### Stat Drop Prevention
- **Full immunity**: Prevents ALL negative stat changes to the user
- **Affected stats**: Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, Evasion
- **Move types blocked**: 
  - Direct stat-lowering moves (Growl, Leer, etc.)
  - Secondary effects from damaging moves
  - Ability-based stat drops (Intimidate, Sticky Web entry)
- **Self-inflicted**: Only blocks stat drops from external sources, not self-inflicted ones

### Endure Effect
- **Activation**: When damage would reduce HP from above 1 to 0 or below
- **Result**: User survives with exactly 1 HP
- **Frequency**: Once per battle (resets when switching out)
- **Damage sources**: Works against all damage types (moves, abilities, entry hazards)
- **Exclusions**: Does not prevent fainting from status conditions that reduce HP to 0

### Technical Implementation
**Note**: Lucky Halo appears to be defined in the protobuf files but not yet implemented in the C++ battle engine. The following represents the intended implementation based on the description.

```c
// Stat drop prevention (similar to Clear Body)
if (ability == ABILITY_LUCKY_HALO && statChange < 0) {
    // Block the stat drop
    return FALSE; // Prevent stat change
}

// Endure effect (similar to Focus Sash + Sturdy)
if (ability == ABILITY_LUCKY_HALO && !GetAbilityState(battler, ability)) {
    if (gBattleMons[battler].hp > 1 && finalDamage >= gBattleMons[battler].hp) {
        // Set HP to 1 and mark ability as used
        gBattleMons[battler].hp = 1;
        SetAbilityState(battler, ability, TRUE);
        // Trigger endure message
        return TRUE;
    }
}
```

### Important Interactions
- **Mold Breaker**: Can bypass both stat drop prevention and endure effect
- **Multi-hit moves**: Only the final hit's damage is considered for endure activation
- **Substitute**: Stat drop prevention still works while behind substitute
- **Baton Pass**: Endure usage state doesn't transfer to the switched-in Pokemon
- **Ability suppression**: Both effects disabled when ability is suppressed

### Stat Drop Prevention Details
- **Intimidate immunity**: Completely blocks Attack drops from Intimidate
- **Sticky Web**: Prevents Speed drop when switching in
- **King's Rock/Razor Fang**: Blocks stat drops from flinch-inducing items
- **Moves with secondary effects**: Blocks stat drops from moves like Crunch, Psychic, etc.
- **Z-Moves**: Cannot prevent stat drops from Z-Status moves

### Endure Effect Limitations
- **Status damage**: Cannot prevent fainting from poison, burn, etc. if HP reaches 0
- **Belly Drum**: Self-inflicted HP reduction bypasses endure
- **Recoil damage**: Works normally against recoil (e.g., from Double-Edge)
- **Future Sight**: Can endure Future Sight damage
- **Entry hazards**: Can survive lethal Stealth Rock damage

### Strategic Implications
- **Setup sweeper protection**: Prevents stat drops while setting up
- **Survivability**: Guarantees survival of one lethal hit
- **Intimidate counter**: Excellent against Intimidate users
- **Hazard immunity**: Provides partial protection against stat-dropping hazards
- **One-time use**: Endure effect needs careful timing

### Common Users
- **Fragile sweepers**: Pokemon that need setup time and survival insurance
- **Lead Pokemon**: Good for reliable lead performance
- **Wallbreakers**: Benefits from stat drop immunity and survival guarantee
- **Support Pokemon**: Can reliably use support moves without stat interference

### Competitive Usage Notes
- **Dual utility**: Provides both offensive and defensive benefits
- **Setup enabler**: Allows safe setup against stat-dropping moves
- **Revenge killer**: Can survive a hit to potentially revenge kill
- **Intimidate meta**: Strong in metas with prevalent Intimidate users
- **Priority weakness**: Vulnerable to priority moves after endure activation

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Gastro Acid
- **Multi-hit moves**: Can overwhelm the endure effect
- **Status conditions**: Poison/burn can finish off after endure
- **Entry hazards**: Repeated hazard damage after endure activation
- **Priority moves**: Can pick off after survival at 1 HP

### Synergies
- **Salac Berry**: Activates after endure for Speed boost
- **Liechi Berry**: Attack boost when at low HP
- **Substitute**: Protects from status after endure
- **Priority moves**: Can strike first after surviving with 1 HP
- **Healing moves**: Can restore HP after endure activation

### Ability Combinations
In Elite Redux's 4-ability system, Lucky Halo pairs well with:
- **Regenerator**: Healing when switching out
- **Magic Guard**: Protection from indirect damage
- **Guts**: Attack boost from status conditions
- **Quick Feet**: Speed boost when statused

### Version History
- **Elite Redux addition**: Custom ability unique to Elite Redux
- **Implementation status**: Defined in protobuf but not yet implemented in battle engine
- **Planned mechanics**: Combines Clear Body stat immunity with once-per-battle endure

### Design Philosophy
Lucky Halo represents a "guardian angel" concept, providing both proactive protection (stat drops) and reactive protection (endure). The ability is designed to give fragile Pokemon more opportunities to contribute meaningfully to battle while maintaining counterplay through its one-time-use limitation and vulnerability to indirect damage.

The combination of effects makes it particularly valuable on Pokemon that need to maintain their stats for sweeping while also appreciating the safety net against unexpected threats. However, the endure effect's single-use nature requires careful positioning and timing to maximize value.