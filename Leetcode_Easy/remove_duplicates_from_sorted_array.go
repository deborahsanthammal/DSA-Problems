package main

import (
	"fmt"
	// "slices"
)

func removeDuplicates(nums []int) {
	i := 0
	for i != len(nums) {
		if nums[i] == nums[i+1] {
			// Remove the duplicate element
			nums = append(nums[:i], nums[:i+1]...)
		} 
		i++
	}
}

func main() {
	nums := []int{1,1,2,2,3,3,3,4,4,5,5,5,5,5}
	fmt.Println("Original slice:", nums)
	removeDuplicates(nums)
	fmt.Println("Slice after removing duplicates:", nums)
}
