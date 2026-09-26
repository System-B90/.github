[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiTool

# Type Alias: AiTool\<TArgs\>

> **AiTool**\<`TArgs`\> = `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:53](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L53)

## Type Parameters

### TArgs

`TArgs` = `Record`\<`string`, `unknown`\>

## Properties

### danger

> `readonly` **danger**: [`AiToolDanger`](../../../../../api-shared/types/ai/enumerations/AiToolDanger.md)

Defined in: [ui/src/api-server/ai/tools/types.ts:69](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L69)

How much damage the call can do. Drives the approval card's severity and
whether a second confirmation is required.

***

### describe?

> `optional` **describe?**: (`args`, `context`) => `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:86](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L86)

Describes what running this call would do, for the approval prompt.
Only meaningful for [AiToolKind.Write](../../../../../api-shared/types/ai/enumerations/AiToolKind.md#write).

#### Parameters

##### args

`TArgs`

##### context

[`AiToolContext`](AiToolContext.md)

#### Returns

`string`

***

### description

> `readonly` **description**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:62](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L62)

***

### execute

> **execute**: (`args`, `context`) => `Promise`\<[`AiToolResult`](AiToolResult.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:95](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L95)

#### Parameters

##### args

`TArgs`

##### context

[`AiToolContext`](AiToolContext.md)

#### Returns

`Promise`\<[`AiToolResult`](AiToolResult.md)\>

***

### impact?

> `optional` **impact?**: (`args`, `context`) => `string`[]

Defined in: [ui/src/api-server/ai/tools/types.ts:93](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L93)

The concrete consequences of approving, one Hebrew bullet each. The
human reads these, not the JSON arguments, so they must name real
effects ("מוחק 12 אירועים") rather than restate the call.

#### Parameters

##### args

`TArgs`

##### context

[`AiToolContext`](AiToolContext.md)

#### Returns

`string`[]

***

### kind

> `readonly` **kind**: [`AiToolKind`](../../../../../api-shared/types/ai/enumerations/AiToolKind.md)

Defined in: [ui/src/api-server/ai/tools/types.ts:64](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L64)

Read tools run unattended; write tools need per-call human approval.

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:55](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L55)

Wire name. Shown to the model, never to a human.

***

### nextSteps?

> `readonly` `optional` **nextSteps?**: `string`[]

Defined in: [ui/src/api-server/ai/tools/types.ts:78](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L78)

Instructions appended to a *successful* envelope, telling the model what
to do with the payload it just got. Tool-specific; the generic advice
("do not invent ids") is added by the envelope itself.

***

### parameters

> `readonly` **parameters**: `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-server/ai/tools/types.ts:71](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L71)

JSON Schema for [execute](#execute)'s argument object.

***

### recovery?

> `readonly` `optional` **recovery?**: `string`[]

Defined in: [ui/src/api-server/ai/tools/types.ts:80](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L80)

Recovery instructions prepended when this tool fails.

***

### title

> `readonly` **title**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:61](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L61)

Friendly Hebrew label, shown wherever a human sees this tool — the
timeline chip, the approval card, the capability list. Every tool has
one, so no screen ever has to fall back to the snake_case wire name.
