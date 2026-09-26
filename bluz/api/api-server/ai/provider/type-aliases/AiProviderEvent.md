[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProviderEvent

# Type Alias: AiProviderEvent

> **AiProviderEvent** = \{ `kind`: `"reasoning"`; `text`: `string`; \} \| \{ `kind`: `"final"`; `result`: [`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md); \} \| \{ `kind`: `"reasoning"`; `text`: `string`; \} \| \{ `kind`: `"text"`; `text`: `string`; \}

Defined in: [ui/src/api-server/ai/provider.ts:37](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/provider.ts#L37)

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

#### text

> **text**: `string`

***

### Type Literal

\{ `kind`: `"final"`; `result`: [`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md); \}

***

### Type Literal

\{ `kind`: `"reasoning"`; `text`: `string`; \}

***

### Type Literal

\{ `kind`: `"text"`; `text`: `string`; \}
