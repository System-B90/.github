[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/reload](../index.md) / ReloadOptions

# Type Alias: ReloadOptions

> **ReloadOptions** = `object`

Defined in: [ui/src/api-server/gantt/reload.ts:60](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L60)

## Properties

### dryRun?

> `optional` **dryRun?**: `boolean`

Defined in: [ui/src/api-server/gantt/reload.ts:61](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L61)

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-server/gantt/reload.ts:62](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L62)

***

### overrideEventIds?

> `optional` **overrideEventIds?**: `string`[]

Defined in: [ui/src/api-server/gantt/reload.ts:63](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L63)

***

### parkNonTemplate?

> `optional` **parkNonTemplate?**: `boolean`

Defined in: [ui/src/api-server/gantt/reload.ts:84](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L84)

True parks whatever the template does not place; false auto-places it.
Either way `parked` becomes a field the reload reconciles. Omitted ⇒
auto-placed, and an event's parked state is left alone.

***

### templateId?

> `optional` **templateId?**: `string`

Defined in: [ui/src/api-server/gantt/reload.ts:78](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L78)

Re-plan the reloaded weeks (all, or just `weekId`) under this template
instead of the one each was cut with, and stamp them with it (#997).

***

### weekId?

> `optional` **weekId?**: `string`

Defined in: [ui/src/api-server/gantt/reload.ts:68](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L68)

Reload only this timeline week. The rest of the schedule is neither
compared nor touched, so other weeks' events never look removed.

***

### weekStarts?

> `optional` **weekStarts?**: `string`[]

Defined in: [ui/src/api-server/gantt/reload.ts:73](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/reload.ts#L73)

Reload only the weeks starting on these Sundays (YYYY-MM-DD). A template
save re-applies itself to exactly the weeks cut with it (#997).
