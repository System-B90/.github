[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AI\_MAX\_TOOL\_RESULT\_CHARS

# Variable: AI\_MAX\_TOOL\_RESULT\_CHARS

> `const` **AI\_MAX\_TOOL\_RESULT\_CHARS**: `12000` = `12_000`

Defined in: [ui/src/api-shared/types/ai.ts:270](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types/ai.ts#L270)

Character cap on one tool result before it is truncated. A tool that hands
the model a 200KB curriculum tree spends the whole context window on a
single call — and bills it again on every later turn of the conversation.
