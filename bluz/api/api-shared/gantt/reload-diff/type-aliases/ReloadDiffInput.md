[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / ReloadDiffInput

# Type Alias: ReloadDiffInput

> **ReloadDiffInput** = `object`

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:52](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/reload-diff.ts#L52)

## Properties

### actual

> **actual**: [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:56](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/reload-diff.ts#L56)

Live cut events currently in the schedule for this curriculum.

***

### desired

> **desired**: [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:54](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/reload-diff.ts#L54)

Documents the current plan would produce, ids irrelevant.

***

### lastManualEditByEvent?

> `optional` **lastManualEditByEvent?**: `ReadonlyMap`\<`string`, [`ReloadConflictReason`](../../../types/gantt/reload/type-aliases/ReloadConflictReason.md)\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:60](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/reload-diff.ts#L60)

Explanation per manually-edited event, for the conflicts dialog.

***

### manuallyEditedIds

> **manuallyEditedIds**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:58](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/reload-diff.ts#L58)

Event ids the change log marks as manually edited.

***

### overrideEventIds?

> `optional` **overrideEventIds?**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:62](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/reload-diff.ts#L62)

Manually-edited events the user chose to overwrite anyway.
