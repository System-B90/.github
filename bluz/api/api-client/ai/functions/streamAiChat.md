[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / streamAiChat

# Function: streamAiChat()

> **streamAiChat**(`payload`, `signal?`): `AsyncGenerator`\<[`AiStreamEvent`](../../../api-shared/types/ai/type-aliases/AiStreamEvent.md)\>

Defined in: [ui/src/api-client/ai.ts:37](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/ai.ts#L37)

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
