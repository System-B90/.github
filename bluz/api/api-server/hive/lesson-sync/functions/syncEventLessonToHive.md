[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / syncEventLessonToHive

# Function: syncEventLessonToHive()

> **syncEventLessonToHive**(`event`, `action`, `controller?`, `previous?`): `void`

Defined in: [ui/src/api-server/hive/lesson-sync.ts:122](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/hive/lesson-sync.ts#L122)

Fire-and-forget hook on the event write routes, mirroring how Google
Calendar sync is attached: it can never fail the Bluz write it accompanies.
Only a running event has anything to push; every other write is a no-op
until the activator reaches the event's start.

Runs with the editing Segel's own Hive credentials.

## Parameters

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The event as stored.

### action

`"upsert"` \| `"delete"`

Whether the event still exists or was just deleted.

### controller?

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

The iteration's Mongo controller.

### previous?

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The event before this write, for an update.

## Returns

`void`

## Example

```typescript
syncEventLessonToHive(updated, "upsert", controller, previous);
```
