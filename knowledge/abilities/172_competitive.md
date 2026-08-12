---
id: 172
name: Competitive
status: reviewed
character_count: 102
---

# Competitive - Ability ID 172

## In-Game Description
"Raises Sp. Atk by two stages if stats are lowered by an enemy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user has their stats lowered by another Pokemon, they raise their Special Attack by 2 stages.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Trigger Conditions:**
- Activates when any stat is lowered by an opponent (not self-inflicted)
- Monitored through `gTurnStructs[battler].changedStatsBattlerId` tracking system
- Only triggers when `changedStatsBattlerId` is set to an enemy battler (gBattlerAttacker ≠ gBattlerTarget)

**Implementation Details:**
- **Location**: `src/battle_util.c` lines 1142-1145
- **Battle Script**: `BattleScript_CompetitiveActivates` in `data/battle_scripts_1.s`
- **Effect**: Raises Special Attack by exactly 2 stages (+2)
- **Safety Check**: Will not activate if Special Attack is already at maximum (+6 stages)

**What Triggers Competitive:**
- Direct stat-lowering moves (Growl, Leer, Intimidate, etc.)
- Secondary effects from damaging moves (Crunch lowering Defense, etc.)
- Opponent abilities that lower stats (Intimidate on switch-in)
- Items used by opponents that lower stats
- Field effects caused by opponents

**What Does NOT Trigger Competitive:**
- Self-inflicted stat drops (Superpower, Close Combat, etc.)
- Stat drops from ally Pokemon in doubles
- Burns lowering Attack (status condition, not direct stat lowering)
- Paralysis lowering Speed (status condition, not direct stat lowering)

**Battle Mechanics:**
1. When an opponent lowers any stat, `STRINGID_DEFENDERSSTATFELL` message is triggered
2. Game checks if target has Competitive ability
3. If Special Attack is not at maximum (+6), ability activates
4. Special Attack is raised by 2 stages immediately
5. Ability popup is displayed and stat change animation plays

**Interaction Notes:**
- Works in singles and doubles battles
- Multiple stat drops in one turn only trigger Competitive once
- Can stack with other stat-boosting effects
- Mold Breaker and similar abilities do NOT bypass this trigger (it's not a protective ability)
- Works even if the Pokemon is behind a Substitute

**Competitive Viability:**
- Excellent deterrent against stat-lowering strategies
- Pairs well with special attacking movesets
- Particularly effective against Intimidate users
- Can turn opponent's debuffing attempts into setup opportunities
- Strong in formats with common stat-lowering moves or abilities

**Code References:**
- Proto definition: `proto/AbilityList.textproto` line 865-868
- Trigger logic: `src/battle_util.c` lines 1142-1145  
- Battle script: `data/battle_scripts_1.s` lines 9490-9493
- Stat change tracking: `src/battle_script_commands.c` line 9575