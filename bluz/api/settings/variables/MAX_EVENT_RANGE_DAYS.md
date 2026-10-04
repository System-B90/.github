[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / MAX\_EVENT\_RANGE\_DAYS

# Variable: MAX\_EVENT\_RANGE\_DAYS

> `const` **MAX\_EVENT\_RANGE\_DAYS**: `366` = `366`

Defined in: [ui/src/settings.tsx:19](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/settings.tsx#L19)

Widest date range a single event query may ask for. A leap year, so a
legitimate "one full year" export is never rejected, while an unbounded
range that would turn one request into a full scan still is.
