---
id: 722
name: Whiplash
status: reviewed
character_count: 162
---

# Whiplash - Ability ID 722

## In-Game Description
"Physical attacks lower defense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Lowers the target's Defense by one stage when hitting with physical attacks. Each target can only be affected once per turn. The Defense drop occurs after damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Whiplash is an offensive ability that weakens the target's defensive capabilities through physical attacks. When the user hits a target with any physical move, the target's Defense stat is lowered by one stage.

### Activation Conditions
- **Move type requirement**: Only physical moves trigger the ability
- **Hit requirement**: The move must successfully hit and deal damage
- **Once per turn per target**: Each individual target can only have their Defense lowered once per turn by this ability
- **Multiple targets**: In multi-target scenarios, each opponent can be affected separately

### Technical Implementation
```c
constexpr Ability Whiplash = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(IS_MOVE_PHYSICAL(move))
        CHECK(StatLowerableOrMirrorArmor(target, STAT_DEF))

        int affected = GetOncePerTurnAbilityCounter(battler, ability);
        CHECK_NOT(affected & (1 << target))

        SetOncePerTurnAbilityCounter(battler, ability, affected | (1 << target));
        return AbilityStatusEffect(MOVE_EFFECT_DEF_MINUS_1);
    },
};
```

### Important Interactions
- **Timing**: Defense drop occurs after damage calculation
- **Multi-hit moves**: Only triggers once per target per turn, not per hit
- **Contact vs non-contact**: Works with both contact and non-contact physical moves
- **Substitute**: Cannot lower Defense through Substitute
- **Mirror Armor**: Blocked by Mirror Armor (Defense drop reflected back)
- **Clear Body/White Smoke**: Blocked by stat-lowering immunity abilities
- **Mist/Safeguard**: Blocked by team-wide stat protection

### Move Compatibility
- **All physical moves**: Every physical attack can trigger Whiplash
- **Priority moves**: Works with Fake Out, Extreme Speed, etc.
- **Multi-hit moves**: Rock Blast, Bullet Seed, etc. (once per turn limit still applies)
- **Recoil moves**: Double-Edge, Brave Bird, etc.
- **Contact moves**: Tackle, Return, Close Combat, etc.
- **Non-contact physical**: Rock Slide, Earthquake, etc.

### Strategic Applications
- **Wall breaking**: Excellent for wearing down defensive Pokemon
- **Team support**: Weakens targets for teammates to finish
- **Sweeper setup**: Creates opportunities for physical sweepers
- **Pivot utility**: Can weaken foes before switching
- **Anti-stall**: Pressures defensive strategies

### Defensive Counterplay
- **Stat reset**: Haze, Clear Smog reset Defense drops
- **Stat immunity**: Clear Body, White Smoke, Full Metal Body
- **Stat reflection**: Mirror Armor reflects the Defense drop
- **Substitute**: Blocks the stat drop effect
- **Special attackers**: Unaffected by Defense drops
- **Evasion**: Missing attacks prevents ability activation

### Team Synergies
- **Physical sweepers**: Benefit from pre-weakened targets
- **Entry hazard setters**: Combine with Stealth Rock for chip damage
- **Pivot moves**: U-turn/Volt Switch after weakening foes
- **Choice item users**: Can weaken multiple targets before switching
- **Mixed attackers**: Can use both physical and special moves

### Common Users
- Physical attackers who want utility beyond just damage
- Pokemon with good Speed and multiple physical moves
- Lead Pokemon that can pressure early game
- Pivot Pokemon that switch frequently
- Pokemon with priority moves for guaranteed activation

### Competitive Usage Notes
- **Early game pressure**: Excellent for gaining early advantages
- **Mid-game utility**: Helps break through defensive cores
- **Late game cleanup**: Weakens remaining walls for sweepers
- **Doubles/Multi-battles**: Can affect multiple targets per turn
- **Risk/reward**: Must use physical moves to gain utility

### Version History
- Elite Redux exclusive ability
- Designed as a physical attack utility ability
- Balanced with once-per-turn limitation to prevent excessive stacking
- Part of the expanded ability roster for strategic diversity