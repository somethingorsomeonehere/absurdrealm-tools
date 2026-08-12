---
id: 154
name: Justified
status: reviewed
character_count: 84
---

# Justified - Ability ID 154

## In-Game Description
"Boosts Attack instead of being hit by Dark-type moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to Dark-type moves, and boost Attack by 1 stage when the user is hit by them. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics

Justified is a defensive absorption ability that provides complete immunity to Dark-type moves while gaining a stat boost. When a Pokemon with Justified would be hit by any Dark-type move:

1. **Damage Immunity**: The move deals 0 damage to the Justified user
2. **Stat Boost**: The user's highest attacking stat increases by +1 stage
3. **Stat Selection**: Uses `GetHighestAttackingStatId(battler, TRUE)` to determine which stat to boost

```c
constexpr Ability Justified = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_DARK);
        *statId = GetHighestAttackingStatId(battler, TRUE);
        return ABSORB_RESULT_STAT;
    },
};
```

### Technical Implementation

**Activation Conditions:**
- Pokemon must be targeted by a Dark-type move
- Move type checking occurs before damage calculation
- Works against both physical and special Dark-type moves
- Functions regardless of move accuracy or whether it would normally hit

**Stat Determination Algorithm:**
```c
u8 GetHighestAttackingStatId(u8 battlerId, u8 includeStatStages) {
    // Compares Attack vs Special Attack (including stat stages)
    // Returns STAT_ATK or STAT_SPATK based on higher value
}
```

**Boost Mechanics:**
- Always grants exactly +1 stage to the chosen stat
- Cannot be boosted further (no `absorbUp2` flag)
- Boost applies immediately when Dark move connects
- Respects normal stat stage limits (cannot exceed +6)

### Complete List of Affected Dark-Type Moves

**Common Dark-Type Moves:**
- Bite, Crunch, Dark Pulse, Night Slash
- Knock Off, Pursuit, Sucker Punch, Foul Play
- Thief, Beat Up, Brutal Swing, Lash Out
- Throat Chop, Darkest Lariat, Malicious Moonsault
- Plus all other Dark-type moves in the game

### Interactions with Other Abilities/Mechanics

**Ability Interactions:**
- **Mold Breaker/Teravolt/Turboblaze**: Can bypass Justified (moves hit normally)
- **Magic Guard**: Does not interfere with Justified's immunity
- **Substitute**: Dark moves hitting substitute do not trigger Justified
- **Multi-hit moves**: Each hit attempts to trigger Justified separately

**Move Interactions:**
- **Status Dark moves**: Still trigger Justified (e.g., status moves like Taunt if made Dark-type)
- **Z-Moves**: Dark-type Z-moves are absorbed completely
- **Max Moves**: Dark-type Max moves are absorbed
- **Hidden Power**: If Dark-type, triggers Justified

**Battle Mechanics:**
- **Critical hits**: Irrelevant since no damage is dealt
- **Type effectiveness**: Overridden by complete immunity
- **STAB**: Irrelevant due to absorption
- **Weather/terrain**: Does not affect Justified activation

### Strategic Implications

**Offensive Strategy:**
- Provides setup opportunities against Dark-type attacks
- Best utilized with mixed attackers or Pokemon with similar Attack/Sp. Attack
- Excellent for pivoting into predicted Dark-type moves
- Synergizes with moves that benefit from both Attack and Special Attack

**Defensive Value:**
- Complete immunity to an entire type
- Turns opponent's offense into user's advantage
- Forces opponents to avoid Dark-type moves entirely
- Particularly effective against Dark-type specialists

### Example Damage Calculations

**Before Justified Activation:**
- Base 80 Attack vs Base 90 Special Attack to Special Attack boosted
- 252 Attack EVs vs 0 Special Attack EVs to Attack likely boosted
- +1 Attack vs +0 Special Attack to Attack boosted (stages considered)

**After +1 Boost:**
- Attack: 100 to 150 (1.5x multiplier at +1 stage)
- Special Attack: 100 to 150 (1.5x multiplier at +1 stage)

### Common Users

**Notable Pokemon with Justified:**
- **Cobalion, Terrakion, Virizion, Keldeo**: Legendary Sword of Justice quartet
- **Lucario**: Mixed attacker that benefits from either stat boost
- **Absol**: Naturally high Attack benefits from further boosting
- **Gallade**: Physical attacker with decent Special Attack
- **Various Elite Redux custom Pokemon**: Many Fighting and Steel types

### Competitive Usage Notes

**Pros:**
- Complete type immunity with offensive benefit
- Unpredictable stat boost keeps opponents guessing
- Excellent switch-in potential
- Forces team preview mindgames

**Cons:**
- Situational activation (requires Dark-type moves)
- Cannot choose which attacking stat gets boosted
- Mold Breaker variants bypass the ability entirely
- Less useful in metas with few Dark-type moves

### Counters

**Direct Counters:**
- **Mold Breaker**: Bypasses Justified completely
- **Non-Dark moves**: Use other types to avoid triggering
- **Status conditions**: Inflict poison, burn, paralysis, sleep before attacking
- **Indirect damage**: Stealth Rock, Spikes, weather damage

**Strategic Counters:**
- **Mixed walls**: Tank both Attack and Special Attack variants
- **Priority moves**: Hit before setup sweeping begins
- **Phazing**: Force switches with Roar, Whirlwind, Dragon Tail
- **Stat debuffs**: Lower Attack/Special Attack with Intimidate or moves

### Synergies

**Item Synergies:**
- **Life Orb**: Amplifies boosted stat's damage output
- **Choice items**: Lock into powerful attacks after boost
- **Weakness Policy**: Double stat boost if hit by super-effective Dark move first
- **Leftovers/Sitrus Berry**: Sustain for multiple setup opportunities

**Move Synergies:**
- **Close Combat**: Physical Fighting move using boosted Attack
- **Aura Sphere**: Special Fighting move using boosted Special Attack
- **Work Up**: Manual boost to complement Justified
- **Stored Power**: Scales with stat boosts accumulated

**Team Synergies:**
- **Baton Pass**: Transfer stat boosts to frailer sweepers
- **Dual screens**: Provide setup time for Justified activation
- **Stealth Rock**: Wear down opponents switching to avoid Dark moves
- **Thunder Wave**: Paralysis support for setup sweeping

### Version History

Justified has been present since Generation V and maintains consistent functionality across all games. In Elite Redux, it retains its original mechanics while being distributed to additional Pokemon that thematically fit the "justice" concept, particularly Fighting, Steel, and heroic Pokemon archetypes.

The ability's implementation in Elite Redux uses the modern absorption system, providing clean immunity while applying stat boosts through the standardized `ABSORB_RESULT_STAT` mechanism.