[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/hive](../index.md) / listPeopleTool

# Variable: listPeopleTool

> `const` **listPeopleTool**: [`AiTool`](../../types/type-aliases/AiTool.md)\<`ListPeopleArgs`\>

Defined in: [ui/src/api-server/ai/tools/hive.ts:109](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/tools/hive.ts#L109)

Hive users by id or name. Events, gantt rows and syllabuses store people as
bare Hive user ids; without this the model can only answer "instructor 32".
