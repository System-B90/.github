[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segments](../index.md) / createSegmentCache

# Function: createSegmentCache()

> **createSegmentCache**(): `object`

Defined in: [ui/src/components/schedule/calendar/split/segments.ts:128](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/split/segments.ts#L128)

Incremental [buildEventSegments](buildEventSegments.md) for the calendar (#927). One websocket
upsert used to rebuild every segment, so every tile and day column
re-laid-out. This keeps, across calls:
- the break windows, while no break actually moved;
- each unchanged event's segments (keyed by the event object);
- a derived array, while its items are the same.

## Returns

### breakWindows()

> **breakWindows**(`events`, `expandCourses?`): readonly [`BreakWindow`](../../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)[]

[collectBreakWindows](../../../../../../api-shared/break-windows/functions/collectBreakWindows.md), but the previous array while equal.

#### Parameters

##### events

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

##### expandCourses?

(`courseIds`) => `Iterable`\<`string`\>

#### Returns

readonly [`BreakWindow`](../../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)[]

### keep()

> **keep**\<`T`\>(`key`, `next`): `T`[]

`next`, or the array last kept under `key` when it holds the same items.

#### Type Parameters

##### T

`T`

#### Parameters

##### key

`string`

##### next

`T`[]

#### Returns

`T`[]

### segments()

> **segments**(`events`, `windows`): [`EventSegment`](../type-aliases/EventSegment.md)[]

[buildEventSegments](buildEventSegments.md), reusing an unchanged event's pieces.

#### Parameters

##### events

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

##### windows

readonly [`BreakWindow`](../../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)[]

#### Returns

[`EventSegment`](../type-aliases/EventSegment.md)[]
