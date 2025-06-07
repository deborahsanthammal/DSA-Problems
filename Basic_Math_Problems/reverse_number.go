package main

func reverseNumber(n int) int {
	var reversed int = 0
	for n > 0 {
		lastDigit := n % 10
		reversed = reversed*10 + lastDigit
		n /= 10
	}
	return reversed
}
