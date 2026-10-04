[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-allotment](../index.md) / useGridAllotment

# Function: useGridAllotment()

> **useGridAllotment**(`ctx`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-allotment.tsx:58](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-allotment.tsx#L58)

Commits a grid week-cell edit to the event's mappings' allotted minutes,
asking first whenever the edit means more than changing a number: removing
a mapping, moving or splitting the event, or detaching a recurrence
occurrence. Never touches the event's minimumDuration.

## Parameters

### ctx

`Context`

## Returns

### commitWeek

> **commitWeek**: (`eventId`, `moduleId`, `week`, `minutes`, `shared?`, `zero?`) => `Promise`\<`void`\>

`zero` answers the keep-0 / remove question up front (the grid menu's explicit entries, #858).

#### Parameters

##### eventId

`string`

##### moduleId

`string`

##### week

`number`

##### minutes

`number`

##### shared?

`SharedShuffles`

##### zero?

[`ZeroChoice`](../../grid-allotment/type-aliases/ZeroChoice.md)

#### Returns

`Promise`\<`void`\>

### dialog

> **dialog**: `ReactNode`

### splitShuffles

> **splitShuffles**: (`eventId`, `moduleId`, `shuffles`) => `Promise`\<`void`\>

Splits one event shared by every shuffle into one event per shuffle, keeping the placement (#858).

#### Parameters

##### eventId

`string`

##### moduleId

`string`

##### shuffles

`string`[]

#### Returns

`Promise`\<`void`\>
