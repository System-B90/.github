[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/module-dialog/ModuleEventView](../index.md) / ModuleEventView

# Variable: ModuleEventView

> `const` **ModuleEventView**: `NamedExoticComponent`\<\{ `eventId`: `string`; `isHighlighted?`: `boolean`; `moduleId`: `string`; \}\>

Defined in: [ui/src/components/gantt/module-dialog/ModuleEventView.tsx:99](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/module-dialog/ModuleEventView.tsx#L99)

One event's row in the module dialog. Memoised, and its sortable row owns
the drag subscription: a sort re-renders the row element and its handle,
never the title field, selects and pickers built here.
