[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/service-client](../index.md) / createHiveServiceClient

# Function: createHiveServiceClient()

> **createHiveServiceClient**(`hiveUrl?`): `Promise`\<[`HiveClient`](../../client/classes/HiveClient.md)\>

Defined in: [ui/src/api-server/hive/service-client.ts:56](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/hive/service-client.ts#L56)

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
