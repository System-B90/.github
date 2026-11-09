[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-clock-skew](../index.md) / CLOCK\_SKEW\_LOG\_INTERVAL\_MS

# Variable: CLOCK\_SKEW\_LOG\_INTERVAL\_MS

> `const` **CLOCK\_SKEW\_LOG\_INTERVAL\_MS**: `number`

Defined in: [ui/src/api-server/student-clock-skew.ts:13](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-clock-skew.ts#L13)

At most one clock record per student per hour. A skewed device stays skewed,
and the board refetches every 90s — without this one wound clock would fill
the day's record and the staff tweet channel by itself.
