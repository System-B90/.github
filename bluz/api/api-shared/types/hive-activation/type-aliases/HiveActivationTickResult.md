[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/hive-activation](../index.md) / HiveActivationTickResult

# Type Alias: HiveActivationTickResult

> **HiveActivationTickResult** = `object`

Defined in: [ui/src/api-shared/types/hive-activation.ts:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/hive-activation.ts#L30)

Outcome of one activator pass, surfaced by the status endpoint and tests.

## Properties

### activated

> **activated**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/hive-activation.ts#L34)

(event, group) pairs newly pushed to Hive in this pass.

***

### alreadyActive

> **alreadyActive**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/hive-activation.ts#L36)

Pairs skipped because an earlier pass already handled them.

***

### consideredEvents

> **consideredEvents**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/hive-activation.ts#L32)

Live events that carry a queue mapping.

***

### errors

> **errors**: `string`[]

Defined in: [ui/src/api-shared/types/hive-activation.ts:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/hive-activation.ts#L40)

Human-readable reasons for the failures, for logs and diagnostics.

***

### failed

> **failed**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:38](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/hive-activation.ts#L38)

Pairs that could not be pushed (unresolved group, Hive error, …).
