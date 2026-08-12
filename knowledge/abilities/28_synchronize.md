---
id: 28
name: Synchronize
status: reviewed
character_count: 234
---

# Synchronize - Ability ID 28

## In-Game Description
"Enemies inflicting status on this Pokemon get same status."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When inflicted with a non-volatile status (except sleep), the attacker receives the same status. Bypasses Substitute. If the user can cure the status when it is inflicted, they will inflict the status to the attacker before curing it.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Synchronize reflects status conditions back to the Pokemon that inflicted them. When a Pokemon with Synchronize is statused, the ability immediately attempts to inflict the same status on the attacker.

### Technical Implementation
The ability uses two effect types:
- `ABILITYEFFECT_SYNCHRONIZE`: When the Synchronize user is targeted
- `ABILITYEFFECT_ATK_SYNCHRONIZE`: When the Synchronize user is the attacker

Key code elements:
- Stores status type in `gBattleStruct->synchronizeMoveEffect`
- Triggers `BattleScript_SynchronizeActivates`
- Uses `HITMARKER_IGNORE_SAFEGUARD` flag

### In-Battle Effects

**Reflected statuses:**
- Poison (including Toxic as of Gen 5+)
- Paralysis
- Burn
- Sleep is NOT reflected

**Activation conditions:**
1. Must be directly statused (not from secondary effects in some cases)
2. Attacker must not already have a status
3. Status immunities still apply to the attacker

**Special properties:**
- Bypasses Safeguard on the attacker
- In Gen 8 (Elite Redux), Toxic inflicts bad poison on the attacker
- Does not trigger from self-inflicted status

### Out-of-Battle Effects

**Wild Pokemon encounters:**
- **Gen 8 mechanics**: 100% chance for wild Pokemon to have the same nature
- Lead Pokemon must have Synchronize
- Does not work on gift Pokemon or static encounters in some games

### Implementation Locations
- Battle logic: `/src/battle_util.c` (lines 4421-4458)
- Status trigger: `/src/battle_script_commands.c` (line 2457)
- Wild encounters: `/src/wild_encounter.c` (line 295)
- Battle script: `/data/battle_scripts_1.s`
- Config flags: `/include/constants/battle_config.h`

### Pokemon with Synchronize
Common users include:
- Munna/Musharna
- Espeon
- Umbreon  
- Gardevoir line
- Various Psychic-type Pokemon

### Strategic Implications

**Defensive use:**
- Deters status moves like Will-O-Wisp and Thunder Wave
- Forces opponents to consider status immunity before using status moves
- Can turn opponent's strategy against them

**Limitations:**
- Cannot proactively status opponents
- Requires taking a status first
- Opponent can switch out to cure status
- No effect if opponent is already statused

### Nature Hunting Applications
- Essential for competitive breeding
- 100% nature transfer rate makes finding specific natures trivial
- Synchronize Pokemon of each useful nature recommended
- Common choices: Modest, Adamant, Jolly, Timid

### Synergies
- **Natural Cure**: Can reflect status then switch to heal
- **Magic Bounce**: Different approach to status prevention
- **Heal Bell/Aromatherapy**: Team support after reflecting

### Counters
- Already statused Pokemon
- Status immune types (Electric vs paralysis, Fire vs burn)
- Substitute blocks direct status
- Magic Guard prevents status damage even if reflected
- Simply avoiding status moves

### Competitive Usage Notes
Synchronize provides moderate defensive utility by creating risk for status users. The nature synchronization effect is invaluable for team building. In battle, it's best on Pokemon that can function despite status or have ways to cure it. The psychological effect often outweighs the practical application, as opponents may avoid using status moves entirely.

### AI Considerations
- AI Rating: 4/10 (moderate defensive value)
- AI recognizes Synchronize and may avoid using status moves
- Factors status reflection risk into move selection

### Version History
- Gen 3-4: Basic status reflection, 50% nature sync
- Gen 5+: Toxic properly reflected as bad poison
- Gen 8+: Nature synchronization increased to 100%