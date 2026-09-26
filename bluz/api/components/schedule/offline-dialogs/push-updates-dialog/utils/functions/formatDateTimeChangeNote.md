[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/offline-dialogs/push-updates-dialog/utils](../index.md) / formatDateTimeChangeNote

# Function: formatDateTimeChangeNote()

> **formatDateTimeChangeNote**(`from`, `to`): `string` \| `null`

Defined in: [ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts:103](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/offline-dialogs/push-updates-dialog/utils.ts#L103)

Builds a human-readable Hebrew note describing a startTime/endTime change,
e.g. "הוקדם משעה 11:15 לשעה 10:15" / "נדחה משעה 10:15 לשעה 11:15" for a
same-day time shift, or "הוקדם מיום שלישי ה-14.4 ליום ראשון ה-11.4 (ב-3 ימים)"
/ "נדחה מיום שני ה-6.4 ליום חמישי ה-9.4 (ב-3 ימים)" when the day changes.
Returns null when there's nothing meaningful to report.

## Parameters

### from

`string` \| `number` \| `boolean` \| `string`[] \| `number`[] \| `Record`\<`string`, `number`\> \| `Dayjs` \| [`ResolvableRoom`](../../../../../../api-shared/types/room/type-aliases/ResolvableRoom.md)[] \| [`PersonId`](../../../../../../api-shared/types/event/type-aliases/PersonId.md)[] \| `null` \| `undefined`

### to

`string` \| `number` \| `boolean` \| `string`[] \| `number`[] \| `Record`\<`string`, `number`\> \| `Dayjs` \| [`ResolvableRoom`](../../../../../../api-shared/types/room/type-aliases/ResolvableRoom.md)[] \| [`PersonId`](../../../../../../api-shared/types/event/type-aliases/PersonId.md)[] \| `null` \| `undefined`

## Returns

`string` \| `null`
