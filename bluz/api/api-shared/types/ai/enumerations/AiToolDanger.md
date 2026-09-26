[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiToolDanger

# Enumeration: AiToolDanger

Defined in: [ui/src/api-shared/types/ai.ts:66](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L66)

How much damage running a tool can do. Drives the colour, the wording and
the extra confirmation on the approval card — a reversible edit and an
irreversible delete must not look alike.

## Enumeration Members

### Caution

> **Caution**: `"caution"`

Defined in: [ui/src/api-shared/types/ai.ts:70](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L70)

Changes stored data; recoverable through history.

***

### Destructive

> **Destructive**: `"destructive"`

Defined in: [ui/src/api-shared/types/ai.ts:72](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L72)

Destroys or overwrites data at scale. Needs an explicit re-confirm.

***

### Safe

> **Safe**: `"safe"`

Defined in: [ui/src/api-shared/types/ai.ts:68](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L68)

Reads only, or a write that loses nothing.
