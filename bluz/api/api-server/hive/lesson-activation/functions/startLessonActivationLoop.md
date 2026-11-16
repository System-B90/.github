[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-activation](../index.md) / startLessonActivationLoop

# Function: startLessonActivationLoop()

> **startLessonActivationLoop**(): `void`

Defined in: [ui/src/api-server/hive/lesson-activation.ts:260](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/hive/lesson-activation.ts#L260)

Starts the activation timer. Idempotent, and a no-op without service
credentials so dev machines and unit runs stay quiet.

## Returns

`void`

## Example

```typescript
startLessonActivationLoop(); // from instrumentation.register()
```
