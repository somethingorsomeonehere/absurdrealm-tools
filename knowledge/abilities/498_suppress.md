---
id: 498
name: Suppress
status: reviewed
character_count: 86
---

# Suppress - Ability ID 498

## In-Game Description
"Uses Torment on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Torment on entry, preventing the opponent from using the same move consecutively. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Suppress automatically inflicts the Torment status condition upon entry, forcing opponents to constantly change their move selection and preventing repetitive attack patterns.

### Activation Conditions
- **Trigger**: Activates immediately when switching into battle
- **Target**: Automatically targets an opposing Pokemon
- **Move used**: Torment (Dark-type status move)
- **Effect**: Inflicts torment status condition
- **Guarantee**: Cannot miss when used by this ability

### Technical Implementation
```c
constexpr Ability Suppress = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_TORMENT, 0); 
    },
};
```

### Torment Status Condition
- **Effect**: Prevents using the same move twice in a row
- **Duration**: Permanent until cured or target switches out
- **Restriction**: Must alternate between different moves
- **Type**: Dark-type status move (affected by type interactions)
- **Category**: Status move (no damage dealt)

### Move Selection Impact
**Before Torment:**
- Turn 1: Thunderbolt
- Turn 2: Thunderbolt (allowed)
- Turn 3: Thunderbolt (allowed)

**After Torment:**
- Turn 1: Thunderbolt
- Turn 2: Cannot use Thunderbolt (must use different move)
- Turn 3: Can use Thunderbolt again
- Turn 4: Cannot use Thunderbolt (must alternate)

### Strategic Applications
- **Repetition disruption**: Stops powerful move spamming
- **Choice item counters**: Forces Choice users into suboptimal moves
- **Setup disruption**: Prevents repeated stat boosting
- **Prediction tool**: Forces opponent into readable patterns
- **Offensive pressure**: Reduces opponent's move flexibility

### Target Interactions
**Excellent against:**
- Choice item users (Specs, Band, Scarf)
- Single-move spammers (Earthquake, Boomburst)
- Setup sweepers (repeated Calm Mind, Swords Dance)
- STAB abusers (Pokemon relying on one powerful move)

**Less effective against:**
- Mixed attackers (multiple viable moves)
- Support Pokemon (various utility moves)
- Status spreaders (multiple different status moves)
- Diverse movesets (many attack options)

### Curing Methods
- **Switching out**: Removes torment status naturally
- **Aromatherapy/Heal Bell**: Team-wide status cure
- **Mental Herb**: Instant torment cure (if applicable)
- **Natural Cure**: Removes on switch-out
- **Refresh**: Self-cure move

### Double Battle Applications
- **Single target**: Only affects one opposing Pokemon
- **Partner protection**: Doesn't affect ally Pokemon
- **Strategic targeting**: Choose which opponent to torment
- **Field control**: Reduces one opponent's offensive options

### Competitive Usage
- **Anti-meta**: Counters common repetitive strategies
- **Disruption**: Forces opponents into suboptimal plays
- **Entry utility**: Provides immediate battlefield impact
- **Support role**: Helps team by limiting opponent options
- **Prediction game**: Creates mind games around move selection

### Choice Item Interactions
**Choice Band/Specs/Scarf users:**
- Locked into one move normally
- Torment forces them to Struggle after first use
- Must switch or use Struggle (40 BP, recoil damage)
- Creates significant disadvantage for Choice users

### Synergies
**Team support:**
- Entry hazards: Stack damage while limiting moves
- Status spreaders: Combine with other disruptive effects
- Prediction users: Easier to predict forced move changes
- Trappers: Prevent switching to escape torment

**Item synergies:**
- Rocky Helmet: Punish forced contact moves
- Leftovers: Sustain while opponent struggles with limits
- Choice items: Ironically good for user after tormenting opponent

### Counters
- **Switching**: Simple escape from torment status
- **Diverse movesets**: Multiple viable moves reduce impact
- **Status immunity**: Some abilities prevent status conditions
- **Mental Herb**: Instant cure for torment
- **Team cures**: Aromatherapy/Heal Bell support

### Limitations
- **Single target**: Only affects one opponent at a time
- **Switch escape**: Easy to remove by switching
- **Movepool dependent**: Less effective against diverse attackers
- **No damage**: Doesn't deal direct damage
- **One activation**: Only triggers once per switch-in

### Dark-Type Interactions
- **Type immunity**: Normal-types immune to Dark moves
- **Effectiveness**: Not affected by type chart (status move)
- **STAB**: User gets STAB if Dark-type (though no damage)
- **Ability interactions**: Affected by Dark-type ability interactions

### Prediction Applications
- **Forced alternation**: Opponent must constantly change moves
- **Pattern recognition**: Easier to predict opponent's next move
- **Move baiting**: Force opponent into disadvantageous moves
- **Setup opportunities**: Predict non-threatening moves for setup

### Version History
- Elite Redux custom ability for move restriction control
- Based on the existing Torment move mechanics
- Designed to counter repetitive strategies
- Part of expanded disruption ability system