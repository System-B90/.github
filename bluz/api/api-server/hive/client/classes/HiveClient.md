[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/client](../index.md) / HiveClient

# Class: HiveClient

Defined in: [ui/src/api-server/hive/client.ts:33](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L33)

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

Defined in: [ui/src/api-server/hive/client.ts:117](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L117)

#### Parameters

##### classId

`number`

#### Returns

`Promise`\<`void`\>

***

### currentAccessToken()

> **currentAccessToken**(): `string`

Defined in: [ui/src/api-server/hive/client.ts:112](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L112)

The access token this client currently holds, for calling another
System-B90 app (Peek-a-Boo) that checks it against Hive.

#### Returns

`string`

***

### getClasses()

> **getClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:41](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L41)

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

Defined in: [ui/src/api-server/hive/client.ts:95](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L95)

Hive's schedule event categories (Segel clearance reads them).

#### Returns

`Promise`\<[`HiveEventCategory`](../type-aliases/HiveEventCategory.md)[]\>

***

### getOwnVisibleStudentGroups()

> **getOwnVisibleStudentGroups**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:80](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L80)

The student groups *this caller's* Hive permissions let them list,
bypassing the shared cache in both directions: a restricted view (a
Hanich may see only their own groups) must never fill the cache other
callers read, nor may it be served a broader view another caller filled.

#### Returns

`Promise`\<`Class`[]\>

***

### getRooms()

> **getRooms**(): `Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:85](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L85)

#### Returns

`Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

***

### refreshClasses()

> **refreshClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:68](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/client.ts#L68)

Drops this Hive's cached student groups and fetches them again, for a
caller that just missed a group that may have been created since the
cache filled (the activator and feed, when a shuffle matches no group).

#### Returns

`Promise`\<`Class`[]\>
