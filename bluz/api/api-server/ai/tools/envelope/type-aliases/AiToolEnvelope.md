[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/envelope](../index.md) / AiToolEnvelope

# Type Alias: AiToolEnvelope

> **AiToolEnvelope** = `object`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:21](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L21)

What the model receives as the content of a `tool` message.

## Properties

### data?

> `optional` **data?**: `unknown`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:26](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L26)

Present on success.

***

### error?

> `optional` **error?**: `object`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:28](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L28)

Present on failure.

#### kind

> **kind**: [`AiToolErrorKind`](../../types/enumerations/AiToolErrorKind.md)

#### message

> **message**: `string`

***

### next

> **next**: `string`[]

Defined in: [ui/src/api-server/ai/tools/envelope.ts:34](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L34)

Imperative instructions: what to do with this result.

***

### notes?

> `optional` **notes?**: `string`[]

Defined in: [ui/src/api-server/ai/tools/envelope.ts:32](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L32)

Transport notes the model must know about, e.g. truncation.

***

### ok

> **ok**: `boolean`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:22](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L22)

***

### retryable?

> `optional` **retryable?**: `boolean`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:30](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L30)

Whether calling again — with corrected arguments — can succeed.

***

### summary

> **summary**: `string`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:24](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L24)

***

### tool

> **tool**: `string`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:23](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tools/envelope.ts#L23)
