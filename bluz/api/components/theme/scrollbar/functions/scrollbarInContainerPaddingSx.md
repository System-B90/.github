[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/theme/scrollbar](../index.md) / scrollbarInContainerPaddingSx

# Function: scrollbarInContainerPaddingSx()

> **scrollbarInContainerPaddingSx**(`theme`, `padding`, `edgeGapPx?`): `SystemStyleObject`\<`Theme`\>

Defined in: [ui/src/components/theme/scrollbar.ts:23](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/theme/scrollbar.ts#L23)

Moves a scroller's scrollbar out to its container's edge.

A scroller nested inside a padded container draws its scrollbar inside that
padding: in RTL the bar floats `padding` px in from the container's left
edge, and the content sits flush against it. This makes the scroller take
over the padding on its inline-end side (the scrollbar's side) and gives it
back inside the bar, so the gap lands between the bar and the content.

The gutter is always reserved, and the space given back is the padding minus
the bar, so the content stays exactly where the container's padding would put
it, and does not shift when the scrollbar appears.

## Parameters

### theme

`Theme`

### padding

`number`

The container's inline-end padding, in theme spacing units.

### edgeGapPx?

`number` = `0`

Room to keep between the bar and the container's edge.

## Returns

`SystemStyleObject`\<`Theme`\>
