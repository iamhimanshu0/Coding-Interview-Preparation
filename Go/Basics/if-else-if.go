package main

import "fmt"

func ifWithAssignment() {
	if num := 10; num%2 == 0 {
		fmt.Println("Number is even")
	} else {
		fmt.Println("Number is odd")
	}
}

func main() {
	ifWithAssignment()
}
