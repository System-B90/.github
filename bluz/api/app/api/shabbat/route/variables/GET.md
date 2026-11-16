[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/shabbat/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiShabbatGet`

Defined in: [ui/src/app/api/shabbat/route.ts:24](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/app/api/shabbat/route.ts#L24)

Shabbat window (Beer Sheva) for the week containing `?date=YYYY-MM-DD`:
candle lighting, havdalah, and the Friday/Saturday event bounds (R-32).
Computed server-side so a client — the `/bluz` agent included — needs no
hebcal and runs no code, just one request.
