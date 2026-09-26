[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-snapshots](../index.md) / apiGetSnapshot

# Function: apiGetSnapshot()

> **apiGetSnapshot**(`snapshotId`, `iterationId?`): `Promise`\<\{ `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; `snapshot`: [`CalendarSnapshot`](../../../api-shared/types/type-aliases/CalendarSnapshot.md); \}\>

Defined in: [ui/src/api-client/calendar-snapshots.ts:48](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/calendar-snapshots.ts#L48)

Fetches a single snapshot including its captured events, mapped back into the
client `Event` shape (Dayjs timestamps) ready for a SET_EVENTS restore.

## Parameters

### snapshotId

`string`

### iterationId?

`string`

## Returns

`Promise`\<\{ `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; `snapshot`: [`CalendarSnapshot`](../../../api-shared/types/type-aliases/CalendarSnapshot.md); \}\>
