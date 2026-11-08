[**TypeDoc API**](../../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/export/excel/workbook](../index.md) / buildGanttExcelWorkbook

# Function: buildGanttExcelWorkbook()

> **buildGanttExcelWorkbook**(`curriculum`, `mappings`, `userNamesById?`): `Promise`\<`Workbook`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/export/excel/workbook.ts:137](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/app/api/gantt/curriculums/[id]/export/excel/workbook.ts#L137)

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
