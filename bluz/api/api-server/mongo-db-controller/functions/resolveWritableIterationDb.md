[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / resolveWritableIterationDb

# Function: resolveWritableIterationDb()

> **resolveWritableIterationDb**(`iterationId?`): `Promise`\<[`DatabaseController`](../classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:641](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/mongo-db-controller.ts#L641)

Like [resolveIterationDb](resolveIterationDb.md) but also rejects past (non-current) iterations.
Avoids the double Mongo lookup of calling resolveIterationDb + assertWritable separately.

## Parameters

### iterationId?

`string`

## Returns

`Promise`\<[`DatabaseController`](../classes/DatabaseController.md)\>
