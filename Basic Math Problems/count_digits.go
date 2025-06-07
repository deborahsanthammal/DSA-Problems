package main

import (
	"fmt"
)

func countDigits(n int) int {
	var count int = 0
	for n > 0 {
		n /= 10
		count += 1
	}
	return count
}

func main() {
	fmt.Printf("%v\n", countDigits(76543))
}