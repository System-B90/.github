[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-security-log](../index.md) / StudentSecurityListener

# Type Alias: StudentSecurityListener

> **StudentSecurityListener** = (`userId`, `event`) => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/api-server/student-security-log.ts:28](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/student-security-log.ts#L28)

Hook for alerting (a sysadmin notifier, later). Never awaited by callers.

## Parameters

### userId

`string`

### event

[`StudentSecurityEvent`](../../../api-shared/types/student-view/type-aliases/StudentSecurityEvent.md)

## Returns

`Promise`\<`void`\> \| `void`
