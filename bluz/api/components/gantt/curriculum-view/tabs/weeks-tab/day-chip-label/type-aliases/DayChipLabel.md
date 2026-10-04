[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label](../index.md) / DayChipLabel

# Type Alias: DayChipLabel

> **DayChipLabel** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts:9](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts#L9)

The weeks-tab day chip (#841). The old "X ש׳ משובץ | נותרו Y ש׳" sentence
was truncated in most cells, cutting off the remaining/over amount. The chip
now shows the short "scheduled / available" pair, and the full sentence moves
to its accessible name and tooltip.

## Properties

### full

> **full**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts:13](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts#L13)

Full sentence for the tooltip and screen readers.

***

### over

> **over**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts:15](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts#L15)

Scheduled exceeds available: the chip carries a warning icon.

***

### short

> **short**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts:11](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/day-chip-label.ts#L11)

Visible chip text, e.g. "0.3 / 6 ש׳".
