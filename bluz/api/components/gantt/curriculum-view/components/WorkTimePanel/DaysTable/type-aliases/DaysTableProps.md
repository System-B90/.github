[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/WorkTimePanel/DaysTable](../index.md) / DaysTableProps

# Type Alias: DaysTableProps

> **DaysTableProps** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L12)

## Properties

### canEdit

> **canEdit**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L14)

***

### days

> **days**: [`GanttDay`](../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L13)

***

### onDayCommentChange

> **onDayCommentChange**: (`weekIndex`, `dayIndex`, `nextComment`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L27)

#### Parameters

##### weekIndex

`number`

##### dayIndex

`number`

##### nextComment

`string`

#### Returns

`void`

***

### onDayCommentKeyDown

> **onDayCommentKeyDown**: (`event`, `weekIndex`, `dayIndex`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:33](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L33)

#### Parameters

##### event

`KeyboardEvent`\<`HTMLInputElement`\>

##### weekIndex

`number`

##### dayIndex

`number`

#### Returns

`void`

***

### onDayCommentSave

> **onDayCommentSave**: (`weekIndex`, `dayIndex`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L32)

#### Parameters

##### weekIndex

`number`

##### dayIndex

`number`

#### Returns

`Promise`\<`void`\>

***

### onHoursChange

> **onHoursChange**: (`weekIndex`, `dayIndex`, `nextValueRaw`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L16)

#### Parameters

##### weekIndex

`number`

##### dayIndex

`number`

##### nextValueRaw

`string`

#### Returns

`void`

***

### onHoursKeyDown

> **onHoursKeyDown**: (`event`, `weekIndex`, `dayIndex`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:22](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L22)

#### Parameters

##### event

`KeyboardEvent`\<`HTMLInputElement`\>

##### weekIndex

`number`

##### dayIndex

`number`

#### Returns

`void`

***

### onHoursSave

> **onHoursSave**: (`weekIndex`, `dayIndex`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L21)

#### Parameters

##### weekIndex

`number`

##### dayIndex

`number`

#### Returns

`Promise`\<`void`\>

***

### weekIndex

> **weekIndex**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/DaysTable.tsx#L15)
