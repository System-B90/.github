[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-gantt-tab-commands](../index.md) / TIMELINE\_VIEW\_KEYWORDS

# Variable: TIMELINE\_VIEW\_KEYWORDS

> `const` **TIMELINE\_VIEW\_KEYWORDS**: `string`[]

Defined in: [ui/src/components/app-commands/use-gantt-tab-commands.tsx:20](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/app-commands/use-gantt-tab-commands.tsx#L20)

What the timeline toolbar's own view commands answer to. Those commands are
registered only while the timeline is mounted, so on the other tabs a search
for e.g. "משובצים" found nothing (#846). The timeline tab command answers to
the same words and takes the user there.
