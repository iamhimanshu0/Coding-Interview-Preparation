package main

import "fmt"

func simpleDecleration() {
	var a [3]int //int arrary with length 3
	fmt.Println(a)

	a[0] = 12
	a[1] = 2
	a[2] = 4

	fmt.Println(a)

	// short hand declaration
	b := [3]int{12, 34, 45}
	fmt.Println(b)

	// It is not necessary that all elements in an array
	//  have to be assigned a value during short hand declaration.
	c := [3]int{12}
	fmt.Println(c)

}

func ignoringLength() {
	a := [...]int{12, 3, 13}
	fmt.Println(a)
}

func arrayValues() {
	/*
		Arrays in Go are value types and not reference types.
		This means that when they are assigned to a new variable,
		a copy of the original array is assigned to the new variable.
		If changes are made to the new variable, it will not be
		reflected in the original array.
	*/

	a := [...]string{"usa", "india", "germany"}
	b := a //copy of a is assigned to b
	b[0] = "singapore"
	fmt.Println("A is ", a)
	fmt.Println("B is ", b)

}

func changeLocal(num [5]int) {
	num[0] = 55
	fmt.Println("Inside function", num)
}

func arryaValuesFunction() {
	num := [...]int{5, 6, 7, 8, 9}
	fmt.Println("Before passing to function", num)
	changeLocal(num)
	fmt.Println("After passing to function", num)
}

// iterting array
func itertingArray() {
	a := [...]int{12, 123, 123, 3, 3, 44, 543, 34}
	for i := 0; i < len(a); i++ {
		fmt.Printf("Values are %d\n", a[i])
	}
}

// better way to loop over array
func intertingArrayBest() {
	a := [...]float64{67.8, 65.8, 45.98, 345.87}
	sum := float64(0)

	// if we want to ignore index then
	// for _, v := range a

	for i, v := range a { //range return both index and value
		fmt.Printf("%d the element of a in %.2f\n", i, v)
		sum += v
	}

	fmt.Println("Sum of all these values are", sum)
}

// multidimensional array
func printarray(a [3][2]string) {
	for _, v1 := range a {
		for _, v2 := range v1 {
			fmt.Printf("%s ", v2)
		}
		fmt.Println("")
	}
}

func multidimensionalArray() {
	a := [3][2]string{
		{"lion", "tiger"},
		{"cat", "dog"},
		{"piegon", "peacock"},
	}
	printarray(a)

}

// slices
/*
A slice is a convenient, flexible and powerful wrapper
on top of an array. Slices do not own any data on their
own. They are just references to existing arrays.

A slice with elements of type T is represented by []T
*/
func slicesArray() {
	a := [5]int{76, 77, 78, 79, 80}
	var b []int = a[1:4]
	fmt.Println(b)
}

func modifySlice() {
	darr := [...]int{57, 89, 90, 82, 100, 78, 67, 69, 59}
	dslice := darr[2:5]
	fmt.Println("arrya before", darr)

	for i := range dslice {
		dslice[i]++
	}
	fmt.Println("array after", darr)

	fmt.Println("Create array with all element", darr[:])
}

func main() {
	// simpleDecleration()
	// ignoringLength()
	// arrayValues()
	// arryaValuesFunction()
	// itertingArray()
	// intertingArrayBest()
	// multidimensionalArray()
	// slicesArray()
	modifySlice()
}
