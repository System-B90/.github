[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/week-templates/use-week-templates](../index.md) / useWeekTemplates

# Function: useWeekTemplates()

> **useWeekTemplates**(`enabled?`): `object`

Defined in: [ui/src/components/week-templates/use-week-templates.ts:12](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/week-templates/use-week-templates.ts#L12)

The week templates (#997), loaded on mount. `refresh` reloads them after a
change; `setTemplates` lets a caller apply a known result without a round trip.

## Parameters

### enabled?

`boolean` = `true`

## Returns

`object`

### loading

> **loading**: `boolean`

### refresh

> **refresh**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### setTemplates

> **setTemplates**: `Dispatch`\<`SetStateAction`\<[`WeekTemplate`](../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)[]\>\>

### templates

> **templates**: [`WeekTemplate`](../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)[]
