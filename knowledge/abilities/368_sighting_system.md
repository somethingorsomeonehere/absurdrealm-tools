---
id: 368
name: Sighting System
status: reviewed
character_count: 131
---

# Sighting System - Ability ID 368

## In-Game Description
"Guarantees all moves hit, but inaccurate moves get -3 priority."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sighting System guarantees all moves hit regardless of accuracy checks. Moves with less than 80% base accuracy receive -3 priority.

## Detailed Mechanical Explanation

### Overview

Sighting System is an Elite Redux-exclusive ability that provides perfect accuracy for all moves while imposing a priority penalty on less accurate moves. This creates an interesting tactical trade-off between reliability and speed, making it particularly valuable for Pokemon that rely on powerful but inaccurate moves.

## Mechanics

### Core Functionality

Sighting System provides two distinct effects:

1. **Perfect Accuracy**: All moves automatically hit regardless of accuracy checks
2. **Priority Penalty**: Moves with less than 80% base accuracy receive -3 priority (move last)

### Technical Implementation

The ability is implemented through two callback functions in `src/abilities.cc` (lines 3826-3833):

#### Accuracy Component (Line 3827)
```cpp
.onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority { return ACCURACY_HITS_IF_POSSIBLE; },
```

#### Priority Component (Lines 3828-3832)
```cpp
.onPriority = +[](ON_PRIORITY) -> int {
    CHECK(gBattleMoves[move].accuracy)
    CHECK(gBattleMoves[move].accuracy < 80);
    return -3;
},
```

### Accuracy System

The ability returns `ACCURACY_HITS_IF_POSSIBLE`, which is processed in the battle system to guarantee a hit. As seen in `src/battle_script_commands.c:1306-1307`, this priority level returns 101% accuracy, ensuring the move always hits.

### Priority Thresholds

The priority penalty applies to moves with:
- Base accuracy less than 80%
- Non-zero accuracy (moves with 0 accuracy, like OHKO moves, are not affected by the priority penalty)

## Strategic Applications

### Guaranteed Accuracy Benefits

Sighting System transforms unreliable moves into consistent threats:
- **High-power, low-accuracy moves** (Thunder, Blizzard, Fire Blast) become reliable
- **Status moves with imperfect accuracy** (Will-O-Wisp, Thunder Wave) never miss
- **Coverage moves** with accuracy issues become dependable

### Priority Trade-offs

The -3 priority penalty creates strategic considerations:
- **Powerful moves** like Zap Cannon (50% accuracy) become extremely slow
- **Status moves** with low accuracy (Hypnosis, Sing) move very late
- **Must consider** whether the guaranteed hit is worth moving last

### Competitive Applications

#### Advantages
- **Eliminates accuracy RNG** on all moves
- **Enables reliable use** of powerful but inaccurate moves
- **Consistent status application** regardless of base accuracy

#### Disadvantages
- **Speed penalty** on many powerful moves
- **Vulnerable to priority moves** when using low-accuracy attacks
- **Telegraphed plays** when opponent knows about the priority penalty

## Pokemon with Sighting System

Based on species data analysis, Sighting System appears on:

### Magnezone
- **Type**: Electric/Steel
- **Stats**: 70/70/115/130/90/60
- **Context**: One of three regular abilities alongside Overcharge and Download
- **Role**: Special attacker that benefits from guaranteed Thunder and Zap Cannon

### Genesect (Multiple Forms)
- **Type**: Bug/Steel  
- **Stats**: 71/120/95/120/95/99
- **Context**: One of three regular abilities alongside Download and Fatal Precision
- **Role**: Versatile attacker that can use both accurate and inaccurate moves effectively

### Innate Abilities
Both Pokemon also possess powerful innate abilities:
- **Magnezone**: Filter (reduces super-effective damage)
- **Genesect**: Mega Launcher, Predator, Full Metal Body (various forms)

## Ability Relationships

