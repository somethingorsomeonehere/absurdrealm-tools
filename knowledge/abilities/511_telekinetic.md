---
id: 511
name: Telekinetic
status: reviewed
character_count: 270
---

# Telekinetic - Ability ID 511

## In-Game Description
"Casts Telekinesis on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Casts Telekinesis on entry. All moves against the target cannot miss, but they become immune to Ground-type moves and other Grounded effects. Cannot affect Rooted Pokemon or if they hold Iron Ball. Wears off under Gravity or if they are hit by Smack Down. Lasts 3 turns.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Telekinetic is a unique entry ability that automatically applies the Telekinesis move effect to its user upon switching in. This creates a double-edged effect where the user gains immunity to certain moves but becomes vulnerable to all attacks.

### Activation Conditions
- **Entry trigger**: Activates immediately when the Pokemon enters battle
- **Duration**: Lasts for 3 turns after activation
- **Auto-cast**: Uses the Telekinesis move effect without consuming PP
- **Species restrictions**: Cannot activate on certain grounded species

### Telekinesis Effect Details
When Telekinetic activates, the user gains the STATUS3_TELEKINESIS status, which provides:
- **Levitation**: Pokemon is lifted off the ground
- **Perfect accuracy**: All moves targeting the user have 100% accuracy
- **Ground immunity**: Becomes immune to Ground-type moves
- **Terrain immunity**: Unaffected by terrain effects (Electric, Grassy, Misty, Psychic)

### Technical Implementation
```c
// Telekinetic ability activates on entry
constexpr Ability Telekinetic = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_TELEKINESIS, 0); 
    },
};

// Telekinesis move effect implementation
static void Cmd_settelekinesis(void) {
    if (gStatuses3[gBattlerTarget] & (STATUS3_TELEKINESIS | STATUS3_ROOTED | STATUS3_SMACKED_DOWN) || 
        gFieldStatuses & STATUS_FIELD_GRAVITY ||
        IsTelekinesisBannedSpecies(gBattleMons[gBattlerTarget].species)) {
        gBattlescriptCurrInstr = T1_READ_PTR(gBattlescriptCurrInstr + 1);
    } else {
        gStatuses3[gBattlerTarget] |= STATUS3_TELEKINESIS;
        gVolatileStructs[gBattlerTarget].telekinesisTimer = 3;
        gBattlescriptCurrInstr += 5;
    }
}
```

### Banned Species
Certain grounded Pokemon cannot be affected by Telekinesis and thus cannot have this ability:
- Diglett and Dugtrio (including Alolan forms)
- Gengar-Mega (partially underground)
- Sand Castle Pokemon (Palossand)
- Other species with permanent ground connection

### Status Interactions
- **Smack Down**: Immediately ends the Telekinesis effect
- **Gravity**: Prevents activation and ends existing effect
- **Rooted**: Cannot activate if user is rooted to the ground
- **Magnet Rise**: Does not stack with existing levitation effects

### Turn Counter Management
```c
// End of turn check for Telekinesis duration
case ENDTURN_TELEKINESIS:
    if (gStatuses3[gActiveBattler] & STATUS3_TELEKINESIS) {
        if (gVolatileStructs[gActiveBattler].telekinesisTimer == 0 || 
            --gVolatileStructs[gActiveBattler].telekinesisTimer == 0) {
            gStatuses3[gActiveBattler] &= ~(STATUS3_TELEKINESIS);
            BattleScriptExecute(BattleScript_TelekinesisEndTurn);
        }
    }
```

### Strategic Implications
**Advantages:**
- **Entry pressure**: Immediate battlefield control upon switching in
- **Ground immunity**: Complete immunity to Earthquake, Earth Power, etc.
- **Terrain immunity**: Unaffected by all terrain effects
- **Setup protection**: Can set up moves while immune to Ground attacks

**Disadvantages:**
- **Perfect accuracy vulnerability**: All attacks hit with 100% accuracy
- **Limited duration**: Only lasts 3 turns
- **Gravity vulnerability**: Completely negated by Gravity field effect
- **Smack Down weakness**: Instantly loses all benefits

### Competitive Usage
- **Anti-Ground**: Excellent against Ground-type heavy teams
- **Setup sweeper**: Allows safe setup against Ground-type attacks
- **Terrain denial**: Prevents opponent from using beneficial terrain effects
- **Entry hazard immunity**: Immune to Spikes while levitating
- **Risk vs reward**: High-risk, high-reward ability requiring careful timing

### Common Strategies
1. **Setup Abuse**: Use the 3-turn immunity window to set up stat boosts
2. **Terrain Control**: Deny opponent access to terrain-based strategies
3. **Anti-Earthquake**: Counter common Ground-type coverage moves
4. **Pivot Tool**: Switch in to absorb Ground attacks, then pivot out

### Counters
**Direct Counters:**
- **Gravity**: Completely negates the ability and grounds the user
- **Smack Down**: Instantly removes all benefits
- **Weather Ball (in Gravity)**: Becomes Rock-type and hits grounded targets
- **High accuracy moves**: Stone Edge, Focus Blast become guaranteed hits

**Indirect Counters:**
- **Status moves**: Perfect accuracy makes status moves unavoidable
- **Multi-hit moves**: Skill Link abilities become more threatening
- **OHKO moves**: Fissure, Guillotine become 30% accurate instead of failing

### Ability Synergies
- **Air Balloon**: Extends levitation beyond 3 turns if balloon isn't popped
- **Levitate**: Redundant with Telekinetic's Ground immunity
- **Magic Guard**: Prevents residual damage while gaining perfect accuracy
- **Sturdy**: Ensures survival of at least one perfect accuracy attack

### Team Synergies
- **Gravity teams**: Ironically, opposing Gravity can shut down the ability
- **Terrain teams**: Denies opponent access to terrain while maintaining your own
- **Setup sweepers**: Partners who can abuse the temporary immunity window
- **Pivot cores**: Pokemon that can switch in to absorb Ground moves

### Version History
- Elite Redux exclusive ability
- Designed as a high-risk, high-reward entry ability
- Balances immunity benefits with perfect accuracy vulnerability
- Part of the expanded ability roster in Elite Redux

### Interaction Notes
- Cannot be Skill Swapped while active (status-based, not ability-based after activation)
- Trace cannot copy the entry effect (occurs before Trace activation)
- Role Play copying occurs after the initial Telekinesis application
- Works with entry-based items like Focus Sash for survival strategies