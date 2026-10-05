[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / streamAiChat

# Function: streamAiChat()

> **streamAiChat**(`payload`, `signal?`): `AsyncGenerator`\<[`AiStreamEvent`](../../../api-shared/types/ai/type-aliases/AiStreamEvent.md)\>

Defined in: [ui/src/api-client/ai.ts:39](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-client/ai.ts#L39)

Opens a turn and yields its events as they arrive.

Errors before the stream opens surface as a thrown `ClientApiError` (the
route still answers a real status there); errors after it opens arrive as a
terminal [AiStreamEventType.Error](../../../api-shared/types/ai/enumerations/AiStreamEventType.md#error) event.

## Parameters

### payload

[`ApiAiChatPayload`](../../../api-shared/types/ai/type-aliases/ApiAiChatPayload.md)

Transcript, scope, and any approved tool-call ids.

### signal?

`AbortSignal`

Aborts the turn — pass the one your "stop" button owns.

## Returns

`AsyncGenerator`\<[`AiStreamEvent`](../../../api-shared/types/ai/type-aliases/AiStreamEvent.md)\>

## Example

```ts
for await (const event of streamAiChat({ messages }, controller.signal)) {
    if (event.type === AiStreamEventType.Delta) append(event.text);
}
```
