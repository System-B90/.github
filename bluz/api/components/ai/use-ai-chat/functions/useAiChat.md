[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/ai/use-ai-chat](../index.md) / useAiChat

# Function: useAiChat()

> **useAiChat**(`scope`): `object`

Defined in: [ui/src/components/ai/use-ai-chat.ts:134](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/ai/use-ai-chat.ts#L134)

## Parameters

### scope

[`AiChatScope`](../type-aliases/AiChatScope.md)

## Returns

### answerChoice

> **answerChoice**: (`value`) => `void`

Answers an `ask_user` question. The server never ran that tool — it
streamed the question and stopped — so the answer is authored here and
the turn resumes with it in place.

#### Parameters

##### value

`string`

#### Returns

`void`

### approve

> **approve**: () => `void`

#### Returns

`void`

### busy

> **busy**: `boolean`

### exportChat

> **exportChat**: (`format`) => `void`

Downloads the conversation, tool calls, results, and CoT included.

#### Parameters

##### format

[`ChatExportFormat`](../../chat-export/enumerations/ChatExportFormat.md)

#### Returns

`void`

### pendingApproval

> **pendingApproval**: \{ `calls`: [`AiApprovalCall`](../type-aliases/AiApprovalCall.md)[]; `id`: `string`; `kind`: [`Approval`](../enumerations/AiTimelineKind.md#approval); `state`: [`AiApprovalState`](../enumerations/AiApprovalState.md); \} \| `undefined`

The write currently awaiting a decision, if any.

#### Union Members

##### Type Literal

\{ `calls`: [`AiApprovalCall`](../type-aliases/AiApprovalCall.md)[]; `id`: `string`; `kind`: [`Approval`](../enumerations/AiTimelineKind.md#approval); `state`: [`AiApprovalState`](../enumerations/AiApprovalState.md); \}

##### calls

> **calls**: [`AiApprovalCall`](../type-aliases/AiApprovalCall.md)[]

Every write the model proposed in one turn. A batch is approved or
declined as a unit — "fill five days" is one decision, not five.

##### id

> **id**: `string`

##### kind

> **kind**: [`Approval`](../enumerations/AiTimelineKind.md#approval)

##### state

> **state**: [`AiApprovalState`](../enumerations/AiApprovalState.md)

***

`undefined`

### pendingChoice

> **pendingChoice**: \{ `allowFreeText`: `boolean`; `answer?`: `string`; `id`: `string`; `kind`: [`Choice`](../enumerations/AiTimelineKind.md#choice); `options`: [`AiChoiceOption`](../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]; `question`: `string`; `toolCallId`: `string`; \} \| `undefined`

The question currently awaiting an answer, if any.

#### Union Members

##### Type Literal

\{ `allowFreeText`: `boolean`; `answer?`: `string`; `id`: `string`; `kind`: [`Choice`](../enumerations/AiTimelineKind.md#choice); `options`: [`AiChoiceOption`](../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]; `question`: `string`; `toolCallId`: `string`; \}

##### allowFreeText

> **allowFreeText**: `boolean`

##### answer?

> `optional` **answer?**: `string`

Set once answered; the buttons become a read-only record.

##### id

> **id**: `string`

##### kind

> **kind**: [`Choice`](../enumerations/AiTimelineKind.md#choice)

##### options

> **options**: [`AiChoiceOption`](../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]

##### question

> **question**: `string`

##### toolCallId

> **toolCallId**: `string`

***

`undefined`

### reject

> **reject**: () => `void`

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

### stats

> **stats**: [`AiChatStats`](../type-aliases/AiChatStats.md)

### stop

> **stop**: () => `void`

#### Returns

`void`

### timeline

> **timeline**: [`AiTimelineItem`](../type-aliases/AiTimelineItem.md)[]
