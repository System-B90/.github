[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/week-template](../index.md) / WeekTemplateLink

# Type Alias: WeekTemplateLink

> **WeekTemplateLink** = `object`

Defined in: [ui/src/api-shared/types/week-template.ts:123](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/week-template.ts#L123)

The template a schedule week is linked to: the one stamped on its cut
events. Drives the week's prayer tint and its next reload.

## Properties

### cut

> **cut**: `boolean`

Defined in: [ui/src/api-shared/types/week-template.ts:131](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/week-template.ts#L131)

The week has live cut events. Linking needs at least one to stamp.

***

### stamped

> **stamped**: `boolean`

Defined in: [ui/src/api-shared/types/week-template.ts:129](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/week-template.ts#L129)

False when no event names a live template: the default applies implicitly.

***

### templateId

> **templateId**: `null` \| [`WeekTemplateId`](WeekTemplateId.md)

Defined in: [ui/src/api-shared/types/week-template.ts:127](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/week-template.ts#L127)

The stamped template, else the default. Null only when none exists.

***

### weekStart

> **weekStart**: `string`

Defined in: [ui/src/api-shared/types/week-template.ts:125](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/week-template.ts#L125)

Sunday of the week, `YYYY-MM-DD`.
