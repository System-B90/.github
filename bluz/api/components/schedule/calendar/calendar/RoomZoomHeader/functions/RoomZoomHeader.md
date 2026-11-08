[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/RoomZoomHeader](../index.md) / RoomZoomHeader

# Function: RoomZoomHeader()

> **RoomZoomHeader**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/calendar/calendar/RoomZoomHeader.tsx:13](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/RoomZoomHeader.tsx#L13)

A day-view room column header, shared by the staff calendar and the student
board. Clicking it zooms the day to that room alone, and clicking the zoomed
header returns every room.

## Parameters

### \_\_namedParameters

#### empty?

`boolean` = `false`

The room has no events that day; its column is drawn narrow.

#### label

`string`

#### onToggle

(`roomKey`) => `void`

#### roomKey

`string`

#### zoomed

`boolean`

## Returns

`Element`
