[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect](../index.md) / hoursCourse

# Variable: hoursCourse

> `const` **hoursCourse**: `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx:14](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx#L14)

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
