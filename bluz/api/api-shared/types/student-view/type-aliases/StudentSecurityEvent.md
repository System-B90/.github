[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSecurityEvent

# Type Alias: StudentSecurityEvent

> **StudentSecurityEvent** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:166](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/student-view.ts#L166)

One recorded attempt.

## Properties

### action

> **action**: [`StudentSecurityAction`](../enumerations/StudentSecurityAction.md)

Defined in: [ui/src/api-shared/types/student-view.ts:167](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/student-view.ts#L167)

***

### at

> **at**: `Date`

Defined in: [ui/src/api-shared/types/student-view.ts:169](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/student-view.ts#L169)

When it happened (server clock).

***

### detail

> **detail**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:171](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/student-view.ts#L171)

Method + path, the offending parameter, the bad value — whatever applies.

***

### ip?

> `optional` **ip?**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:173](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/student-view.ts#L173)

As forwarded by nginx; absent outside a request.
