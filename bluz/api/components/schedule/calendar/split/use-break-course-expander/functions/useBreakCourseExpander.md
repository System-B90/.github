[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/use-break-course-expander](../index.md) / useBreakCourseExpander

# Function: useBreakCourseExpander()

> **useBreakCourseExpander**(): (`courseIds`) => `Set`\<`string`\>

Defined in: [ui/src/components/schedule/calendar/split/use-break-course-expander.ts:10](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/split/use-break-course-expander.ts#L10)

Widens a break's courses to their descendants, so a Bis90 break also
interrupts Apollo events (#974). Stable while the course tree is unchanged.

## Returns

(`courseIds`) => `Set`\<`string`\>
