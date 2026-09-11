[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / ApiAiChatPayload

# Type Alias: ApiAiChatPayload

> **ApiAiChatPayload** = `object`

Defined in: [ui/src/api-shared/types/ai.ts:63](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L63)

Request body of `POST /api/ai/chat`.

## Properties

### approvedToolCallIds?

> `optional` **approvedToolCallIds?**: `string`[]

Defined in: [ui/src/api-shared/types/ai.ts:78](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L78)

Tool-call ids the human approved. A write tool runs only when its id is
listed here, so an approval covers one specific call and nothing else.

***

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:73](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L73)

Curriculum in view, if the user is on a Gantt screen.

***

### iterationId?

> `optional` **iterationId?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:71](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L71)

The iteration the questions are about. Omitted means the current one.

***

### messages

> **messages**: [`AiMessage`](AiMessage.md)[]

Defined in: [ui/src/api-shared/types/ai.ts:69](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L69)

Full transcript, oldest first, excluding the system prompt — the server
owns that. Replay whatever the previous turn's `Done` event returned so
assistant tool calls and their results stay paired.

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:80](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L80)

Overrides the server default; normally unset so no vendor slug leaks.
