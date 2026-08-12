---
id: 427
name: Cheating Death
status: reviewed
character_count: 122
---

# Cheating Death - Ability ID 427

## In-Game Description
"Gets no damage for the first two hits."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Negates the first two instances of damage received. Moves still connect and secondary effects apply, but damage becomes 0.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Cheating Death is a defensive ability that provides complete damage immunity for exactly 2 hits per battle. Unlike immunity abilities, the moves still connect and can trigger secondary effects - only the damage is negated.

### Activation Conditions
- **Hit counter**: Blocks damage for the first 2 hits received in battle
- **Damage type requirement**: Only blocks direct attack damage
- **Persistence**: Counter persists across switches (`.persistent = TRUE`)
- **Per-Pokemon basis**: Each Pokemon has its own 2-hit counter

### Technical Implementation
```cpp
// Cheating Death ability definition in abilities.cc
constexpr Ability CheatingDeath = {
    .onEntry = +[](ON_ENTRY) -> int {
        int uses = 2 - GetSingleUseAbilityCounter(battler, ability);
        CHECK(uses)

        if (uses == 1)
            BattleScriptPushCursorAndCallback(BattleScript_BattlerHasASingleNoDamageHit);
        else if (uses > 1) {
            ConvertIntToDecimalStringN(gBattleTextBuff4, uses, STR_CONV_MODE_LEFT_ALIGN, 2);
            BattleScriptPushCursorAndCallback(BattleScript_BattlerHasNoDamageHits);
        }
        return TRUE;
    },
    .noDamageHits = 2,
    .persistent = TRUE,
};
```

### Damage Blocking Logic
```cpp
// In battle_script_commands.c - Cmd_datahpupdate()
else if (gBattleMoveDamage > 0 && !(gHitMarker & HITMARKER_PASSIVE_DAMAGE) && RemainingNoDamageHits(gActiveBattler) > 0) {
    IncrementSingleUseAbilityCounter(gActiveBattler, GetNoDamageAbility(gActiveBattler), 1);
    if (RemainingNoDamageHits(gActiveBattler) <= 0) {
        BattleScriptCall(BattleScript_BattlerCanNoLongerEndureHits);
    }
}
```

### Important Interactions
- **Move still connects**: Accuracy checks pass, contact effects trigger
- **Secondary effects can still occur**: Status conditions, stat changes, etc. can still happen
- **No "immune" message**: Shows hit animation but 0 damage
- **Works against all physical damage**: Not type-specific like immunities
- **Cannot be suppressed**: No `.breakable = TRUE` flag
- **Counter system**: Uses `GetSingleUseAbilityCounter()` for tracking

### What Gets Blocked
- ✅ **Direct attack damage**: All damaging moves
- ✅ **Multi-hit moves**: Each hit decrements counter
- ✅ **Critical hits**: Damage still becomes 0
- ✅ **STAB/type effectiveness**: Damage modifiers irrelevant

### What Doesn't Get Blocked
- ❌ **Passive damage**: Poison, burn, weather damage
- ❌ **Entry hazards**: Stealth Rock, Spikes, etc.
- ❌ **Non-damaging moves**: Status moves, stat changes
- ❌ **Recoil damage**: Self-inflicted damage
- ❌ **Confusion/attraction damage**: Self-harm

### Entry Messages
- **When entering with 2 hits remaining**: "X has N no damage hits!" 
- **When entering with 1 hit remaining**: "X has a single no damage hit!"
- **When the last hit is used**: "X can no longer endure hits!"

### Strategic Implications
- **Guaranteed protection**: Provides 2 turns of damage immunity
- **Secondary effects vulnerability**: Still susceptible to status, stat drops
- **Switch value**: Counter persists, making switches tactical
- **Priority moves**: No special interaction - still blocked if damaging
- **One-time use**: Once depleted, ability provides no further benefit

### Competitive Usage Notes
- **Lead potential**: Excellent for setting up or absorbing hits early
- **Pivot protection**: Safe switching with guaranteed damage absorption
- **Setup enabler**: Two free turns to boost stats or set up
- **Endgame insurance**: Can tank crucial hits in close matches
- **Multi-hit vulnerability**: Abilities like Skill Link can deplete quickly

### Counters
- **Status moves**: Inflict conditions without using hit counter
- **Multi-hit moves**: Deplete counter faster than single hits
- **Entry hazards**: Bypass the ability entirely
- **Passive damage**: Weather, abilities don't trigger counter
- **Non-damaging harassment**: Taunt, disable, etc.

### Synergies
- **Setup moves**: Calm Mind, Dragon Dance, etc.
- **Recovery moves**: Roost, Recover while protected
- **Hazard setting**: Stealth Rock, Spikes setup
- **Status spreading**: Will-O-Wisp, Thunder Wave
- **Substitute**: Can set up behind guaranteed protection

### Version History
- Custom Elite Redux ability (ID 427)
- Uses modern single-use ability counter system
- Persistent across switches unlike traditional Endure
- No vanilla equivalent - unique defensive mechanism

### Technical Notes
- **Counter storage**: Persistent per Pokemon in party
- **Battle reset**: Counters reset between battles
- **Double battles**: Each Pokemon has independent counters
- **Forme changes**: Counter persists through forme changes
- **Ability changes**: Losing ability doesn't reset counter