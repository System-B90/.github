[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiToolContext

# Type Alias: AiToolContext

> **AiToolContext** = `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L33)

Everything a tool may know about the session it runs in.

## Properties

### actor

> **actor**: `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:39](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L39)

The signed-in staff member, for write attribution.

#### displayName

> **displayName**: `string`

#### id

> **id**: `string`

***

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:37](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L37)

Curriculum the user is looking at, when on a Gantt screen.

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../../../../api-shared/types/iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-server/ai/tools/types.ts:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L35)

Target iteration; undefined means the current one.

***

### readController

> **readController**: () => `Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:41](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L41)

Calendar store scoped to [iterationId](#iterationid), resolved lazily.

#### Returns

`Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

***

### writeController

> **writeController**: () => `Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L43)

Same, but refuses a past iteration. Write tools use this one.

#### Returns

`Promise`\<[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)\>
