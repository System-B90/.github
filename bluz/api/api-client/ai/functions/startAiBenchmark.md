[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / startAiBenchmark

# Function: startAiBenchmark()

> **startAiBenchmark**(`signal?`): `Promise`\<[`AiBenchmarkJob`](../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkJob.md)\>

Defined in: [ui/src/api-client/ai.ts:119](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-client/ai.ts#L119)

Starts the assistant self-test in the background (#704).

Returns at once with the job state: the run itself takes minutes, so it
lives on the server and is read back with [fetchAiBenchmarkJob](fetchAiBenchmarkJob.md). The
throttle (one run per hour per user) arrives as a 429 with a readable message.

## Parameters

### signal?

`AbortSignal`

## Returns

`Promise`\<[`AiBenchmarkJob`](../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkJob.md)\>
