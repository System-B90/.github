[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AI\_MAX\_TOOL\_RESULT\_CHARS

# Variable: AI\_MAX\_TOOL\_RESULT\_CHARS

> `const` **AI\_MAX\_TOOL\_RESULT\_CHARS**: `12000` = `12_000`

Defined in: [ui/src/api-shared/types/ai.ts:265](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/ai.ts#L265)

Character cap on one tool result before it is truncated. A tool that hands
the model a 200KB curriculum tree spends the whole context window on a
single call — and bills it again on every later turn of the conversation.
