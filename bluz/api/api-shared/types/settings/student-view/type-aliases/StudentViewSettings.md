[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/student-view](../index.md) / StudentViewSettings

# Type Alias: StudentViewSettings

> **StudentViewSettings** = `object`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:17](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/settings/student-view.ts#L17)

## Properties

### eventNameMode

> **eventNameMode**: [`StudentEventNameMode`](../enumerations/StudentEventNameMode.md)

Defined in: [ui/src/api-shared/types/settings/student-view.ts:18](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/settings/student-view.ts#L18)

***

### refreshSeconds?

> `optional` **refreshSeconds?**: `number`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:29](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/settings/student-view.ts#L29)

How often an open student board refetches, in seconds, set by staff from
the student preview. The board does not follow edits live; this is how
changes reach it. Unset falls back to `BLUZ_STUDENT_REFRESH_SECONDS`.

***

### typeLabels

> **typeLabels**: `Partial`\<`Record`\<[`EventType`](../../../event/enumerations/EventType.md), `string`\>\>

Defined in: [ui/src/api-shared/types/settings/student-view.ts:23](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/settings/student-view.ts#L23)

Per-type label placed before the subject symbol. Missing types fall back
to `DEFAULT_STUDENT_TYPE_LABELS`.
