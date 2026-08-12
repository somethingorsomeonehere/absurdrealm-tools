---
id: 676
name: Sidewinder
status: reviewed
character_count: 165
---

# Sidewinder - Ability ID 676

## In-Game Description
First biting move each entry gets +1 priority. Resets on KO.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

On entry, gives +1 priority to the first biting move used. Priority boost is consumed after landing any biting move. Upon scoring a direct KO, regains priority buff.

## Detailed Mechanical Explanation

### Technical Implementation

- **Entry Effect:** Sets STATUS4_COILED status (same as Coil Up ability)
- **Priority Boost:** Biting moves (FLAG_STRONG_JAW_BOOST) gain +1 priority when coiled
- **Status Consumption:** Coiled status is removed after using a biting move (unless Sidewinder ability is active)
- **KO Reset:** When KOing with a biting move, immediately restores coiled status for next entry
- **Faints Trigger:** Only applies when the attacker has Sidewinder and uses a biting move to KO

### Battle Mechanics

- Coiled status persists until a biting move is used
- Multiple entries restore the coiled status each time
- Works with all moves that have the Strong Jaw flag
- Priority calculation occurs during move selection phase
- Status is displayed in battle UI when active

### Strategic Applications

Sidewinder excels on revenge killers and Pokemon that frequently switch in and out. The guaranteed priority on the first biting move makes it excellent for cleaning up weakened opponents or getting crucial first strikes. The KO reset mechanic rewards aggressive play and successful finishes.