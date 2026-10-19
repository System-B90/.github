[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-linked-curriculum](../index.md) / useLinkedCurriculum

# Function: useLinkedCurriculum()

> **useLinkedCurriculum**(`enabled?`): `object` & `Omit`\<`object` & [`BaseGantItem`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"syllabuses"` \| `"weeks"`\> \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/use-linked-curriculum.ts:14](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar/use-linked-curriculum.ts#L14)

The gantt curriculum linked to the viewed iteration, or null while there is
none, it is loading, or the fetch failed — every caller treats it as a
nicety. Fetched only while `enabled`, and once per curriculum.

## Parameters

### enabled?

`boolean` = `true`

## Returns

`object` & `Omit`\<`object` & [`BaseGantItem`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"syllabuses"` \| `"weeks"`\> \| `null`
