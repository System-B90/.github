[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/onboarding/core/storage](../index.md) / browserStorage

# Variable: browserStorage

> `const` **browserStorage**: [`OnboardingStorage`](../../../types/type-aliases/OnboardingStorage.md)

Defined in: [ui/src/components/onboarding/core/storage.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/storage.ts#L16)

`localStorage`, minus the ways it throws: Safari's private mode, a server
render, and a browser configured to block site data all end up as a no-op
store rather than a crash on first paint.
