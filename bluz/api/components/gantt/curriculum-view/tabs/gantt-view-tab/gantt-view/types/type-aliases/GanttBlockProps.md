[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types](../index.md) / GanttBlockProps

# Type Alias: GanttBlockProps

> **GanttBlockProps** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:144](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L144)

## Properties

### blockLeftPercent?

> `optional` **blockLeftPercent?**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:158](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L158)

Percentage (of the anchor cell's own width) offset/width for multi-week spans (#118).

***

### blockWidthPercent?

> `optional` **blockWidthPercent?**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:159](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L159)

***

### disableDrag?

> `optional` **disableDrag?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:173](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L173)

Zoomed single-week day view: module blocks are pinned, not draggable (#640).

***

### elementId?

> `optional` **elementId?**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:153](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L153)

***

### id

> **id**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:145](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L145)

***

### isAbsolute?

> `optional` **isAbsolute?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:152](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L152)

***

### isOpaque?

> `optional` **isOpaque?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:150](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L150)

***

### isRecurrence?

> `optional` **isRecurrence?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:166](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L166)

Auto-generated recurrence occurrence (a repeat of a recurring event's
start block). Rendered as a faded, non-draggable indicator (#111).

***

### isSkipped?

> `optional` **isSkipped?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:171](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L171)

A recurrence occurrence the user skipped. Shown as a hollow, struck-out
ghost so the gap is visible, and restored on double-click (#469).

***

### isSpillover?

> `optional` **isSpillover?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:161](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L161)

Multi-day overflow block: rendered with a spillover gradient (#105).

***

### minutes?

> `optional` **minutes?**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:156](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L156)

Hours named in the tooltip (#828). Events default to their duration.

***

### onDoubleClick?

> `optional` **onDoubleClick?**: () => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:175](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L175)

Replaces the block's default double-click (e.g. a split part reopens its split).

#### Returns

`void`

***

### payload

> **payload**: [`GanttBlockPayload`](GanttBlockPayload.md)

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:146](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L146)

***

### spanLength?

> `optional` **spanLength?**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:151](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L151)

***

### timeLabel?

> `optional` **timeLabel?**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:149](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L149)

Required-time label shown on the block (zoomed single-week day view).

***

### title?

> `optional` **title?**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:147](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L147)

***

### violations?

> `optional` **violations?**: `string`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:154](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L154)
