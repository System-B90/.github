[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/access-token](../index.md) / AccessTokenScope

# Enumeration: AccessTokenScope

Defined in: [ui/src/api-shared/types/access-token.ts:28](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/access-token.ts#L28)

What a token may do. `ReadOnly` is limited to safe HTTP methods (GET/HEAD),
so it can never change data, including reads the API exposes as POST.
`ReadWrite` can do whatever its owner can.

## Enumeration Members

### ReadOnly

> **ReadOnly**: `"ReadOnly"`

Defined in: [ui/src/api-shared/types/access-token.ts:30](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/access-token.ts#L30)

***

### ReadWrite

> **ReadWrite**: `"ReadWrite"`

Defined in: [ui/src/api-shared/types/access-token.ts:31](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/access-token.ts#L31)
