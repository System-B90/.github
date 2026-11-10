[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-monitor](../index.md) / StudentMonitorRow

# Type Alias: StudentMonitorRow

> **StudentMonitorRow** = `object`

Defined in: [ui/src/api-shared/types/student-monitor.ts:4](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-monitor.ts#L4)

Staff-only: one student's day on the board, as the monitor shows it.

## Properties

### ips

> **ips**: `string`[]

Defined in: [ui/src/api-shared/types/student-monitor.ts:11](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-monitor.ts#L11)

Every address the board reported from, plus those of recorded attempts.

***

### name

> **name**: `null` \| `string`

Defined in: [ui/src/api-shared/types/student-monitor.ts:7](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-monitor.ts#L7)

Hive display name; null when Hive could not name the id (or `anonymous`).

***

### seconds

> **seconds**: `number`

Defined in: [ui/src/api-shared/types/student-monitor.ts:9](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-monitor.ts#L9)

Seconds the board was open and focused.

***

### securityEventCount

> **securityEventCount**: `number`

Defined in: [ui/src/api-shared/types/student-monitor.ts:13](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-monitor.ts#L13)

True total of suspected attempts, including any dropped from `securityEvents`.

***

### securityEvents

> **securityEvents**: `object`[]

Defined in: [ui/src/api-shared/types/student-monitor.ts:15](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-monitor.ts#L15)

Most recent attempts, newest first.

#### action

> **action**: [`StudentSecurityAction`](../../student-view/enumerations/StudentSecurityAction.md)

#### at

> **at**: `string`

ISO timestamp.

#### detail

> **detail**: `string`

#### ip?

> `optional` **ip?**: `string`

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-shared/types/student-monitor.ts:5](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-monitor.ts#L5)
