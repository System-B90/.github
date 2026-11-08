[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/use-break-course-expander](../index.md) / useBreakCourseExpander

# Function: useBreakCourseExpander()

> **useBreakCourseExpander**(): (`courseIds`) => `Set`\<`string`\>

Defined in: [ui/src/components/schedule/calendar/split/use-break-course-expander.ts:10](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/split/use-break-course-expander.ts#L10)

Widens a break's courses to their descendants, so a Bis90 break also
interrupts Apollo events (#974). Stable while the course tree is unchanged.

## Returns

(`courseIds`) => `Set`\<`string`\>
