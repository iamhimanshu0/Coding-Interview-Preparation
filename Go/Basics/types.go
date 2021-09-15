package main

import (
	"fmt"
	"unsafe"
)

/*
The following are the basic types available in Go

bool
Numeric Types
int8, int16, int32, int64, int
uint8, uint16, uint32, uint64, uint
float32, float64
complex64, complex128
byte
rune
string
*/
func boolen() {
	a := true
	b := false
	fmt.Println("a", a, "b", b)

	c := a && b
	fmt.Println("c", c)

	d := a || b
	fmt.Println("d", d)

}

func signedIntegers() {
	var a int = 89
	b := 95
	fmt.Println("value of a is", a, "b is", b)
	fmt.Printf("type of a is %T, size of a is %d", a, unsafe.Sizeof(a))
	fmt.Printf("\ntype of b is %T, size of b is %d\n", b, unsafe.Sizeof(b))

}

func flotingPointType() {
	a, b := 5.67, 8.97
	fmt.Printf("type of a %T b %T\n", a, b)
	sum := a + b
	diff := a - b
	fmt.Println("sum", sum, "diff", diff)

	no1, no2 := 56, 89
	fmt.Println("sum", no1+no2, "diff", no1-no2)
}

// Complex types
/*
complex64: complex numbers which have float32 real and imaginary parts
complex128: complex numbers with float64 real and imaginary parts

The builtin function complex is used to construct a complex number with real and imaginary parts.
The complex function has the following definition

func complex(r, i FloatType) ComplexType
*/

func complexType() {
	// shortand method
	// c := 6+ 7i

	c1 := complex(5, 7)
	c2 := 8 + 27i

	cadd := c1 + c2
	fmt.Println("sum", cadd)

	cmul := c1 * c2
	fmt.Println("multiple", cmul)
}

func main() {
	// boolen()
	// signedIntegers()
	// flotingPointType()
	complexType()
}

/*
Other numeric types
byte is an alias of uint8
rune is an alias of int32

*/

// for more :- https://golangbot.com/types/
