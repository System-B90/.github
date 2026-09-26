[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-balancer](../index.md) / BalancerSlot

# Type Alias: BalancerSlot

> **BalancerSlot** = `object`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L23)

One placeable unit of work on a day, before it has a clock time.

## Properties

### durationMinutes

> **durationMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:28](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L28)

Duration in minutes, already resolved from allocated/minimum.

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:26](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L26)

***

### isDailyRecurrence

> **isDailyRecurrence**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L32)

***

### isPinnedMeal

> **isPinnedMeal**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L33)

***

### isRecurrenceEcho

> **isRecurrenceEcho**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L31)

***

### key

> **key**: `string`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L25)

Stable key, unique within a plan: `${eventId}@${dayId}#${ordinal}`.

***

### moduleId

> **moduleId**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L30)

Gantt module the event belongs to; drives module cohesion.

***

### sortOrder

> **sortOrder**: `number`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-balancer.ts#L35)

Original position within its day, preserved for stable ordering.
