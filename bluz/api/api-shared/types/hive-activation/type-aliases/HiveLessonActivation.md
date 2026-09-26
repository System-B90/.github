[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/hive-activation](../index.md) / HiveLessonActivation

# Type Alias: HiveLessonActivation

> **HiveLessonActivation** = `object`

Defined in: [ui/src/api-shared/types/hive-activation.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L20)

One recorded queue opening: the activator pushed `lessonId` onto Hive class
`hiveClassId` because event `eventId` started at `occurrenceStart`.

The (eventId, hiveClassId, occurrenceStart) triple is uniquely indexed, so
inserting the row *is* the claim: a second replica — or the same replica a
tick later — loses the insert and does nothing. Moving an event changes
`occurrenceStart`, which deliberately re-arms it for its new time.

## Properties

### activatedAt

> **activatedAt**: `Date`

Defined in: [ui/src/api-shared/types/hive-activation.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L27)

When Hive accepted the assignment.

***

### eventId

> **eventId**: [`EventId`](../../event/type-aliases/EventId.md)

Defined in: [ui/src/api-shared/types/hive-activation.ts:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L21)

***

### hiveClassId

> **hiveClassId**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L22)

***

### lessonId

> **lessonId**: [`HiveLessonId`](../../hive/type-aliases/HiveLessonId.md)

Defined in: [ui/src/api-shared/types/hive-activation.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L25)

***

### occurrenceStart

> **occurrenceStart**: `string`

Defined in: [ui/src/api-shared/types/hive-activation.ts:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L24)

ISO timestamp of the event start this activation belongs to.
