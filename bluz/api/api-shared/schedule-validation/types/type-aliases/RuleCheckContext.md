[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/types](../index.md) / RuleCheckContext

# Type Alias: RuleCheckContext

> **RuleCheckContext** = `object`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:41](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L41)

What the checks know beyond the events. Name lookups only label results;
the optional sources are loaded by the server only for the rules that
declare them (`RuleCheck.needs`).

## Properties

### courseInstructors

> **courseInstructors**: (`courseId`) => `number`[]

Defined in: [ui/src/api-shared/schedule-validation/types.ts:52](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L52)

Instructors set on a course in the course builder; empty when none.

#### Parameters

##### courseId

`string`

#### Returns

`number`[]

***

### courseLineage

> **courseLineage**: (`courseId`) => `string`[]

Defined in: [ui/src/api-shared/schedule-validation/types.ts:50](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L50)

The course and its ancestors, nearest first.

#### Parameters

##### courseId

`string`

#### Returns

`string`[]

***

### courseName

> **courseName**: (`courseId`) => `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:46](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L46)

#### Parameters

##### courseId

`string`

#### Returns

`string`

***

### ganttRank?

> `optional` **ganttRank?**: (`ganttEventId`) => [`GanttRank`](GanttRank.md) \| `undefined`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:58](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L58)

The event's Gantt order, when it was cut from a curriculum that still has it.

#### Parameters

##### ganttEventId

`string`

#### Returns

[`GanttRank`](GanttRank.md) \| `undefined`

***

### isShuffle

> **isShuffle**: (`courseId`) => `boolean`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:43](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L43)

#### Parameters

##### courseId

`string`

#### Returns

`boolean`

***

### mealTimes?

> `optional` **mealTimes?**: (`date`) => [`MealSettings`](../../../types/settings/meal/type-aliases/MealSettings.md) \| `null`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:56](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L56)

The linked week template's meal times for a date; null when the week has no template.

#### Parameters

##### date

`string`

#### Returns

[`MealSettings`](../../../types/settings/meal/type-aliases/MealSettings.md) \| `null`

***

### personName

> **personName**: (`id`) => `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:48](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L48)

#### Parameters

##### id

`number` \| `string`

#### Returns

`string`

***

### prayerWindows?

> `optional` **prayerWindows?**: [`DayPrayerWindow`](../../../types/prayer-windows/type-aliases/DayPrayerWindow.md)[]

Defined in: [ui/src/api-shared/schedule-validation/types.ts:54](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L54)

Daily prayer windows for the checked dates.

***

### roomName

> **roomName**: (`room`) => `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:47](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L47)

#### Parameters

##### room

[`ResolvableRoom`](../../../types/room/type-aliases/ResolvableRoom.md)

#### Returns

`string`

***

### shuffleName

> **shuffleName**: (`courseId`) => `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:44](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L44)

#### Parameters

##### courseId

`string`

#### Returns

`string`

***

### syllabusName

> **syllabusName**: (`subjectId`) => `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:45](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L45)

#### Parameters

##### subjectId

`number` \| `string`

#### Returns

`string`

***

### timezone?

> `optional` **timezone?**: `string`

Defined in: [ui/src/api-shared/schedule-validation/types.ts:42](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-validation/types.ts#L42)
