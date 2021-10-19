package main

import "fmt"

/*
What is an interface?

In Go, an interface is a set of method signatures.
When a type provides definition for all the methods in
the interface, it is said to implement the interface.

For example WashingMachine can be an interface with method signatures
Cleaning() and Drying(). Any type which provides definition for Cleaning()
and Drying() methods is said to implement the WashingMachine interface
*/

// Declaring and implementing an interface
type VowelsFinder interface {
	FindVowels() []rune
}
type MyString string

// MyString implements VowelsFinder
func (ms MyString) FindVowels() []rune {
	var vowels []rune

	for _, rune := range ms {
		if rune == 'a' || rune == 'e' || rune == 'i' || rune == 'o' || rune == 'u' {
			vowels = append(vowels, rune)
		}
	}

	return vowels
}

func simpleInterface() {
	name := MyString("Himanshu Tripathi")
	var v VowelsFinder
	v = name
	fmt.Printf("Vowels are %c\n", v.FindVowels())
}

// Practical use of an interface
/*
We will write a simple program that calculates the total expense for a company
based on the individual salaries of the employees. For brevity, we have assumed
that all expenses are in USD.
*/
type SalaryCalculator interface {
	CalculateSalary() int
}
type Permanent struct {
	empId    int
	basicpay int
	pf       int
}

type Contract struct {
	empId    int
	basicpay int
}

// salary of parmanent employee is the sum of the basic pay + pf
func (p Permanent) CalculateSalary() int {
	return p.basicpay + p.pf
}

// salary of contract employee is the basic pay alone
func (c Contract) CalculateSalary() int {
	return c.basicpay
}

/*
total expense is calculated by iterating through the SalaryCalculator slice and summing
the salaries of the individual employees
*/
func totalExpense(s []SalaryCalculator) {
	expense := 0
	for _, v := range s {
		expense = expense + v.CalculateSalary()
	}
	fmt.Printf("Total Expense Per Month $%d\n", expense)
}

func realWorldImplementation() {
	p1 := Permanent{
		empId:    1,
		basicpay: 5000,
		pf:       20,
	}
	p2 := Permanent{
		empId:    2,
		basicpay: 6000,
		pf:       30,
	}

	c1 := Contract{
		empId:    3,
		basicpay: 3000,
	}

	employees := []SalaryCalculator{p1, p2, c1}
	totalExpense(employees)
}

func main() {
	// simpleInterface()
	realWorldImplementation()
}
