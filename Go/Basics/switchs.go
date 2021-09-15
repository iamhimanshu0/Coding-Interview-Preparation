package main

import (
	"fmt"
	"math/rand"
)

func switchCaseSimple() {
	value := 4
	fmt.Println("value is", value)

	switch value {
	case 1:
		fmt.Println("this is 1 not value")
	case 2:
		fmt.Println("this is 2 not value")
	case 3:
		fmt.Println("this is 3 not value")
	case 4:
		fmt.Println("Yes this is what we're looking for")
	default:
		fmt.Println("this is default not value")
	}
}

func multipleExpression() {
	value := 7
	fmt.Println("value is", value)

	switch value {
	case 1, 3, 5, 7, 9:
		fmt.Println("Number is odd", value)
	default:
		fmt.Println("Number is even below 10")

	}
}

func expressionLess() {
	num := 75
	switch { // expression is omitted
	case num >= 0 && num <= 50:
		fmt.Printf("%d is greater than 0 and less than 50\n", num)
	case num >= 51 && num <= 100:
		fmt.Printf("%d is greater than 51 and less than 100\n", num)
	case num >= 101:
		fmt.Printf("%d is greater than 100\n", num)
	}
}

/*
In Go, the control comes out of the switch statement
immediately after a case is executed. A fallthrough
statement is used to transfer control to the first
statement of the case that is present immediately after
the case which has been executed.


Our program will check whether the input number is less
than 50, 100, or 200. For instance, if we input 75, the
program will print that 75 is less than both 100 and 200.
We will achieve this using fallthrough.
*/

func number() int {
	num := 15 * 5
	return num
}

func switchFallthrough() {
	switch num := number(); {
	case num < 50:
		fmt.Printf("%d is lesser than 50\n", num)
		fallthrough
	case num < 100:
		fmt.Printf("%d is lesser than 100\n", num)
		fallthrough
	case num < 200:
		fmt.Printf("%d is lesser than 200\n", num)
	}
}

// Breaking the outer for loop
func breakingOuterLoop() {
randloop:
	for {
		switch i := rand.Intn(100); {
		case i%2 == 0:
			fmt.Printf("Generated even number %d\n", i)
			break randloop
		}
	}
}

func main() {
	// switchCaseSimple()
	// multipleExpression()
	// expressionLess()
	// switchFallthrough()
	breakingOuterLoop()
}
