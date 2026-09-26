[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/envelope](../index.md) / AiToolEnvelope

# Type Alias: AiToolEnvelope

> **AiToolEnvelope** = `object`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L20)

What the model receives as the content of a `tool` message.

## Properties

### data?

> `optional` **data?**: `unknown`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L25)

Present on success.

***

### error?

> `optional` **error?**: `object`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L27)

Present on failure.

#### kind

> **kind**: [`AiToolErrorKind`](../../types/enumerations/AiToolErrorKind.md)

#### message

> **message**: `string`

***

### next

> **next**: `string`[]

Defined in: [ui/src/api-server/ai/tools/envelope.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L33)

Imperative instructions: what to do with this result.

***

### notes?

> `optional` **notes?**: `string`[]

Defined in: [ui/src/api-server/ai/tools/envelope.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L31)

Transport notes the model must know about, e.g. truncation.

***

### ok

> **ok**: `boolean`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L21)

***

### retryable?

> `optional` **retryable?**: `boolean`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L29)

Whether calling again — with corrected arguments — can succeed.

***

### summary

> **summary**: `string`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L23)

***

### tool

> **tool**: `string`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L22)
