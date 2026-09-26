[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiStreamEvent

# Type Alias: AiStreamEvent

> **AiStreamEvent** = \{ `allowFreeText`: `boolean`; `options`: [`AiChoiceOption`](AiChoiceOption.md)[]; `question`: `string`; `toolCallId`: `string`; `type`: [`Choice`](../enumerations/AiStreamEventType.md#choice); \} \| \{ `text`: `string`; `type`: [`Delta`](../enumerations/AiStreamEventType.md#delta); \} \| \{ `awaitingApproval`: `boolean`; `messages`: [`AiMessage`](AiMessage.md)[]; `model`: `string`; `type`: [`Done`](../enumerations/AiStreamEventType.md#done); `usage?`: [`AiUsage`](AiUsage.md); \} \| \{ `message`: `string`; `messages?`: [`AiMessage`](AiMessage.md)[]; `type`: [`Error`](../enumerations/AiStreamEventType.md#error); \} \| \{ `text`: `string`; `type`: [`Reasoning`](../enumerations/AiStreamEventType.md#reasoning); \} \| \{ `text`: `string`; `type`: [`ReasoningDelta`](../enumerations/AiStreamEventType.md#reasoningdelta); \} \| \{ `arguments`: `unknown`; `danger`: [`AiToolDanger`](../enumerations/AiToolDanger.md); `impact?`: `string`[]; `name`: `string`; `summary`: `string`; `title`: `string`; `toolCallId`: `string`; `type`: [`ToolProposal`](../enumerations/AiStreamEventType.md#toolproposal); \} \| \{ `detail?`: `unknown`; `durationMs?`: `number`; `name`: `string`; `ok`: `boolean`; `summary`: `string`; `title`: `string`; `toolCallId`: `string`; `type`: [`ToolResult`](../enumerations/AiStreamEventType.md#toolresult); \} \| \{ `name`: `string`; `title`: `string`; `toolCallId`: `string`; `type`: [`ToolStart`](../enumerations/AiStreamEventType.md#toolstart); \}

Defined in: [ui/src/api-shared/types/ai.ts:167](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L167)

One frame of a streamed turn. A turn ends with exactly one `Done` **or**
one `Error`, never both.

## Union Members

### Type Literal

\{ `allowFreeText`: `boolean`; `options`: [`AiChoiceOption`](AiChoiceOption.md)[]; `question`: `string`; `toolCallId`: `string`; `type`: [`Choice`](../enumerations/AiStreamEventType.md#choice); \}

#### allowFreeText

> **allowFreeText**: `boolean`

Whether the human may type an answer instead of picking one.

#### options

> **options**: [`AiChoiceOption`](AiChoiceOption.md)[]

#### question

> **question**: `string`

#### toolCallId

> **toolCallId**: `string`

The `ask_user` call this answers; the client writes its result.

#### type

> **type**: [`Choice`](../enumerations/AiStreamEventType.md#choice)

***

### Type Literal

\{ `text`: `string`; `type`: [`Delta`](../enumerations/AiStreamEventType.md#delta); \}

***

### Type Literal

\{ `awaitingApproval`: `boolean`; `messages`: [`AiMessage`](AiMessage.md)[]; `model`: `string`; `type`: [`Done`](../enumerations/AiStreamEventType.md#done); `usage?`: [`AiUsage`](AiUsage.md); \}

#### awaitingApproval

> **awaitingApproval**: `boolean`

True when the turn stopped on a pending write approval.

#### messages

> **messages**: [`AiMessage`](AiMessage.md)[]

The turn's new messages, to be appended to the transcript and
replayed on the next request. Includes assistant tool calls and
their tool results so an approved call resumes with its context.

#### model

> **model**: `string`

#### type

> **type**: [`Done`](../enumerations/AiStreamEventType.md#done)

#### usage?

> `optional` **usage?**: [`AiUsage`](AiUsage.md)

***

### Type Literal

\{ `message`: `string`; `messages?`: [`AiMessage`](AiMessage.md)[]; `type`: [`Error`](../enumerations/AiStreamEventType.md#error); \}

#### message

> **message**: `string`

#### messages?

> `optional` **messages?**: [`AiMessage`](AiMessage.md)[]

The turn's produced messages so far, if any tool calls ran before
the failure. Optional: a pre-stream failure (auth, validation)
has none. When present the client should still append it to the
transcript before showing the error, so a retried turn does not
replay tool calls the server already executed.

#### type

> **type**: [`Error`](../enumerations/AiStreamEventType.md#error)

***

### Type Literal

\{ `text`: `string`; `type`: [`Reasoning`](../enumerations/AiStreamEventType.md#reasoning); \}

***

### Type Literal

\{ `text`: `string`; `type`: [`ReasoningDelta`](../enumerations/AiStreamEventType.md#reasoningdelta); \}

***

### Type Literal

\{ `arguments`: `unknown`; `danger`: [`AiToolDanger`](../enumerations/AiToolDanger.md); `impact?`: `string`[]; `name`: `string`; `summary`: `string`; `title`: `string`; `toolCallId`: `string`; `type`: [`ToolProposal`](../enumerations/AiStreamEventType.md#toolproposal); \}

#### arguments

> **arguments**: `unknown`

Parsed arguments, for showing the human what will change.

#### danger

> **danger**: [`AiToolDanger`](../enumerations/AiToolDanger.md)

#### impact?

> `optional` **impact?**: `string`[]

Hebrew bullets: the concrete consequences of approving.

#### name

> **name**: `string`

#### summary

> **summary**: `string`

Hebrew, one line: what approving this will do.

#### title

> **title**: `string`

Friendly Hebrew label for name.

#### toolCallId

> **toolCallId**: `string`

#### type

> **type**: [`ToolProposal`](../enumerations/AiStreamEventType.md#toolproposal)

***

### Type Literal

\{ `detail?`: `unknown`; `durationMs?`: `number`; `name`: `string`; `ok`: `boolean`; `summary`: `string`; `title`: `string`; `toolCallId`: `string`; `type`: [`ToolResult`](../enumerations/AiStreamEventType.md#toolresult); \}

#### detail?

> `optional` **detail?**: `unknown`

The envelope handed to the model, for the details panel.

#### durationMs?

> `optional` **durationMs?**: `number`

Wall-clock duration of the call, for the timeline chip.

#### name

> **name**: `string`

#### ok

> **ok**: `boolean`

#### summary

> **summary**: `string`

#### title

> **title**: `string`

#### toolCallId

> **toolCallId**: `string`

#### type

> **type**: [`ToolResult`](../enumerations/AiStreamEventType.md#toolresult)

***

### Type Literal

\{ `name`: `string`; `title`: `string`; `toolCallId`: `string`; `type`: [`ToolStart`](../enumerations/AiStreamEventType.md#toolstart); \}
