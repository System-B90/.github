[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/ai/tools/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/ai/tools/route.ts:15](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/app/api/ai/tools/route.ts#L15)

What the assistant can do, for the chat's capability hint. Also reports
whether AI is configured at all, so the UI can hide the launcher on a
deployment with no key rather than failing on first use, and which model
would actually answer — the personal-settings card shows it so a user with
their own key can tell it apart from the server's default.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
