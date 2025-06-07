package main

import (
	"fmt"
)
func printSeven(n int) {
	for i := 1; i<=5; i++ {
		for j:=1; j<=n-i+1; j++{
			fmt.Printf("%v ", n-j+1)
		}
		fmt.Println("")
	}
}