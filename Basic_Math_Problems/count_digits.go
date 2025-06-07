package main


func countDigits(n int) int {
	var count int = 0
	for n > 0 {
		n /= 10
		count += 1
	}
	return count
}
