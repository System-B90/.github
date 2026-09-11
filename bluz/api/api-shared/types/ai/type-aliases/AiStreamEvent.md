[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiStreamEvent

# Type Alias: AiStreamEvent

> **AiStreamEvent** = \{ `text`: `string`; `type`: [`Delta`](../enumerations/AiStreamEventType.md#delta); \} \| \{ `awaitingApproval`: `boolean`; `messages`: [`AiMessage`](AiMessage.md)[]; `model`: `string`; `type`: [`Done`](../enumerations/AiStreamEventType.md#done); `usage?`: [`AiUsage`](AiUsage.md); \} \| \{ `message`: `string`; `messages?`: [`AiMessage`](AiMessage.md)[]; `type`: [`Error`](../enumerations/AiStreamEventType.md#error); \} \| \{ `arguments`: `unknown`; `name`: `string`; `summary`: `string`; `toolCallId`: `string`; `type`: [`ToolProposal`](../enumerations/AiStreamEventType.md#toolproposal); \} \| \{ `name`: `string`; `ok`: `boolean`; `summary`: `string`; `toolCallId`: `string`; `type`: [`ToolResult`](../enumerations/AiStreamEventType.md#toolresult); \} \| \{ `name`: `string`; `toolCallId`: `string`; `type`: [`ToolStart`](../enumerations/AiStreamEventType.md#toolstart); \}

Defined in: [ui/src/api-shared/types/ai.ts:122](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L122)

One frame of a streamed turn. A turn ends with exactly one `Done` **or**
one `Error`, never both.

## Union Members

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

\{ `arguments`: `unknown`; `name`: `string`; `summary`: `string`; `toolCallId`: `string`; `type`: [`ToolProposal`](../enumerations/AiStreamEventType.md#toolproposal); \}

#### arguments

> **arguments**: `unknown`

Parsed arguments, for showing the human what will change.

#### name

> **name**: `string`

#### summary

> **summary**: `string`

Hebrew, one line: what approving this will do.

#### toolCallId

> **toolCallId**: `string`

#### type

> **type**: [`ToolProposal`](../enumerations/AiStreamEventType.md#toolproposal)

***

### Type Literal

\{ `name`: `string`; `ok`: `boolean`; `summary`: `string`; `toolCallId`: `string`; `type`: [`ToolResult`](../enumerations/AiStreamEventType.md#toolresult); \}

***

### Type Literal

\{ `name`: `string`; `toolCallId`: `string`; `type`: [`ToolStart`](../enumerations/AiStreamEventType.md#toolstart); \}
