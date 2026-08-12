---
id: 377
name: Artillery
status: reviewed
character_count: 155
---

# Artillery - Ability ID 377

## In-Game Description
"Mega Launcher moves always hit and hit both foes."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mega Launcher moves always hit and strike both opposing Pokemon simultaneously. Unable to miss with pulse, beam, ball, aura, and other blast related moves. 

## Detailed Mechanical Explanation
**Artillery** combines perfect accuracy with multi-targeting functionality, making it a powerful offensive enhancement ability that revolutionizes how Mega Launcher moves operate.

### Core Mechanics

#### Perfect Accuracy System
- **Accuracy Override**: Returns `ACCURACY_HITS_IF_POSSIBLE` for all Mega Launcher moves
- **Implementation**: Located in abilities.cc line 3925-3928
- **Logic**: Uses `IsMegaLauncherBoosted(battler, move)` function to determine qualifying moves

```cpp
constexpr Ability Artillery = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(IsMegaLauncherBoosted(battler, move))
        return ACCURACY_HITS_IF_POSSIBLE;
    },
};
```

#### Multi-Target Transformation
- **Target Change**: Converts `MOVE_TARGET_SELECTED` to `MOVE_TARGET_BOTH` for qualifying moves
- **Implementation**: Located in battle_util.c lines 124-126
- **Requirement**: Move must originally target a single selected opponent

```c
if ((BATTLER_HAS_ABILITY(battler, ABILITY_ARTILLERY) || BATTLER_HAS_ABILITY(battler, ABILITY_SUPER_SCOPE)) && 
    IsMegaLauncherBoosted(battler, moveId) && gBattleMoves[moveId].target == MOVE_TARGET_SELECTED)
    return MOVE_TARGET_BOTH;
```

### Move Selection Logic
Artillery affects moves through the **IsMegaLauncherBoosted** function (battle_util.c line 9177):

1. **FLAG_MEGA_LAUNCHER_BOOST moves**: Any move with the specific Mega Launcher flag
2. **All Status moves**: Every status move is treated as Mega Launcher boosted
3. **Gunman ability synergy**: Expands the move pool when combined with Gunman

```c
int IsMegaLauncherBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_MEGA_LAUNCHER_BOOST) return TRUE;
    if (IS_MOVE_STATUS(move) || BattlerHasAbility(battler, ABILITY_GUNMAN, FALSE)) return TRUE;
    return FALSE;
}
```

### Comprehensive Move Coverage

#### High-Power Offensive Moves
- **Water Gun** (40 BP + priority): Perfect accuracy multi-hit
- **Hydro Pump** (110 BP): Never-miss dual targeting
- **Solar Beam** (120 BP): Weather-independent accuracy
- **Energy Ball, Shadow Ball, Focus Blast**: All gain perfect accuracy + dual target

#### Status Move Enhancement
- **ALL status moves** are affected by Artillery
- Perfect accuracy on status infliction
- Dual targeting for battlefield control
- Includes moves like Thunder Wave, Toxic, Sleep Powder

#### Elite Redux Custom Moves
- Any custom moves with FLAG_MEGA_LAUNCHER_BOOST
- Archer Shot variants with perfect accuracy
- Drake Missile and projectile moves

### Strategic Applications

#### Offensive Dominance
- **Guaranteed Damage**: No accuracy checks means consistent damage output
- **Dual Targeting**: Hits both opponents in doubles/raids simultaneously
- **Weather Independence**: Accuracy remains perfect regardless of weather conditions
- **Evasion Counter**: Bypasses Double Team, Minimize, and other evasion boosts

#### Status Control
- **Perfect Status Infliction**: All status moves hit both opponents with 100% accuracy
- **Battlefield Control**: Spread Thunder Wave, Toxic, or Sleep Powder reliably
- **Support Utility**: Enhanced reliability for team support moves

#### Competitive Advantages
1. **Consistency**: Eliminates accuracy RNG from key moves
2. **Action Economy**: Single move affects both opponents
3. **Pressure**: Forces opponents to account for guaranteed dual hits
4. **Versatility**: Works with physical, special, and status moves

