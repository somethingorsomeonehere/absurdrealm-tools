---
id: 485
name: Soothing Aroma
status: reviewed
character_count: 120
---

# Soothing Aroma - Ability ID 485

## In-Game Description
"Entry heals all party status if any exists."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

On entry, heals all status conditions from every Pokemon in the user's party, including both active and benched Pokemon.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Soothing Aroma provides automatic team-wide status healing upon entry, but only activates when status conditions are actually present in the party.

### Activation Conditions
- **Trigger**: Activates when entering battle
- **Requirement**: At least one party member must have a status condition
- **Scope**: Heals ALL status conditions from ALL 6 party Pokemon
- **Detection**: Checks for any STATUS1_ANY condition in the party
- **Efficiency**: Only activates when healing is actually needed

### Technical Implementation
```c
constexpr Ability SoothingAroma = {
    .onEntry = +[](ON_ENTRY) -> int {
        // Check if any party member has status conditions
        for (u8 i = 0; i < PARTY_SIZE; i++) {
            if (GetMonData(&gPlayerParty[GET_BATTLER_SIDE(battler)][i], MON_DATA_STATUS) & STATUS1_ANY) {
                BattleScriptCall(BattleScript_EffectSoothingAroma);
                return TRUE;
            }
        }
        return FALSE;
    },
};
```

### Status Conditions Healed
**All major status conditions:**
- Sleep (including sleep counters)
- Poison (regular and badly poisoned)
- Burn (damage and attack reduction)
- Freeze (immobilization)
- Paralysis (speed reduction and move failure)
- Toxic (increasing poison damage)
- Frostbite (special attack reduction)
- Bleed (HP loss over time)

**Additional effects:**
- Nightmare status removal from active battlers
- Complete status restoration for entire party

### Strategic Applications
- **Status absorber**: Switch in after status moves to heal team
- **Aromatherapy alternative**: Provides team healing without move slot
- **Emergency healing**: Instant status cure when needed most
- **Pivot utility**: Safe switching with team support benefit
- **Anti-status teams**: Hard counter to status-heavy strategies

### Comparison to Similar Effects
**vs Aromatherapy move:**
- Automatic activation vs manual use
- Entry timing vs turn investment
- Conditional activation vs guaranteed use
- No PP limitation vs 5 PP

**vs Natural Cure:**
- Team healing vs self-only
- Entry activation vs switch-out timing
- All party members vs single Pokemon

**vs Heal Bell:**
- No Soundproof immunity vs blocked by Soundproof
- Entry effect vs move usage
- Conditional vs guaranteed activation

### Team Synergy
**Excellent with:**
- Status-weak teammates: Protects valuable team members
- Pivot strategies: Enhanced switching value
- Stall teams: Removes status pressure from defensive core
- Setup sweepers: Clears status before critical setup turns
- Choice users: Removes status without switching items

### Battle Scenarios
**Early game activation:**
- Opponent uses Toxic Spikes
- Switch in Soothing Aroma user
- Entire team cured of poison
- Immediate battlefield advantage

**Mid-battle support:**
- Key Pokemon gets burned/paralyzed
- Switch to Soothing Aroma user
- Status removed from entire team
- Tactical reset without turn loss

### Limitations
- **Conditional activation**: No effect if team is healthy
- **One-time per switch**: Only triggers once per entry
- **Entry requirement**: Must actually switch in to activate
- **No prevention**: Doesn't prevent future status conditions
- **Timing dependency**: Must switch at right moment

### Counters
- **Immediate re-status**: Apply status again after healing
- **Multi-turn pressure**: Continuous status application
- **Non-status strategies**: Physical/special damage focus
- **Trap moves**: Prevent switching to activate ability
- **Speed pressure**: KO before switch opportunity

### Competitive Usage
- **Support role**: Primary function as team status cleanser
- **Defensive pivots**: Enhanced switching utility
- **Anti-meta**: Counters status-heavy team compositions
- **Emergency response**: Clutch healing in critical moments
- **Team insurance**: Safety net against status pressure

### Double Battle Applications
- **Partner protection**: Heals ally Pokemon immediately
- **Field presence**: Team-wide benefit upon entry
- **Coordination**: Enables status-weak strategies
- **Support utility**: Primary team support function

### Item Synergies
- **Leftovers**: Sustain while providing team support
- **Mental Herb**: Additional status protection
- **Chople Berry**: Survive to provide healing
- **Rocky Helmet**: Punish contact while healing team

### Move Synergies
- **U-turn/Volt Switch**: Pivot out after healing team
- **Protect**: Stall while team benefits from healing
- **Recovery moves**: Personal sustain + team status healing
- **Status moves**: Apply pressure after clearing team status

### Usage Patterns
**Reactive switching:**
- Monitor team status conditions
- Switch when healing provides maximum value
- Coordinate with team needs

**Proactive positioning:**
- Anticipate status moves
- Position for optimal switch timing
- Maximize team benefit

### Version History
- Elite Redux custom ability for enhanced team support
- Designed to provide conditional but powerful team utility
- Part of expanded support ability system
- Encourages tactical switching and team coordination