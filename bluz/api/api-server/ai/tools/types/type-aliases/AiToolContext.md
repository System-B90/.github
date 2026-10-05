[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiToolContext

# Type Alias: AiToolContext

> **AiToolContext** = `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:33](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L33)

Everything a tool may know about the session it runs in.

## Properties

### actor

> **actor**: `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:44](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L44)

The signed-in staff member, for write attribution.

#### displayName

> **displayName**: `string`

#### id

> **id**: `string`

***

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:37](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L37)

Curriculum the user is looking at, when on a Gantt screen.

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../../../../api-shared/types/iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-server/ai/tools/types.ts:35](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L35)

Target iteration; undefined means the current one.

***

### now?

> `optional` **now?**: `Date`

Defined in: [ui/src/api-server/ai/tools/types.ts:42](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L42)

The moment the turn treats as "now". Defaults to the wall clock; the
self-test pins it so "Tuesday" resolves to the same date every run.

***

### readController

> **readController**: () => `Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:46](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L46)

Calendar store scoped to [iterationId](#iterationid), resolved lazily.

#### Returns

`Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

***

### writeController

> **writeController**: () => `Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:48](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L48)

Same, but refuses a past iteration. Write tools use this one.

#### Returns

`Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>
