[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/shabbat/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiShabbatGet`

Defined in: [ui/src/app/api/shabbat/route.ts:24](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/app/api/shabbat/route.ts#L24)

Shabbat window (Beer Sheva) for the week containing `?date=YYYY-MM-DD`:
candle lighting, havdalah, and the Friday/Saturday event bounds (R-32).
Computed server-side so a client — the `/bluz` agent included — needs no
hebcal and runs no code, just one request.
