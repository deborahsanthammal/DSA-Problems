package main

// import (
// 	"fmt"
// )

func ContainsDuplicates(nums []int) bool{
	var count map[string]int = map[string]int{}

	for i:=0; i<len(nums); i++ {
		_, exists := count[string(nums[i])]
		if exists {
			return true
		}
		count[string(nums[i])] += 1
	}
	return false

}

