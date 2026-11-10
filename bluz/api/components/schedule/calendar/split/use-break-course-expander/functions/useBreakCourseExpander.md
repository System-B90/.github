[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/use-break-course-expander](../index.md) / useBreakCourseExpander

# Function: useBreakCourseExpander()

> **useBreakCourseExpander**(): (`courseIds`) => `Set`\<`string`\>

Defined in: [ui/src/components/schedule/calendar/split/use-break-course-expander.ts:10](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/split/use-break-course-expander.ts#L10)

Widens a break's courses to their descendants, so a Bis90 break also
interrupts Apollo events (#974). Stable while the course tree is unchanged.

## Returns

(`courseIds`) => `Set`\<`string`\>
