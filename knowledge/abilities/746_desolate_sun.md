---
id: 746
name: Desolate Sun
status: reviewed
character_count: 242
---

# Desolate Sun - Ability ID 746

## In-Game Description
"Desolate Land + Earth Eater."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates extremely harsh sunlight that lasts until the user switches out. Has the standard sun effects and nullifies all Water-type moves. Additionally, the user heals 25% of their max HP when hit by Ground-type moves instead of taking damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Desolate Sun is a powerful combination ability that merges two distinct defensive mechanics: permanent weather control and move-type absorption. It provides both offensive support through weather manipulation and defensive utility through Ground-type immunity with healing.

### Component Abilities Analysis

#### Desolate Land Component
- **Weather Effect**: Creates extremely harsh sunlight (WEATHER_SUN_PRIMAL)
- **Duration**: Permanent until the user switches out or faints
- **Water Nullification**: All Water-type moves become unusable while active
- **Fire Boost**: Fire-type moves receive 50% damage boost
- **Solar Moves**: Solar Beam/Solar Blade fire immediately without charge turn
- **Weather Override**: Cannot be overridden by normal weather moves

#### Earth Eater Component  
- **Ground Absorption**: Absorbs all Ground-type moves targeting the user
- **HP Recovery**: Heals 25% of max HP when absorbing Ground moves
- **No Damage**: Ground moves deal 0 damage and trigger healing instead
- **Move Immunity**: Complete immunity to Ground-type damage
- **Breakable**: Effect can be suppressed by Mold Breaker-type abilities

### Technical Implementation
```c
// Current implementation is incomplete - only has randomizerBanned flag
constexpr Ability DesolateSun = {
    .randomizerBanned = TRUE,
};

// Should be implemented as combination ability:
constexpr Ability DesolateSun = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return DesolateLand.onEntry(DELEGATE_ENTRY); 
    },
    .onAbsorb = +[](ON_ABSORB) -> int {
        return EarthEater.onAbsorb(DELEGATE_ABSORB);
    },
    .randomizerBanned = TRUE,
};
```

### Weather Mechanics
- **Primal Weather**: Uses ENUM_WEATHER_SUN_PRIMAL (value 5)
- **Permanent Duration**: Unlike regular sun (8 turns), lasts until user switches
- **Priority**: Overrides all other weather except Delta Stream
- **Water Nullification**: All Water moves fail with "There's no relief from this heat!"
- **Fire Enhancement**: Fire moves get 1.5x damage multiplier
- **Solar Synergy**: Solar Beam/Solar Blade skip charge turn

### Ground Absorption Mechanics
- **Trigger Condition**: Any Ground-type move targeting the user
- **Healing Amount**: 25% of max HP restored
- **Priority**: Occurs before move damage calculation
- **Status Moves**: Also absorbs Ground-type status moves like Spikes
- **Multi-Hit**: Each hit of multi-hit Ground moves triggers absorption
- **Indirect Damage**: Does not protect against indirect Ground damage (hazards)

### Strategic Applications

#### Offensive Support
- **Fire Team Core**: Essential for Fire-type sweepers and setup
- **Solar Beam Users**: Enables immediate Solar Beam/Solar Blade usage
- **Water Counter**: Completely shuts down Water-type attackers
- **Weather Control**: Maintains permanent sun for team synergy

#### Defensive Utility
- **Ground Immunity**: Complete protection from Earthquake, Earth Power
- **Recovery Source**: Reliable healing when opponents use Ground moves
- **Hazard Protection**: Absorbs Ground-type entry hazards
- **Pivot Capability**: Can switch in on predicted Ground moves for free healing

### Competitive Viability
- **Role**: Weather setter + defensive pivot
- **Tier**: Extremely powerful due to permanent weather + immunity
- **Usage**: Central to sun teams, anti-Ground core member
- **Restrictions**: Banned from randomizer due to power level

### Key Interactions

#### Positive Synergies
- **Chlorophyll**: Team members get doubled Speed in permanent sun
- **Solar Power**: Special attackers get 50% damage boost
- **Fire Types**: All Fire moves boosted, Water moves nullified
- **Drought**: Redundant but ensures sun if ability is suppressed
- **Heat Rock**: No effect since weather is permanent anyway

#### Notable Counters
- **Ability Suppression**: Mold Breaker, Neutralizing Gas disable both effects
- **Delta Stream**: Only weather that can override Desolate Land
- **Cloud Nine/Air Lock**: Negates weather effects but not Ground absorption
- **Role Play/Skill Swap**: Can copy or remove the ability
- **Non-Ground Physical**: Must rely on other move types for damage

### Common Matchups
- **vs Water Types**: Completely walls them with move nullification
- **vs Ground Types**: Absorbs their STAB for healing
- **vs Fire Types**: Provides permanent sun support
- **vs Grass Types**: Solar moves become immediately usable
- **vs Rock/Steel**: Often carry Ground moves for coverage

### Team Building Considerations
- **Sun Team Core**: Perfect permanent weather setter
- **Fire-Type Support**: Enables Fire spam strategies  
- **Ground Counter**: Reliable switch-in for Ground attacks
- **Defensive Pivot**: Healing on switch provides longevity
- **Weather Wars**: Dominates weather control battles

### Weaknesses and Limitations
- **Single Ability Slot**: Takes up the primary ability slot
- **Switch Dependence**: Weather ends when user switches out
- **Limited Coverage**: Still vulnerable to other move types
- **Setup Vulnerable**: Can be setup on if lacking offensive presence
- **Ability Disruption**: Vulnerable to ability-changing effects

### Version History
- **Elite Redux Addition**: Custom combination ability
- **Implementation Status**: Currently incomplete (placeholder only)
- **Design Intent**: Combine premier weather control with Ground immunity
- **Balance Consideration**: Banned from randomizer due to power level

### Recommended Implementation
The ability should combine both component abilities' effects:
1. On entry: Activate extremely harsh sunlight (like Desolate Land)
2. On absorption: Heal from Ground moves (like Earth Eater)  
3. Maintain both effects simultaneously for full utility
4. Keep randomizer ban due to combined power level