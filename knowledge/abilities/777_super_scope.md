---
id: 777
name: Super Scope
status: reviewed
character_count: 204
---

# Super Scope - Ability ID 777

## In-Game Description
"Mega Launcher + Artillery."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts pulse, beam, ball, and aura moves by 30%. Mega Launcher moves always hit and strike both opposing Pokemon simultaneously. Unable to miss with pulse, beam, ball, aura, and other blast related moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Super Scope** is the ultimate fusion ability that combines the offensive power of Mega Launcher with the tactical superiority of Artillery, creating the most comprehensive projectile-based ability in Elite Redux.

### Core Mechanics

#### Dual-Component Design
Super Scope implements both parent abilities simultaneously:
- **Mega Launcher Component**: 1.3x damage multiplier to qualifying moves
- **Artillery Component**: Perfect accuracy + dual targeting transformation

```cpp
constexpr Ability SuperScope = {
    .onOffensiveMultiplier = MegaLauncher.onOffensiveMultiplier,  // 1.3x damage boost
    .onAccuracy = Artillery.onAccuracy,                          // Perfect accuracy
    .megaLauncherBoost = TRUE,                                   // Enables move detection
};
```

#### Damage Enhancement System
- **Multiplier**: 1.3x damage to all qualifying Mega Launcher moves
- **Implementation**: Inherited from MegaLauncher's `onOffensiveMultiplier`
- **Interaction**: Stacks with other damage modifiers (items, weather, etc.)

#### Perfect Accuracy System
- **Accuracy Override**: Returns `ACCURACY_HITS_IF_POSSIBLE` for all qualifying moves
- **Implementation**: Inherited from Artillery's `onAccuracy` function
- **Bypasses**: All accuracy checks, evasion boosts, weather interference

#### Multi-Target Transformation
Super Scope shares Artillery's target modification system:
```c
if ((BATTLER_HAS_ABILITY(battler, ABILITY_ARTILLERY) || BATTLER_HAS_ABILITY(battler, ABILITY_SUPER_SCOPE)) && 
    IsMegaLauncherBoosted(battler, moveId) && gBattleMoves[moveId].target == MOVE_TARGET_SELECTED)
    return MOVE_TARGET_BOTH;
```

### Move Selection Logic

Super Scope affects moves through the **IsMegaLauncherBoosted** function:

1. **FLAG_MEGA_LAUNCHER_BOOST moves**: Any move with the specific Mega Launcher flag
2. **All Status moves**: Every status move receives both accuracy and damage benefits
3. **Gunman synergy**: Enhanced interaction when combined with Gunman ability

### Comprehensive Move Coverage

#### High-Power Offensive Moves (Enhanced Examples)
- **Hydro Pump**: 110 BP to 143 BP (1.3x), perfect accuracy, hits both foes
- **Solar Beam**: 120 BP to 156 BP (1.3x), weather-independent, dual target
- **Focus Blast**: 120 BP to 156 BP (1.3x), never misses, hits both opponents
- **Energy Ball**: 90 BP to 117 BP (1.3x), guaranteed hit, dual targeting

#### Status Move Mastery
- **Thunder Wave**: Perfect accuracy, paralyzes both opponents
- **Toxic**: Never misses, badly poisons both foes
- **Sleep Powder**: Guaranteed sleep infliction on both targets
- **All status moves**: Enhanced reliability with dual battlefield control

#### Signature Move Synergies
- **Heal Pulse**: 75% HP healing (Mega Launcher bonus), perfect accuracy, can target both allies in certain formats
- **Dragon Pulse**: Type coverage with perfect reliability and power boost
- **Dark Pulse**: Flinch chance with guaranteed dual hits

### Strategic Applications

#### Ultimate Offensive Package
1. **Guaranteed Damage**: 1.3x boosted moves that never miss
2. **Action Economy**: Single moves affect both opponents with enhanced power
3. **Consistency**: Eliminates both accuracy RNG and provides damage security
4. **Versatility**: Effective across physical, special, and status movesets

#### Battlefield Control Mastery
- **Status Dominance**: Perfect accuracy status moves affecting both opponents
- **Field Pressure**: Opponents cannot rely on evasion or accuracy drops
- **Strategic Depth**: Forces opponents to account for guaranteed enhanced dual hits

