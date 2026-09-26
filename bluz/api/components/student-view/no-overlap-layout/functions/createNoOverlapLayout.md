[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/no-overlap-layout](../index.md) / createNoOverlapLayout

# Function: createNoOverlapLayout()

> **createNoOverlapLayout**(`minTileMs?`): \<`TEvent`\>(`__namedParameters`) => `object`[]

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:38](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/student-view/no-overlap-layout.ts#L38)

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

## Parameters

### minTileMs?

`number` = `0`

## Returns

\<`TEvent`\>(`__namedParameters`) => `object`[]
