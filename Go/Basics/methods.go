package main

import (
	"fmt"
	"math"
)

/*
A method is just a function with a special receiver type between the func keyword
and the method name. The receiver can either be a struct type or non-struct type.

The syntax of a method declaration is provided below.

func (t Type) methodName(parameter list) {
}

The above snippet creates a method named methodName with receiver type Type.
t is called as the receiver and it can be accessed within the method.

*/
type Name struct {
	firstName string
	lastName  string
}

// simple method type
func (n Name) displayFullName() {
	fmt.Printf("Your name is %s %s\n", n.firstName, n.lastName)
}

// a bit intersting
type Rectangle struct {
	length int
	width  int
}

type Circle struct {
	radius float64
}

func (r Rectangle) Area() int {
	return r.length * r.width
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

func bitInteresting() {
	r := Rectangle{
		length: 10,
		width:  5,
	}
	fmt.Printf("Area of rectangle %d\n", r.Area())
	c := Circle{
		radius: 12,
	}
	fmt.Printf("Area of circle %f", c.Area())

}

func main() {

	// call simple method
	n1 := Name{
		firstName: "Himanshu",
		lastName:  "Tripathi",
	}

	n1.displayFullName() // calling displayFullName() method of name type

}
