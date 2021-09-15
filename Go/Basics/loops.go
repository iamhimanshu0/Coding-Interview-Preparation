package main

import "fmt"

func simpleLoop() {
	for i := 1; i <= 10; i++ {
		fmt.Println(i)
	}
}

func loopBreak() {
	for i := 1; i <= 10; i++ {
		if i > 5 {
			break
		}
		fmt.Println(i)
	}
	fmt.Println("Line After loop")
}

func loopContinue() {
	for i := 1; i <= 10; i++ {
		if i%2 == 0 {
			continue
		}
		fmt.Println(i)
	}

}

func loopNested() {
	n := 5
	for i := 0; i < n; i++ {
		for j := 0; j <= i; j++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
}

func loopInfinite() {
	for {
		fmt.Printf("Welcome to infinity loop")
	}
}

func main() {
	// simpleLoop()
	// loopBreak()
	// loopContinue()
	loopNested()
}
