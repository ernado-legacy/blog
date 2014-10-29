+++
Categories = []
Description = "Короткая заметка о профилировании юнит-тестов и бенчмарков в Go"
Keywords = []
Tags = ["golang", "pprof", "tests"]
date = "2014-10-29T06:50:17+03:00"
title = "Golang: профилирование тестов"
+++


Для `go test` есть [набор флагов](http://golang.org/cmd/go/#hdr-Description_of_testing_flags), среди которых можно найти
`cpuprofile` и `memprofile`, с помощью которых можно указать путь к результатам профилирования.

Запускается оно так:
```bash
$ go test -cpuprofile cpu.out -memprofile mem.out
```

При этом создастся бинарный файл `name.test`, где name - имя пакета.

Для анализа данных используется `pprof`, запускается так:

```bash
$ go tool pprof cache.test cpu.out
```

Например, top10 получить можно так:

```bash
$ go tool pprof cache.test cpu.out 
Welcome to pprof!  For help, type 'help'.
(pprof) web
Total: 1 samples
Loading web page file:////tmp/n0adIdkDZk.0.svg
Created new window in existing browser session.
(pprof) top10
Total: 1 samples
       1 100.0% 100.0%        1 100.0% syscall.Syscall
       0   0.0% 100.0%        1 100.0% fmt.Fprint
       0   0.0% 100.0%        1 100.0% fmt.Print
       0   0.0% 100.0%        1 100.0% github.com/ernado/cache.TestCache
       0   0.0% 100.0%        1 100.0% github.com/ernado/cache.func·007
# ...
```