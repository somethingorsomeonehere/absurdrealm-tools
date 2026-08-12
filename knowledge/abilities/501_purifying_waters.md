---
id: 501
name: Purifying Waters
status: reviewed
character_count: 188
---

# Purifying Waters - Ability ID 501

## In-Game Description
"Hydration + Water Veil."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Aqua Ring on entry, which restores 1/16 HP each turn. Grants immunity to burn status and removes burn on switching in. During rain, cures all status conditions at the end of the turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Purifying Waters is a combination ability that merges the protective benefits of Water Veil with the status-cleansing power of Hydration. It provides both passive healing and comprehensive status protection under the right conditions.

### Component Abilities
This ability inherits effects from two separate abilities:
- **Water Veil**: Entry healing and burn immunity
- **Hydration**: Rain-based status cleansing

### Activation Conditions

#### Water Veil Component (Always Active)
- **On entry**: Automatically surrounds the Pokemon with Aqua Ring
  - Provides 1/16 maximum HP healing at the end of each turn
  - Healing boosted by Big Root if held
  - Visual effect shows water veil surrounding the Pokemon
- **Burn immunity**: Completely immune to burn status
- **Burn removal**: Removes existing burn status when switching in

#### Hydration Component (Rain-Dependent)
- **Weather requirement**: Any form of rain weather must be active
  - Regular rain (from Rain Dance)
  - Heavy rain (from Drizzle ability)  
  - Primordial rain (from Primordial Sea)
- **Timing**: Activates at the end of turn during rain
- **Status cure**: Removes all major status conditions:
  - Burn (though already immune)
  - Freeze
  - Paralysis
  - Poison (including badly poisoned)
  - Sleep

### Technical Implementation
```c
// Purifying Waters inherits from both abilities
constexpr Ability PurifyingWaters = {
    .onEntry = WaterVeil.onEntry,         // Aqua Ring on entry
    .onEndTurn = Hydration.onEndTurn,     // Status healing in rain
    .onStatusImmune = WaterVeil.onStatusImmune, // Burn immunity
    .breakable = TRUE,                    // Can be suppressed
    .removesStatusOnImmunity = TRUE,      // Removes burn on entry
};
```

### Detailed Effect Breakdown

#### Aqua Ring Healing (Entry Effect)
- Grants STATUS3_AQUA_RING on entry if not already present
- Heals 1/16 maximum HP at the end of each turn
- Healing occurs during ENDTURN_AQUA_RING phase
- Compatible with Big Root for 1.3x healing (approximately 1/12 HP)
- Persists even if ability is later suppressed
- Cannot be removed by normal means (unlike the move version)

#### Burn Immunity
- Completely prevents burn status from being applied
- Triggers immunity message when burn is attempted
- Removes existing burn status when the Pokemon enters battle
- Works against all burn sources including Flame Body, Scald, etc.

#### Rain Status Cleansing
- Only activates when WEATHER_RAIN_ANY is present
- Includes temporary rain, permanent rain, and primal rain
- Removes all status conditions at end of turn
- Uses AbilityHealMonStatus function for consistent behavior
- Triggers appropriate healing messages

### Important Interactions

#### Weather Interactions
- **Rain teams**: Excellent synergy with Drizzle setters
- **Weather wars**: Vulnerable to weather override
- **Primordial Sea**: Works with all forms of rain weather
- **Cloud Nine/Air Lock**: Disables rain-based healing component

#### Status Interactions
- **Burn immunity**: Always active, not weather dependent
- **Sleep Talk**: Can use Sleep Talk on turn you wake up in rain
- **Rest**: Can use Rest and wake up same turn in rain
- **Toxic**: Resets badly poisoned counter when cured
- **Status timing**: Status damage occurs before cure

#### Healing Interactions
- **Aqua Ring**: Stacks with other healing sources
- **Leftovers**: Combines with passive item healing
- **Big Root**: Boosts Aqua Ring healing to ~1/12 HP
- **Maximum HP**: Cannot heal beyond full HP

### Strategic Implications

#### Defensive Benefits
- **Passive sustain**: Constant 1/16 HP healing provides longevity
- **Status immunity**: Near-complete status protection on rain teams
- **Entry hazard cushion**: Healing helps offset Stealth Rock damage
- **Burn wall**: Excellent counter to physical attackers with Flame Body

#### Team Synergy
- **Rain team core**: Perfect fit for rain-based strategies
- **Drizzle support**: Pairs excellently with Politoed, Pelipper, Kyogre
- **Defensive pivot**: Can switch into status moves safely
- **Wall potential**: Sustained healing supports defensive roles

#### Competitive Usage
- **Rain sweeper support**: Provides longevity for setup sweepers
- **Status absorber**: Takes status moves for team
- **Anti-stall**: Counters toxic and burn stall strategies
- **Weather dependency**: Less reliable outside of dedicated rain teams

### Counters and Limitations

#### Weather Counters
- **Sun/Sand/Hail**: Override rain to disable status cleansing
- **Cloud Nine**: Negates weather effects entirely
- **Air Lock**: Similar to Cloud Nine, prevents weather benefits
- **Weather moves**: Can be overridden by opposing weather setters

#### Ability Counters
- **Mold Breaker**: Ignores ability effects entirely
- **Neutralizing Gas**: Suppresses ability while active
- **Skill Swap/Role Play**: Can steal or change the ability
- **Gastro Acid**: Suppresses ability until switching

#### Strategic Counters
- **Taunt**: Prevents Rest abuse in rain
- **Heal Block**: Prevents all healing including Aqua Ring
- **Entry hazards**: Chip damage that healing must offset
- **Multi-hit moves**: Can overwhelm healing with repeated damage

### Synergies and Team Support

#### Rain Team Partners
- **Drizzle setters**: Politoed, Pelipper, Kyogre for permanent rain
- **Swift Swim sweepers**: Kingdra, Ludicolo, Kabutops
- **Thunder users**: Perfect accuracy Thunder in rain
- **Water-type attackers**: STAB moves boosted in rain

#### Defensive Synergies
- **Wish support**: Combines with team healing
- **Aromatherapy/Heal Bell**: Backup status removal
- **Rapid Spin/Defog**: Hazard removal for better longevity
- **Light Screen/Reflect**: Damage reduction enhances healing

#### Item Synergies
- **Big Root**: Boosts Aqua Ring healing significantly
- **Leftovers**: Stacks with Aqua Ring for major sustain
- **Damp Rock**: Extends rain duration for more status cures
- **Assault Vest**: Special bulk with passive healing

### Common Users and Applications

#### Ideal Candidates
- Bulky Water types that benefit from sustained healing
- Rain team defensive cores
- Pokemon that fear status conditions
- Mixed walls that need longevity

#### Competitive Roles
- **Rain team anchor**: Provides reliability and sustain
- **Status absorber**: Switches into status moves safely  
- **Defensive pivot**: Healing supports switching strategies
- **Setup support**: Longevity helps setup sweepers

### Version History and Notes
- Elite Redux exclusive combination ability
- Merges two classic defensive abilities into one powerful package
- Benefits from 8-turn weather duration in Elite Redux
- Breakable ability that can be suppressed by appropriate counters
- Removes status on immunity, making it excellent against burn spreaders

### Technical Notes
- Ability ID 501 in the Elite Redux ability system
- Inherits onEntry, onEndTurn, and onStatusImmune handlers
- Uses standard AbilityHealMonStatus for consistent behavior
- Breakable flag allows counterplay through ability suppression
- removesStatusOnImmunity flag provides immediate burn cleansing