[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiTool

# Type Alias: AiTool\<TArgs\>

> **AiTool**\<`TArgs`\> = `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:64](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L64)

## Type Parameters

### TArgs

`TArgs` = `Record`\<`string`, `unknown`\>

## Properties

### danger

> `readonly` **danger**: [`AiToolDanger`](../../../../../api-shared/types/ai/enumerations/AiToolDanger.md)

Defined in: [ui/src/api-server/ai/tools/types.ts:80](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L80)

How much damage the call can do. Drives the approval card's severity and
whether a second confirmation is required.

***

### describe?

> `optional` **describe?**: (`args`, `context`) => `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:97](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L97)

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

Defined in: [ui/src/api-server/ai/tools/types.ts:73](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L73)

***

### execute

> **execute**: (`args`, `context`) => `Promise`\<[`AiToolResult`](AiToolResult.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:106](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L106)

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

Defined in: [ui/src/api-server/ai/tools/types.ts:104](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L104)

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

Defined in: [ui/src/api-server/ai/tools/types.ts:75](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L75)

Read tools run unattended; write tools need per-call human approval.

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:66](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L66)

Wire name. Shown to the model, never to a human.

***

### nextSteps?

> `readonly` `optional` **nextSteps?**: `string`[]

Defined in: [ui/src/api-server/ai/tools/types.ts:89](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L89)

Instructions appended to a *successful* envelope, telling the model what
to do with the payload it just got. Tool-specific; the generic advice
("do not invent ids") is added by the envelope itself.

***

### parameters

> `readonly` **parameters**: `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-server/ai/tools/types.ts:82](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L82)

JSON Schema for [execute](#execute)'s argument object.

***

### recovery?

> `readonly` `optional` **recovery?**: `string`[]

Defined in: [ui/src/api-server/ai/tools/types.ts:91](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L91)

Recovery instructions prepended when this tool fails.

***

### title

> `readonly` **title**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:72](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/ai/tools/types.ts#L72)

Friendly Hebrew label, shown wherever a human sees this tool — the
timeline chip, the approval card, the capability list. Every tool has
one, so no screen ever has to fall back to the snake_case wire name.
