[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/NoIterationPrompt](../index.md) / NoIterationPrompt

# Function: NoIterationPrompt()

> **NoIterationPrompt**(): `Element`

Defined in: [ui/src/components/base/NoIterationPrompt.tsx:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/NoIterationPrompt.tsx#L24)

A fresh install no longer inherits an auto-created "current" iteration
(#471) — that iteration had no real name, and its literal id collided with
the `/api/iterations/current` route. Instead the app asks for a real one on
first boot and points at the tab that creates it.

Re-checked whenever the settings dialog closes, so creating the iteration
dismisses the prompt without a reload. A failed list leaves the prompt shut:
an unreachable registry is an outage, not an empty install.

## Returns

`Element`
