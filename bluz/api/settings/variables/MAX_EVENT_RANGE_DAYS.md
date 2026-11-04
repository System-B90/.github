[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / MAX\_EVENT\_RANGE\_DAYS

# Variable: MAX\_EVENT\_RANGE\_DAYS

> `const` **MAX\_EVENT\_RANGE\_DAYS**: `366` = `366`

Defined in: [ui/src/settings.tsx:19](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/settings.tsx#L19)

Widest date range a single event query may ask for. A leap year, so a
legitimate "one full year" export is never rejected, while an unbounded
range that would turn one request into a full scan still is.
