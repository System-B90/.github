[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-latest-callback](../index.md) / useLatestCallback

# Function: useLatestCallback()

> **useLatestCallback**\<`Args`, `Result`\>(`handler`): (...`args`) => `Result`

Defined in: [ui/src/components/base/use-latest-callback.ts:11](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/use-latest-callback.ts#L11)

A function whose identity never changes but which always runs the `handler`
of the latest render. For event handlers handed to many memoised children
through context: the handler can close over fresh state without every child
re-rendering each time it is rebuilt. Not for use during render — before
the layout effect runs it still calls the previous render's handler.

## Type Parameters

### Args

`Args` *extends* `unknown`[]

### Result

`Result`

## Parameters

### handler

(...`args`) => `Result`

## Returns

(...`args`) => `Result`
