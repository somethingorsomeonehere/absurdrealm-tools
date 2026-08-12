---
id: 387
name: Discipline
status: reviewed
character_count: 193
---

# Discipline - Ability ID 387

## In-Game Description
"Can switch while rampaging. Can't be confused or intimidated."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents confusion and grants immunity to Intimidation effects. When using rampage moves like Thrash or Outrage, allows switching out during the lock period instead of being forced to continue. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Discipline provides a unique combination of status immunity and rampage move flexibility through three distinct mechanisms:

### 1. Confusion Immunity
**Implementation** (`src/abilities.cc` lines 4002-4005):
```cpp
constexpr Ability Discipline = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_CONFUSION)
        return TRUE;
    },
```

- Grants complete immunity to confusion from all sources
- Works against Confuse Ray, Swagger confusion, Outrage/Thrash confusion
- Uses the same `CHECK_CONFUSION` flag as other confusion-immune abilities
- Displays ability pop-up when confusion is blocked

### 2. Taunt Immunity
**Implementation** (`src/abilities.cc` line 4008):
```cpp
    .tauntImmune = TRUE,
```

- Complete immunity to Taunt and similar "intimidation" effects
- Allows use of status moves even when Taunt is active
- Shared with abilities like Oblivious, Aroma Veil, and Queenly Majesty
- Prevents mental manipulation and maintains tactical flexibility

### 3. Rampage Switching Mechanism
**Switch Permission** (`src/battle_script_commands.c` lines 4402-4405):
```c
if (BATTLER_HAS_ABILITY(gBattlerAttacker, ABILITY_DISCIPLINE) && gBattleMoves[gChosenMove].effect == EFFECT_RAMPAGE)
    gVolatileStructs[gBattlerAttacker].disciplineCounter = 3;
```

**Lock Timer Management** (`src/battle_util.c` lines 2797-2803):
```c
if (BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_DISCIPLINE) && 
    gVolatileStructs[gActiveBattler].disciplineCounter) {
    gVolatileStructs[gActiveBattler].disciplineCounter--;
    if (gVolatileStructs[gActiveBattler].disciplineCounter == 0) {
        gBattleStruct->choicedMove[gActiveBattler] = MOVE_NONE;
        BattleScriptExecute(BattleScript_DisciplineLockEnds);
    }
}
```

### Rampage Move Interactions

**Affected Moves** (all have `EFFECT_RAMPAGE`):
- **Thrash** (Normal-type, 130 BP, Physical)
- **Petal Dance** (Grass-type, 130 BP, Special) 
- **Outrage** (Dragon-type, 130 BP, Physical)
- **Uproar** (Normal-type, 100 BP, Special)

**Normal Rampage Behavior**:
1. Move locks user for 2-3 turns
2. User cannot switch or use other moves
3. After completion, user becomes confused
4. Lock can only end through fainting or rampage completion

**With Discipline**:
1. User can switch out during the rampage lock
2. 3-turn timer (`disciplineCounter`) tracks the lock duration
3. Timer decrements each turn the user remains in battle
4. When timer reaches 0, lock ends cleanly without confusion
5. Message displays: "{Pokemon} is no longer locked into only using one move!"

### Technical Implementation Details

**Ability Properties**:
- `breakable = TRUE`: Can be suppressed by abilities like Mold Breaker
- `removesStatusOnImmunity = TRUE`: Clears existing confusion when ability activates
- `tauntImmune = TRUE`: Prevents Taunt and similar effects

**Battle Script Integration**:
- Uses `STRINGID_DISCIPLINE_LOCK_ENDS` (ID 684) for lock expiration message
- Integrated with Choice item logic for move locking mechanics
- Compatible with Gorilla Tactics and Sage Power lock systems

### Strategic Implications

**Rampage Move Advantages**:
- Safe usage of high-power rampage moves without confusion risk
- Ability to scout and pivot during rampage sequences
- Maintains team momentum through strategic switching
- Eliminates the traditional drawback of rampage moves

**Status Control Benefits**:
- Complete immunity to confusion disruption
- Taunt immunity enables reliable status/setup moves
- Prevents common confusion + paralysis strategies
- Maintains consistency in battle flow

