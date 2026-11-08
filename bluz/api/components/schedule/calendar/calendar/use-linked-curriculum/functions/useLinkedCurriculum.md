[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-linked-curriculum](../index.md) / useLinkedCurriculum

# Function: useLinkedCurriculum()

> **useLinkedCurriculum**(`enabled?`): `object` & `Omit`\<`object` & [`BaseGantItem`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"syllabuses"` \| `"weeks"`\> \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/use-linked-curriculum.ts:24](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/calendar/use-linked-curriculum.ts#L24)

The gantt curriculum linked to the viewed iteration, or null while there is
none, it is loading, or the fetch failed — every caller treats it as a
nicety. Fetched only while `enabled`, and once per curriculum.

## Parameters

### enabled?

`boolean` = `true`

## Returns

`object` & `Omit`\<`object` & [`BaseGantItem`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"syllabuses"` \| `"weeks"`\> \| `null`
