package main

import (
	"fmt"
)

func printThree(n int) {
	for i := 1; i <= n; i++ {
		for j:=1; j<=i; j++ {
			fmt.Printf("%v ", j)
		}
		fmt.Println("")
	}
}