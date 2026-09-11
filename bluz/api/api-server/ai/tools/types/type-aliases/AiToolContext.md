[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiToolContext

# Type Alias: AiToolContext

> **AiToolContext** = `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L15)

Everything a tool may know about the session it runs in.

## Properties

### actor

> **actor**: `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L21)

The signed-in staff member, for write attribution.

#### displayName

> **displayName**: `string`

#### id

> **id**: `string`

***

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L19)

Curriculum the user is looking at, when on a Gantt screen.

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../../../../api-shared/types/iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-server/ai/tools/types.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L17)

Target iteration; undefined means the current one.

***

### readController

> **readController**: () => `Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L23)

Calendar store scoped to [iterationId](#iterationid), resolved lazily.

#### Returns

`Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

***

### writeController

> **writeController**: () => `Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L25)

Same, but refuses a past iteration. Write tools use this one.

#### Returns

`Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>
