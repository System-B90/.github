[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-activation](../index.md) / startLessonActivationLoop

# Function: startLessonActivationLoop()

> **startLessonActivationLoop**(): `void`

Defined in: [ui/src/api-server/hive/lesson-activation.ts:263](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/hive/lesson-activation.ts#L263)

Starts the activation timer. Idempotent, and a no-op without service
credentials so dev machines and unit runs stay quiet.

## Returns

`void`

## Example

```typescript
startLessonActivationLoop(); // from instrumentation.register()
```
