package main
import (
	"fmt"
)
func printSix(n int) {
	for i := 1; i <= n; i++ {
		for j := 1; j <= n-i+1; j++ {
			fmt.Printf("%v ", j)
		}
		fmt.Println("")
	}
}