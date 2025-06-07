package main

func checkAmstrongNumber(num int) bool {
	original := num

	sum := 0
	for num > 0{
		digit := num % 10
		sum = sum + digit * digit * digit
		num /= 10
	}
	return original == sum

}