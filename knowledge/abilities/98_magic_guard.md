---
id: 98
name: Magic Guard
status: reviewed
character_count: 120
---

# Magic Guard - Ability ID 98

## In-Game Description
Only damaged by attacks.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants immunity to all non-attack damage sources including entry hazards, weather damage, status conditions, and recoil.

## Detailed Mechanical Explanation

### Basic Information
- **Ability ID**: ABILITY_MAGIC_GUARD (98)
- **Name**: Magic Guard
- **Category**: Damage Prevention
- **Introduced**: Generation IV

### Detailed Effects

### What Magic Guard Prevents
1. **Entry Hazard Damage**
   - Stealth Rock damage
   - Spikes damage
   - All other entry hazards

2. **Weather Damage**
   - Sandstorm damage
   - Hail damage

3. **Status Condition Damage**
   - Poison damage (both in battle and in the field)
   - Burn damage (but still receives Attack reduction)
   - Bad poison (Toxic) damage
   - Curse damage (when used by Ghost-type)

4. **Recoil Damage**
   - Move recoil (Head Smash, Brave Bird, etc.)
   - Struggle recoil
   - Life Orb recoil
   - Other item-based recoil

5. **Other Indirect Damage**
   - Leech Seed damage
   - Nightmare damage
   - Flame Burst splash damage to allies
   - Trap move damage (Bind, Wrap, etc.)
   - Rocky Helmet/Rough Skin/Iron Barbs damage

### What Magic Guard Does NOT Prevent
- Direct damage from attacks
- Stat reductions from burn/paralysis
- Other status condition effects (sleep, freeze, paralysis speed reduction)
- Perish Song KO
- Pain Split damage
- Substitute creation HP cost

## Implementation Details

### Code Structure
- Defined in `src/abilities.cc` with the `magicGuard = TRUE` flag
- Protection checked via `IsMagicGuardProtected()` function throughout the battle engine
- Field poison immunity handled in `src/field_poison.c`

### Abilities with Magic Guard Effect
The following abilities share the `magicGuard = TRUE` property:
1. **Magic Guard** - The original ability
2. **Impenetrable** - Elite Redux custom ability with additional effects
3. **Apple Enlightenment** - Elite Redux custom ability
4. **Conjurer of Deceit** - Elite Redux custom ability
5. **Immovable Object** - Elite Redux custom ability

### Key Code Locations
- Ability definition: `src/abilities.cc:1228`
- Field poison check: `src/field_poison.c:136-137`
- Entry hazard checks: `src/battle_script_commands.c`
- Recoil prevention: `src/battle_script_commands.c`
- AI evaluation: `src/battle_ai_util.c` (Rating: 9/10)

## Strategic Implications

### Offensive Benefits
- **Recoil Move Usage**: Can freely use powerful recoil moves like Head Smash without taking damage
- **Life Orb Synergy**: Gets 30% damage boost from Life Orb with no HP loss
- **Reckless Strategy**: Can ignore self-damaging aspects of moves

### Defensive Benefits
- **Hazard Immunity**: Can switch in repeatedly without taking Stealth Rock/Spikes damage
- **Weather Team Counter**: Immune to Sandstorm/Hail chip damage
- **Status Absorber**: Can take Toxic/Will-O-Wisp without taking damage over time

### Common Pokemon with Magic Guard
- Alakazam line
- Clefable line
- Reuniclus line
- Sigilyph

## Competitive Usage

### Common Sets
1. **Life Orb Sweeper**: Maximizes damage output without drawbacks
2. **Hazard Immune Pivot**: Switches in freely on hazards
3. **Status Absorber**: Takes status moves without long-term damage
4. **Calm Mind Setup**: Sets up without fear of chip damage

### Counters and Limitations
- Still vulnerable to direct attacks
- Doesn't prevent status condition effects (paralysis speed drop, burn attack drop)
- Can still be phazed or forced out
- Taunt can prevent setup strategies

## Interactions with Other Mechanics

### Positive Interactions
- **Life Orb**: Full benefit with no drawback
- **Flame Orb/Toxic Orb**: Can activate other abilities without taking damage
- **Sticky Barb**: No damage from holding
- **Black Sludge on non-Poison types**: No damage taken

### Notable Synergies
- **Trick Room**: Many Magic Guard users have low Speed
- **Cosmic Power**: Can boost defenses without chip damage concerns
- **Recover/Moonlight**: Only needs to heal direct damage

## Notes
- In Elite Redux, multiple custom abilities share the Magic Guard effect, providing similar protection with additional benefits
- The AI highly values this ability (9/10 rating) due to its powerful defensive properties
- Field poison damage is also prevented, making overworld traversal safer