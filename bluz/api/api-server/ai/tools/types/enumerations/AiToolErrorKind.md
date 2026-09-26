[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiToolErrorKind

# Enumeration: AiToolErrorKind

Defined in: [ui/src/api-server/ai/tools/types.ts:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L19)

Failure classes a tool can produce, chosen for what the *model* should do
next rather than for what went wrong internally. Two errors with the same
recovery path share a kind.

## Enumeration Members

### Conflict

> **Conflict**: `"conflict"`

Defined in: [ui/src/api-server/ai/tools/types.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L27)

Existing data conflicts. Needs a human decision.

***

### InvalidArguments

> **InvalidArguments**: `"invalid_arguments"`

Defined in: [ui/src/api-server/ai/tools/types.ts:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L21)

The model's arguments were malformed or invalid. Fix and retry.

***

### NotFound

> **NotFound**: `"not_found"`

Defined in: [ui/src/api-server/ai/tools/types.ts:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L23)

The referenced record does not exist. Re-list, do not retry as-is.

***

### Rejected

> **Rejected**: `"rejected"`

Defined in: [ui/src/api-server/ai/tools/types.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L25)

A business rule refused it. Not retryable by any phrasing.

***

### Unavailable

> **Unavailable**: `"unavailable"`

Defined in: [ui/src/api-server/ai/tools/types.ts:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/types.ts#L29)

A dependency is down. Retry at most once.
