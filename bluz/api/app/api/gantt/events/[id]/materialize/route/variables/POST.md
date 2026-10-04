[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/events/\[id\]/materialize/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/events/\[id\]/materialize/route.ts:28](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/app/api/gantt/events/[id]/materialize/route.ts#L28)

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
