package main

import (
	"fmt"
)

func main() {
	// Reverse a number
	reversed := reverseNumber(121)
	fmt.Printf("Reversed Number: %v\n", reversed)

	// Count digits in a number
	digitCount := countDigits(121)
	fmt.Printf("Digit Count: %v\n", digitCount)

	// Check if a number is a palindrome
	palindrome := checkPalindrome(121)
	fmt.Printf("Is Palindrome: %v\n", palindrome)

	// Check if a number is an Armstrong number
	armstrong := checkAmstrongNumber(371)
	fmt.Printf("Is Armstrong Number: %v\n", armstrong)
}