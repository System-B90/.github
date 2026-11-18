[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/events/\[id\]/materialize/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/events/\[id\]/materialize/route.ts:28](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/app/api/gantt/events/[id]/materialize/route.ts#L28)

POST: Materializes a recurring occurrence into its own standalone event,
mapped onto the occurrence day, and excepts the source event from
echoing onto that day going forward.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
