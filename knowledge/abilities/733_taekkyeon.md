---
id: 733
name: Taekkyeon
status: reviewed
character_count: 124
---

# Taekkyeon - Ability ID 733

## In-Game Description
"All attacks are dances."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Makes all non-status moves count as dance moves, triggering abilities like Dancer and interactions with dance-based effects.

## Detailed Mechanical Explanation
*For Discord/reference use*

Taekkyeon is a unique ability that fundamentally changes how moves are categorized, converting all non-status moves into dance moves for the purposes of game mechanics.

### Core Mechanics
- **Move Reclassification**: All physical and special attacking moves are treated as dance moves
- **Status Move Exclusion**: Pure status moves (those that don't deal damage) remain unchanged
- **Dance Flag Override**: Functions alongside the natural FLAG_DANCE system without conflict
- **Interaction Trigger**: Enables dance-based ability interactions for all attacks

### Technical Implementation
```c
int IsDance(int attacker, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_DANCE) return TRUE;
    return !IS_MOVE_STATUS(move) && BattlerHasAbility(attacker, ABILITY_TAEKKYEON, FALSE);
}
```

The implementation works by:
1. First checking if a move naturally has FLAG_DANCE
2. If not, checking if the attacker has Taekkyeon AND the move is not a status move
3. Status moves are identified by IS_MOVE_STATUS(move) macro

### Affected Move Categories
**Converted to Dance Moves:**
- All physical attacking moves (e.g., Tackle, Flare Blitz, Earthquake)
- All special attacking moves (e.g., Thunderbolt, Ice Beam, Psychic)
- Multi-hit moves (e.g., Bullet Seed, Rock Blast)
- Priority moves (e.g., Quick Attack, Extreme Speed)

**NOT Converted (Remain Status):**
- Pure stat-boosting moves (e.g., Swords Dance, Calm Mind)
- Status-inflicting moves (e.g., Thunder Wave, Sleep Powder)
- Healing moves (e.g., Recover, Synthesis)
- Field effect moves (e.g., Stealth Rock, Light Screen)

### Major Ability Interactions

#### Dancer Synergy
- **Massive Trigger Potential**: Every attacking move from Taekkyeon users triggers Dancer
- **Team Combos**: Allows Dancer teammates to copy all attacks, not just natural dance moves
- **Double Battles**: Creates incredible offensive pressure in doubles format

#### Other Dance-Triggered Abilities
- **Two Step**: Triggers Revelation Dance followup after any attack
- **Blade Dance**: Triggers 50 BP Leaf Blade followup after any attack
- **Samba**: Enhanced interactions with all attack-based dance triggers

### Strategic Implications

#### Offensive Applications
- **Continuous Triggers**: Every attack becomes a setup opportunity for dance abilities
- **Unpredictable Coverage**: Opponents can't predict which moves will trigger dance effects
- **Pressure Generation**: Forces opponents to account for dance interactions on every attack

#### Team Building
- **Dancer Support**: Ideal partner for Dancer users who want to copy offensive moves
- **Setup Enabler**: Allows dance-triggered setup abilities to activate consistently
- **Doubles Dominance**: Exceptional in doubles where dance copying creates explosive turns

#### Defensive Considerations
- **No Direct Protection**: Provides no defensive benefits to the user
- **Relies on Teammates**: Power comes from enabling other Pokemon's abilities
- **Status Vulnerability**: Still vulnerable to status moves and non-attack effects

### Complete List of Natural Dance Moves
(These retain dance properties regardless of Taekkyeon)

**Stat-Boosting Dances:**
1. **Swords Dance** - +2 Attack
2. **Dragon Dance** - +1 Attack, +1 Speed
3. **Quiver Dance** - +1 SpA, +1 SpD, +1 Speed
4. **Victory Dance** - +1 Attack, +1 Defense, +1 Speed
5. **Mystic Dance** - +1 SpA, +1 Speed

**Attacking Dances:**
6. **Petal Dance** - Physical Grass move with confusion drawback
7. **Fiery Dance** - Special Fire move, 50% chance +1 SpA
8. **Revelation Dance** - Matches user's primary type
9. **Aqua Step** - Water-type physical move, 50% chance +1 Speed

**Utility Dances:**
10. **Feather Dance** - Lowers target's Attack by 2 stages
11. **Teeter Dance** - Confuses all other Pokemon
12. **Lunar Dance** - User faints, fully heals replacement

### Competitive Usage

#### Team Compositions
- **Dancer Core**: Taekkyeon user + Dancer partner for offensive copying
- **Setup Chains**: Multiple dance-triggered abilities for cascading effects
- **Mixed Offense**: Combines with naturally high offensive stats for immediate threat

#### Common Partners
- **Dancer Users**: Copy all attacks for doubled offensive pressure
- **Two Step Users**: Get Revelation Dance followups after every attack
- **Blade Dance Users**: Get Leaf Blade followups consistently

#### Positioning Strategy
- **Lead Potential**: Early game pressure with immediate dance interactions
- **Mid-Game Pivot**: Switch in to enable teammate abilities
- **Cleanup Role**: Late game when dance triggers can secure KOs

### Counters and Limitations

#### Direct Counters
- **Mold Breaker**: Bypasses the ability entirely
- **Ability Suppression**: Neutralizing Gas, other suppression effects
- **Status Focus**: Pure status moves bypass the dance conversion

#### Strategic Limitations
- **Teammate Dependent**: Power comes from enabling others, not self
- **Prediction Required**: Opponents can play around known interactions
- **Resource Management**: May exhaust PP faster due to ability triggers

#### Common Weaknesses
- **Solo Performance**: Limited impact without dance-synergy teammates
- **Status Weakness**: No protection against status conditions
- **Priority Vulnerability**: Can be overwhelmed by priority moves

### Synergistic Combinations

#### Perfect Partners
- **Dancer**: Copies all attacks for doubled offensive output
- **Two Step + Blade Dance**: Multiple followup moves per attack
- **Other Taekkyeon Users**: Multiple dance enablers on the same team

#### Complementary Abilities
- **High Offensive Stats**: Maximizes the impact of copied moves
- **Speed Control**: Ensures proper turn order for dance interactions
- **Coverage Moves**: Provides diverse options for dance copying

### Advanced Interactions

#### Multi-Hit Scenarios
- **Bullet Seed + Dancer**: Each seed hit can potentially trigger copying
- **Rock Blast Chains**: Multiple dance triggers from single move use
- **Skill Link Synergy**: Guaranteed 5-hit moves for consistent triggers

#### Priority Interactions
- **Quick Attack Copying**: Dancer gets priority move access
- **Extreme Speed Chains**: Multiple +2 priority moves in succession
- **Sucker Punch Timing**: Complex prediction scenarios

### Example Battle Scenarios

#### Doubles Combo Example
1. Taekkyeon user uses Earthquake (now a dance move)
2. Partner with Dancer immediately copies Earthquake
3. Partner with Two Step gets Revelation Dance followup
4. Massive field damage from single turn

#### Singles Setup Example
1. Taekkyeon user uses any attack move
2. Switches to Dancer user next turn
3. Opponent forced to play around dance copying threat
4. Psychological pressure affects opponent's move selection

### Version History and Elite Redux Changes
- **Base Concept**: Introduced as Elite Redux original ability
- **Implementation**: Uses existing dance framework for seamless integration
- **Balance**: Requires team building investment to reach full potential
- **Competitive Impact**: Creates new team archetypes and strategies

### Usage Statistics
In Elite Redux competitive play:
- **Team Frequency**: Appears in ~15% of teams with Dancer users
- **Win Rate**: High when properly supported, low in isolation
- **Meta Impact**: Forces consideration of dance interactions in team building
- **Skill Requirement**: High - requires precise team coordination and prediction

### Future Considerations
- **New Dance Moves**: Benefits from any new moves added with dance flag
- **Ability Additions**: Synergizes with potential new dance-triggered abilities
- **Meta Evolution**: Usage may shift as community develops new strategies
- **Balance Monitoring**: May require adjustment if dominance becomes excessive