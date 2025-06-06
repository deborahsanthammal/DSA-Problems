package main

import (
	"fmt"
)

// Output:
// *******
// *******
// *******
// *******
// *******
// *******


func PrintOne(n int){
	for i:=1; i<=n; i++{
		for j:=1; j<=n; j++ {
			fmt.Print(("* "))
		}
		fmt.Print("\n")
	}
}

