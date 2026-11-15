[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/room-reservation](../index.md) / ROOM\_RESERVATION\_TYPE

# Variable: ROOM\_RESERVATION\_TYPE

> `const` **ROOM\_RESERVATION\_TYPE**: `"שיריון כיתה"` = `"שיריון כיתה"`

Defined in: [ui/src/components/schedule/event-dialog/room-reservation.ts:11](https://github.com/System-B90/Bluz/blob/ef5f1592ad9f013b150ea581b494f4fff71a8490/ui/src/components/schedule/event-dialog/room-reservation.ts#L11)

שיריון כיתה: a pseudo event type the event dialog offers so a room can be
reserved with the grid's own drag-to-create. It is never stored on an
event: picking it turns the dialog into a reservation form, and saving
creates one reservation per picked room through `/api/reservations`.
