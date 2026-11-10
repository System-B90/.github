[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / ReloadDiffInput

# Type Alias: ReloadDiffInput

> **ReloadDiffInput** = `object`

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:84](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L84)

## Properties

### actual

> **actual**: [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:88](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L88)

Live cut events currently in the schedule for this curriculum.

***

### desired

> **desired**: [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:86](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L86)

Documents the current plan would produce, ids irrelevant.

***

### fields?

> `optional` **fields?**: `ReadonlyArray`\<keyof [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:103](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L103)

Fields compared; defaults to [GANTT\_OWNED\_FIELDS](../variables/GANTT_OWNED_FIELDS.md).

***

### lastManualEditByEvent?

> `optional` **lastManualEditByEvent?**: `ReadonlyMap`\<`string`, [`ReloadConflictReason`](../../../types/gantt/reload/type-aliases/ReloadConflictReason.md)\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:92](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L92)

Explanation per manually-edited event, for the conflicts dialog.

***

### manuallyDeletedKeys?

> `optional` **manuallyDeletedKeys?**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:101](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L101)

[occurrenceKey](../functions/occurrenceKey.md)s of occurrences a human deleted from the schedule.
Re-adding them would undo the user's work, so they come back parked
(in the unassigned-events box) instead of on the grid — breaks not at
all ([isDeletedBreak](../functions/isDeletedBreak.md)).

***

### manuallyEditedIds

> **manuallyEditedIds**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:90](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L90)

Event ids the change log marks as manually edited.

***

### overrideEventIds?

> `optional` **overrideEventIds?**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:94](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/reload-diff.ts#L94)

Manually-edited events the user chose to overwrite anyway.
