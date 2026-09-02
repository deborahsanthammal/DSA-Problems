package main

import (
	"fmt"
)

func main() {
	// nums := []int{1,2,3,4}
	// var result bool = ContainsDuplicates(nums)
	// fmt.Println(result)

	// var s, t string = "racecar", "carrace"
	// var result bool = isAnagram(s, t)
	// fmt.Println(result)

	var target int = 7
	var nums []int = []int{3,4,5,6}
	var result []int = twoSum(nums, target)
	fmt.Println(result)
}