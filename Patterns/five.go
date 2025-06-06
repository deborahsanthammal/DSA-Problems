package main

import (
	"fmt"
)

func printFive(n int) {
	for i := 1; i <= n; i++ {
		for j := 1; j <= n-i+1; j++ {
			fmt.Print("* ")
		}
		fmt.Println("")
	}
}