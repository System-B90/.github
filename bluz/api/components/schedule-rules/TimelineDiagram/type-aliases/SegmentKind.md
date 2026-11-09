[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule-rules/TimelineDiagram](../index.md) / SegmentKind

# Type Alias: SegmentKind

> **SegmentKind** = `"absent"` \| `"break"` \| `"exercise"` \| `"forbidden"` \| `"frame"` \| `"free"` \| `"lecture"` \| `"other"`

Defined in: [ui/src/components/schedule-rules/TimelineDiagram.tsx:15](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule-rules/TimelineDiagram.tsx#L15)

A small horizontal day timeline for the rules page: lanes (shuffles, rooms,
days) of labelled segments over a clock range. Time runs with the reading
direction, so in RTL it starts on the right — positions are logical
(`insetInlineStart`). Every segment carries its label, so color is never
the only signal.
