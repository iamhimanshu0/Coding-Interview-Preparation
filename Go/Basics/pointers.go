package main

import "fmt"

/*
What is a pointer?
A pointer is a variable that stores the
memory address of another variable.
*/
func simplePointer() {
	b := 255
	var a *int = &b
	fmt.Printf("Type of a is %T\n", a)
	fmt.Println("address of b is", a)
}

func zeroValueOfAPointer() {
	// zero value of a pointer is nil.

	a := 25
	var b *int
	if b == nil {
		fmt.Println("b is ", b)
		b = &a
		fmt.Println("b after initializatin is ", b)
	}
}

func createPointerUsingNewFunction() {
	/*
		Go also provides a handy function new to create pointers.
		The new function takes a type as an argument and returns a pointer
		to a newly allocated zero value of the type passed as argument.
	*/
	size := new(int)
	fmt.Printf("Size value is %d, type is %T, address is %v\n", *size, size, size)
	*size = 85
	fmt.Println("New size value is", *size)

}

func dereferencingPointer() {
	/*
		Dereferencing a pointer means accessing the value of the variable
		to which the pointer points. *a is the syntax to deference a.
	*/
	b := 255
	a := &b
	fmt.Println("address of b is", a)
	fmt.Println("value of b is", *a)
}

// passing pointer to a function
func change(val *int) {
	*val = 55
}

func passingPointerTOFunction() {
	a := 58
	fmt.Println("Value of a before function call is", a)
	b := &a
	change(b)
	fmt.Println("Value of a after function call is", a)
}

// Returning pointer from a function
func hello() *int {
	i := 5
	return &i
}

func ReturnPointer() {
	d := hello()
	fmt.Println("value of d", *d)
}

// Do not pass a pointer to an array as an argument to a function. Use slice instead.
func modifyArray(arr *[3]int) {
	// (*arr)[0] = 90
	// a[x] is shorthand for (*a)[x].
	arr[0] = 90
}

func modifySlice(sls []int) {
	sls[0] = 90
}

func argumentPass() {
	a := [3]int{89, 90, 91}

	// modifyArray(&a)

	modifySlice(a[:])

	fmt.Println(a)
}

func main() {
	// simplePointer()
	// zeroValueOfAPointer()
	// createPointerUsingNewFunction()
	// dereferencingPointer()
	// passingPointerTOFunction()
	// ReturnPointer()
	argumentPass()
}

// Go does not support pointer arithmetic
