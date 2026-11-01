[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-security-log](../index.md) / recordStudentSecurityEvent

# Function: recordStudentSecurityEvent()

> **recordStudentSecurityEvent**(`userId`, `action`, `detail`, `ip?`): `void`

Defined in: [ui/src/api-server/student-security-log.ts:119](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/student-security-log.ts#L119)

Records a suspected malicious attempt by a student (or an unattributable
caller) on that day's student time record.

Fire-and-forget: never throws and never delays the refusal it accompanies —
a logging failure must not change what the attacker sees.

## Parameters

### userId

`string`

Session-derived id, or [ANONYMOUS\_SECURITY\_USER](../variables/ANONYMOUS_SECURITY_USER.md).

### action

[`StudentSecurityAction`](../../../api-shared/types/student-view/enumerations/StudentSecurityAction.md)

What was attempted.

### detail

`string`

The specifics (method + path, offending parameter, …).

### ip?

`string`

The caller's address, for callers outside a request scope (the
          proxy); route code leaves it out and the request's is used.

## Returns

`void`
