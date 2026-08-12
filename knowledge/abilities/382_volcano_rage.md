---
id: 382
name: Volcano Rage
status: reviewed
character_count: 182
---

# Volcano Rage - Ability ID 382

## In-Game Description
"After using Fire-type moves, triggers a followup Eruption attack."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After using any Fire-type move, Volcano Rage triggers a followup Eruption attack with 50 base power. Damage scales with the user's current HP percentage, having 50 BP at full health.

## Detailed Mechanical Explanation

### Overview
Volcano Rage is an offensive ability that triggers an automatic followup attack whenever the user successfully uses a Fire-type move. After any Fire-type attack connects, the Pokemon immediately launches a 50 base power Eruption at the same target, creating a devastating double-hit combination that can overwhelm opponents with volcanic fury.

## Technical Implementation

### Source Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 3960-3967
- **Ability Definition**: `VolcanoRage`

### Implementation Details
```cpp
constexpr Ability VolcanoRage = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(moveType == TYPE_FIRE)
        CHECK(AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_STANDARD))

        return UseAttackerFollowUpMove(battler, target, ability, MOVE_ERUPTION, 50);
    },
};
```

### Key Functions
- **`moveType == TYPE_FIRE`**: Ensures the ability only triggers after Fire-type moves
- **`AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_STANDARD)`**: Determines appropriate target for the followup attack
- **`UseAttackerFollowUpMove(battler, target, ability, MOVE_ERUPTION, 50)`**: Executes the followup Eruption with 50 base power

### Triggered Move: Eruption (Modified)
- **Base Power**: 50 BP (reduced from normal Eruption)
- **Type**: Fire
- **Accuracy**: 100%
- **Category**: Special
- **Effect**: Damage scales with user's current HP percentage
- **Target**: Single target (same as triggering move)
- **Priority**: Normal (executed immediately after the triggering move)

## Battle Mechanics

### Activation Conditions
1. **Must use a Fire-type move**: Any Fire-type attack that successfully executes will trigger the ability
2. **Move must complete**: The triggering Fire-type move must finish its execution
3. **Target must be valid**: The followup target must be available and reachable
4. **No self-targeting**: Uses standard followup targeting (typically the same target as the original move)

### Followup Attack Properties
- **Immediate execution**: Occurs directly after the triggering Fire-type move
- **HP-based scaling**: Eruption's damage scales with the user's current HP percentage
- **Special attack**: Uses the user's Special Attack stat
- **Type effectiveness applies**: Super effective against Grass, Bug, Ice, and Steel types
- **Can be blocked**: Subject to abilities like Flash Fire, Water Absorb, etc.
- **STAB eligible**: Gains Same Type Attack Bonus if the user is Fire-type

### Damage Calculation
The followup Eruption calculates damage as:
- **Base Power**: 50 x (Current HP / Max HP)
- **Maximum Power**: 50 BP (at full HP)
- **Minimum Power**: 1 BP (at 1 HP)

## Strategic Analysis

### Competitive Advantages
1. **Guaranteed Followup**: Every Fire-type move becomes a potential double-hit
2. **HP Scaling**: Maximum effectiveness when used by healthy Pokemon
3. **Type Coverage**: Fire-type followup provides consistent super effective opportunities
4. **Action Economy**: Essentially grants an extra attack per Fire-type move used
5. **Pressure Building**: Forces opponents to consider the followup damage in their calculations

### Tactical Applications
- **Sweep Enhancement**: Turns Fire-type sweepers into double-hitting powerhouses
- **Chip Damage**: Even at low HP, provides additional damage output
- **Shield Breaking**: Excellent against defensive strategies and substitutes
- **Wallbreaking**: Combined damage can overwhelm defensive Pokemon
- **Revenge Killing**: Followup damage can secure KOs that the initial move couldn't

### Synergistic Strategies
Volcano Rage works exceptionally well with:
- **Fire-type STAB**: Maximizes both the initial move and followup damage
- **HP maintenance**: Abilities and items that preserve HP maintain followup power
- **Special Attack investment**: Enhances the Eruption followup significantly
- **Choice items**: Since followup is automatic, doesn't interfere with Choice restrictions

## Competitive Tier Assessment: HIGH

### Reasons for High Tier Rating
1. **Consistent Value**: Provides benefit on every Fire-type move used
2. **Scaling Damage**: Maintains relevance throughout the battle via HP scaling
3. **Action Economy**: Effectively doubles the impact of Fire-type attacks
4. **Versatile Triggering**: Works with any Fire-type move, from weak to powerful

### Potential Drawbacks
- **HP Dependency**: Followup power decreases as HP drops
- **Type Limitation**: Only triggers on Fire-type moves
- **Defensive Response**: Opponents can prepare for the followup damage
- **Immunity Issues**: Fire-immune abilities completely negate the followup

## Related Abilities Comparison

### Similar Followup Abilities

#### High Tide (Ability #503)
- **Trigger**: Water-type moves
- **Followup**: Surf (50 BP)
- **Comparison**: Similar power but Surf hits multiple targets in doubles

#### Glacial Rage (Ability #620)
- **Trigger**: Ice-type moves  
- **Followup**: Blizzard (50 BP)
- **Comparison**: Blizzard has accuracy issues but potential freeze chance

#### Thundercall (Ability #385)
- **Trigger**: Electric-type moves
- **Followup**: Smite (20% of base power)
- **Comparison**: Variable power but typically stronger than 50 BP

#### Frost Burn (Ability #475)
- **Trigger**: Fire-type moves
- **Followup**: Ice Beam (40 BP)
- **Comparison**: Lower power but unique Ice-type coverage from Fire moves

### Unique Positioning
Volcano Rage stands out as the only Fire-type followup ability that triggers another Fire-type move, creating pure offensive synergy rather than coverage diversity. The HP-scaling mechanic also makes it unique among the elemental followup abilities.

## Usage Recommendations

### Ideal Pokemon Types
- **Fire-type specialists**: Maximize STAB on both triggering moves and followups
- **Special attackers**: Benefit most from the Special Attack-based Eruption followup
- **Bulky attackers**: Can maintain high HP for maximum followup power
- **Versatile Fire users**: Pokemon with diverse Fire-type movesets

### Team Role Integration
- **Primary Sweeper**: Excellent on offensive Fire-types leading sweeps
- **Wallbreaker**: Perfect for breaking through defensive cores
- **Revenge Killer**: Followup damage helps secure crucial KOs
- **Late-Game Cleaner**: Maintains effectiveness even at lower HP ranges

### Optimal Movesets
Consider Fire-type moves that:
- **High accuracy**: Ensure consistent triggering
- **Diverse targets**: Spread moves can trigger multiple followups
- **Status effects**: Moves like Will-O-Wisp still trigger the followup
- **Priority moves**: Quick moves still gain the followup benefit

### Caution Advised
- Monitor HP carefully to maintain followup power
- Be wary of Fire-immune opponents (Flash Fire, Water Absorb users)
- Consider the doubled Fire-type damage when facing Rock/Water types
- Plan around the predictable nature of Fire-type followups

## Conclusion

Volcano Rage represents a premier offensive ability that transforms Fire-type users into devastating double-hitting powerhouses. Its combination of guaranteed followup damage, HP-scaling mechanics, and consistent triggering makes it invaluable for offensive strategies. While HP dependency and type limitations provide some constraints, the sheer action economy and damage potential place it firmly in the high-tier category. Fire-type specialists equipped with Volcano Rage become formidable threats capable of overwhelming even the most prepared defensive strategies through sheer volcanic fury.

