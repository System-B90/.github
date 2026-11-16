[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-monitor/StudentMonitorDialog](../index.md) / StudentMonitorDialog

# Function: StudentMonitorDialog()

> **StudentMonitorDialog**(`__namedParameters`): `Element`

Defined in: [ui/src/components/student-monitor/StudentMonitorDialog.tsx:55](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/student-monitor/StudentMonitorDialog.tsx#L55)

Staff-only: for one day, how long each student had the board open and
focused, and every suspected malicious attempt recorded against them.
Opened from the student-view preview bar; the data comes from the staff
route `/api/student-monitor`, never from the student surface.

## Parameters

### \_\_namedParameters

#### initialDate?

`string`

#### onClose

() => `void`

#### open

`boolean`

## Returns

`Element`
