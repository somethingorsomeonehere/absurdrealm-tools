---
id: 223
name: Power of Alchemy
status: reviewed
character_count: 202
---

# Power of Alchemy - Ability ID 223

## In-Game Description
"Transmutes berries on entry. Transmutes items when lost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entry, transmutes all opposing Berries into Black Sludge. When any Pokemon loses an item during battle, it gets replaced by Black Sludge. If Black Sludge is removed, it gets replaced by Big Nugget.

## Detailed Mechanical Explanation
**Power of Alchemy** creates a sophisticated "magical item economy" where the user acts as an alchemist, immediately disrupting opposing Berry strategies and continuously transmuting lost items.

### Core Mechanics

#### Transmutation on Entry
When the Pokemon with Power of Alchemy enters battle:
1. **Scans all opposing Pokemon** for held items
2. **Any opponent holding a Berry** gets their Berry instantly transmuted to Black Sludge
3. **Triggers message**: "{Pokemon} transmutes {target}'s lost item!" followed by "It turned into sludge..."
4. **Berry Detection**: Uses `POCKET_BERRIES` check to identify Berries

#### Transmutation When Items Are Lost
The ability tracks when any Pokemon on the field loses an item:
1. **State Tracking**: Uses 2 bits per battler to track what type of item was lost
2. **Loss Detection**: Triggers on `UpdateBattlerItem` calls when items are removed
3. **Replacement Creation**: When the Power of Alchemy user gets a turn after an item loss, it creates a replacement

### Item Transmutation Rules

#### State System Values
- **Value 1**: Creates Black Sludge (sludge transmutation)
- **Value 2**: Creates Big Nugget (gold transmutation)

#### Transmutation Logic
```cpp
// SetPowerOfAlchemyState function logic:
if (lost item is BLACK_SLUDGE || BIG_NUGGET) {
    store value 2;  // Will create Big Nugget
} else {
    store value 1;  // Will create Black Sludge
}
```

#### Item Types and Results
- **Regular items** to Black Sludge
- **Previously transmuted items** (Black Sludge/Big Nugget) to Big Nugget
- **Berries** to Black Sludge (on entry only)

### Item Properties

#### Black Sludge
- **Type**: Poison-type recovery item
- **Effect**: Heals Poison-type Pokemon, damages non-Poison types
- **Strategic Use**: Benefits Poison-types while punishing others

#### Big Nugget
- **Type**: Valuable item
- **Effect**: No battle effect, purely valuable
- **Strategic Use**: End result of repeated transmutation

### Technical Implementation

#### State Management
- Uses bit-shifting state management (2 bits per battler)
- State is cleared when items are successfully transmitted
- Tracks losses across the entire battlefield, not just the user

#### Trigger Conditions
- Entry effect uses `onEntry` callback
- Loss tracking uses `UpdateBattlerItem` monitoring
- Replacement creation occurs on the alchemist's next turn

### Strategic Implications

#### Anti-Berry Strategy
- **Immediately counters** opposing Berry strategies (Sitrus, Lum, etc.)
- **Converts beneficial items** into harmful ones for non-Poison types
- **Forces item reconsideration** in team building

#### Battlefield Control
- **Tracks ALL item losses**, not just the user's items
- **Creates item economy** where lost items don't disappear permanently
- **Benefits Poison-type teams** through Black Sludge creation

#### Continuous Value
- **Ongoing effect** throughout the battle
- **Memory system** ensures no item loss goes unrewarded
- **Escalating value** as transmuted items become Big Nuggets

### Unique Features
Power of Alchemy is distinctive because:
1. **Cross-battlefield tracking**: Affects items of ALL Pokemon, not just allies
2. **Item memory**: Remembers losses and acts on them later
3. **Type-specific benefits**: Particularly valuable with Poison-type teams
4. **Economic disruption**: Fundamentally changes item-based strategies

The ability creates a true "alchemical laboratory" environment where the user continuously transforms the battlefield's item economy, punishing Berry strategies while creating value from item losses.
