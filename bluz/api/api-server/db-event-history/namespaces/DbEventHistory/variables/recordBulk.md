[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event-history](../../../index.md) / [DbEventHistory](../index.md) / recordBulk

# Variable: recordBulk

> `const` **recordBulk**: (`args`) => `Promise`\<`void`\> = `recordMany`

Defined in: [ui/src/api-server/db-event-history.ts:228](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/db-event-history.ts#L228)

Bulk variant of [record](add.md) for cut/reload writes.

## Parameters

### args

#### action

[`EventChangeAction`](../../../../../api-shared/types/event-history/enumerations/EventChangeAction.md)

#### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)

#### events

`object`[]

#### origin

[`EventWriteOrigin`](../../../type-aliases/EventWriteOrigin.md)

## Returns

`Promise`\<`void`\>
