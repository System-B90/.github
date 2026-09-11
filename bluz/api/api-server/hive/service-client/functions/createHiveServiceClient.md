[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/service-client](../index.md) / createHiveServiceClient

# Function: createHiveServiceClient()

> **createHiveServiceClient**(`hiveUrl?`): `Promise`\<[`HiveClient`](../../client/classes/HiveClient.md)\>

Defined in: [ui/src/api-server/hive/service-client.ts:55](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/service-client.ts#L55)

A Hive client authenticated as the Bluz service account.

## Parameters

### hiveUrl?

`string`

Hive instance to target; defaults to `NEXT_PUBLIC_HIVE_URL`.

## Returns

`Promise`\<[`HiveClient`](../../client/classes/HiveClient.md)\>

A client acting as the service account.

## Throws

HiveClientError when credentials are missing or Hive rejects them.

## Example

```typescript
const hive = await createHiveServiceClient();
await hive.setLessonForClass(classId, lessonId);
```
