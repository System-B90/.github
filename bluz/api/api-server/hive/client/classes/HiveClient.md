[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/client](../index.md) / HiveClient

# Class: HiveClient

Defined in: [ui/src/api-server/hive/client.ts:24](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/hive/client.ts#L24)

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

Defined in: [ui/src/api-server/hive/client.ts:31](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/hive/client.ts#L31)

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

Defined in: [ui/src/api-server/hive/client.ts:60](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/hive/client.ts#L60)

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

Defined in: [ui/src/api-server/hive/client.ts:48](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/hive/client.ts#L48)

#### Returns

`Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>
