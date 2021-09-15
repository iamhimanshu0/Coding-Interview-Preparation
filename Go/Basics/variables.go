package main

import "fmt"

func singleVariable() {
	var age int         // without value
	var newage int = 21 //with value
	// age = 0
	fmt.Println("Age is", age)

	age = 21
	fmt.Println("Age is", age)

	fmt.Println("New age", newage)
}

/*
If a variable has an initial value, Go will
automatically be able to infer the type of that variable using
that initial value. Hence if a variable has an initial
value, the type in the variable declaration can be
removed.
*/
func typeInference() {
	var age = 29
	fmt.Println("Age is", age)
}

// Multiple variables can be declared using a single statement.
func multipleVairableDeclaration() {
	// var width, height int = 100, 50
	var width, height = 100, 50
	fmt.Println("width is", width, "and height is", height)

	// ---------- //
	var (
		name   = "Himanshu"
		age    = 21
		skills string
	)
	fmt.Println("My name is", name, "Age is", age, "skills is", skills)

}

// name := initialvalue is the short hand syntax to declare a variable.
func shortHandDeclaration() {
	count := 5
	name, age := "Himanshu", 21
	fmt.Println(count)

	fmt.Println(name, age)
}

// The keyword const is used to declare a constant.
func constant() {
	const a = 50
	const (
		name   = "Himanshu"
		age    = 23
		skills = "Machine Learning"
	)

	fmt.Println(a, name, age, skills)
}

func main() {
	// singleVariable()
	// typeInference()
	// multipleVairableDeclaration()
	// shortHandDeclaration()
	constant()
}
