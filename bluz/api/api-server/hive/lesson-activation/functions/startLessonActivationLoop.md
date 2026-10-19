[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-activation](../index.md) / startLessonActivationLoop

# Function: startLessonActivationLoop()

> **startLessonActivationLoop**(): `void`

Defined in: [ui/src/api-server/hive/lesson-activation.ts:264](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/hive/lesson-activation.ts#L264)

Starts the activation timer. Idempotent, and a no-op without service
credentials so dev machines and unit runs stay quiet.

## Returns

`void`

## Example

```typescript
startLessonActivationLoop(); // from instrumentation.register()
```
