[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/student-view](../index.md) / StudentViewSettings

# Type Alias: StudentViewSettings

> **StudentViewSettings** = `object`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:17](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/settings/student-view.ts#L17)

## Properties

### eventNameMode

> **eventNameMode**: [`StudentEventNameMode`](../enumerations/StudentEventNameMode.md)

Defined in: [ui/src/api-shared/types/settings/student-view.ts:18](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/settings/student-view.ts#L18)

***

### typeLabels

> **typeLabels**: `Partial`\<`Record`\<[`EventType`](../../../event/enumerations/EventType.md), `string`\>\>

Defined in: [ui/src/api-shared/types/settings/student-view.ts:23](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/settings/student-view.ts#L23)

Per-type label placed before the subject symbol. Missing types fall back
to `DEFAULT_STUDENT_TYPE_LABELS`.
