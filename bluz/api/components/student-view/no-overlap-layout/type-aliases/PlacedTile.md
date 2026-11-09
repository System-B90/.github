[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/no-overlap-layout](../index.md) / PlacedTile

# Type Alias: PlacedTile\<TEvent\>

> **PlacedTile**\<`TEvent`\> = `object`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:78](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/student-view/no-overlap-layout.ts#L78)

Side-by-side day layout shared by the staff calendar and the student board
(#1031), which never draws one tile over another.

Replaces react-big-calendar's `"no-overlap"`, which decides overlap from
the tiles' floating-point percentage `top`/`height`: an event ending at
11:15 and one starting at 11:15 can land a rounding error apart and get
split into half-width columns. Overlap here is decided on timestamps, so
back-to-back events stack vertically at full width - and so do events
running at most [SLIGHT\_OVERLAP\_MS](../variables/SLIGHT_OVERLAP_MS.md) into the next one, which are laid
out as if they ended there but keep their real height. A zero-length event
still claims 1ms, since it draws a tile too.

Events are grouped into clusters of transitively overlapping tiles; each
cluster is split into as many columns as it needs, and a tile stretches
over neighbouring columns it has to itself.

## Type Parameters

### TEvent

`TEvent`

## Properties

### column

> **column**: `number`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:82](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/student-view/no-overlap-layout.ts#L82)

***

### event

> **event**: `TEvent`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:79](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/student-view/no-overlap-layout.ts#L79)

***

### geometry

> **geometry**: `object`

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:81](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/student-view/no-overlap-layout.ts#L81)

All percentages of the day column.

#### height

> **height**: `number`

#### top

> **top**: `number`

#### width

> **width**: `number`

#### xOffset

> **xOffset**: `number`
