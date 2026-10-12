[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / EventHistoryEntry

# Type Alias: EventHistoryEntry

> **EventHistoryEntry** = `object`

Defined in: [ui/src/api-shared/types/event-history.ts:131](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L131)

One immutable change row. `actorName` is denormalized on purpose: display
names live in Hive (an external service), so the log stores the name as it
read at write time and remains readable when Hive is unreachable or the
user is gone.

## Properties

### action

> **action**: [`EventChangeAction`](../enumerations/EventChangeAction.md)

Defined in: [ui/src/api-shared/types/event-history.ts:136](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L136)

***

### actorHiveId

> **actorHiveId**: `null` \| `number`

Defined in: [ui/src/api-shared/types/event-history.ts:148](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L148)

Same identity in numeric form, for joins and aggregations against Hive
user ids. Null when absent or non-numeric.

***

### actorId

> **actorId**: `null` \| `string`

Defined in: [ui/src/api-shared/types/event-history.ts:143](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L143)

Hive user id exactly as the SSO session issued it (string), or null for
machine/unauthenticated writes. This is the row's foreign key to Hive.

***

### actorName

> **actorName**: `null` \| `string`

Defined in: [ui/src/api-shared/types/event-history.ts:150](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L150)

Display name as read at write time; null for machine writes.

***

### changedAt

> **changedAt**: `Date`

Defined in: [ui/src/api-shared/types/event-history.ts:151](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L151)

***

### changes

> **changes**: [`EventFieldChange`](EventFieldChange.md)[]

Defined in: [ui/src/api-shared/types/event-history.ts:153](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L153)

Empty for [EventChangeAction.Created](../enumerations/EventChangeAction.md#created).

***

### context?

> `optional` **context?**: [`EventChangeContext`](EventChangeContext.md)

Defined in: [ui/src/api-shared/types/event-history.ts:138](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L138)

***

### eventId

> **eventId**: [`EventId`](../../event/type-aliases/EventId.md)

Defined in: [ui/src/api-shared/types/event-history.ts:135](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L135)

The event this row describes. Never embeds the event itself.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/event-history.ts:133](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L133)

Row id (uuid).

***

### initiator

> **initiator**: [`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

Defined in: [ui/src/api-shared/types/event-history.ts:137](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/event-history.ts#L137)
