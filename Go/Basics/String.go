package main

import "fmt"

func printBytes(s string) {
	fmt.Println("Bytes:")
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x", s[i])
	}
}

func printChars(s string) {
	fmt.Println("Characters:")
	for i := 0; i < len(s); i++ {
		fmt.Printf("%c", s[i])
	}
}

// Rune
/*
A rune is a builtin type in Go and it's the alias of int32.
Rune represents a Unicode code point in Go.
It doesn't matter how many bytes the code point occupies,
it can be represented by a rune.
*/
func printCharsRune(s string) {
	fmt.Printf("Bytes: ")
	runes := []rune(s)
	for i := 0; i < len(runes); i++ {
		fmt.Printf("%c", runes[i])
	}
}

// Accessing Individual runes using for range loop
func charsAndBytesPosition(s string) {
	for index, rune := range s {
		fmt.Printf("%c start at byte %d\n", rune, index)
	}
}

// Creating a string from a slice of bytes
func createString() {
	byteSlice := []byte{0x43, 0x61, 0x66, 0xC3, 0xA9}
	str := string(byteSlice)
	fmt.Println(str)
}

func main() {
	// name := "Hello World"
	// fmt.Printf("String: %s\n", name)
	// printChars(name)
	// fmt.Printf("\n")
	// printBytes(name)
	// fmt.Printf("\n\n")
	// name = "Señor"
	// fmt.Printf("String: %s\n", name)
	// printChars(name)
	// fmt.Printf("\n")
	// printBytes(name)

	// fmt.Printf("\n")
	// printCharsRune(name)
	// fmt.Printf("\n")

	// name := "Señor"
	// charsAndBytesPosition(name)

	createString()
}
