[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-activation](../index.md) / startLessonActivationLoop

# Function: startLessonActivationLoop()

> **startLessonActivationLoop**(): `void`

Defined in: [ui/src/api-server/hive/lesson-activation.ts:249](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/lesson-activation.ts#L249)

Starts the activation timer. Idempotent, and a no-op without service
credentials so dev machines and unit runs stay quiet.

## Returns

`void`

## Example

```typescript
startLessonActivationLoop(); // from instrumentation.register()
```
