---
id: 562
name: Costar
status: reviewed
character_count: 116
---

# Costar - Ability ID 562

## In-Game Description
"Copies its ally's stat changes on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Costar copies all stat stage changes (positive and negative) from the ally when switching in during doubles battles.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger**: On switch-in (entry) during doubles/multi battles
- **Requirement**: Must have a living battle partner (ally)
- **Effect**: Copies all stat stage changes from ally to self
- **Stats Affected**: All 7 battle stats (Attack, Defense, Sp. Attack, Sp. Defense, Speed, Accuracy, Evasion)

### Technical Implementation
```cpp
constexpr Ability Costar = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(IsBattlerAlive(BATTLE_PARTNER(battler)))

        int anyChanged = FALSE;
        for (int i = STAT_ATK; i < NUM_BATTLE_STATS; i++) {
            if (gBattleMons[battler].statStages[i] != gBattleMons[BATTLE_PARTNER(battler)].statStages[i]) {
                gBattleMons[battler].statStages[i] = gBattleMons[BATTLE_PARTNER(battler)].statStages[i];
                anyChanged = TRUE;
            }
        }

        CHECK(anyChanged)
        return SwitchInAnnounce(B_MSG_SWITCHIN_COSTAR);
    },
};
```

### Battle Message
When activated: "{Pokemon} copied its ally's stat changes!"

### Doubles Battle Mechanics
- **Partner Detection**: Uses `BATTLE_PARTNER(battler)` to identify ally
- **Stat Stage Copy**: Direct copy of `statStages[i]` values from ally to self
- **No Activation**: If ally has no stat changes or is fainted
- **Immediate Effect**: Stat changes apply instantly upon switch-in

### Competitive Applications
- **Support Synergy**: Pairs well with setup sweepers who can pass boosts
- **Late Game**: Strong when ally has accumulated multiple stat boosts
- **Pivot Strategy**: Switch in after ally sets up to copy boosts
- **Double Intimidate**: Can copy ally's Attack drops from opposing Intimidate

### Strategic Team Building
- **Setup Partners**: Pokemon with boosting moves (Swords Dance, Calm Mind, etc.)
- **Baton Pass**: Combines well with Baton Pass teams in doubles
- **Stat Boost Abuse**: Maximizes value of temporary stat increases
- **Entry Hazard Support**: Switch-in timing becomes crucial with hazards present

### Important Notes
- Only works in doubles, triples, or multi battles (requires ally)
- Copies both positive and negative stat changes
- Does not work if ally is fainted
- Applies to accuracy and evasion modifications as well
- One-time effect on entry, doesn't continuously sync with ally