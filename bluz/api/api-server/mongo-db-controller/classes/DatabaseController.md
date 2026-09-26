[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / DatabaseController

# Class: DatabaseController

Defined in: [ui/src/api-server/mongo-db-controller.ts:114](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L114)

## Constructors

### Constructor

> **new DatabaseController**(`dbName?`): `DatabaseController`

Defined in: [ui/src/api-server/mongo-db-controller.ts:118](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L118)

#### Parameters

##### dbName?

`string` = `DEFAULT_ITERATION_DB_NAME`

#### Returns

`DatabaseController`

## Properties

### dbName

> `readonly` **dbName**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:116](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L116)

## Accessors

### calendarDrafts

#### Get Signature

> **get** **calendarDrafts**(): `Collection`\<[`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:188](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L188)

##### Returns

`Collection`\<[`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md)\>

***

### calendarSnapshots

#### Get Signature

> **get** **calendarSnapshots**(): `Collection`\<[`CalendarSnapshot`](../../../api-shared/types/type-aliases/CalendarSnapshot.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:184](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L184)

##### Returns

`Collection`\<[`CalendarSnapshot`](../../../api-shared/types/type-aliases/CalendarSnapshot.md)\>

***

### client

#### Get Signature

> **get** **client**(): `MongoClient`

Defined in: [ui/src/api-server/mongo-db-controller.ts:212](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L212)

##### Returns

`MongoClient`

***

### courses

#### Get Signature

> **get** **courses**(): `Collection`\<[`Course`](../../../api-shared/types/course/type-aliases/Course.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:148](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L148)

##### Returns

`Collection`\<[`Course`](../../../api-shared/types/course/type-aliases/Course.md)\>

***

### curriculumCuts

#### Get Signature

> **get** **curriculumCuts**(): `Collection`\<[`CurriculumCutClaim`](../../../api-shared/types/curriculum-cut/type-aliases/CurriculumCutClaim.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:208](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L208)

Claims of the one-shot curriculum cut. Like the activation ledger above,
the unique index is the concurrency control — an unlocked
check-then-insert let two concurrent cuts both pass the guard and each
insert the whole schedule (#515).

##### Returns

`Collection`\<[`CurriculumCutClaim`](../../../api-shared/types/curriculum-cut/type-aliases/CurriculumCutClaim.md)\>

***

### curriculums

#### Get Signature

> **get** **curriculums**(): `Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:156](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L156)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

***

### eventHistory

#### Get Signature

> **get** **eventHistory**(): `Collection`\<[`EventHistoryEntry`](../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:140](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L140)

Append-only change log for events. Rows reference events by id and never
copy event state, so the events collection stays free of audit columns.

##### Returns

`Collection`\<[`EventHistoryEntry`](../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)\>

***

### events

#### Get Signature

> **get** **events**(): `Collection`\<[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:132](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L132)

##### Returns

`Collection`\<[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>

***

### hiveLessonActivations

#### Get Signature

> **get** **hiveLessonActivations**(): `Collection`\<[`HiveLessonActivation`](../../../api-shared/types/hive-activation/type-aliases/HiveLessonActivation.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:198](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L198)

Ledger of Hive queue openings: one row per (event, occurrence, student
group) that the activator has already pushed to Hive. Its unique index
is what makes the activator idempotent and safe to run in more than one
replica — the insert, not a lock, decides who acts.

##### Returns

`Collection`\<[`HiveLessonActivation`](../../../api-shared/types/hive-activation/type-aliases/HiveLessonActivation.md)\>

***

### moduleEvents

#### Get Signature

> **get** **moduleEvents**(): `Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:168](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L168)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

***

### modules

#### Get Signature

> **get** **modules**(): `Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:164](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L164)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

***

### outsiders

#### Get Signature

> **get** **outsiders**(): `Collection`\<[`Outsider`](../../../api-shared/types/outsider/type-aliases/Outsider.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:176](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L176)

##### Returns

`Collection`\<[`Outsider`](../../../api-shared/types/outsider/type-aliases/Outsider.md)\>

***

### reservations

#### Get Signature

> **get** **reservations**(): `Collection`\<[`DbReservation`](../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:180](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L180)

##### Returns

`Collection`\<[`DbReservation`](../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>

***

### roomExtendedInfo

#### Get Signature

> **get** **roomExtendedInfo**(): `Collection`\<[`RoomExtendedInfoDocument`](../type-aliases/RoomExtendedInfoDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:172](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L172)

##### Returns

`Collection`\<[`RoomExtendedInfoDocument`](../type-aliases/RoomExtendedInfoDocument.md)\>

***

### rooms

#### Get Signature

> **get** **rooms**(): `Collection`\<[`CustomRoom`](../../../api-shared/types/room/type-aliases/CustomRoom.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:152](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L152)

##### Returns

`Collection`\<[`CustomRoom`](../../../api-shared/types/room/type-aliases/CustomRoom.md)\>

***

### settings

#### Get Signature

> **get** **settings**(): `Collection`\<[`Setting`](../../../api-shared/types/settings/settings/type-aliases/Setting.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:144](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L144)

##### Returns

`Collection`\<[`Setting`](../../../api-shared/types/settings/settings/type-aliases/Setting.md)\>

***

### syllabuses

#### Get Signature

> **get** **syllabuses**(): `Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:160](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/mongo-db-controller.ts#L160)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>
