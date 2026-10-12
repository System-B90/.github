[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segment-layout](../index.md) / MINIMUM\_START\_DIFFERENCE\_MIN

# Variable: MINIMUM\_START\_DIFFERENCE\_MIN

> `const` **MINIMUM\_START\_DIFFERENCE\_MIN**: `1` = `1`

Defined in: [ui/src/components/schedule/calendar/split/segment-layout.ts:40](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/split/segment-layout.ts#L40)

Minutes apart two starts must be for react-big-calendar not to force the
events side by side. Its default is half a slot group (30 minutes on the
schedule), which split back-to-back events such as 9:00–9:15 and 9:15.
