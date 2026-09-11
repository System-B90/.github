[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/use-help-topics](../index.md) / useHelpTopics

# Function: useHelpTopics()

> **useHelpTopics**(`topics`): `void`

Defined in: [ui/src/components/onboarding/use-help-topics.ts:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-help-topics.ts#L12)

Contributes entries to the help panel. Same contract as `useTour`: the array
must be referentially stable, and the topics live exactly as long as the
component that registered them.

## Parameters

### topics

readonly [`HelpTopic`](../../types/type-aliases/HelpTopic.md)[]

## Returns

`void`
