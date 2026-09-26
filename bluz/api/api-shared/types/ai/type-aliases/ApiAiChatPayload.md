[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / ApiAiChatPayload

# Type Alias: ApiAiChatPayload

> **ApiAiChatPayload** = `object`

Defined in: [ui/src/api-shared/types/ai.ts:96](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L96)

Request body of `POST /api/ai/chat`.

## Properties

### approvedToolCallIds?

> `optional` **approvedToolCallIds?**: `string`[]

Defined in: [ui/src/api-shared/types/ai.ts:111](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L111)

Tool-call ids the human approved. A write tool runs only when its id is
listed here, so an approval covers one specific call and nothing else.

***

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:106](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L106)

Curriculum in view, if the user is on a Gantt screen.

***

### iterationId?

> `optional` **iterationId?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:104](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L104)

The iteration the questions are about. Omitted means the current one.

***

### messages

> **messages**: [`AiMessage`](AiMessage.md)[]

Defined in: [ui/src/api-shared/types/ai.ts:102](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L102)

Full transcript, oldest first, excluding the system prompt — the server
owns that. Replay whatever the previous turn's `Done` event returned so
assistant tool calls and their results stay paired.

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:113](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L113)

Overrides the server default; normally unset so no vendor slug leaks.
