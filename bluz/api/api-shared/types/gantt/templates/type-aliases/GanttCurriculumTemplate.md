[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/templates](../index.md) / GanttCurriculumTemplate

# Type Alias: GanttCurriculumTemplate

> **GanttCurriculumTemplate** = `object`

Defined in: [ui/src/api-shared/types/gantt/templates.ts:6](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/templates.ts#L6)

## Properties

### defaultDayMinutes

> **defaultDayMinutes**: [`TemplateDayConfig`](TemplateDayConfig.md)

Defined in: [ui/src/api-shared/types/gantt/templates.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/templates.ts#L17)

Default working-minutes per day (applied uniformly to every week).
Each week can still be overridden individually after applying.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/gantt/templates.ts:8](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/templates.ts#L8)

Unique key used in code / localStorage

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types/gantt/templates.ts:10](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/templates.ts#L10)

Hebrew display label

***

### weekCount

> **weekCount**: `number`

Defined in: [ui/src/api-shared/types/gantt/templates.ts:12](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/templates.ts#L12)

Number of weeks the template prescribes

***

### weekOverrides?

> `optional` **weekOverrides?**: `Record`\<`number`, [`TemplateDayConfig`](TemplateDayConfig.md)\>

Defined in: [ui/src/api-shared/types/gantt/templates.ts:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/templates.ts#L19)

Optional per-week overrides: index → day-minutes. Sparse — unset weeks get defaultDayMinutes.
