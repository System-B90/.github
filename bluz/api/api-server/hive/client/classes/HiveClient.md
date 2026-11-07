[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/client](../index.md) / HiveClient

# Class: HiveClient

Defined in: [ui/src/api-server/hive/client.ts:33](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/client.ts#L33)

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

Defined in: [ui/src/api-server/hive/client.ts:106](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/client.ts#L106)

#### Parameters

##### classId

`number`

#### Returns

`Promise`\<`void`\>

***

### currentAccessToken()

> **currentAccessToken**(): `string`

Defined in: [ui/src/api-server/hive/client.ts:101](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/client.ts#L101)

The access token this client currently holds, for calling another
System-B90 app (Peek-a-Boo) that checks it against Hive.

#### Returns

`string`

***

### getClasses()

> **getClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:41](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/client.ts#L41)

Student groups change rarely and Bluz never writes them, yet every cut,
activation tick and feed fetches them: share one request per Hive instance
for `CLASSES_TTL_MS`. The promise is cached, so concurrent callers share
the in-flight request; a failure is dropped so the next call retries.

#### Returns

`Promise`\<`Class`[]\>

#### Overrides

`HiveClientBase.getClasses`

***

### getEventCategories()

> **getEventCategories**(): `Promise`\<[`HiveEventCategory`](../type-aliases/HiveEventCategory.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:84](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/client.ts#L84)

Hive's schedule event categories (Segel clearance reads them).

#### Returns

`Promise`\<[`HiveEventCategory`](../type-aliases/HiveEventCategory.md)[]\>

***

### getRooms()

> **getRooms**(): `Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:74](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/client.ts#L74)

#### Returns

`Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

***

### refreshClasses()

> **refreshClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:68](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/hive/client.ts#L68)

Drops this Hive's cached student groups and fetches them again, for a
caller that just missed a group that may have been created since the
cache filled (the activator and feed, when a shuffle matches no group).

#### Returns

`Promise`\<`Class`[]\>
