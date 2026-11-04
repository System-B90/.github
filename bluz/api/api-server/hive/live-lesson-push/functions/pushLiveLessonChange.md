[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/live-lesson-push](../index.md) / pushLiveLessonChange

# Function: pushLiveLessonChange()

> **pushLiveLessonChange**(`client`, `db`, `change`, `now?`): `Promise`\<[`LiveLessonPushResult`](../type-aliases/LiveLessonPushResult.md)\>

Defined in: [ui/src/api-server/hive/live-lesson-push.ts:168](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/hive/live-lesson-push.ts#L168)

Pushes an edit of a live event to Hive and moves the activation ledger to
match, so the activator neither repeats nor undoes it.

Does nothing when Hive drives lessons from the ICS feed: its own
`update_schedule` task owns the classes then. Never throws for a single
group — each failure is collected so the rest still go through.

## Parameters

### client

[`HiveClient`](../../client/classes/HiveClient.md)

Hive client to push with.

### db

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md)

The iteration's Mongo controller.

### change

[`LiveLessonChange`](../type-aliases/LiveLessonChange.md)

The edit.

### now?

`Date` = `...`

The moment of the edit (injectable for tests).

## Returns

`Promise`\<[`LiveLessonPushResult`](../type-aliases/LiveLessonPushResult.md)\>

What was pushed, and what failed.
