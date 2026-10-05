[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/types](../index.md) / PersonField

# Type Alias: PersonField

> **PersonField** = `"instructors"` \| `"lecturers"`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/types.ts:8](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/calendar/instructor-dnd/types.ts#L8)

Field of an [Event](../../../../../../api-shared/types/event/type-aliases/Event.md) a dropped person is written into. Plain drops write
`instructors` (מבוזרים); holding Shift while dropping writes `lecturers`
(מרצים/מנהלים) for the event types that carry that field.
