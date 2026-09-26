[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / SPILLOVER\_RULES

# Variable: SPILLOVER\_RULES

> `const` **SPILLOVER\_RULES**: `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:70](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-rules.ts#L70)

Spillover moves events off an over-full day onto a later day that has room.

Invariants — these are the rules the balancer may never break:

1. **Never across weeks.** A spill target must live in the same
   `GanttWeek` as the source day. A week that cannot absorb its own load
   overlaps instead (see [OVERFLOW\_RULES](OVERFLOW_RULES.md)).
2. **Never forward-only into a full day.** An event is only moved onto a
   day that can actually hold it inside its working window. Overlapping on
   day X beats spilling onto an already-full day X+1.
3. **Never outside working hours.** Nothing is ever placed past a day's end
   time by the balancer. Overlap is always the lesser wrong.
4. **Forward only.** Events flow to later days in the week, never earlier —
   the mapped day is the earliest a user asked for it.

Spill may cascade over several days in the same week, so a week with
everything piled onto ראשון rebalances across ראשון–חמישי.

## Type Declaration

### moduleCohesionBonusMinutes

> `readonly` **moduleCohesionBonusMinutes**: `120` = `120`

Bonus weight, in minutes, added to a candidate's fitness when moving it
keeps its whole module together on one day. Module cohesion is a strong
preference but yields to a strictly better packing.

### moduleSplitPenaltyMinutes

> `readonly` **moduleSplitPenaltyMinutes**: `90` = `90`

Penalty weight, in minutes, for splitting a module across days. Applied
when a move would leave siblings from the same module behind.

### strategy

> `readonly` **strategy**: `"best-fit"`

Candidate selection inside an over-full day. Best-fit: pick whichever
movable event packs the later days most tightly (largest event that
still fits the largest gap), rather than blindly spilling the tail.
