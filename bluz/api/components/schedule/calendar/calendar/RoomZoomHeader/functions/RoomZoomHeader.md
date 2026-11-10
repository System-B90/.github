[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/RoomZoomHeader](../index.md) / RoomZoomHeader

# Function: RoomZoomHeader()

> **RoomZoomHeader**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/calendar/calendar/RoomZoomHeader.tsx:14](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/calendar/RoomZoomHeader.tsx#L14)

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

#### onContextMenu?

(`event`) => `void`

Right-click on the header (the staff calendar's room menu).

#### onToggle

(`roomKey`) => `void`

#### roomKey

`string`

#### zoomed

`boolean`

## Returns

`Element`
