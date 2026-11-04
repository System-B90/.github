[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/week-templates/links/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/week-templates/links/route.ts:23](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/app/api/week-templates/links/route.ts#L23)

GET /api/week-templates/links?week=YYYY-MM-DD — the template the week is
linked to (#997). Read-only, so a past iteration (`?it=`) may be asked too.

## Parameters

### request

`NextRequest`

### context?

`any`

## Returns

`Promise`\<`Response`\>
