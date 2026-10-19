[**TypeDoc API**](../../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/export/excel/workbook](../index.md) / buildGanttExcelWorkbook

# Function: buildGanttExcelWorkbook()

> **buildGanttExcelWorkbook**(`curriculum`, `mappings`, `userNamesById?`): `Promise`\<`Workbook`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/export/excel/workbook.ts:130](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/app/api/gantt/curriculums/[id]/export/excel/workbook.ts#L130)

## Parameters

### curriculum

[`ApiCurriculum`](../../../../../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)

### mappings

[`DayMapping`](../type-aliases/DayMapping.md)[]

### userNamesById?

`Map`\<`number`, `string`\> = `...`

Hive user id → display name. Missing ids fall back to the raw id.

## Returns

`Promise`\<`Workbook`\>
