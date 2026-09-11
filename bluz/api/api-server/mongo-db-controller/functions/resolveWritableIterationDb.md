[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / resolveWritableIterationDb

# Function: resolveWritableIterationDb()

> **resolveWritableIterationDb**(`iterationId?`): `Promise`\<[`DatabaseController`](../classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:544](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/mongo-db-controller.ts#L544)

Like [resolveIterationDb](resolveIterationDb.md) but also rejects past (non-current) iterations.
Avoids the double Mongo lookup of calling resolveIterationDb + assertWritable separately.

## Parameters

### iterationId?

`string`

## Returns

`Promise`\<[`DatabaseController`](../classes/DatabaseController.md)\>
