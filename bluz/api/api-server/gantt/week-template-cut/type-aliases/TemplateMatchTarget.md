[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-cut](../index.md) / TemplateMatchTarget

# Type Alias: TemplateMatchTarget

> **TemplateMatchTarget** = `object`

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:29](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/week-template-cut.ts#L29)

What the cut needs to know about a gantt event to match it (#997).

## Properties

### courseNames

> **courseNames**: `string`[]

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:34](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/week-template-cut.ts#L34)

Its shuffles and courses (with their ancestors), by name.

***

### daily?

> `optional` **daily?**: `boolean`

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:39](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/week-template-cut.ts#L39)

Recurs every day. One template placement then stands for every weekday
the template does not place it on itself.

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:30](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/week-template-cut.ts#L30)

***

### names

> **names**: `string`[]

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:32](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/week-template-cut.ts#L32)

Every name the event may carry: its gantt title and its cut name.
