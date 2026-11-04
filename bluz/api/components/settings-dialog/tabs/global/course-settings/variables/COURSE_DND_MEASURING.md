[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings](../index.md) / COURSE\_DND\_MEASURING

# Variable: COURSE\_DND\_MEASURING

> `const` **COURSE\_DND\_MEASURING**: `MeasuringConfiguration`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/index.tsx:136](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/settings-dialog/tabs/global/course-settings/index.tsx#L136)

Re-measure drop targets throughout the drag. The layout shifts after a drag
starts, and with the default (measure once at drag start) the root drop
zone's stored rect no longer matched where it was drawn: releasing on the
zone hit nothing and un-nesting silently failed (#771).
