[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/events/\[id\]/recurrence-exceptions/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/events/\[id\]/recurrence-exceptions/route.ts:26](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/app/api/gantt/events/[id]/recurrence-exceptions/route.ts#L26)

POST: Deletes a single recurring occurrence (the event keeps recurring
everywhere else — only this day is excepted).

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
