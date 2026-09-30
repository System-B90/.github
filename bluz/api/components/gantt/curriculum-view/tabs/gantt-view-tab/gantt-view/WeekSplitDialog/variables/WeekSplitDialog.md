[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/WeekSplitDialog](../index.md) / WeekSplitDialog

# Variable: WeekSplitDialog

> `const` **WeekSplitDialog**: `React.FC`\<\{ `eventTitle`: `string`; `initialParts`: `number`[] \| `undefined`; `onClose`: () => `void`; `onSave`: (`parts`) => `void`; `open`: `boolean`; `totalMinutes`: `number`; \}\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/WeekSplitDialog.tsx:40](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/WeekSplitDialog.tsx#L40)

Edits how an event's hours spread over consecutive weeks (#768): one field
per week, starting at the mapped week. Saving needs the parts to add up to
the event's whole duration; clearing runs it whole again.
