---
id: 758
name: Bruteforce
status: reviewed
character_count: 278
---

# Bruteforce - Ability ID 758

## In-Game Description
"Combines Reckless and Rock Head effects."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the damage of moves that cause recoil by 20%. While enraged, this boost applies to all moves. Prevents all recoil damage from the user's moves and abilities. Also grants immunity to enrage recoil damage. Does not prevent crash damage or Explosion/Self-Destruct damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

Bruteforce is a powerful hybrid ability that combines the offensive capabilities of Reckless with the protective aspects of Rock Head, creating an ideal ability for aggressive physical attackers.

### Core Mechanics

**Reckless Component (Offensive Multiplier):**
```cpp
.onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
    if (gBattleMoves[move].flags & FLAG_RECKLESS_BOOST) MUL(1.2);
}
```
- Provides a 20% damage boost to moves with the FLAG_RECKLESS_BOOST flag
- Applies before other damage calculations

**Rock Head Component (Status Immunity + Recoil Prevention):**
```cpp
.onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
    CHECK(status & CHECK_CONFUSION)
    return TRUE;
},
.noRecoil = TRUE,
.removesStatusOnImmunity = TRUE,
```

### Affected Moves (FLAG_RECKLESS_BOOST)

Bruteforce provides a 20% damage boost to the following recoil moves:
- **Jump Kick** - High-power Fighting-type move with crash damage risk
- **High Jump Kick** - Higher power version of Jump Kick
- **Double-Edge** - High-power Normal-type move with 1/3 recoil
- **Submission** - Fighting-type move with 1/4 recoil
- **Volt Tackle** - Electric-type signature move with 1/3 recoil
- **Head Smash** - Rock-type move with 1/2 recoil
- **Wood Hammer** - Grass-type move with 1/3 recoil
- **Flare Blitz** - Fire-type move with 1/3 recoil
- **Brave Bird** - Flying-type move with 1/3 recoil
- **Wild Charge** - Electric-type move with 1/4 recoil
- **Take Down** - Normal-type move with 1/4 recoil

### Activation Conditions

1. **Damage Boost**: Automatically applies when using any move with FLAG_RECKLESS_BOOST
2. **Recoil Prevention**: Prevents ALL recoil damage from any source
3. **Confusion Immunity**: Blocks confusion status from any source
4. **Status Removal**: Removes existing confusion when the immunity would trigger

### Technical Implementation

The ability inherits its components from existing abilities:
- `Reckless.onOffensiveMultiplier` for the 20% damage boost
- `RockHead.onStatusImmune` for confusion immunity
- `noRecoil = TRUE` prevents all recoil damage
- `removesStatusOnImmunity = TRUE` clears confusion when blocked

### Damage Calculations

**Example with Double-Edge (120 BP):**
- Base damage: 120 BP
- With Bruteforce: 120 x 1.2 = 144 effective BP
- Normal recoil: 1/3 of damage dealt = 0 (prevented by Rock Head component)
- Net result: 20% more damage with no drawback

**Example with High Jump Kick (130 BP):**
- Base damage: 130 BP  
- With Bruteforce: 130 x 1.2 = 156 effective BP
- Miss crash damage: 0 (prevented by Rock Head component)
- Net result: Massive damage boost with safety net

### Strategic Implications

**Offensive Advantages:**
- Transforms risky recoil moves into safe, high-power options
- 20% damage boost makes recoil moves competitively viable
- Enables hit-and-run strategies without health loss
- Perfect for Choice Band/Life Orb sets

**Defensive Advantages:**
- Confusion immunity prevents self-damage and loss of control
- No recoil means sustained offensive pressure
- Removes need for healing support in many cases

### Common Users

**Mega Emboar** (Primary User):
- Type: Fire/Fighting
- Stats: 110/148/137/70/90/80
- Innate ability alongside Hellblaze and Violent Rush
- Perfect synergy with signature moves like Flare Blitz
- Benefits from Fighting-type recoil moves like High Jump Kick

### Competitive Usage Notes

**Tier Placement**: Extremely powerful for physical attackers
**Usage Rate**: High on Pokemon with access to multiple recoil moves
**Common Sets**: 
- Choice Band for maximum immediate power
- Life Orb for flexibility without recoil stacking
- Assault Vest for special bulk while maintaining offense

### Counters and Weaknesses

**Direct Counters:**
- **Physical walls** with high Defense stats
- **Burn status** to cripple physical attacks
- **Intimidate** users to reduce Attack stat
- **Will-O-Wisp** and other burn-inducing moves

**Indirect Counters:**
- **Priority moves** to revenge kill after setup
- **Residual damage** (Stealth Rock, Spikes, weather)
- **Status moves** other than confusion
- **Speed control** to outpace and KO

### Synergies

**Item Synergies:**
- **Choice Band**: Massive immediate power without recoil drawback
- **Life Orb**: Extra damage boost, recoil prevention stacks well
- **Leftovers**: Passive recovery to offset other damage sources

**Team Synergies:**
- **Entry hazard support**: Forces switches to get KOs
- **Speed control**: Trick Room or Thunder Wave support
- **Healing support**: Wish passing for longevity
- **Status clerics**: For non-confusion status conditions

**Move Synergies:**
- **Setup moves**: Swords Dance, Bulk Up before sweeping
- **Coverage moves**: Non-recoil moves for type coverage
- **Priority moves**: Mach Punch, Quick Attack for revenge kills

### Version History

**Elite Redux Implementation**: 
- Added as part of the extended ability system
- Designed specifically for Mega Emboar's offensive role
- Balances high-risk moves with protective benefits
- Code implementation uses inheritance from Reckless and Rock Head

### Interaction Notes

**Does NOT stack with:**
- Other Reckless-type abilities (if somehow obtained)
- Other recoil prevention abilities

**DOES stack with:**
- Life Orb damage boost (applied after Bruteforce boost)
- STAB (Same Type Attack Bonus)
- Type effectiveness multipliers
- Weather damage boosts (sun for Fire moves, etc.)

**Special Interactions:**
- Jump Kick/High Jump Kick crash damage completely prevented
- Confusion from Outrage/Thrash/Petal Dance blocked
- Self-inflicted confusion from berries prevented
- Confusion from moves like Dynamic Punch blocked

This ability represents the pinnacle of offensive ability design, removing the traditional risk-reward balance of recoil moves while providing additional utility through status immunity.