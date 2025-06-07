package main

import (
	"fmt"
)

func main() {
	// Reverse a number
	reversed := reverseNumber(76543)
	fmt.Printf("Reversed Number: %v\n", reversed)

	// Count digits in a number
	digitCount := countDigits(76543)
	fmt.Printf("Digit Count: %v\n", digitCount)
}