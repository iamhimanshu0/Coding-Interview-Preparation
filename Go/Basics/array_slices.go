package main

import (
	"fmt"
)

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

// length and capacity of a slice

/*
The length of the slice is the number of elements in the slice.
The capacity of the slice is the number of elements in the
underlying array starting from the index from which the slice
is created.
*/

func lengthCapicty() {
	a := [...]string{"apple", "orange", "grapes", "mango", "pine apple", "chikoo"}
	aSlice := a[1:3]
	fmt.Printf("length of slice %d capacity %d\n", len(aSlice), cap(aSlice)) //length of is 2 and capacity is 5

	aSlice = aSlice[:cap(aSlice)] //re-slicing furitslice till its capacity
	fmt.Println("After re-slicing length is", len(aSlice), "and capacity is", cap(aSlice))

}

// creating a slice using make
/*
func make([]T, len, cap) []T can be used to create a slice by passing the type,
length and capacity. The capacity parameter is optional
defaults to the length. The make function creates an array and
returns a slice reference to it.
*/
func makeSlice() {
	i := make([]int, 5, 5)
	fmt.Println(i)
}

// appending to a slice
/*
As we already know arrays are restricted to fixed length and their length
cannot be increased. Slices are dynamic and new elements
can be appended to the slice using append function.
The definition of append function is func append(s []T, x ...T) []T.

x ...T in the function definition means that the function accepts
variable number of arguments for the parameter x.
These type of functions are called variadic functions.
*/
func appendingToSlice() {
	cars := []string{"Ferrari", "Audi", "Ford"}
	fmt.Println("cars:", cars, "has old length", len(cars), "and capacity", cap(cars)) //capacity of cars is 3
	cars = append(cars, "Toyota")
	fmt.Println("cars:", cars, "has new length", len(cars), "and capacity", cap(cars)) //capacity of cars is doubled to 6
}

// It is also possible to append one slice to another using the ... operator.
func slicesAppend() {
	programming := []string{"Python", "JavaScript", "C++", "GoLang"}
	uniqueness := []string{"Very good", "epic", "Fast", "Awesome"}

	quality := append(programming, uniqueness...)
	fmt.Println("Quality", quality)
}

// passing a slice to a function
func addOne(numbers []int) {
	for i := range numbers {
		numbers[i] += 1
	}
}

func passingSlice() {
	nos := []int{8, 9, 10}
	fmt.Println("Slice before function call ", nos)
	addOne(nos)
	fmt.Println("slice after function call ", nos)
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
	// modifySlice()
	// lengthCapicty()
	// makeSlice()
	// appendingToSlice()
	// slicesAppend()
	passingSlice()

}
