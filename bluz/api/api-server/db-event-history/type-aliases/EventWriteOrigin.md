[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-event-history](../index.md) / EventWriteOrigin

# Type Alias: EventWriteOrigin

> **EventWriteOrigin** = `object`

Defined in: [ui/src/api-server/db-event-history.ts:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event-history.ts#L29)

Who/what is performing a write. Actor identity is always resolved
server-side from the session; only the initiator is declared by the caller.

## Properties

### actor?

> `optional` **actor?**: \{ `displayName`: `string`; `id`: `string`; \} \| `null`

Defined in: [ui/src/api-server/db-event-history.ts:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event-history.ts#L36)

Pre-resolved actor, for bulk writes that would otherwise resolve the
session once per event (cut, reload, snapshot restore).

***

### context?

> `optional` **context?**: [`EventChangeContext`](../../../api-shared/types/event-history/type-aliases/EventChangeContext.md)

Defined in: [ui/src/api-server/db-event-history.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event-history.ts#L31)

***

### initiator

> **initiator**: [`EventChangeInitiator`](../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

Defined in: [ui/src/api-server/db-event-history.ts:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event-history.ts#L30)
