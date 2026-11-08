[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / WsScope

# Enumeration: WsScope

Defined in: [session-server/session-common.ts:110](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/session-server/session-common.ts#L110)

Privilege label signed into a connect ticket (#656). Bluz serves two kinds
of socket and they may not see the same traffic, so the scope decides what a
socket is allowed to register for — see `session-server.ts`.

## Enumeration Members

### Hanich

> **Hanich**: `"hanich"`

Defined in: [session-server/session-common.ts:114](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/session-server/session-common.ts#L114)

Hanich. Content-free refresh pings and nothing else.

***

### Segel

> **Segel**: `"segel"`

Defined in: [session-server/session-common.ts:112](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/session-server/session-common.ts#L112)

Segel/Admin. The full staff calendar wire.
