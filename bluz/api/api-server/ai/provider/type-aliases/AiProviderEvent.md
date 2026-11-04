[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProviderEvent

# Type Alias: AiProviderEvent

> **AiProviderEvent** = \{ `kind`: `"reasoning"`; `text`: `string`; \} \| \{ `kind`: `"final"`; `result`: [`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md); \} \| \{ `kind`: `"text"`; `text`: `string`; \}

Defined in: [ui/src/api-server/ai/provider.ts:40](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/provider.ts#L40)

Provider-level stream frame. Deliberately narrower than the app-level
`AiStreamEvent`: a provider knows about text and completions, not about
tool approval or Bluz's transcript.

## Union Members

### Type Literal

\{ `kind`: `"reasoning"`; `text`: `string`; \}

#### kind

> **kind**: `"reasoning"`

Private chain-of-thought, on backends that expose it. Kept
separate from `text` so the UI can collapse it: merged into the
answer it would read as the assistant thinking out loud at the
user, and it is not part of the transcript replayed next turn.
Distinct from an answer wrapped in <think> tags, which arrives as
ordinary `text` and is split client-side.

#### text

> **text**: `string`

***

### Type Literal

\{ `kind`: `"final"`; `result`: [`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md); \}

***

### Type Literal

\{ `kind`: `"text"`; `text`: `string`; \}
