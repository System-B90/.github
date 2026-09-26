[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / TriState

# Type Alias: TriState

> **TriState** = `"all"` \| `"none"` \| `"some"`

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/actions.ts#L17)

Whether a marker is on for none, some or all of the targets. A bulk toggle
is only "on" when every target carries it, so one click over a mixed
selection turns the marker on everywhere rather than flipping each event
to the opposite of whatever it happened to be.
