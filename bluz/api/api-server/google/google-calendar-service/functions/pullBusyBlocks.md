[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pullBusyBlocks

# Function: pullBusyBlocks()

> **pullBusyBlocks**(`userId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:1012](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/google/google-calendar-service.ts#L1012)

Reads the user's Google free/busy blocks over the next 30 days so Bluz can
surface external conflicts. Returns an empty array on any failure
(unconfigured, not connected, offline) rather than throwing.

## Parameters

### userId

`string`

## Returns

`Promise`\<`object`[]\>
