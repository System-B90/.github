[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segment-layout](../index.md) / createSegmentLaneKey

# Function: createSegmentLaneKey()

> **createSegmentLaneKey**(`isShuffle`): [`LaneKey`](../../../../../student-view/no-overlap-layout/type-aliases/LaneKey.md)\<[`EventSegment`](../../segments/type-aliases/EventSegment.md)\>

Defined in: [ui/src/components/schedule/calendar/split/segment-layout.ts:35](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/split/segment-layout.ts#L35)

The lane a tile belongs to (#988): its shuffles if it has any, else its
courses, else its rooms. Tiles of one lane share one column band and width;
tiles with none of the three pack freely.

## Parameters

### isShuffle

(`courseId`) => `boolean`

## Returns

[`LaneKey`](../../../../../student-view/no-overlap-layout/type-aliases/LaneKey.md)\<[`EventSegment`](../../segments/type-aliases/EventSegment.md)\>
