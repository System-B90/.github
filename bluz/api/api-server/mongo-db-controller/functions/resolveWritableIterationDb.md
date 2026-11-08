[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / resolveWritableIterationDb

# Function: resolveWritableIterationDb()

> **resolveWritableIterationDb**(`iterationId?`): `Promise`\<[`DatabaseController`](../classes/DatabaseController.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:641](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/mongo-db-controller.ts#L641)

Like [resolveIterationDb](resolveIterationDb.md) but also rejects past (non-current) iterations.
Avoids the double Mongo lookup of calling resolveIterationDb + assertWritable separately.

## Parameters

### iterationId?

`string`

## Returns

`Promise`\<[`DatabaseController`](../classes/DatabaseController.md)\>
