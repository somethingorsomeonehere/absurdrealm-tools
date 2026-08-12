---
id: 488
name: Tipping Point
status: reviewed
character_count: 129
---

# Tipping Point - Ability ID 488

## In-Game Description
"Hit by attacks raises Special Attack by 1, or maximizes on critical hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit, raises the user's Special Attack by 1 stage or maximizes it on critical hits. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Tipping Point turns defensive vulnerability into offensive opportunity, with critical hits providing explosive setup potential that can instantly transform the Pokemon into a special sweeping threat.

### Activation Conditions
- **Trigger**: When hit by any damaging move
- **Requirements**: Move must hit and deal damage
- **Stat check**: Special Attack must be able to increase
- **Critical hit bonus**: Instantly maximizes Special Attack to +6 stages
- **Normal hit**: Raises Special Attack by 1 stage only

### Technical Implementation
```c
constexpr Ability TippingPoint = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(CanRaiseStat(battler, STAT_SPATK))
        
        if (gIsCriticalHit) {
            SetStatChanger(STAT_SPATK, 12);  // +6 stages (max)
            BattleScriptCall(BattleScript_TargetsStatWasMaxedOut);
        } else {
            SetStatChanger(STAT_SPATK, 1);   // +1 stage
            BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        }
        return TRUE;
    },
};
```

### Critical Hit Mechanics
**Normal critical hits:**
- 1/24 chance for most moves (4.17%)
- High critical ratio moves: 1/8 chance (12.5%)
- Critical hit items: Scope Lens, Razor Claw increase odds
- Focus Energy: Guarantees critical hits

**Critical hit interaction:**
- **Instant setup**: +6 Special Attack in one hit
- **Maximum power**: 4x special attack multiplier immediately
- **Game changer**: Can turn losing positions into sweeping opportunities

### Special Attack Stage Benefits
- **+1 stage**: 1.5x special attack (50% increase)
- **+2 stages**: 2x special attack (100% increase)
- **+3 stages**: 2.5x special attack (150% increase)
- **+4 stages**: 3x special attack (200% increase)
- **+5 stages**: 3.5x special attack (250% increase)
- **+6 stages**: 4x special attack (300% increase)

### Strategic Applications
- **Tank and sweep**: Take hits to build up, then sweep
- **Critical hit fishing**: Use moves with high crit rates
- **Revenge sweeper**: Turn opponent's offense into your setup
- **Special tank**: High special bulk enables safe setup
- **Momentum swing**: Transform defensive situations into offense

### Critical Hit Synergies
**Critical hit boosters:**
- Focus Energy: Guarantees critical hits for max setup
- Scope Lens: +1 critical hit stage
- Razor Claw: +1 critical hit stage
- Super Luck ability: +1 critical hit stage

**High critical ratio moves:**
- Slash, Night Slash: 1/8 crit chance naturally
- Psycho Cut, Air Cutter: Psychic/Flying coverage with crit
- Crabhammer, Karate Chop: Physical moves that can crit

### Defensive Setup Strategy
**Optimal setup conditions:**
- Switch into resisted/weak attacks
- Use protective moves while taking hits
- Tank physical hits with high Defense
- Accumulate boosts through repeated hits

### Risk-Reward Gameplay
**High-risk scenarios:**
- Staying in against powerful attackers
- Fishing for critical hits from opponents
- Taking unnecessary damage for setup

**High-reward potential:**
- Instant max Special Attack from one crit
- Sweeping potential after accumulating boosts
- Turning defense into overwhelming offense

### Competitive Usage
- **Special sweepers**: Excellent on Pokemon with diverse special movesets
- **Bulky setup**: Pairs with high HP/Defense for survival
- **Anti-physical**: Punishes physical attackers specifically
- **Momentum control**: Can shift battle flow dramatically
- **Crit fishing**: Rewards high-crit strategies

### Move Synergies
**Special attacks:**
- High-power specials: Psychic, Thunderbolt, Flamethrower
- Coverage moves: Hidden Power, Focus Blast
- Priority specials: Vacuum Wave for revenge killing

**Support moves:**
- Substitute: Block status while taking damage
- Recover: Heal while maintaining boosts
- Protect: Stall and force opponent attacks

### Item Synergies
**Defensive items:**
- Leftovers: Sustain while taking hits
- Sitrus Berry: Heal during setup phase
- Focus Sash: Survive to get guaranteed boost

**Offensive items:**
- Life Orb: Amplify boosted special attacks
- Choice Specs: Stack with ability boosts
- Expert Belt: Boost super-effective coverage

### Counters
- **Status moves**: Don't trigger ability, inflict status
- **Taunt**: Prevents recovery/setup moves
- **Haze/Clear Smog**: Reset accumulated boosts
- **Critical hit immunity**: Some abilities prevent crits
- **Substitute**: User can block hits safely

### Double Battle Applications
- **Spread moves**: Multiple hits can trigger multiple boosts
- **Partner support**: Ally can trigger boosts safely
- **Redirection**: Use redirection to control when ability triggers
- **Protection**: Protect user while building boosts

### Advanced Tactics
**Critical hit manipulation:**
- Focus Energy + high-crit moves
- Critical hit rate stacking
- Opponent crit fishing strategies

**Boost preservation:**
- Baton Pass to transfer boosts
- U-turn/Volt Switch timing
- Strategic switching to maintain boosts

### Limitations
- **Damage requirement**: Must actually take hits to benefit
- **Special Attack only**: Doesn't help physical attacks
- **Critical hit dependency**: Best effects require crits
- **Stat cap**: Cannot exceed +6 Special Attack
- **Fragility**: Taking hits can lead to fainting

### Team Building
**Ideal team support:**
- Entry hazard control: Keep user healthy
- Healing support: Heal between setup sessions
- Physical walls: Redirect physical attacks away
- Redirection users: Control when ability triggers

### Version History
- Elite Redux custom ability for dynamic special setup
- Designed to reward defensive play with offensive potential
- Part of expanded risk-reward ability design
- Creates unique critical hit interaction gameplay