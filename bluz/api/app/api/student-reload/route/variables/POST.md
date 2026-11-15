[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/student-reload/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/student-reload/route.ts:14](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/app/api/student-reload/route.ts#L14)

POST /api/student-reload — staff "push update": every open student board
reloads the page over its existing socket.

Staff-only, and deliberately outside `student-view/`: a student must not be
able to reload everyone else's screen.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
