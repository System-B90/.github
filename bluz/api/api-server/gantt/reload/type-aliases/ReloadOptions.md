[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/reload](../index.md) / ReloadOptions

# Type Alias: ReloadOptions

> **ReloadOptions** = `object`

Defined in: [ui/src/api-server/gantt/reload.ts:56](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/reload.ts#L56)

## Properties

### dryRun?

> `optional` **dryRun?**: `boolean`

Defined in: [ui/src/api-server/gantt/reload.ts:57](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/reload.ts#L57)

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-server/gantt/reload.ts:58](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/reload.ts#L58)

***

### overrideEventIds?

> `optional` **overrideEventIds?**: `string`[]

Defined in: [ui/src/api-server/gantt/reload.ts:59](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/reload.ts#L59)

***

### weekId?

> `optional` **weekId?**: `string`

Defined in: [ui/src/api-server/gantt/reload.ts:64](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/reload.ts#L64)

Reload only this timeline week. The rest of the schedule is neither
compared nor touched, so other weeks' events never look removed.

***

### weekStarts?

> `optional` **weekStarts?**: `string`[]

Defined in: [ui/src/api-server/gantt/reload.ts:69](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/reload.ts#L69)

Reload only the weeks starting on these Sundays (YYYY-MM-DD). A template
save re-applies itself to exactly the weeks cut with it (#997).
