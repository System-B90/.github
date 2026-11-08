[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-transactions](../index.md) / isTransactionUnsupportedError

# Function: isTransactionUnsupportedError()

> **isTransactionUnsupportedError**(`error`): `boolean`

Defined in: [ui/src/api-server/mongo-transactions.ts:11](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/mongo-transactions.ts#L11)

Mongo multi-document transactions require the server to run as a replica
set. A standalone `mongod` — which is how some deployments (and every plain
`docker run mongo`) are set up — rejects them outright, and the driver error
used to escape uncaught and surface as a bare HTTP 500 (#435).

## Parameters

### error

`unknown`

## Returns

`boolean`
