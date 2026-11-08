[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-security-log](../index.md) / StudentSecurityListener

# Type Alias: StudentSecurityListener

> **StudentSecurityListener** = (`userId`, `event`) => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/api-server/student-security-log.ts:28](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/student-security-log.ts#L28)

Hook for alerting (a sysadmin notifier, later). Never awaited by callers.

## Parameters

### userId

`string`

### event

[`StudentSecurityEvent`](../../../api-shared/types/student-view/type-aliases/StudentSecurityEvent.md)

## Returns

`Promise`\<`void`\> \| `void`
