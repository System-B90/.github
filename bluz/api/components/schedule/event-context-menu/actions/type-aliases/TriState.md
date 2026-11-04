[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / TriState

# Type Alias: TriState

> **TriState** = `"all"` \| `"none"` \| `"some"`

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:17](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/actions.ts#L17)

Whether a marker is on for none, some or all of the targets. A bulk toggle
is only "on" when every target carries it, so one click over a mixed
selection turns the marker on everywhere rather than flipping each event
to the opposite of whatever it happened to be.
