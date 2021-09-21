package main

import "fmt"

/*
What is a struct?
A struct is a user-defined type that represents a collection of fields.
It can be used in places where it makes sense to group the data into a
single unit rather than having each of them as separate values.
*/

type Programming struct {
	name   string
	can_do string
	used   string
}

func simpleStruct() {
	prog := Programming{
		name:   "Python",
		can_do: "Eveything",
		used:   "AnyWhere",
	}

	fmt.Println(prog)
	fmt.Printf("Programming name is %s and we can use this %s and we used this %s\n", prog.name, prog.can_do, prog.used)

}

func pointerToStruct() {
	prog := &Programming{
		name:   "GOlang",
		can_do: "Just name anything",
		used:   "Where you want to use",
	}
	fmt.Println(*prog)
	fmt.Printf("Programming name is %s and we can use this %s and we used this %s\n", prog.name, prog.can_do, prog.used)

}

// Anonymous fields
/*
It is possible to create structs with fields that contain only a type without the field name.
These kinds of fields are called anonymous fields.
*/
type Person struct {
	string
	int
}

func AnonymousStruct() {
	p := Person{
		string: "Himanshu",
		int:    23,
	}
	fmt.Println(p)
}

// Nested Structs
type Address struct {
	city  string
	state string
}

type People struct {
	name    string
	age     int
	address Address
}

func nestedStruct() {
	p := People{
		name: "Himanshu",
		age:  24,
		address: Address{
			city:  "Delhi",
			state: "Delhi",
		},
	}
	fmt.Println("Name:", p.name)
	fmt.Println("Age:", p.age)
	fmt.Println("City:", p.address.city)
	fmt.Println("State:", p.address.state)

}

// promoted fields
/*
Fields that belong to an anonymous struct field in a struct are called promoted fields
since they can be accessed as if they belong to the struct which holds the anonymous
struct field.
*/
type Languages struct {
	born string
	Programming
}

func promotedFields() {
	l := Languages{
		born: "November 10, 2009",
		Programming: Programming{
			name:   "GO",
			can_do: "Anything",
			used:   "For Everything",
		},
	}

	fmt.Println("Born", l.born)
	fmt.Println("name", l.name)
	fmt.Println("can do", l.can_do)
	fmt.Println("used", l.used)
}

// Structs Equality
/*
Structs are value types and are comparable if each of their fields are comparable.
Two struct variables are considered equal if their corresponding fields are equal.
*/
type Name struct {
	firstName string
	lastName  string
}

func StructEquality() {
	n1 := Name{
		firstName: "Himanshu",
		lastName:  "Tripathi",
	}

	n2 := Name{
		firstName: "Himanshu",
		lastName:  "Tripathi",
	}

	n3 := Name{
		firstName: "Gaurav",
		lastName:  "Tripathi",
	}

	if n1 == n2 {
		fmt.Println("n1 and n2 are equal")
	}

	if n1 != n3 {
		fmt.Println("n1 and n3 are not equal")
	}
}

func main() {
	// simpleStruct()
	// pointerToStruct()
	// AnonymousStruct()
	// nestedStruct()
	// promotedFields()
	StructEquality()
}

// https://golangbot.com/structs/
