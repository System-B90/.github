[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/settings-dialog/tabs/global/course-settings](../index.md) / COURSE\_DND\_MEASURING

# Variable: COURSE\_DND\_MEASURING

> `const` **COURSE\_DND\_MEASURING**: `MeasuringConfiguration`

Defined in: [ui/src/components/settings-dialog/tabs/global/course-settings/index.tsx:134](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/settings-dialog/tabs/global/course-settings/index.tsx#L134)

Re-measure drop targets throughout the drag. The layout shifts after a drag
starts, and with the default (measure once at drag start) the root drop
zone's stored rect no longer matched where it was drawn: releasing on the
zone hit nothing and un-nesting silently failed (#771).
