[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pullBusyBlocks

# Function: pullBusyBlocks()

> **pullBusyBlocks**(`userId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:836](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/google/google-calendar-service.ts#L836)

Reads the user's Google free/busy blocks over the next 30 days so Bluz can
surface external conflicts. Returns an empty array on any failure
(unconfigured, not connected, offline) rather than throwing.

## Parameters

### userId

`string`

## Returns

`Promise`\<`object`[]\>
