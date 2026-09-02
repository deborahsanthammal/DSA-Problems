package main

import (
	"fmt"
)

func main() {
	// nums := []int{1,2,3,4}
	// var result bool = ContainsDuplicates(nums)
	// fmt.Println(result)

	var s, t string = "racecar", "carrace"
	var result bool = isAnagram(s, t)
	fmt.Println(result)
}