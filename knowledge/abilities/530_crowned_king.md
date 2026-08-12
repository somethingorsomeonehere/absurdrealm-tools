---
id: 530
name: Crowned King
status: reviewed
character_count: 160
---

# Crowned King - Ability ID 530

## In-Game Description
"Unnerve + Grim Neigh + Chilling Neigh."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all opposing Pokemon from consuming held items. Raise Attack and Special Attack by one stage when the user knocks out an opponent with a direct attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

Crowned King is a triple-combination ability that merges three distinct effects into one powerful package:

### Core Mechanics

**1. Unnerve Effect:**
- Prevents opposing Pokemon from consuming berries and activating berry-based held items
- Affects items like Focus Sash, Custap Berry, Eject Button, and all berries
- Displays message "The opposing team is too nervous to use items!" on switch-in
- Cannot be suppressed or negated

**2. Chilling Neigh Effect:**
- Raises the user's Attack stat by one stage (1.5x multiplier) when knocking out an opponent
- Only triggers when the ability user directly causes a faint through damage
- Uses the same mechanism as Moxie but specifically for Attack
- Shows appropriate stat boost animation and message

**3. Grim Neigh Effect:**
- Raises the user's Special Attack stat by one stage (1.5x multiplier) when knocking out an opponent  
- Only triggers when the ability user directly causes a faint through damage
- Complementary to Chilling Neigh, boosting the special attacking stat instead
- Shows appropriate stat boost animation and message

### Technical Implementation
```cpp
constexpr Ability CrownedKing = {
    .onEntry = +[](ON_ENTRY) -> int { return SwitchInAnnounce(B_MSG_SWITCHIN_CROWNEDKING); },
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        return AsOneShadowRider.onBattlerFaints(DELEGATE_BATTLER_FAINTS) | 
               AsOneIceRider.onBattlerFaints(DELEGATE_BATTLER_FAINTS);
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
    .unnerve = TRUE,
};
```

### Activation Conditions
- **Switch-in:** Unnerve effect activates immediately upon entering battle
- **On KO:** Both Chilling Neigh and Grim Neigh effects trigger simultaneously when the user knocks out an opponent
- **Attack and Special Attack:** Both offensive stats are boosted by one stage each per KO

### Affected Items (Unnerve Component)
- All berries (Oran, Sitrus, Lum, etc.)
- Focus Sash and Focus Band
- Custap Berry
- Eject Button
- Quick Claw (timing-based items)
- Any consumable held item that activates during battle

### Interactions with Other Abilities/Mechanics
- **Stat Boosts:** Can stack with other stat-boosting effects like Swords Dance or Nasty Plot
- **Unsuppressable:** Cannot be disabled by abilities like Neutralizing Gas or moves like Gastro Acid  
- **Randomizer Banned:** Excluded from random ability assignment in ROM hacks
- **Multi-Hit:** Only triggers once per opponent defeated, not per hit
- **Substitute:** Does not prevent Unnerve from affecting item usage

### Strategic Implications
- **Offensive Sweeper:** Perfect for mixed attackers that can utilize both physical and special moves
- **Item Denial:** Shuts down defensive strategies relying on berries or Focus Sash
- **Snowball Effect:** Each KO makes the user progressively more dangerous
- **Entry Hazard Synergy:** Pairs well with hazards that can bring opponents into KO range

### Example Damage Calculations
**Base scenario (100 Base Attack/Special Attack, neutral nature):**
- Before KO: 252 Atk = 299, 252 SpA = 299
- After 1 KO: 448 Atk (+1), 448 SpA (+1) 
- After 2 KOs: 598 Atk (+2), 598 SpA (+2)

### Common Users
- Signature ability of legendary or mythical Pokemon
- Typically found on versatile mixed attackers
- Often paired with diverse movepools covering both physical and special attacks

### Competitive Usage Notes
- **Priority:** High-priority ability for team building due to multiple effects
- **Counters:** Switching frequently to avoid giving free KOs, using non-item defensive strategies
- **Synergies:** Works excellently with Life Orb, Choice items, or Z-moves to secure initial KOs
- **Team Support:** Benefits from entry hazards and stat-lowering moves to help secure KOs

### Version History
- Introduced as custom ability in Elite Redux
- Based on combination of existing Pokemon abilities: Unnerve (Gen 5), Chilling Neigh (Gen 8), Grim Neigh (Gen 8)
- Represents royal/legendary status through combination of intimidation and battle prowess