### Iron Barrage Connection
Iron Barrage (Ability #379) directly inherits Sighting System's effects:
```cpp
constexpr Ability IronBarrage = {
    .onOffensiveMultiplier = MegaLauncher.onOffensiveMultiplier,
    .onAccuracy = SightingSystem.onAccuracy,
    .onPriority = SightingSystem.onPriority,
    .megaLauncherBoost = TRUE,
};
```
This shows Sighting System is considered valuable enough to be incorporated into other abilities.

### Similar Accuracy Abilities
Other abilities that provide guaranteed accuracy:
- **Deadeye** (ABILITY_DEADEYE): Perfect accuracy for Mega Launcher and arrow-based moves
- **Artillery** (ABILITY_ARTILLERY): Perfect accuracy for Mega Launcher moves only
- **No Guard** (ABILITY_NO_GUARD): All moves hit both ways, no priority penalty

## Move Interactions

### Affected by Priority Penalty
- **Thunder** (70% accuracy) to Perfect accuracy but -3 priority
- **Blizzard** (70% accuracy) to Perfect accuracy but -3 priority  
- **Fire Blast** (85% accuracy) to Perfect accuracy, normal priority
- **Hydro Pump** (80% accuracy) to Perfect accuracy, normal priority
- **Zap Cannon** (50% accuracy) to Perfect accuracy but -3 priority
- **Focus Blast** (70% accuracy) to Perfect accuracy but -3 priority

### Not Affected by Priority Penalty
- **Thunderbolt** (100% accuracy) to Perfect accuracy, normal priority
- **Ice Beam** (100% accuracy) to Perfect accuracy, normal priority
- **OHKO moves** (0% accuracy listed) to Still miss normally, no priority change

## Competitive Viability

### Tier Assessment: Medium

**Strengths:**
- Eliminates accuracy-based losses entirely
- Enables use of otherwise unreliable powerful moves
- Provides consistent status application
- Valuable in formats where accuracy matters

**Weaknesses:**
- Priority penalty can be exploited by faster opponents
- Limits the effectiveness of speed-based strategies
- Telegraph strategy to experienced opponents
- Not beneficial for Pokemon already using accurate moves

### Team Synergy

**Works well with:**
- **Trick Room teams**: Priority penalty becomes less relevant
- **Bulky builds**: Can tank hits while using slow, powerful moves  
- **Status spreaders**: Guaranteed paralysis/sleep without speed concerns

**Problematic with:**
- **Speed-based teams**: Priority penalty conflicts with fast playstyles
- **Priority move users**: May want to go first consistently
- **Choice Scarf sets**: Speed investment partially wasted on low-accuracy moves

## Technical Details

### Accuracy Priority System
The game's accuracy system uses a priority-based approach where higher priority results override lower ones:
- `ACCURACY_ALWAYS_HITS` and `ACCURACY_HITS_IF_POSSIBLE` both return 101% accuracy
- This bypasses all accuracy calculations, evasion boosts, and accuracy debuffs
- Weather-based accuracy modifications are also ignored

### Priority Modification
The -3 priority penalty is substantial:
- Most moves have 0 priority
- Priority moves range from +1 to +5
- -3 ensures the move goes after almost all other actions
- Only moves with lower priority (Quick Guard, some Trick Room effects) would go later

## Conclusion

Sighting System represents a well-designed ability that offers significant power at a meaningful cost. The guaranteed accuracy eliminates one of the most frustrating aspects of competitive play - missing crucial moves due to RNG. However, the priority penalty on less accurate moves creates genuine strategic decisions about when to use powerful but slow attacks.

The ability's implementation on Magnezone and Genesect forms provides both Pokemon with unique tactical options, allowing them to use moves like Thunder and Focus Blast without accuracy concerns while forcing careful consideration of timing and positioning.

From a competitive standpoint, Sighting System occupies a middle tier - powerful enough to be relevant but not overwhelmingly strong. Its success depends heavily on team composition, opposing threats, and the pilot's ability to leverage guaranteed accuracy while managing the priority penalties effectively.

