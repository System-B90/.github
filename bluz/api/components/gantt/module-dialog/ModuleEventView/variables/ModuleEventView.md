[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/module-dialog/ModuleEventView](../index.md) / ModuleEventView

# Variable: ModuleEventView

> `const` **ModuleEventView**: `NamedExoticComponent`\<\{ `eventId`: `string`; `isHighlighted?`: `boolean`; `moduleId`: `string`; \}\>

Defined in: [ui/src/components/gantt/module-dialog/ModuleEventView.tsx:99](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/module-dialog/ModuleEventView.tsx#L99)

One event's row in the module dialog. Memoised, and its sortable row owns
the drag subscription: a sort re-renders the row element and its handle,
never the title field, selects and pickers built here.
