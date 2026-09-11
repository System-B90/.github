[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion](../index.md) / WeekAccordionProps

# Type Alias: WeekAccordionProps

> **WeekAccordionProps** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:11](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L11)

## Properties

### canAddDay

> **canAddDay**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L14)

***

### canEdit

> **canEdit**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L13)

***

### onAddDay

> **onAddDay**: (`weekId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L15)

#### Parameters

##### weekId

[`GanttWeekId`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeekId.md)

#### Returns

`Promise`\<`void`\>

***

### onWeekCommentChange

> **onWeekCommentChange**: (`weekId`, `nextComment`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L16)

#### Parameters

##### weekId

[`GanttWeekId`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeekId.md)

##### nextComment

`string`

#### Returns

`void`

***

### onWeekCommentKeyDown

> **onWeekCommentKeyDown**: (`event`, `weekId`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L18)

#### Parameters

##### event

`KeyboardEvent`\<`HTMLInputElement`\>

##### weekId

[`GanttWeekId`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeekId.md)

#### Returns

`void`

***

### onWeekCommentSave

> **onWeekCommentSave**: (`weekId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L17)

#### Parameters

##### weekId

[`GanttWeekId`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeekId.md)

#### Returns

`Promise`\<`void`\>

***

### weekId

> **weekId**: [`GanttWeekId`](../../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeekId.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/WorkTimePanel/WeekAccordion.tsx#L12)
