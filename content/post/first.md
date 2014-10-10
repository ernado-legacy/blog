+++
date = "2014-10-11T00:20:38+04:00"
draft = false
title = "Первый"
+++

Первый пост, он сложный самый
Ну и что за фигня?

```go

package main

import (
	"bytes"
	"fmt"
)

const (
	header = "kek"
)

type SitemapItem struct {
	Loc string
}

func (item SitemapItem) String() string {
	return fmt.Sprintf(sitemapTemplate, item.Loc)
}

func SitemapStr(items []SitemapItem) (string, error) {
	var buffer bytes.Buffer
	buffer.WriteString(header)
	for _, item := range items {
		_, err := buffer.WriteString(item.String())
		if err != nil {
			return "", err
		}
	}
	buffer.WriteString(footer)
	return buffer.String(), nil
}


```