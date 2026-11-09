[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutSpillDetail

# Type Alias: CutSpillDetail

> **CutSpillDetail** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:260](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L260)

One relocated slot, described in terms a user can read: which event moved,
from which date to which. A slot the balancer bounced twice (off ראשון, then
off שני) collapses into a single detail spanning its first and last day.

## Properties

### durationMinutes

> **durationMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:271](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L271)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:262](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L262)

***

### fromDate

> **fromDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:268](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L268)

ISO date (yyyy-MM-dd) the slot was originally mapped to.

***

### fromDayId

> **fromDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:265](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L265)

***

### slotKey

> **slotKey**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:261](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L261)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:264](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L264)

Event title at plan time; falls back to the id for generated slots.

***

### toDate

> **toDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:270](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L270)

ISO date (yyyy-MM-dd) it ended up on.

***

### toDayId

> **toDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:266](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-planner.ts#L266)
