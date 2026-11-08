[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/student-view](../index.md) / StudentViewSettings

# Type Alias: StudentViewSettings

> **StudentViewSettings** = `object`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:18](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/student-view.ts#L18)

## Properties

### eventNameMode

> **eventNameMode**: [`StudentEventNameMode`](../enumerations/StudentEventNameMode.md)

Defined in: [ui/src/api-shared/types/settings/student-view.ts:19](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/student-view.ts#L19)

***

### refreshSeconds?

> `optional` **refreshSeconds?**: `number`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:30](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/student-view.ts#L30)

How often an open student board refetches, in seconds, set by staff from
the student preview. The board does not follow edits live; this is how
changes reach it. Unset falls back to `BLUZ_STUDENT_REFRESH_SECONDS`.

***

### typeLabels

> **typeLabels**: `Partial`\<`Record`\<[`EventType`](../../../event/enumerations/EventType.md), `string`\>\>

Defined in: [ui/src/api-shared/types/settings/student-view.ts:24](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/settings/student-view.ts#L24)

Per-type label placed before the subject symbol. Missing types fall back
to `DEFAULT_STUDENT_TYPE_LABELS`.
