[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/prayer-windows](../index.md) / getWeekPrayerWindows

# Function: getWeekPrayerWindows()

> **getWeekPrayerWindows**(`date`, `controller`): `Promise`\<[`DayPrayerWindow`](../../../api-shared/types/prayer-windows/type-aliases/DayPrayerWindow.md)[]\>

Defined in: [ui/src/api-server/prayer-windows.ts:11](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/prayer-windows.ts#L11)

The daily prayer windows of the week holding `date` in `controller`'s
iteration, at the prayer times of the template that week is linked to.

## Parameters

### date

`string`

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`DayPrayerWindow`](../../../api-shared/types/prayer-windows/type-aliases/DayPrayerWindow.md)[]\>
