[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/side-dock/dock-panel](../index.md) / DockPanelStore

# Type Alias: DockPanelStore

> **DockPanelStore** = [`ExternalStore`](../../../../../base/external-store/type-aliases/ExternalStore.md)\<[`DockPanel`](DockPanel.md) \| `null`\>

Defined in: [ui/src/components/schedule/calendar/side-dock/dock-panel.ts:14](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/calendar/side-dock/dock-panel.ts#L14)

Which panel the side dock has open, or `null` for the bare rail.

Held outside React state, and created by the calendar rather than the dock,
so that something other than the rail's own buttons can open a panel — a
tour about the מבוזרים list opens it before pointing at it — without the
calendar re-rendering around every toggle.
