package main

import (
	"fmt"
)

func PrintTwo(n int) {
	for i:=1; i<=n; i++{
		for j:=1; j<=i; j++ {
			fmt.Print("* ")
		}
		fmt.Println("")
	}
}