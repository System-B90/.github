[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/types](../index.md) / InsightVisual

# Type Alias: InsightVisual

> **InsightVisual** = \{ `bars`: `object`[]; `kind`: `"bars"`; \} \| \{ `caption`: `string`; `kind`: `"bigNumber"`; `value`: `string`; \} \| \{ `chips`: `object`[]; `kind`: `"chips"`; \} \| \{ `centerLabel`: `string`; `kind`: `"donut"`; `slices`: `object`[]; \} \| \{ `kind`: `"leaderboard"`; `rows`: `object`[]; \} \| \{ `kind`: `"ring"`; `label`: `string`; `max`: `number`; `value`: `number`; \} \| \{ `endLabel`: `string`; `kind`: `"timeline"`; `progress`: `null` \| `number`; `startLabel`: `string`; \} \| \{ `cells`: `object`[]; `kind`: `"weekdayHeatmap"`; \}

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:18](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L18)

A visual is plain data so generators stay pure `.ts` functions; the card maps
each `kind` to its renderer.

## Union Members

### Type Literal

\{ `bars`: `object`[]; `kind`: `"bars"`; \}

***

### Type Literal

\{ `caption`: `string`; `kind`: `"bigNumber"`; `value`: `string`; \}

***

### Type Literal

\{ `chips`: `object`[]; `kind`: `"chips"`; \}

***

### Type Literal

\{ `centerLabel`: `string`; `kind`: `"donut"`; `slices`: `object`[]; \}

***

### Type Literal

\{ `kind`: `"leaderboard"`; `rows`: `object`[]; \}

***

### Type Literal

\{ `kind`: `"ring"`; `label`: `string`; `max`: `number`; `value`: `number`; \}

***

### Type Literal

\{ `endLabel`: `string`; `kind`: `"timeline"`; `progress`: `null` \| `number`; `startLabel`: `string`; \}

#### endLabel

> **endLabel**: `string`

#### kind

> **kind**: `"timeline"`

#### progress

> **progress**: `null` \| `number`

0..1 position of "today", or null when outside the course.

#### startLabel

> **startLabel**: `string`

***

### Type Literal

\{ `cells`: `object`[]; `kind`: `"weekdayHeatmap"`; \}
