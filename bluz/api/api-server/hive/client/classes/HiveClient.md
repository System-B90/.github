[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/client](../index.md) / HiveClient

# Class: HiveClient

Defined in: [ui/src/api-server/hive/client.ts:24](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/hive/client.ts#L24)

Bluz's Hive client: the request core (token refresh, 401 retry, 500
backoff, network-error classification, users/classes, lessons and lesson
rules, subjects, modules) lives in `@system-b90/hive-core`; this subclass
adds rooms, a cached student-group list and clearing a group's lesson.

## Extends

- `HiveClient`

## Constructors

### Constructor

> **new HiveClient**(`accessToken`, `refreshToken?`, `hiveBaseUrl?`): `HiveClient`

Defined in: node\_modules/@system-b90/hive-core/dist/client.d.ts:173

#### Parameters

##### accessToken

`string`

##### refreshToken?

`string`

##### hiveBaseUrl?

`string`

#### Returns

`HiveClient`

#### Inherited from

`HiveClientBase.constructor`

## Methods

### clearClassLesson()

> **clearClassLesson**(`classId`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/hive/client.ts:89](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/hive/client.ts#L89)

#### Parameters

##### classId

`number`

#### Returns

`Promise`\<`void`\>

***

### currentAccessToken()

> **currentAccessToken**(): `string`

Defined in: [ui/src/api-server/hive/client.ts:84](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/hive/client.ts#L84)

The access token this client currently holds, for calling another
System-B90 app (Peek-a-Boo) that checks it against Hive.

#### Returns

`string`

***

### getClasses()

> **getClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:32](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/hive/client.ts#L32)

Student groups change rarely and Bluz never writes them, yet every cut,
activation tick and feed fetches them: share one request per Hive instance
for `CLASSES_TTL_MS`. The promise is cached, so concurrent callers share
the in-flight request; a failure is dropped so the next call retries.

#### Returns

`Promise`\<`Class`[]\>

#### Overrides

`HiveClientBase.getClasses`

***

### getRooms()

> **getRooms**(): `Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:65](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/hive/client.ts#L65)

#### Returns

`Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

***

### refreshClasses()

> **refreshClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:59](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/hive/client.ts#L59)

Drops this Hive's cached student groups and fetches them again, for a
caller that just missed a group that may have been created since the
cache filled (the activator and feed, when a shuffle matches no group).

#### Returns

`Promise`\<`Class`[]\>
