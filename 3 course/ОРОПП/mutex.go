package main

import (
	"fmt"
	"sync"
)

func main() {
	var mu sync.Mutex
	var count int

	for i := 0; i < 5; i++ {
		go func(id int) {
			mu.Lock()
			count++
			fmt.Printf("Goroutine %d increasing count to %d\n", id, count)
			mu.Unlock()
		}(i)
	}

	fmt.Scanln()
}
