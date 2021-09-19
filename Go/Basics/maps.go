package main

import "fmt"

/*
What is a map?

A map is a builtin type in Go that is used to store key-value pairs.

How to create a map?
make(map[type of key]type of value)
*/

func simpleMap() {
	employeeSalary := make(map[string]int)
	employeeSalary["steve"] = 12000
	employeeSalary["jamie"] = 10000
	employeeSalary["mike"] = 9000
	fmt.Println("Employee Salary map contents:", employeeSalary)
	fmt.Println("Length is ", len(employeeSalary))
	fmt.Print("********\n")
	companies := map[string][]string{
		"Facebook": {"Whastapp", "instagram"},
		"Google":   {"Android", "Youtube"},
	}
	fmt.Println("Companies ", companies)

}

// checking if a key exists
func checkKey() {
	salary := map[string]int{
		"Himanshu": 1000,
		"Rakshit":  1305,
	}

	value, ok := salary["Gaurav"]
	if ok == true {
		fmt.Println("Salary of Gaurav is", value)
		return
	}

	fmt.Println("Gaurav not found")
}

// loop over values in map
func loopMap() {
	salary := map[string]int{
		"Himanshu": 1000,
		"Rakshit":  1305,
		"Gaurav":   2500,
	}

	for key, value := range salary {
		fmt.Printf("salary -> %s = %d\n", key, value)
	}
}

// deleteing items from a map
/*
delete(map, key) is the syntax to delete key from a map.
The delete function does not return any value.
*/
func deleteItems() {
	employeeSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	fmt.Println("map before deletion", employeeSalary)
	delete(employeeSalary, "steve")
	fmt.Println("map after deletion", employeeSalary)
}

// map of structs
type employee struct {
	salary  int
	country string
}

func mapOfStruct() {
	emp1 := employee{
		salary:  1200,
		country: "USA",
	}

	emp2 := employee{
		salary:  14500,
		country: "India",
	}

	employeeInfo := map[string]employee{
		"Himanshu": emp1,
		"Gaurav":   emp2,
	}

	for name, info := range employeeInfo {
		fmt.Printf("Employee: %s Salary:$%d  Country: %s\n", name, info.salary, info.country)
	}
}

/*
Maps are reference types

Similar to slices, maps are reference types. When a map is assigned to a
new variable, they both point to the same internal data structure.
Hence changes made in one will reflect in the other.
*/
func referenceMaps() {
	employeeSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	fmt.Println("Original employee salary", employeeSalary)
	modified := employeeSalary
	modified["mike"] = 18000
	fmt.Println("Employee salary changed", employeeSalary)

}

func main() {
	// simpleMap()
	// checkKey()
	// loopMap()
	// deleteItems()
	// mapOfStruct()
	// referenceMaps()
}
