[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/prayers/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiPrayerWindowsGet`

Defined in: [ui/src/app/api/prayers/route.ts:25](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/prayers/route.ts#L25)

Daily prayer windows (Beer Sheva) for the week containing `?date=YYYY-MM-DD`,
at the prayer times of the week template the week was cut with, lengthened
on Rosh Chodesh, fasts and the like. The schedule draws them as a tint; they
are not events. Read-only, so a past iteration (`?it=`) may be asked too.
