[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSecurityEvent

# Type Alias: StudentSecurityEvent

> **StudentSecurityEvent** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:194](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L194)

One recorded attempt.

## Properties

### action

> **action**: [`StudentSecurityAction`](../enumerations/StudentSecurityAction.md)

Defined in: [ui/src/api-shared/types/student-view.ts:195](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L195)

***

### at

> **at**: `Date`

Defined in: [ui/src/api-shared/types/student-view.ts:197](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L197)

When it happened (server clock).

***

### detail

> **detail**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:199](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L199)

Method + path, the offending parameter, the bad value — whatever applies.

***

### ip?

> `optional` **ip?**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:201](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L201)

As forwarded by nginx; absent outside a request.
