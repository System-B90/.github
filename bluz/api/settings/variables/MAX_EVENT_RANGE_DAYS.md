[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / MAX\_EVENT\_RANGE\_DAYS

# Variable: MAX\_EVENT\_RANGE\_DAYS

> `const` **MAX\_EVENT\_RANGE\_DAYS**: `366` = `366`

Defined in: [ui/src/settings.tsx:19](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/settings.tsx#L19)

Widest date range a single event query may ask for. A leap year, so a
legitimate "one full year" export is never rejected, while an unbounded
range that would turn one request into a full scan still is.
