package main

func checkPalindrome(num int) bool {
	reversed := 0
	original := num
	for num > 0 {
		last_digit := num % 10
		reversed = reversed*10 + last_digit
		num /= 10
	}
	return original == reversed
}