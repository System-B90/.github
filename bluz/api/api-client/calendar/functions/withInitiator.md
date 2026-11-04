[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / withInitiator

# Function: withInitiator()

> **withInitiator**(`props`, `initiator?`): [`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

Defined in: [ui/src/api-client/calendar.ts:91](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-client/calendar.ts#L91)

Declares which user action produced a write, so the server can log it in the
event change log (`api-server/db-event-history.ts`). Sent as a header rather
than in the body: the body is the event document itself, and DELETE carries
only an id. The server never trusts the client for *who* acted — only for
*what kind of action* this was.

## Parameters

### props

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md) \| `undefined`

Caller-supplied request props to merge into.

### initiator?

[`EventChangeInitiator`](../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

The action being performed; omitted ⇒ server logs "unknown".

## Returns

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)