#### Competitive Advantages
1. **Power + Reliability**: Combines the best of both parent abilities
2. **Multi-Format Excellence**: Dominant in singles, doubles, and raid battles
3. **Move Versatility**: Enhances diverse movesets from offense to support
4. **Psychological Pressure**: Opponents know key moves will always connect with bonus damage

### Ability Synergies

#### Internal Synergy
Super Scope's components work in perfect harmony:
- **Mega Launcher damage** makes the guaranteed hits more impactful
- **Artillery accuracy** ensures the boosted damage is always delivered
- **Dual targeting** maximizes the value of the enhanced moves

#### External Synergies
- **Gunman**: Expands move pool to include ALL moves as Mega Launcher boosted
- **Choice Items**: Perfect accuracy allows safe locking into powerful moves
- **Life Orb**: Damage boost stacks with Super Scope's multiplier for devastating results

### Comparison Analysis

#### vs Parent Abilities
- **vs Mega Launcher**: Trades some move flexibility for perfect accuracy and dual targeting
- **vs Artillery**: Gains significant damage boost while maintaining all accuracy benefits
- **Combined Value**: Represents the mathematical peak of projectile-based abilities

#### vs Other Ultimate Abilities
- **vs No Guard**: More selective but provides damage boost and multi-targeting
- **vs Magic Guard**: Different defensive vs offensive focus
- **vs Wonder Guard**: Defensive immunity vs offensive enhancement

### Notable Applications

#### Legendary Tier Usage
Super Scope's power level suggests legendary or mythical Pokemon usage:
- **Ultra Necrozma variants**: Signature ability for ultimate light-based Pokemon
- **Rayquaza forms**: Sky-based projectile mastery
- **Elite Redux Legendaries**: Custom legendary Pokemon with signature movesets

#### Team Building Considerations
1. **Move Priority**: Maximize Mega Launcher flagged moves in moveset
2. **Coverage**: Utilize diverse projectile types (beam, pulse, ball, aura)
3. **Support Integration**: Include status moves for battlefield control
4. **Partner Synergy**: Combine with setup Pokemon for guaranteed enhanced sweeps

### Technical Implementation

#### Flag System Integration
- **megaLauncherBoost = TRUE**: Enables detection by IsMegaLauncherBoosted function
- **Dual inheritance**: Combines function pointers from both parent abilities
- **Battle priority**: Accuracy takes precedence, then damage calculation occurs

#### Battle Flow Integration
1. **Move Selection**: IsMegaLauncherBoosted checks move eligibility
2. **Target Modification**: Single-target moves become dual-target
3. **Accuracy Resolution**: ACCURACY_HITS_IF_POSSIBLE overrides all accuracy checks
4. **Damage Calculation**: 1.3x multiplier applied to qualifying moves
5. **Effect Application**: Enhanced effects delivered to both targets

### Competitive Impact

#### Meta Implications
Super Scope fundamentally changes battle calculations:
- **Accuracy Strategy**: Eliminates evasion-based defensive strategies
- **Power Scaling**: Creates new damage benchmarks for projectile moves
- **Multi-Target Value**: Makes dual-battle formats heavily favor Super Scope users
- **Team Building**: Forces opponents to prepare for guaranteed enhanced dual hits

#### Format Analysis
- **Singles**: Provides unmatched reliability and power for key moves
- **Doubles**: Dominates through guaranteed dual targeting with damage boost
- **Raids**: Ensures consistent high damage output against multiple targets
- **Tournament**: High ban consideration due to combined power level

### Conclusion

Super Scope represents the pinnacle of projectile-based abilities, combining the most desirable aspects of offensive enhancement and tactical reliability. Its implementation as a true fusion ability makes it exceptionally powerful while maintaining clear mechanical coherence.

The ability's design philosophy of "perfect accuracy meets maximum power" creates a compelling risk-reward dynamic where Super Scope users gain tremendous consistency at the cost of ability slot opportunity cost. For Pokemon capable of learning diverse Mega Launcher moves, Super Scope transforms them into formidable threats capable of controlling entire battlefields through guaranteed enhanced projectile attacks.

This combination of power, reliability, and versatility firmly establishes Super Scope as an elite-tier ability worthy of legendary Pokemon or end-game competitive consideration.