[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiChoiceOption

# Type Alias: AiChoiceOption

> **AiChoiceOption** = `object`

Defined in: [ui/src/api-shared/types/ai.ts:86](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai.ts#L86)

One selectable answer in an [AiStreamEventType.Choice](../enumerations/AiStreamEventType.md#choice) prompt.

## Properties

### description?

> `optional` **description?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:92](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai.ts#L92)

Optional one-line clarification under the label.

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:90](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai.ts#L90)

Hebrew label on the button.

***

### value

> **value**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:88](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai.ts#L88)

Sent back to the model verbatim.
