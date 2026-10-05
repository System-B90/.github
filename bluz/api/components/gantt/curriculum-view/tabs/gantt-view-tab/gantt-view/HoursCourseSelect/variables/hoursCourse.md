[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect](../index.md) / hoursCourse

# Variable: hoursCourse

> `const` **hoursCourse**: `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx:13](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx#L13)

Whose time the gantt's scheduled-hours totals count (#899): one course's
students, or (null) whichever course is busiest. Shared by the grid and the
timeline, and remembered per viewer.

## Type Declaration

### get

> **get**: () => `string` \| `null`

#### Returns

`string` \| `null`

### set

> **set**: (`next`) => `void`

#### Parameters

##### next

`string` \| `null`

#### Returns

`void`

### use

> **use**: () => `string` \| `null`

#### Returns

`string` \| `null`