**Competitive Applications**:
- **Physical Sweepers**: Safe Outrage/Thrash usage
- **Pivot Pokemon**: Switch during rampage for tempo control  
- **Setup Pokemon**: Taunt immunity protects setup moves
- **Mixed Attackers**: Access to diverse move types without lock risk

### Example Battle Scenarios

**Scenario 1 - Rampage Switching**:
1. Dragonite with Discipline uses Outrage (turn 1)
2. Player switches Dragonite out (disciplineCounter = 2)
3. Dragonite returns later, can use any move (lock expired)
4. No confusion inflicted when lock ends

**Scenario 2 - Taunt Immunity**:
1. Opponent uses Taunt on Discipline user
2. Discipline user can still use Dragon Dance, Nasty Plot, etc.
3. Maintains setup potential against disruption strategies

**Scenario 3 - Confusion Prevention**:
1. Opponent uses Confuse Ray
2. Discipline blocks confusion with ability pop-up
3. User maintains clear decision-making

### Interactions with Other Mechanics

**Choice Items**: 
- Choice lock and Discipline rampage lock are separate systems
- Can be locked by Choice Band while using Discipline rampage mechanics
- Timer system doesn't interfere with Choice item restrictions

**Multi-Hit Abilities**:
- Parental Bond works normally with rampage moves
- Each hit contributes to the same rampage sequence
- Discipline switching still available between turns

**Status Conditions**:
- Sleep, paralysis, burn work normally
- Only confusion is blocked by Discipline
- Other mental effects (attraction) may still work

### Competitive Usage Notes

**Tier Placement**: Medium-tier ability providing solid utility
- Valuable on Pokemon that want rampage move access
- Excellent on pivot Pokemon that need flexibility
- Strong on setup sweepers requiring status move access

**Team Synergies**:
- **Momentum Teams**: Enables rampage moves without commitment
- **Setup Offense**: Taunt immunity protects setup sequences
- **Mixed Attackers**: Access to rampage coverage without drawbacks

**Common Users in Elite Redux**:
- Pokemon with access to Outrage/Thrash as coverage
- Setup sweepers that need status move reliability
- Pivot Pokemon that benefit from rampage power + switching

### Counters and Counterplay

**Direct Counters**:
- **Mold Breaker**: Suppresses all Discipline benefits
- **Status Moves**: Sleep, paralysis still work normally
- **Gastro Acid**: Removes ability entirely
- **Raw Power**: Ability provides no defensive stats

**Indirect Counters**:
- **Priority Moves**: Circumvent setup attempts
- **Residual Damage**: Punish switching during rampage
- **Defensive Walls**: Force unfavorable trades
- **Speed Control**: Prevent setup opportunities

### Synergies

**Offensive Synergies**:
- **Life Orb**: Increased rampage move power
- **Choice Band/Specs**: Massive power boost (separate from rampage lock)
- **Dragon Dance/Nasty Plot**: Protected setup into rampage moves

**Defensive Synergies**:
- **Multiscale**: Survive to use rampage moves safely
- **Intimidate**: Pivot support while using rampage moves
- **Recovery Moves**: Taunt immunity protects healing

**Team Support**:
- **U-turn/Volt Switch**: Maintain momentum during rampage switching
- **Rapid Spin/Defog**: Taunt immunity protects hazard removal
- **Wish Support**: Enable rampage move users to stay healthy

### Version History
- Added in Elite Redux as ability #387
- Unique combination of confusion immunity and rampage flexibility
- Part of Elite Redux's expanded status control options
- Designed to make rampage moves more viable in competitive play

### Pokemon with Discipline
*Note: Specific distribution varies by Elite Redux version*
- Available as changeable ability on various Pokemon
- Commonly found on Dragon-types with Outrage access
- Physical attackers that benefit from Thrash coverage
- Setup Pokemon that need status move protection

Discipline represents Elite Redux's innovative approach to ability design, combining traditional status immunity with unique mechanical interactions that address long-standing issues with rampage moves in competitive Pokemon.