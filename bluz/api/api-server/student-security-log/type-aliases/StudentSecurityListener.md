[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-security-log](../index.md) / StudentSecurityListener

# Type Alias: StudentSecurityListener

> **StudentSecurityListener** = (`userId`, `event`) => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/api-server/student-security-log.ts:28](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/student-security-log.ts#L28)

Hook for alerting (a sysadmin notifier, later). Never awaited by callers.

## Parameters

### userId

`string`

### event

[`StudentSecurityEvent`](../../../api-shared/types/student-view/type-aliases/StudentSecurityEvent.md)

## Returns

`Promise`\<`void`\> \| `void`
