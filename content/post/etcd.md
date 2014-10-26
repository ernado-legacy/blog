+++
Categories = []
Description = ""
Keywords = []
Tags = ["nginx", "coreos", "etcd"]
date = "2014-10-27T02:07:38+03:00"
title = "Ошибки подключения к etcd в docker"
+++

Настройка etcd не так тривиальна, как может показаться на первый взгляд. Может возникнуть ошибка:

```
Error: 501: All the given peers are not reachable
```
Причем совершенно непонятно откуда. Такое у меня вылезло в логах при использовании confd или etcdctl, 
причем к кластеру оно подключалось нормально. Дело оказалось в способе запуска etcd в docker.


Сначала контейнер запускался так:
```bash
docker run -d --name etcd -p 4001:4001 -p 7001:7001 coreos/etcd
```

И попытки подключиться из контейнеров вызывали ошибку 501. Выяснилось, что необходимо указать etcd адрес, который он будет отдавать клиентам
при попытке соединения с ним. Как-то так:


```bash
#!/bin/bash

# для удобства адреса вынесены в переменные окружения
export ETCD_PORT=${ETCD_PORT:-4001}
export HOST_IP=${HOST_IP:-172.17.42.1}
export ETCD=$HOST_IP:$ETCD_PORT

docker run -d --name etcd -p $ETCD:4001 -p $HOST_IP:7001:7001 \ 
	coreos/etcd -addr=$ETCD -vv -name="etcd"
```

Такая штука мне была нужна для тестирования [nginx-balancer](https://github.com/cydev/nginx-balancer), который настраивается через etcd.
