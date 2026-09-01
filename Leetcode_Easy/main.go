package main

import (
	"fmt"
)

func main() {
	nums := []int{1,2,3,4}
	var result bool = ContainsDuplicates(nums)
	fmt.Println(result)
}