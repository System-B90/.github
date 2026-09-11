[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / syncEventLessonToHive

# Function: syncEventLessonToHive()

> **syncEventLessonToHive**(`event`, `action`, `controller?`): `void`

Defined in: [ui/src/api-server/hive/lesson-sync.ts:205](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/lesson-sync.ts#L205)

Fire-and-forget wrapper hung off the event write routes, mirroring how
Google Calendar sync is attached: it runs with the editing Segel's Hive
credentials and can never fail the Bluz write it accompanies. The lesson id
it settles on is written straight back onto the stored event, without going
through `DbEvent.set` — that would re-enter this sync.

## Parameters

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The event as stored.

### action

`"delete"` \| `"upsert"`

Whether the event still exists or was just deleted.

### controller?

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

The iteration's Mongo controller.

## Returns

`void`

## Example

```typescript
syncEventLessonToHive(updated, "upsert", controller);
```
