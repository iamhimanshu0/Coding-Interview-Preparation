/*
A function is a block of code that performs a specific
task. A function takes an input, performs some
calculations on the input, and generates an output.
*/

package main

import "fmt"

/*
func functionname(parametername type) returntype {
 //function body
}
*/

// func calculateBill(price int, no int) int {
// 	var totalPrice = price * no
// 	return totalPrice
// }

func calculateBills(price, no int) int {
	var totalPrice = price * no
	return totalPrice
}

// multiple return type
func rectProps(length, width float64) (float64, float64) {
	var area = length * width
	var parameter = (length + width) * 2
	return area, parameter
}

// named return value
func triProps(base, height, side float64) (area, perimeter float64) {
	area = (base * height) / 2
	perimeter = base + height + side
	return
}

func main() {
	// price, no := 50, 2
	// fmt.Println(calculateBills(price, no))

	// area, perimeter := rectProps(10.8, 12.8)
	// fmt.Printf("Area %f Perimeter %f\n", area, perimeter)

	area, perimeter := triProps(5.2, 6.1, 2.3)
	fmt.Printf("Area %f Perimeter %f\n", area, perimeter)
}
