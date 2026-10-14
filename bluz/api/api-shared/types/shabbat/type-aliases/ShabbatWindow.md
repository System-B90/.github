[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/shabbat](../index.md) / ShabbatWindow

# Type Alias: ShabbatWindow

> **ShabbatWindow** = `object`

Defined in: [ui/src/api-shared/types/shabbat.ts:7](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/shabbat.ts#L7)

The Shabbat window of one Sunday-to-Saturday week, in Israel local time
(Beer Sheva). Times are zero-padded `HH:mm`.

## Properties

### candleLighting

> **candleLighting**: `string`

Defined in: [ui/src/api-shared/types/shabbat.ts:12](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/shabbat.ts#L12)

`כניסת שבת`, Friday.

***

### friday

> **friday**: `string`

Defined in: [ui/src/api-shared/types/shabbat.ts:9](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/shabbat.ts#L9)

Civil dates (`YYYY-MM-DD`) of the week's Friday and Saturday.

***

### fridayLastEventEnd

> **fridayLastEventEnd**: `string`

Defined in: [ui/src/api-shared/types/shabbat.ts:16](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/shabbat.ts#L16)

Friday: the last event must end by this time (candle lighting − 2h).

***

### havdalah

> **havdalah**: `string`

Defined in: [ui/src/api-shared/types/shabbat.ts:14](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/shabbat.ts#L14)

`צאת שבת`, Saturday.

***

### saturday

> **saturday**: `string`

Defined in: [ui/src/api-shared/types/shabbat.ts:10](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/shabbat.ts#L10)

***

### saturdayFirstEventStart

> **saturdayFirstEventStart**: `string`

Defined in: [ui/src/api-shared/types/shabbat.ts:18](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/shabbat.ts#L18)

Saturday: the first event may start at this time (havdalah + 30m).
