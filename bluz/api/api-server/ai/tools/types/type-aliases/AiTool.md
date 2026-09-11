[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiTool

# Type Alias: AiTool\<TArgs\>

> **AiTool**\<`TArgs`\> = `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L35)

## Type Parameters

### TArgs

`TArgs` = `Record`\<`string`, `unknown`\>

## Properties

### describe?

> `optional` **describe?**: (`args`, `context`) => `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L47)

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

Defined in: [ui/src/api-server/ai/tools/types.ts:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L37)

***

### execute

> **execute**: (`args`, `context`) => `Promise`\<[`AiToolResult`](AiToolResult.md)\>

Defined in: [ui/src/api-server/ai/tools/types.ts:49](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L49)

#### Parameters

##### args

`TArgs`

##### context

[`AiToolContext`](AiToolContext.md)

#### Returns

`Promise`\<[`AiToolResult`](AiToolResult.md)\>

***

### kind

> `readonly` **kind**: [`AiToolKind`](../../../../../api-shared/types/ai/enumerations/AiToolKind.md)

Defined in: [ui/src/api-server/ai/tools/types.ts:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L39)

Read tools run unattended; write tools need per-call human approval.

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L36)

***

### parameters

> `readonly` **parameters**: `Record`\<`string`, `unknown`\>

Defined in: [ui/src/api-server/ai/tools/types.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/tools/types.ts#L41)

JSON Schema for [execute](#execute)'s argument object.
