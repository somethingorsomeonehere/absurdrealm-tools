---
id: 451
name: Lingering Aroma
status: reviewed
character_count: 119
---

# Lingering Aroma - Ability ID 451

## In-Game Description
"If hit, makes the attacker's ability Lingering Aroma."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Lingering Aroma changes the attacker's ability (not innates) to Lingering Aroma when the user is hit by a contact move. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Lingering Aroma is an ability-spreading effect that changes the attacker's ability to Lingering Aroma when hit by contact moves. It uses the exact same implementation as Mummy (`Mummy.onDefender`), making it functionally identical to that ability but with a different thematic presentation.

### Activation Conditions
- **Contact requirement**: Only triggers when hit by moves that make contact
- **Timing**: Activates immediately when the contact move hits
- **Target**: Affects the attacking Pokemon, not the defending one
- **Hit requirement**: Must successfully hit to trigger (not blocked by substitutes)

### Technical Implementation
```c
// Lingering Aroma uses Mummy's implementation
constexpr Ability LingeringAroma = {
    .onDefender = Mummy.onDefender,
};

// The actual mechanic from Mummy:
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(attacker))
    CHECK_NOT(HasAbilityIgnoringSuppression(attacker, ability))
    CHECK(IsMoveMakingContact(move, attacker))
    CHECK_NOT(IsPersistentOrUnsuppressableAbility(GetBattlerAbility(attacker)))
    CHECK_NOT(DoesBattlerHaveAbilityShield(attacker))

    UpdateAbilityStateIndicesForNewAbility(attacker, ability);
    ReplaceAbility(attacker, ability);
    BattleScriptCall(BattleScript_MummyActivates);
    return TRUE;
},
```

### Ability Spreading Mechanics
- **Overrides**: Replaces the attacker's current ability with Lingering Aroma
- **Chain reaction**: If the newly affected Pokemon gets hit by contact, they can spread it further
- **Permanent**: The ability change lasts for the entire battle
- **No immunities**: Unlike status moves, there are no type-based immunities

### Abilities That Cannot Be Overridden
Lingering Aroma cannot override certain "persistent or unsuppressable" abilities:
- **Multitype** (Arceus)
- **RKS System** (Silvally) 
- **Disguise** (Mimikyu)
- **Ice Face** (Eiscue)
- **Battle Bond** (Greninja)
- **Power Construct** (Zygarde)
- **Schooling** (Wishiwashi)
- **Shields Down** (Minior)
- **Comatose** (Komala)
- Other form-changing or core identity abilities

### Protective Measures
- **Ability Shield**: Completely blocks Lingering Aroma from taking effect
- **Long Reach**: Prevents activation by making moves not make contact
- **Magic Guard**: Still gets affected (doesn't prevent ability change)
- **Non-contact moves**: Safe to use against Lingering Aroma users

### Strategic Implications
- **Ability denial**: Removes opponent's key abilities permanently
- **Team disruption**: Can cripple ability-dependent strategies
- **Chain spreading**: Can affect entire teams through contact moves
- **Defensive tool**: Punishes physical attackers who make contact
- **Setup counter**: Removes setup abilities like Speed Boost or Moody

### Contact Moves That Trigger
All moves with the contact flag, including:
- **Physical attacks**: Most physical moves make contact
- **Multi-hit moves**: Each hit can potentially trigger
- **Priority moves**: Mach Punch, Aqua Jet, etc.
- **Status moves**: Thunder Wave, Spore (if they make contact)

### Non-Contact Moves (Safe)
- **Projectile moves**: Water Gun, Flamethrower, etc.
- **Special attacks**: Most special moves don't make contact
- **Long-range moves**: Surf, Earthquake, Rock Slide
- **Status moves**: Most status moves are non-contact

### Counterplay
- **Ability Shield**: Hard counter that prevents the effect
- **Non-contact moves**: Use ranged attacks exclusively  
- **Ability replacement**: Use moves like Skill Swap to replace it
- **Team positioning**: Keep important ability users away from contact
- **Speed control**: Outspeed and KO before they can spread

### Synergies
- **Spiky Shield/King's Shield**: Punish contact moves further
- **Rough Skin/Iron Barbs**: Stack contact damage
- **Static/Flame Body**: Multiple contact-based effects
- **Guts/Quick Feet**: Can benefit from opponent's hesitation to make contact

### Common Users
- Pokemon that want to disrupt opponent's strategies
- Defensive walls that expect physical contact
- Support Pokemon that can afford to lose their original ability
- Anti-setup specialists

### Competitive Usage Notes
- **Meta disruptor**: Can completely change team dynamics mid-battle
- **Mindgames**: Forces opponents to play around contact moves
- **Late game tool**: More impactful when abilities have been established
- **Risk/reward**: User loses their own ability to gain this effect

### Differences from Mummy
While mechanically identical, Lingering Aroma has a different thematic presentation:
- **Visual effects**: Different animation/message when activating
- **Lore**: Aromatherapy theme vs. Egyptian mummy theme
- **Distribution**: May be on different Pokemon species
- **Name recognition**: Players may not immediately recognize the mechanic

### Version History
- New ability in Elite Redux
- Uses proven Mummy mechanics for reliability
- Part of the expanded ability roster
- Provides thematic alternative to Mummy