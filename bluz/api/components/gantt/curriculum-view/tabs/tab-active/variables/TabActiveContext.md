[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/tabs/tab-active](../index.md) / TabActiveContext

# Variable: TabActiveContext

> `const` **TabActiveContext**: `Context`\<`boolean`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/tab-active.ts:9](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/gantt/curriculum-view/tabs/tab-active.ts#L9)

Whether the gantt tab this subtree renders in is the one on screen.
Visited tabs stay mounted while hidden (#326), so window-level shortcuts
must check this, or a hidden tab answers keys meant for the visible one.
Defaults to true outside the tab container.
