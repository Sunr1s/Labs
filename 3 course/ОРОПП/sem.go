package main

import (
	"fmt"
)

func main() {
	semaphore := make(chan struct{}, 1)

	for i := 0; i < 5; i++ {
		go func(id int) {
			semaphore <- struct{}{}
			fmt.Printf("Goroutine %d accessing shared resource\n", id)
			<-semaphore
		}(i)
	}

	fmt.Scanln()
}
