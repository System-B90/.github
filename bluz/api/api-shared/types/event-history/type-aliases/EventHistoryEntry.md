[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / EventHistoryEntry

# Type Alias: EventHistoryEntry

> **EventHistoryEntry** = `object`

Defined in: [ui/src/api-shared/types/event-history.ts:125](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L125)

One immutable change row. `actorName` is denormalized on purpose: display
names live in Hive (an external service), so the log stores the name as it
read at write time and remains readable when Hive is unreachable or the
user is gone.

## Properties

### action

> **action**: [`EventChangeAction`](../enumerations/EventChangeAction.md)

Defined in: [ui/src/api-shared/types/event-history.ts:130](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L130)

***

### actorHiveId

> **actorHiveId**: `null` \| `number`

Defined in: [ui/src/api-shared/types/event-history.ts:142](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L142)

Same identity in numeric form, for joins and aggregations against Hive
user ids. Null when absent or non-numeric.

***

### actorId

> **actorId**: `null` \| `string`

Defined in: [ui/src/api-shared/types/event-history.ts:137](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L137)

Hive user id exactly as the SSO session issued it (string), or null for
machine/unauthenticated writes. This is the row's foreign key to Hive.

***

### actorName

> **actorName**: `null` \| `string`

Defined in: [ui/src/api-shared/types/event-history.ts:144](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L144)

Display name as read at write time; null for machine writes.

***

### changedAt

> **changedAt**: `Date`

Defined in: [ui/src/api-shared/types/event-history.ts:145](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L145)

***

### changes

> **changes**: [`EventFieldChange`](EventFieldChange.md)[]

Defined in: [ui/src/api-shared/types/event-history.ts:147](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L147)

Empty for [EventChangeAction.Created](../enumerations/EventChangeAction.md#created).

***

### context?

> `optional` **context?**: [`EventChangeContext`](EventChangeContext.md)

Defined in: [ui/src/api-shared/types/event-history.ts:132](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L132)

***

### eventId

> **eventId**: [`EventId`](../../event/type-aliases/EventId.md)

Defined in: [ui/src/api-shared/types/event-history.ts:129](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L129)

The event this row describes. Never embeds the event itself.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/event-history.ts:127](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L127)

Row id (uuid).

***

### initiator

> **initiator**: [`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

Defined in: [ui/src/api-shared/types/event-history.ts:131](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event-history.ts#L131)
