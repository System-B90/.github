[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-activation](../index.md) / runLessonActivationTick

# Function: runLessonActivationTick()

> **runLessonActivationTick**(`now?`, `controller?`, `client?`): `Promise`\<[`HiveActivationTickResult`](../../../../api-shared/types/hive-activation/type-aliases/HiveActivationTickResult.md)\>

Defined in: [ui/src/api-server/hive/lesson-activation.ts:93](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/hive/lesson-activation.ts#L93)

Runs one activation pass over the current iteration.

Idempotent: re-running it inside the same event occurrence assigns nothing
further. Never throws — a Hive outage degrades to a logged failure count so
the timer keeps ticking and recovers by itself on the next pass.

## Parameters

### now?

`Date` = `...`

The moment to evaluate (injectable for tests).

### controller?

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md)

Iteration controller; defaults to the current iteration's.

### client?

[`HiveClient`](../../client/classes/HiveClient.md)

Hive client; defaults to the service account.

## Returns

`Promise`\<[`HiveActivationTickResult`](../../../../api-shared/types/hive-activation/type-aliases/HiveActivationTickResult.md)\>

What the pass did.
