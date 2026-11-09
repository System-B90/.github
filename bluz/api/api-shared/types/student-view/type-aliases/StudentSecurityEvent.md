[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSecurityEvent

# Type Alias: StudentSecurityEvent

> **StudentSecurityEvent** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:185](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L185)

One recorded attempt.

## Properties

### action

> **action**: [`StudentSecurityAction`](../enumerations/StudentSecurityAction.md)

Defined in: [ui/src/api-shared/types/student-view.ts:186](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L186)

***

### at

> **at**: `Date`

Defined in: [ui/src/api-shared/types/student-view.ts:188](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L188)

When it happened (server clock).

***

### detail

> **detail**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:190](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L190)

Method + path, the offending parameter, the bad value — whatever applies.

***

### ip?

> `optional` **ip?**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:192](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L192)

As forwarded by nginx; absent outside a request.
