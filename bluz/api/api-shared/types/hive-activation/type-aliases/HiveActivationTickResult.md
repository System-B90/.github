[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/hive-activation](../index.md) / HiveActivationTickResult

# Type Alias: HiveActivationTickResult

> **HiveActivationTickResult** = `object`

Defined in: [ui/src/api-shared/types/hive-activation.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L31)

Outcome of one activator pass, surfaced by the status endpoint and tests.

## Properties

### activated

> **activated**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L35)

(event, group) pairs newly pushed to Hive in this pass.

***

### alreadyActive

> **alreadyActive**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:37](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L37)

Pairs skipped because an earlier pass already handled them.

***

### consideredEvents

> **consideredEvents**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L33)

Live events that carry a queue mapping.

***

### errors

> **errors**: `string`[]

Defined in: [ui/src/api-shared/types/hive-activation.ts:41](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L41)

Human-readable reasons for the failures, for logs and diagnostics.

***

### failed

> **failed**: `number`

Defined in: [ui/src/api-shared/types/hive-activation.ts:39](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/hive-activation.ts#L39)

Pairs that could not be pushed (unresolved group, Hive error, …).
