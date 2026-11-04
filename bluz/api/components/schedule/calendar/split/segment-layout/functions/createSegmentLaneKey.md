[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segment-layout](../index.md) / createSegmentLaneKey

# Function: createSegmentLaneKey()

> **createSegmentLaneKey**(`isShuffle`): [`LaneKey`](../../../../../student-view/no-overlap-layout/type-aliases/LaneKey.md)\<[`EventSegment`](../../segments/type-aliases/EventSegment.md)\>

Defined in: [ui/src/components/schedule/calendar/split/segment-layout.ts:35](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/split/segment-layout.ts#L35)

The lane a tile belongs to (#988): its shuffles if it has any, else its
courses, else its rooms. Tiles of one lane share one column band and width;
tiles with none of the three pack freely.

## Parameters

### isShuffle

(`courseId`) => `boolean`

## Returns

[`LaneKey`](../../../../../student-view/no-overlap-layout/type-aliases/LaneKey.md)\<[`EventSegment`](../../segments/type-aliases/EventSegment.md)\>
