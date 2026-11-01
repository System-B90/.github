[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSecurityEvent

# Type Alias: StudentSecurityEvent

> **StudentSecurityEvent** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:160](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L160)

One recorded attempt.

## Properties

### action

> **action**: [`StudentSecurityAction`](../enumerations/StudentSecurityAction.md)

Defined in: [ui/src/api-shared/types/student-view.ts:161](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L161)

***

### at

> **at**: `Date`

Defined in: [ui/src/api-shared/types/student-view.ts:163](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L163)

When it happened (server clock).

***

### detail

> **detail**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:165](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L165)

Method + path, the offending parameter, the bad value — whatever applies.

***

### ip?

> `optional` **ip?**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:167](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L167)

As forwarded by nginx; absent outside a request.
