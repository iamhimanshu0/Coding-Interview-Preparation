package main

import "fmt"

/*
What is a variadic function?

Functions in general accept only a fixed number of arguments.
A variadic function is a function that accepts a variable number of arguments.
If the last parameter of a function definition is prefixed by ellipsis ...,
then the function can accept any number of arguments for that parameter.

Only the last parameter of a function can be variadic.

func hello(a int, b ...int) {
}

*/

func find(num int, nums ...int) {
	fmt.Printf("type of nums is %T\n", nums)

	found := false
	for i, v := range nums {
		if v == num {
			fmt.Println(num, "found at index", i, "in", nums)
			found = true
		}
	}
	if !found {
		fmt.Println(num, "not found in ", nums)
	}
	fmt.Printf("\n")
}

// Slice arguments vs Variadic arguments
func sliceVardic(num int, nums []int) {
	fmt.Printf("type of nums is %T\n", nums)
	found := false
	for i, v := range nums {
		if v == num {
			fmt.Println(num, "found at index", i, "in", nums)
			found = true
		}
	}
	if !found {
		fmt.Println(num, "not found in ", nums)
	}
	fmt.Printf("\n")
}

// passing a slice to a variadic function
func passingSliceVariadic(num int, nums ...int) {
	fmt.Printf("type of nums is %T\n", nums)
	found := false
	for i, v := range nums {
		if v == num {
			fmt.Println(num, "found at index", i, "in", nums)
			found = true
		}
	}
	if !found {
		fmt.Println(num, "not found in ", nums)
	}
	fmt.Printf("\n")
}

// change string
func change(s ...string) {
	s[0] = "GO"
}

func main() {
	// find(89, 89, 90, 95)
	// find(45, 89, 90, 95, 45, 2, 3)
	// find(12, 1, 2, 3, 4, 5)
	// find(89, 89)
	// sliceVardic(89, []int{89, 90, 9})
	// sliceVardic(45, []int{89, 90, 95, 45, 2, 3})
	// sliceVardic(12, []int{1, 2, 3, 4, 5})
	// sliceVardic(89, []int{89})

	// nums := []int{12, 13, 14}
	// passingSliceVariadic(89, nums) // this will give error
	// passingSliceVariadic(12, nums...)

	welcome := []string{"Hello", "World"}
	change(welcome...)
	fmt.Println(welcome)
}
