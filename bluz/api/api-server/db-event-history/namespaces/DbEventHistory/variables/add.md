[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event-history](../../../index.md) / [DbEventHistory](../index.md) / add

# Variable: add

> `const` **add**: (`args`) => `Promise`\<`void`\> = `record`

Defined in: [ui/src/api-server/db-event-history.ts:227](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-event-history.ts#L227)

Append one row describing a write. Never throws: the log is best-effort and
must not take down the write it documents.

## Parameters

### args

#### action

[`EventChangeAction`](../../../../../api-shared/types/event-history/enumerations/EventChangeAction.md)

What kind of write happened.

#### after?

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md) \| `null`

Document after the write (omit for archival).

#### before?

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md) \| `null`

Stored document before the write (null on creation).

#### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)

#### eventId

`string`

Event the change applies to.

#### origin?

[`EventWriteOrigin`](../../../type-aliases/EventWriteOrigin.md)

Declared initiator plus optional context/actor.

## Returns

`Promise`\<`void`\>

## Example

```typescript
await DbEventHistory.record({
    eventId, action: EventChangeAction.Updated,
    before: stored, after: incoming, origin, controller,
});
```
