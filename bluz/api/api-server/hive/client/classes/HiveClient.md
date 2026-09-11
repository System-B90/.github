[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/client](../index.md) / HiveClient

# Class: HiveClient

Defined in: [ui/src/api-server/hive/client.ts:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L39)

Bluz's Hive client: the request core (token refresh, 401 retry, 500
backoff, cookie-auth fetch, users/classes) lives in
`@system-b90/hive-core`; this subclass adds the scheduling endpoints.

## Extends

- `HiveClient`

## Constructors

### Constructor

> **new HiveClient**(`accessToken`, `refreshToken?`, `hiveBaseUrl?`): `HiveClient`

Defined in: node\_modules/@system-b90/hive-core/dist/client.d.ts:15

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

### createLesson()

> **createLesson**(`data`): `Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

Defined in: [ui/src/api-server/hive/client.ts:89](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L89)

#### Parameters

##### data

`LessonRequest`

#### Returns

`Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

***

### createLessonRule()

> **createLessonRule**(`parentId`, `data`): `Promise`\<`LessonRule`\>

Defined in: [ui/src/api-server/hive/client.ts:145](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L145)

#### Parameters

##### parentId

`number`

##### data

`LessonRuleRequest`

#### Returns

`Promise`\<`LessonRule`\>

***

### deleteLesson()

> **deleteLesson**(`id`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/hive/client.ts:116](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L116)

#### Parameters

##### id

`number`

#### Returns

`Promise`\<`void`\>

***

### deleteLessonRule()

> **deleteLessonRule**(`parentId`, `id`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/hive/client.ts:177](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L177)

#### Parameters

##### parentId

`number`

##### id

`number`

#### Returns

`Promise`\<`void`\>

***

### getClasses()

> **getClasses**(): `Promise`\<`Class`[]\>

Defined in: [ui/src/api-server/hive/client.ts:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L40)

All Hive classes; pass a `type` to filter (e.g. Student Group / Room).

#### Returns

`Promise`\<`Class`[]\>

#### Overrides

`HiveClientBase.getClasses`

***

### getLesson()

> **getLesson**(`id`): `Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

Defined in: [ui/src/api-server/hive/client.ts:82](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L82)

#### Parameters

##### id

`number`

#### Returns

`Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

***

### getLessonRule()

> **getLessonRule**(`parentId`, `id`): `Promise`\<`LessonRule`\>

Defined in: [ui/src/api-server/hive/client.ts:138](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L138)

#### Parameters

##### parentId

`number`

##### id

`number`

#### Returns

`Promise`\<`LessonRule`\>

***

### getLessonRules()

> **getLessonRules**(`parentId`): `Promise`\<`LessonRule`[]\>

Defined in: [ui/src/api-server/hive/client.ts:131](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L131)

#### Parameters

##### parentId

`number`

#### Returns

`Promise`\<`LessonRule`[]\>

***

### getLessons()

> **getLessons**(`params?`): `Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:74](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L74)

#### Parameters

##### params?

`Record`\<`string`, `any`\>

#### Returns

`Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)[]\>

***

### getModuleQueues()

> **getModuleQueues**(`moduleId`): `Promise`\<`Queue`[]\>

Defined in: [ui/src/api-server/hive/client.ts:68](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L68)

The queues of one Hive module — the only queues a lesson rule may point
at (Hive rejects user queues on a rule).

#### Parameters

##### moduleId

`number`

#### Returns

`Promise`\<`Queue`[]\>

***

### getModules()

> **getModules**(): `Promise`\<[`Module`](../../../../api-shared/types/module/type-aliases/Module.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:58](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L58)

#### Returns

`Promise`\<[`Module`](../../../../api-shared/types/module/type-aliases/Module.md)[]\>

***

### getRooms()

> **getRooms**(): `Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L44)

#### Returns

`Promise`\<[`HiveRoom`](../../../../api-shared/types/room/type-aliases/HiveRoom.md)[]\>

***

### getSubjects()

> **getSubjects**(): `Promise`\<[`Subject`](../../../../api-shared/types/subject/type-aliases/Subject.md)[]\>

Defined in: [ui/src/api-server/hive/client.ts:52](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L52)

#### Returns

`Promise`\<[`Subject`](../../../../api-shared/types/subject/type-aliases/Subject.md)[]\>

***

### patchLesson()

> **patchLesson**(`id`, `data`): `Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

Defined in: [ui/src/api-server/hive/client.ts:105](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L105)

#### Parameters

##### id

`number`

##### data

`Partial`\<`LessonRequest`\>

#### Returns

`Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

***

### patchLessonRule()

> **patchLessonRule**(`parentId`, `id`, `data`): `Promise`\<`LessonRule`\>

Defined in: [ui/src/api-server/hive/client.ts:165](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L165)

#### Parameters

##### parentId

`number`

##### id

`number`

##### data

`Partial`\<`LessonRuleRequest`\>

#### Returns

`Promise`\<`LessonRule`\>

***

### setLessonForClass()

> **setLessonForClass**(`classId`, `lessonId`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/hive/client.ts:123](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L123)

#### Parameters

##### classId

`number`

##### lessonId

`number` \| `null`

#### Returns

`Promise`\<`void`\>

***

### updateLesson()

> **updateLesson**(`id`, `data`): `Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

Defined in: [ui/src/api-server/hive/client.ts:97](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L97)

#### Parameters

##### id

`number`

##### data

`LessonRequest`

#### Returns

`Promise`\<[`HiveLesson`](../../../../api-shared/types/hive/type-aliases/HiveLesson.md)\>

***

### updateLessonRule()

> **updateLessonRule**(`parentId`, `id`, `data`): `Promise`\<`LessonRule`\>

Defined in: [ui/src/api-server/hive/client.ts:153](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/client.ts#L153)

#### Parameters

##### parentId

`number`

##### id

`number`

##### data

`LessonRuleRequest`

#### Returns

`Promise`\<`LessonRule`\>
