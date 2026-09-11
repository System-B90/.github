[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/ai/use-ai-chat](../index.md) / useAiChat

# Function: useAiChat()

> **useAiChat**(`scope`): `object`

Defined in: [ui/src/components/ai/use-ai-chat.ts:55](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/ai/use-ai-chat.ts#L55)

## Parameters

### scope

[`AiChatScope`](../type-aliases/AiChatScope.md)

## Returns

### approve

> **approve**: () => `void`

#### Returns

`void`

### busy

> **busy**: `boolean`

### error

> **error**: `string` \| `null`

### pendingApproval

> **pendingApproval**: [`AiPendingApproval`](../type-aliases/AiPendingApproval.md) \| `null`

### reject

> **reject**: () => `void`

Declining still has to answer the model's tool call. An unanswered call
would make every later request malformed, so the refusal is written into
the transcript as the call's result.

#### Returns

`void`

### reset

> **reset**: () => `void`

#### Returns

`void`

### send

> **send**: (`text`) => `void`

#### Parameters

##### text

`string`

#### Returns

`void`

### stop

> **stop**: () => `void`

#### Returns

`void`

### timeline

> **timeline**: [`AiTimelineItem`](../type-aliases/AiTimelineItem.md)[]
