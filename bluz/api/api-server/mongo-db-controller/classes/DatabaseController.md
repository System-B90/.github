[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / DatabaseController

# Class: DatabaseController

Defined in: [ui/src/api-server/mongo-db-controller.ts:120](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L120)

## Constructors

### Constructor

> **new DatabaseController**(`dbName?`): `DatabaseController`

Defined in: [ui/src/api-server/mongo-db-controller.ts:124](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L124)

#### Parameters

##### dbName?

`string` = `DEFAULT_ITERATION_DB_NAME`

#### Returns

`DatabaseController`

## Properties

### dbName

> `readonly` **dbName**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:122](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L122)

## Accessors

### calendarDrafts

#### Get Signature

> **get** **calendarDrafts**(): `Collection`\<[`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:194](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L194)

##### Returns

`Collection`\<[`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md)\>

***

### calendarSnapshots

#### Get Signature

> **get** **calendarSnapshots**(): `Collection`\<[`CalendarSnapshot`](../../../api-shared/types/type-aliases/CalendarSnapshot.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:190](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L190)

##### Returns

`Collection`\<[`CalendarSnapshot`](../../../api-shared/types/type-aliases/CalendarSnapshot.md)\>

***

### client

#### Get Signature

> **get** **client**(): `MongoClient`

Defined in: [ui/src/api-server/mongo-db-controller.ts:218](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L218)

##### Returns

`MongoClient`

***

### courses

#### Get Signature

> **get** **courses**(): `Collection`\<[`Course`](../../../api-shared/types/course/type-aliases/Course.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:154](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L154)

##### Returns

`Collection`\<[`Course`](../../../api-shared/types/course/type-aliases/Course.md)\>

***

### curriculumCuts

#### Get Signature

> **get** **curriculumCuts**(): `Collection`\<[`CurriculumCutClaim`](../../../api-shared/types/curriculum-cut/type-aliases/CurriculumCutClaim.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:214](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L214)

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

Defined in: [ui/src/api-server/mongo-db-controller.ts:162](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L162)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

***

### eventHistory

#### Get Signature

> **get** **eventHistory**(): `Collection`\<[`EventHistoryEntry`](../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:146](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L146)

Append-only change log for events. Rows reference events by id and never
copy event state, so the events collection stays free of audit columns.

##### Returns

`Collection`\<[`EventHistoryEntry`](../../../api-shared/types/event-history/type-aliases/EventHistoryEntry.md)\>

***

### events

#### Get Signature

> **get** **events**(): `Collection`\<[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:138](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L138)

##### Returns

`Collection`\<[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>

***

### hiveLessonActivations

#### Get Signature

> **get** **hiveLessonActivations**(): `Collection`\<[`HiveLessonActivation`](../../../api-shared/types/hive-activation/type-aliases/HiveLessonActivation.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:204](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L204)

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

Defined in: [ui/src/api-server/mongo-db-controller.ts:174](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L174)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

***

### modules

#### Get Signature

> **get** **modules**(): `Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:170](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L170)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

***

### outsiders

#### Get Signature

> **get** **outsiders**(): `Collection`\<[`Outsider`](../../../api-shared/types/outsider/type-aliases/Outsider.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:182](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L182)

##### Returns

`Collection`\<[`Outsider`](../../../api-shared/types/outsider/type-aliases/Outsider.md)\>

***

### reservations

#### Get Signature

> **get** **reservations**(): `Collection`\<[`DbReservation`](../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:186](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L186)

##### Returns

`Collection`\<[`DbReservation`](../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>

***

### roomExtendedInfo

#### Get Signature

> **get** **roomExtendedInfo**(): `Collection`\<[`RoomExtendedInfoDocument`](../type-aliases/RoomExtendedInfoDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:178](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L178)

##### Returns

`Collection`\<[`RoomExtendedInfoDocument`](../type-aliases/RoomExtendedInfoDocument.md)\>

***

### rooms

#### Get Signature

> **get** **rooms**(): `Collection`\<[`CustomRoom`](../../../api-shared/types/room/type-aliases/CustomRoom.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:158](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L158)

##### Returns

`Collection`\<[`CustomRoom`](../../../api-shared/types/room/type-aliases/CustomRoom.md)\>

***

### settings

#### Get Signature

> **get** **settings**(): `Collection`\<[`Setting`](../../../api-shared/types/settings/settings/type-aliases/Setting.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:150](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L150)

##### Returns

`Collection`\<[`Setting`](../../../api-shared/types/settings/settings/type-aliases/Setting.md)\>

***

### syllabuses

#### Get Signature

> **get** **syllabuses**(): `Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>

Defined in: [ui/src/api-server/mongo-db-controller.ts:166](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/mongo-db-controller.ts#L166)

##### Returns

`Collection`\<`object` & [`BaseGantItem`](../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDbDocument`](../../gantt/db-base/type-aliases/BaseDbDocument.md)\>
