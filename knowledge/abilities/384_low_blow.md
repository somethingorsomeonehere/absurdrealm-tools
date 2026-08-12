---
id: 384
name: Low Blow
status: reviewed
character_count: 145
---

# Low Blow - Ability ID 384

## In-Game Description
"Attacks with 40BP Feint Attack on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Low Blow uses a 40 BP Feint Attack when switching in, targeting a random opponent. Feint Attack is a Dark-type physical attack that never misses.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Low Blow is an aggressive entry ability that automatically uses a modified version of Feint Attack when the Pokemon switches into battle, forcing immediate offensive pressure with guaranteed chip damage.

### Activation Conditions
- **Trigger**: Activates immediately upon switching into battle
- **Target selection**: Targets a random opponent in battle
- **Move properties**: Uses Feint Attack with 40 BP instead of normal 80 BP
- **Type**: Dark-type physical attack
- **Accuracy**: Cannot miss (Feint Attack's inherent property)

### Technical Implementation
```c
constexpr Ability LowBlow = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_FEINT_ATTACK, 40); 
    },
};
```

The ability uses the `UseEntryMove` function to execute Feint Attack with reduced power on switch-in.

### Feint Attack Mechanics
Based on the move's implementation:
- **Never misses**: Bypasses all accuracy and evasion modifications
- **Physical attack**: Uses user's Attack stat and target's Defense stat
- **Contact move**: Makes contact for abilities like Static, Flame Body
- **Dark-type**: Benefits from STAB on Dark-type users
- **Power**: Reduced from 80 BP to 40 BP for balance

### Important Interactions
- **STAB bonus**: Dark-type users get 1.5x damage (40 BP becomes 60 effective BP)
- **Guaranteed hit**: Cannot be avoided by evasion boosts or accuracy drops
- **Multi-target**: In doubles, targets one random opponent
- **Priority**: No priority; uses standard switch-in timing
- **Type effectiveness**: Subject to normal type chart (resisted by Fighting, Dark, Fairy)

### Strategic Implications
- **Guaranteed damage**: Forces chip damage on every switch-in
- **Focus Sash breaker**: 40 BP is sufficient to break Focus Sash items
- **Sturdy breaker**: Can break Sturdy ability to enable KOs
- **Entry hazard synergy**: Combines with Stealth Rock/Spikes for cumulative damage
- **Pivot strategy**: Works excellently with U-turn/Volt Switch users
- **Mind games**: Forces opponents to consider switching costs

### Defensive Counterplay
- **Type resistance**: Fighting, Dark, and Fairy types resist Dark attacks
- **Steel immunity**: Steel types are immune to Dark-type moves in some contexts
- **Protect/Detect**: Can block the entry move if predicted correctly
- **Intimidate**: Reduces incoming damage by lowering Attack stat
- **Rocky Helmet**: Deals contact damage back to the user
- **Rough Skin/Iron Barbs**: Punishes the contact move with recoil

### Common Users
Based on the ability implementation, this is typically found on:
- Dark-type Pokemon with sneaky or underhanded themes
- Pokemon with decent Attack stats to maximize damage potential
- Pivot Pokemon designed to switch in and out frequently
- Pokemon built for disrupting opponent's strategies

### Competitive Usage Notes
- **Chip damage tool**: Provides consistent damage output on switches
- **Hazard complement**: Works well with entry hazards for KO setups
- **Pivot support**: Excellent on U-turn/Volt Switch users
- **Anti-setup**: Discourages opponent setup by forcing immediate damage
- **Sash breaking**: Counters Focus Sash strategies effectively
- **Double battles**: Random targeting can disrupt opponent positioning

### Synergies
- **Life Orb**: Boosts the entry move damage significantly (40 BP to 52 BP)
- **Choice Band**: Increases damage output with Attack boost
- **Entry hazards**: Stealth Rock + Low Blow creates immediate pressure
- **Pivot moves**: U-turn/Volt Switch after dealing entry damage
- **Speed control**: Works well with Thunder Wave or other speed control
- **Knock Off**: Follows up by removing opponent's items

### Counters
- **Type resistance**: Fighting/Dark/Fairy types take reduced damage
- **Protective moves**: Protect, Detect, Spiky Shield block the move
- **High Defense**: Physically defensive Pokemon minimize damage
- **Contact punishment**: Static, Flame Body, Effect Spore abilities
- **Aftermath**: Can KO the user if Low Blow brings opponent to 1 HP
- **Rocky Helmet/Rough Skin**: Punishes contact with recoil damage

### Comparison to Similar Abilities
- **vs. Phantom Thief**: Low Blow focuses on damage, Phantom Thief steals stats
- **vs. Entry hazards**: Guaranteed single-target damage vs. team-wide pressure
- **vs. Intimidate**: Offensive pressure vs. defensive stat reduction
- **vs. Weather abilities**: Immediate damage vs. field condition setup

### Tier Assessment
**Tier: B+**
- Reliable and consistent effect that always provides value
- Good utility for breaking defensive items and abilities
- Excellent on pivot Pokemon and offensive teams
- Not overpowered due to moderate damage and resistances
- Solid choice for aggressive team compositions

### Version History
- Elite Redux custom ability (ID 384)
- Part of the expanded ability roster beyond Generation VIII
- Uses existing Feint Attack mechanics with entry trigger
- Reduced power from 80 BP to 40 BP balances automatic activation

### Technical Notes
- Uses MOVE_FEINT_ATTACK (ID 185) with modified 40 BP
- Triggers through onEntry ability hook in the battle engine
- Benefits from all normal move mechanics (STAB, items, type effectiveness)
- Subject to standard battle mechanics and damage calculation formulas
- Cannot miss property is inherent to Feint Attack itself