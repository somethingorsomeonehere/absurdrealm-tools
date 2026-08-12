---
id: 468
name: Super Hot Goo
status: reviewed
character_count: 132
---

# Super Hot Goo - Ability ID 468

## In-Game Description
"Inflicts burn and lowers Speed on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact moves have a 30% chance to inflict burn and the user lowers the attacker's Speed by one stage when receiving a contact move. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Super Hot Goo is a hybrid defensive ability that combines the effects of two existing abilities: Flame Body and Gooey. When a Pokemon with Super Hot Goo is hit by a contact move, both effects trigger independently.

### Activation Conditions
- **Contact requirement**: Only triggers when hit by moves that make contact
- **Health requirement**: User must not faint from the attack
- **No status immunity bypass**: Burn effect respects normal burn immunity

### Effect Components

#### Flame Body Component
- **Burn chance**: 30% probability to inflict burn status on the attacker
- **Burn damage**: Burned Pokemon takes 1/16 of maximum HP damage each turn
- **Status precedence**: Cannot burn already-statused Pokemon (except in certain cases)
- **Fire immunity**: Fire-type Pokemon cannot be burned

#### Gooey Component  
- **Speed reduction**: Always lowers attacker's Speed by 1 stage
- **Guaranteed activation**: Unlike burn, speed reduction always occurs
- **Safeguard bypass**: Explicitly ignores Safeguard protection
- **Mirror Armor interaction**: Can trigger Mirror Armor to redirect the stat reduction

### Technical Implementation
```c
constexpr Ability SuperHotGoo = {
    .onAttacker = FlameBody.onAttacker,  // 30% burn chance
    .onDefender = +[](ON_DEFENDER) -> int { 
        return Gooey.onDefender(DELEGATE_DEFENDER) | FlameBody.onDefender(DELEGATE_DEFENDER); 
    },
};
```

### Activation Sequence
1. Pokemon with Super Hot Goo is hit by contact move
2. Both Flame Body and Gooey effects check activation conditions
3. Flame Body: 30% chance roll for burn infliction
4. Gooey: Speed reduction always applies (if stat can be lowered)
5. Battle messages display for any successful effects

### Important Interactions

#### Status Conditions
- **Burn immunity**: Fire types, already-burned Pokemon, and status immune Pokemon avoid burn
- **Lum Berry**: Can cure burn immediately after infliction
- **Guts/Marvel Scale**: Benefit from burn status if inflicted
- **Status absorption**: Does not trigger on status-immune abilities like Limber

#### Stat Changes
- **Clear Body/White Smoke**: Blocks speed reduction component
- **Mirror Armor**: Can reflect speed reduction back to user
- **Contrary**: Converts speed reduction to speed boost for attacker
- **Competitive/Defiant**: Triggers from speed reduction

#### Battle Mechanics
- **Substitute**: Prevents both effects when attacker is behind Substitute
- **Magic Guard**: Prevents burn damage but not burn status
- **Multi-hit moves**: Each hit can trigger effects independently
- **Mold Breaker**: Does not bypass Super Hot Goo (ability is not breakable)

### Strategic Applications

#### Defensive Usage
- **Physical wall support**: Punishes physical attackers heavily
- **Speed control**: Slows down physical sweepers attempting setup
- **Status spreading**: Burn cripples physical attackers long-term
- **Switch punishment**: Deters contact move users from switching in

#### Team Synergy
- **Trick Room**: Benefits from opposing speed reduction
- **Toxic Spikes**: Combines with burn for passive damage
- **Will-O-Wisp**: Redundant with burn effect but provides backup
- **Thunder Wave**: Can layer with speed reduction for full paralysis

### Counters and Limitations

#### Direct Counters
- **Special attackers**: Avoid contact entirely
- **Fire types**: Immune to burn component
- **Clear Body/White Smoke**: Blocks speed reduction
- **Magic Bounce**: Can reflect status moves back
- **Lum Berry**: Removes burn status immediately

#### Indirect Counters
- **Long-range attacks**: Projectile and ranged moves avoid contact
- **Status immunity**: Safeguard teams (though speed reduction bypasses)
- **Heal Bell/Aromatherapy**: Team-wide status cure removes burn
- **Natural Cure**: Switches out to cure burn status

### Competitive Viability

#### Strengths
- **Dual punishment**: Both immediate and long-term consequences
- **No immunity overlap**: Few Pokemon resist both effects completely  
- **Passive damage**: Burn provides consistent chip damage
- **Speed control**: Immediate impact on opponent's action economy

#### Weaknesses
- **Special attack vulnerability**: No protection against special moves
- **RNG dependent**: Burn effect relies on 30% probability
- **Status cure availability**: Burn can be easily removed
- **Limited users**: Typically found on slower, defensive Pokemon

### Common Users Profile
- **Type preference**: Often found on Fire/Steel, Fire/Rock, or similar defensive types
- **Role in team**: Tank, physical wall, or slow pivot
- **Stat distribution**: High HP and Defense, lower Speed
- **Move synergy**: Recovery moves, status moves, defensive utilities

### Version History
- **Elite Redux exclusive**: Custom ability combining existing mechanics
- **Implementation**: Uses delegate pattern to combine Flame Body + Gooey
- **Balance considerations**: Provides strong physical deterrent without being oppressive

### Related Abilities
- **Flame Body**: Provides the burn component (30% on contact)
- **Gooey**: Provides the speed reduction component
- **Static**: Similar contact-based status infliction (paralysis)
- **Poison Point**: Similar contact-based status infliction (poison)
- **Rough Skin**: Contact damage but no status effects