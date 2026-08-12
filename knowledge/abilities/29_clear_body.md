---
id: 29
name: Clear Body
status: reviewed
character_count: 114
---

# Clear Body - Ability ID 29

## In-Game Description
"Immune to stat drops."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gives immunity to all stat reductions from moves and abilities. Includes self stat drops from moves like Overheat.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Clear Body provides complete immunity to stat reductions caused by opposing Pokemon. This includes direct stat-lowering moves, secondary effects of attacks, and ability-based stat drops.

### Technical Implementation
Protection is checked in `battle_script_commands.c` (lines 4046-4054):
- Clear Body is checked alongside similar protective abilities
- Prevents stat changes before they're applied
- Works identically to Full Metal Body (but Full Metal Body is unbreakable)

### What Clear Body Prevents

**Blocked effects:**
1. **Direct stat-lowering moves**: Growl, Leer, Screech, etc.
2. **Secondary effects**: Shadow Ball's SpDef drop, Psychic's SpDef drop
3. **Ability-based drops**: 
   - All Intimidate variants (Intimidate, Scare, Fearmonger, Yuki-Onna, Monkey Business, Malicious, Terrify, Petrify)
   - Other stat-lowering abilities

**NOT blocked:**
- Self-inflicted stat drops (Close Combat, Superpower, Draco Meteor)
- Stat drops with STAT_CHANGE_CANT_PREVENT flag
- Stat resets (Haze, Clear Smog)
- Stat swaps or power splits

### Ability Properties
- **Breakable**: TRUE (can be suppressed by Mold Breaker)
- **AI awareness**: AI reduces score for stat-lowering moves by 10 points

### Pokemon with Clear Body

**Innate ability (always active):**
- Tentacool/Tentacruel
- Flygon
- Deoxys (all forms)
- Cofagrigus  
- Carbink

**Changeable ability:**
- Flygon (can have as both innate and changeable)
- Darmanitan (Zen Mode)
- Frillish/Jellicent
- Shelmet
- Nihilego
- Magearna (both forms)
- Stonjourner
- Dreepy/Drakloak/Dragapult
- Bariong

### Strategic Implications

**Advantages:**
- **Intimidate immunity**: Crucial in formats with common Intimidate
- **Setup protection**: Can boost stats without fear of being lowered
- **Consistent stats**: Maintains offensive/defensive capabilities
- **Mind games**: Opponents waste turns trying stat-lowering moves

**Limitations:**
- No protection against self-inflicted drops
- Can be bypassed by Mold Breaker
- Doesn't prevent positive stat changes
- No effect on critical hit mechanics

### Similar Abilities
- **Full Metal Body**: Identical but unbreakable (Mold Breaker can't bypass)
- **White Smoke**: Identical to Clear Body  
- **Keen Eye**: Only prevents accuracy drops
- **Minds Eye**: Prevents accuracy drops + ignores evasion
- **Lucky Halo**: Prevents stat drops when ability affects user

### Synergies
- **Setup moves**: Safely use Dragon Dance, Swords Dance, etc.
- **Physical attackers**: No Intimidate weakness
- **Hyper offense**: Maintain momentum without stat drops
- **Contrary**: Different approach - turns drops into boosts

### Counters
- Mold Breaker and variants
- Status conditions (not prevented)
- Direct damage (ignores stat protection)
- Haze/Clear Smog (reset stats entirely)
- Power/Guard Split (equalize stats)

### Competitive Usage Notes
Clear Body is highly valued in competitive play, especially in formats where Intimidate is common. It enables consistent performance from setup sweepers and physical attackers. The ability to ignore the omnipresent Intimidate alone makes it worthwhile. Particularly effective on offensive Pokemon that can't afford stat drops.

### AI Behavior
- Recognizes Clear Body and avoids stat-lowering moves
- Score adjustment: -10 points for stat-lowering moves
- Still considers moves with additional effects beyond stat drops

### Version History
Clear Body has remained mechanically consistent since its introduction. The main changes have been clarifications on what it does and doesn't block, and the introduction of similar abilities like Full Metal Body that provide unbreakable versions of the same effect.