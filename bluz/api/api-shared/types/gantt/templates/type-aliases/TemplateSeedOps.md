[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/templates](../index.md) / TemplateSeedOps

# Type Alias: TemplateSeedOps

> **TemplateSeedOps** = `object`

Defined in: [ui/src/api-shared/types/gantt/templates.ts:73](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/gantt/templates.ts#L73)

Persistence the template seeder needs; the client and server each supply their own.

## Properties

### createWeek

> **createWeek**: (`payload`) => `Promise`\<\{ `w2d?`: `object`[]; \}\>

Defined in: [ui/src/api-shared/types/gantt/templates.ts:74](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/gantt/templates.ts#L74)

#### Parameters

##### payload

###### comment

`string`

###### curriculumId

[`GanttCurriculumId`](../../models/curriculum/type-aliases/GanttCurriculumId.md)

###### number

`number`

###### weekendDuty

`boolean`

#### Returns

`Promise`\<\{ `w2d?`: `object`[]; \}\>

***

### setDayMinutes

> **setDayMinutes**: (`dayId`, `minutes`) => `Promise`\<`unknown`\>

Defined in: [ui/src/api-shared/types/gantt/templates.ts:84](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/gantt/templates.ts#L84)

#### Parameters

##### dayId

`string`

##### minutes

`number`

#### Returns

`Promise`\<`unknown`\>