### Synergistic Abilities

#### Super Scope (Ability #890)
- **Description**: "Mega Launcher + Artillery"
- **Combined Effect**: Gains both the 1.3x damage boost AND Artillery's dual-targeting
- **Ultimate Launcher**: The definitive projectile-based ability

#### Related Artillery Abilities
- **Deadeye (#376)**: Similar accuracy enhancement for arrow/cannon moves + critical hit targeting
- **Sighting System (#368)**: Accuracy and critical hit enhancement system
- **Mega Launcher (#178)**: Base damage boost that Artillery builds upon

### Battle Applications

#### Singles Format
- **Accuracy Security**: Never miss crucial attacks or status moves
- **Reliable Finisher**: Guaranteed hits on low-HP opponents
- **Status Spreading**: Perfect accuracy status infliction

#### Doubles/Multi-Battle Format
- **Dual Pressure**: Both opponents take damage/status simultaneously  
- **Field Control**: Status moves affect entire opposing field
- **Resource Efficiency**: One move slot controls both opponents

#### Raid Battles
- **Consistent Damage**: Perfect accuracy against raid bosses
- **Multi-Hit Potential**: Hits multiple raid Pokemon when applicable
- **Status Reliability**: Guaranteed status infliction for support roles

### Competitive Tier Analysis

#### High Tier Justification
- **Perfect Accuracy**: Eliminates one of the most frustrating RNG elements
- **Multi-Target**: Effectively doubles move value in multi-battles
- **Move Pool Synergy**: Works with extensive Mega Launcher move list
- **Strategic Depth**: Changes opponent calculations and team building

#### Comparison to Other Abilities
- **vs No Guard**: Artillery is more selective but applies multi-targeting
- **vs Compound Eyes**: Artillery provides perfect accuracy rather than just improvement  
- **vs Mega Launcher**: Artillery trades damage boost for accuracy and targeting
- **vs Super Scope**: Super Scope combines both benefits but is extremely rare

### Notable Pokemon Applications

#### Potential Users
Given Artillery's power level, it would likely be found on:
- **Legendary/Mythical Pokemon**: High-tier offensive threats
- **Elite Redux Custom Pokemon**: Signature ability users
- **Evolved Forms**: Final evolution exclusive ability
- **Special Forms**: Regional variants or special event Pokemon

#### Team Building Considerations
- **Move Selection**: Prioritize Mega Launcher flagged moves
- **Role Definition**: Can function as accurate sweeper OR status support
- **Partner Synergy**: Works well with setup Pokemon that benefit from guaranteed status hits
- **Coverage**: Excellent for Pokemon with diverse Mega Launcher movesets

### Technical Implementation Notes

#### Accuracy Priority System
- **ACCURACY_HITS_IF_POSSIBLE**: Highest accuracy priority level
- **Bypasses**: All accuracy checks, evasion boosts, weather effects
- **Interaction**: Works alongside other accuracy modifiers but overrides them

#### Target Flag System  
- **Original Target**: Must be `MOVE_TARGET_SELECTED` (single opponent)
- **New Target**: Becomes `MOVE_TARGET_BOTH` (both opponents)
- **Limitation**: Does not affect moves that already hit multiple targets

### Strategic Implications

Artillery represents a paradigm shift in battle reliability, transforming Pokemon from accuracy-dependent attackers into guaranteed-hit machines. The dual-targeting component makes it exceptionally valuable in doubles formats, while the perfect accuracy ensures consistent performance regardless of battle conditions.

The ability excels at both offensive pressure and defensive utility, making Artillery users versatile team members capable of adapting to multiple roles within a single moveset. Its broad move compatibility ensures that most Pokemon with Artillery can find effective applications regardless of their base stats or typing.

This combination of reliability and versatility places Artillery firmly in the high-tier category, where it competes with game-changing abilities like Mold Breaker, Magic Bounce, and Prankster for team consideration.