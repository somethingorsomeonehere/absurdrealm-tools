---
id: 20
name: Own Tempo
status: reviewed
character_count: 109
---

# Own Tempo - Ability ID 20

## In-Game Description
"Immune to confusion, Intimidate and Scare."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants immunity to confusion, Intimidate, and Scare. Immediately cures confusion when receiving this ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Own Tempo provides triple immunity through various battle script checks and ability flags:

### 1. Confusion Immunity

Handled through the `checktargetowntempoprotects` battle script macro:
- Groups Own Tempo with Discipline, Rock Head, and Steel Barrel
- Prevents confusion from ALL sources
- Displays ability pop-up and message when triggered

**Blocked Confusion Sources**:
- **Moves**: Confuse Ray, Supersonic, Sweet Kiss, Teeter Dance
- **Secondary Effects**: Confusion from Water Pulse, Psybeam, etc.
- **Swagger**: Blocks confusion but attack boost still applies
- **Attract**: Listed in some battle scripts suggesting possible interaction
- **Self-Inflicted**: Prevents Outrage/Petal Dance confusion

**Battle Message**: "Pokemon prevents confusion with [Own Tempo]!"

### 2. Intimidate Immunity

According to the ability description, Own Tempo blocks Intimidate:
- Prevents Attack reduction when opponent switches in with Intimidate
- Part of Elite Redux's expanded Own Tempo functionality
- Maintains offensive pressure against Intimidate users

### 3. Scared Status Immunity

Protects against the custom "Scared" status effect:
- Scared is tracked via `RESOURCE_FLAG_SCARED` in battle resources
- Appears to be a custom Elite Redux status condition
- Found in battle structure as `scaredMon`
- Own Tempo users cannot be inflicted with this status

### Ability Properties
- **AI Rating**: 3 (moderate value)
- Works both defensively and preemptively
- Cannot be temporarily suppressed during battle

### Strategic Implications

**Offensive Benefits**:
- Maintains setup against Intimidate leads
- Can use Swagger on allies safely (if doubles)
- No Outrage/Petal Dance drawback

**Defensive Benefits**:
- Immune to confusion disruption strategies
- Counters Swagger + Thunder Wave combos
- Reliable against RNG confusion

**Unique Elite Redux Features**:
- Scared status immunity (custom mechanic)
- Intimidate blocking (expanded from originals)

### Technical Implementation
- Confusion immunity via battle script macros
- Multiple script checks for different confusion sources
- Grouped with other confusion-preventing abilities
- Custom status immunities added for Elite Redux

### Pokemon with Own Tempo
Many Pokemon have access to Own Tempo as a changeable ability option in Elite Redux, significantly more than in the original games.

### Competitive Usage Notes

**Team Roles**:
- Setup sweepers that use Outrage/Petal Dance
- Physical attackers countering Intimidate
- Defensive pivots immune to disruption

**Key Advantages**:
- Enables safe Outrage/Thrash spam
- Counters confusion + paralysis strategies  
- Maintains momentum against Intimidate

**Limitations**:
- No direct offensive boost
- Other status conditions work normally
- Doesn't prevent other stat drops

### Interactions

1. **With Swagger**:
   - Receives Attack boost
   - Immune to confusion
   - Can benefit from ally Swagger in doubles

2. **With Intimidate**:
   - Completely blocks Attack reduction
   - Maintains offensive pressure

3. **With Multi-Turn Moves**:
   - Outrage/Petal Dance/Thrash have no drawback
   - Can be used consecutively without risk

### Counters
- Direct status moves (paralysis, burn, sleep)
- Stat reduction moves besides Intimidate
- Raw offensive pressure
- Ability suppression

### Synergies
- Outrage users gain consistent damage
- Physical attackers bypass Intimidate
- Teams that struggle with confusion
- Pairs well with other status immunities

### Version History
Elite Redux significantly expanded Own Tempo:
- **Original**: Only prevented confusion
- **Elite Redux**: Added Intimidate and Scared immunity

This makes Own Tempo a versatile ability providing multiple forms of disruption immunity, particularly valuable in Elite Redux's expanded status effect environment.