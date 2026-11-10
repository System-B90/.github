[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segment-layout](../index.md) / splitAwareDayLayout

# Function: splitAwareDayLayout()

> **splitAwareDayLayout**(`input`, `laneKey?`): `StyledSegment`[]

Defined in: [ui/src/components/schedule/calendar/split/segment-layout.ts:66](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/split/segment-layout.ts#L66)

The built-in `overlap` layout, with the pieces of a split event squared up
into a single column band.

Left alone, each piece is measured against whatever it collides with on its
own: the piece running into a break is narrowed to share the column, while
the pieces on the other side have the column to themselves and stay full
width. The result is a ragged event that reads as several unrelated blocks.

So every piece is given the *intersection* of its run's bands — the widest
strip all of them can occupy. Narrowing a piece can never make it collide
with anything, since the strip is contained in the band the algorithm
already cleared for it.

## Parameters

### input

`LayoutInput`

### laneKey?

[`LaneKey`](../../../../../student-view/no-overlap-layout/type-aliases/LaneKey.md)\<[`EventSegment`](../../segments/type-aliases/EventSegment.md)\>

## Returns

`StyledSegment`[]
