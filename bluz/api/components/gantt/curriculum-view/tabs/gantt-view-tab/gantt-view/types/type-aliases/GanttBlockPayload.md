[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types](../index.md) / GanttBlockPayload

# Type Alias: GanttBlockPayload

> **GanttBlockPayload** = \{ `eventId`: `string`; `moduleId`: `string`; `type?`: `undefined`; \} \| \{ `eventId`: `string`; `moduleId`: `string`; `type`: `"event-map"`; \} \| \{ `eventId`: `string`; `moduleId`: `string`; `sourceDayId`: `string`; `type`: `"event-move"`; \} \| \{ `dayId`: `string`; `eventId`: `string`; `moduleId`: `string`; `type`: `"event-occurrence"`; \} \| \{ `dayId`: `string`; `eventId`: `string`; `moduleId`: `string`; `type`: `"event-skipped-occurrence"`; \} \| \{ `moduleId`: `string`; `type`: `"module-map"`; \} \| \{ `moduleId`: `string`; `sourceDayId`: `string`; `type`: `"module-shift"`; \}

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts:115](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/types.ts#L115)

Drag payload carried by a block (module/event chip or cell anchor).
