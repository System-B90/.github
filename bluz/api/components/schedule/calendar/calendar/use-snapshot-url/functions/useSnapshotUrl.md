[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-snapshot-url](../index.md) / useSnapshotUrl

# Function: useSnapshotUrl()

> **useSnapshotUrl**(): `void`

Defined in: [ui/src/components/schedule/calendar/calendar/use-snapshot-url.ts:26](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/schedule/calendar/calendar/use-snapshot-url.ts#L26)

Two-way sync between `?snapshot=` and the provider's snapshot view: opening
the URL shows the snapshot (once the first live fetch lands, so the view's
own range push cannot overwrite the snapshot's), and opening or closing the
view from the menu or banner rewrites the URL.

## Returns

`void`
