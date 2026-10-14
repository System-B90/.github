[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/types](../index.md) / PersonField

# Type Alias: PersonField

> **PersonField** = `"instructors"` \| `"lecturers"`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/types.ts:8](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/schedule/calendar/instructor-dnd/types.ts#L8)

Field of an [Event](../../../../../../api-shared/types/event/type-aliases/Event.md) a dropped person is written into. Plain drops write
`instructors` (מבוזרים); holding Shift while dropping writes `lecturers`
(מרצים/מנהלים) for the event types that carry that field.
