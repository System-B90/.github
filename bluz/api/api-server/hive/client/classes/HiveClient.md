[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/client](../index.md) / HiveClient

# Class: HiveClient

Defined in: [ui/src/api-server/hive/client.ts:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/hive/client.ts#L24)

Bluz's Hive client: the request core (token refresh, 401 retry, 500
backoff, network-error classification, users/classes, lessons and lesson
rules, subjects, modules) lives in `@system-b90/hive-core`; this subclass
adds rooms and the student-group/module-queue shortcuts.

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

### getClasses()

> **getClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:31](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/hive/client.ts#L31)

Student groups change rarely and Bluz never writes them, yet every cut,
lesson sync and feed fetches them: share one request per Hive instance
for `CLASSES_TTL_MS`. The promise is cached, so concurrent callers share
the in-flight request; a failure is dropped so the next call retries.

#### Returns

`Promise`\<`Class`[]\>

#### Overrides

`HiveClientBase.getClasses`

***

### getModuleQueues()

> **getModuleQueues**(`moduleId`): `Promise`\<`Queue`[]\>

Defined in: [ui/src/api-server/hive/client.ts:70](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/hive/client.ts#L70)

The queues of one Hive module — the only queues a lesson rule may point
at (Hive rejects user queues on a rule).

#### Parameters

##### moduleId

`number`

#### Returns

`Promise`\<`Queue`[]\>

***

### getRooms()

> **getRooms**(): `Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:58](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/hive/client.ts#L58)

#### Returns

`Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

***

### refreshClasses()

> **refreshClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:53](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/hive/client.ts#L53)

Drops this Hive's cached student groups and fetches them again, for a
caller that just missed a group that may have been created since the
cache filled (the lesson sync, when a shuffle matches no group).

#### Returns

`Promise`\<`Class`[]\>
