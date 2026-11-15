[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-monitor](../index.md) / ApiStudentMonitorGetResponse

# Type Alias: ApiStudentMonitorGetResponse

> **ApiStudentMonitorGetResponse** = `object`

Defined in: [ui/src/api-shared/types/student-monitor.ts:24](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/types/student-monitor.ts#L24)

## Properties

### date

> **date**: `string`

Defined in: [ui/src/api-shared/types/student-monitor.ts:26](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/types/student-monitor.ts#L26)

`yyyy-MM-dd`, app timezone.

***

### rows

> **rows**: [`StudentMonitorRow`](StudentMonitorRow.md)[]

Defined in: [ui/src/api-shared/types/student-monitor.ts:28](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/types/student-monitor.ts#L28)

Students with attempts first, then by focused time.
