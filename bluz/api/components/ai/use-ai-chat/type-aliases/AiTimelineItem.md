[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/ai/use-ai-chat](../index.md) / AiTimelineItem

# Type Alias: AiTimelineItem

> **AiTimelineItem** = \{ `calls`: [`AiApprovalCall`](AiApprovalCall.md)[]; `id`: `string`; `kind`: [`Approval`](../enumerations/AiTimelineKind.md#approval); `state`: [`AiApprovalState`](../enumerations/AiApprovalState.md); \} \| \{ `id`: `string`; `kind`: [`Assistant`](../enumerations/AiTimelineKind.md#assistant); `text`: `string`; \} \| \{ `allowFreeText`: `boolean`; `answer?`: `string`; `id`: `string`; `kind`: [`Choice`](../enumerations/AiTimelineKind.md#choice); `options`: [`AiChoiceOption`](../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]; `question`: `string`; `toolCallId`: `string`; \} \| \{ `id`: `string`; `kind`: [`Failure`](../enumerations/AiTimelineKind.md#failure); `message`: `string`; \} \| \{ `id`: `string`; `kind`: [`Thinking`](../enumerations/AiTimelineKind.md#thinking); `text`: `string`; \} \| \{ `detail?`: `unknown`; `durationMs?`: `number`; `id`: `string`; `kind`: [`Tool`](../enumerations/AiTimelineKind.md#tool); `name`: `string`; `state`: [`AiToolState`](../enumerations/AiToolState.md); `summary`: `string`; `title`: `string`; \} \| \{ `id`: `string`; `kind`: [`User`](../enumerations/AiTimelineKind.md#user); `text`: `string`; \}

Defined in: [ui/src/components/ai/use-ai-chat.ts:74](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/ai/use-ai-chat.ts#L74)

## Union Members

### Type Literal

\{ `calls`: [`AiApprovalCall`](AiApprovalCall.md)[]; `id`: `string`; `kind`: [`Approval`](../enumerations/AiTimelineKind.md#approval); `state`: [`AiApprovalState`](../enumerations/AiApprovalState.md); \}

#### calls

> **calls**: [`AiApprovalCall`](AiApprovalCall.md)[]

Every write the model proposed in one turn. A batch is approved or
declined as a unit — "fill five days" is one decision, not five.

#### id

> **id**: `string`

#### kind

> **kind**: [`Approval`](../enumerations/AiTimelineKind.md#approval)

#### state

> **state**: [`AiApprovalState`](../enumerations/AiApprovalState.md)

***

### Type Literal

\{ `id`: `string`; `kind`: [`Assistant`](../enumerations/AiTimelineKind.md#assistant); `text`: `string`; \}

***

### Type Literal

\{ `allowFreeText`: `boolean`; `answer?`: `string`; `id`: `string`; `kind`: [`Choice`](../enumerations/AiTimelineKind.md#choice); `options`: [`AiChoiceOption`](../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]; `question`: `string`; `toolCallId`: `string`; \}

#### allowFreeText

> **allowFreeText**: `boolean`

#### answer?

> `optional` **answer?**: `string`

Set once answered; the buttons become a read-only record.

#### id

> **id**: `string`

#### kind

> **kind**: [`Choice`](../enumerations/AiTimelineKind.md#choice)

#### options

> **options**: [`AiChoiceOption`](../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]

#### question

> **question**: `string`

#### toolCallId

> **toolCallId**: `string`

***

### Type Literal

\{ `id`: `string`; `kind`: [`Failure`](../enumerations/AiTimelineKind.md#failure); `message`: `string`; \}

***

### Type Literal

\{ `id`: `string`; `kind`: [`Thinking`](../enumerations/AiTimelineKind.md#thinking); `text`: `string`; \}

***

### Type Literal

\{ `detail?`: `unknown`; `durationMs?`: `number`; `id`: `string`; `kind`: [`Tool`](../enumerations/AiTimelineKind.md#tool); `name`: `string`; `state`: [`AiToolState`](../enumerations/AiToolState.md); `summary`: `string`; `title`: `string`; \}

#### detail?

> `optional` **detail?**: `unknown`

The envelope the model received, for the details disclosure.

#### durationMs?

> `optional` **durationMs?**: `number`

#### id

> **id**: `string`

#### kind

> **kind**: [`Tool`](../enumerations/AiTimelineKind.md#tool)

#### name

> **name**: `string`

#### state

> **state**: [`AiToolState`](../enumerations/AiToolState.md)

#### summary

> **summary**: `string`

#### title

> **title**: `string`

***

### Type Literal

\{ `id`: `string`; `kind`: [`User`](../enumerations/AiTimelineKind.md#user); `text`: `string`; \}
