[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/no-overlap-layout](../index.md) / PlacedTile

# Type Alias: PlacedTile\<TEvent\>

> **PlacedTile**\<`TEvent`\> = `object`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:38](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/student-view/no-overlap-layout.ts#L38)

Side-by-side day layout that never draws one tile over another.

Replaces react-big-calendar's `"no-overlap"`, which decides overlap from
the tiles' floating-point percentage `top`/`height`: an event ending at
11:15 and one starting at 11:15 can land a rounding error apart and get
split into half-width columns. Overlap here is decided on timestamps, so
back-to-back events stack vertically at full width.

`minTileMs` is how much time the grid's minimum tile height covers. A short
event is drawn taller than its duration, so it claims that much time; zero
or unknown still claims 1ms, since a zero-length event draws a tile too.

Events are grouped into clusters of transitively overlapping tiles; each
cluster is split into as many columns as it needs, and a tile stretches
over neighbouring columns it has to itself.

## Type Parameters

### TEvent

`TEvent`

## Properties

### column

> **column**: `number`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:42](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/student-view/no-overlap-layout.ts#L42)

***

### event

> **event**: `TEvent`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:39](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/student-view/no-overlap-layout.ts#L39)

***

### geometry

> **geometry**: `object`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:41](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/student-view/no-overlap-layout.ts#L41)

All percentages of the day column.

#### height

> **height**: `number`

#### top

> **top**: `number`

#### width

> **width**: `number`

#### xOffset

> **xOffset**: `number`
