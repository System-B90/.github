[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/draft-range](../index.md) / draftRangeOf

# Function: draftRangeOf()

> **draftRangeOf**(`draft`, `events`, `fallback`): [`CalendarDraftRange`](../../../../../../api-shared/types/type-aliases/CalendarDraftRange.md)

Defined in: [ui/src/components/schedule/calendar/calendar/draft-range.ts:8](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/calendar/draft-range.ts#L8)

The range a draft covers (#62): its stored range, else — for drafts saved
before ranges were stored — the span of its own events, else `fallback`.

## Parameters

### draft

`Pick`\<[`CalendarDraft`](../../../../../../api-shared/types/type-aliases/CalendarDraft.md), `"rangeEnd"` \| `"rangeStart"`\>

### events

readonly `Pick`\<[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md), `"startTime"` \| `"endTime"`\>[]

### fallback

[`CalendarDraftRange`](../../../../../../api-shared/types/type-aliases/CalendarDraftRange.md)

## Returns

[`CalendarDraftRange`](../../../../../../api-shared/types/type-aliases/CalendarDraftRange.md)
