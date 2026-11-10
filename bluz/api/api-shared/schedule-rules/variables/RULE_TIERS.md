[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/schedule-rules](../index.md) / RULE\_TIERS

# Variable: RULE\_TIERS

> `const` **RULE\_TIERS**: `object`

Defined in: [ui/src/api-shared/schedule-rules.ts:14](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/schedule-rules.ts#L14)

Priority tiers (RULES.md §0). On conflict the higher tier wins; inside one, the lower id.

## Type Declaration

### A

> `readonly` **A**: `object`

#### A.description

> `readonly` **description**: `"יישור שאפלים. נשבר רק מול מסגרת קשיחה."` = `"יישור שאפלים. נשבר רק מול מסגרת קשיחה."`

#### A.label

> `readonly` **label**: `"יישור"` = `"יישור"`

### C

> `readonly` **C**: `object`

#### C.description

> `readonly` **description**: `"אילוצי גאנט. כולם רכים ומתוקנים אחרונים."` = `"אילוצי גאנט. כולם רכים ומתוקנים אחרונים."`

#### C.label

> `readonly` **label**: `"אילוץ"` = `"אילוץ"`

### H

> `readonly` **H**: `object`

#### H.description

> `readonly` **description**: `"לא מופרת בלי אישור מפורש."` = `"לא מופרת בלי אישור מפורש."`

#### H.label

> `readonly` **label**: `"מסגרת קשיחה"` = `"מסגרת קשיחה"`

### S

> `readonly` **S**: `object`

#### S.description

> `readonly` **description**: `"העדפת שיבוץ. נכנעת ליישור ולמסגרות."` = `"העדפת שיבוץ. נכנעת ליישור ולמסגרות."`

#### S.label

> `readonly` **label**: `"שיבוץ רך"` = `"שיבוץ רך"`
