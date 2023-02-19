package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	ch := make(chan int)

	// Launch two goroutines that both increment a counter 100000 times
	for i := 0; i < 2; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := 0; j < 100000; j++ {
				ch <- 1 // send a value to the channel
			}
		}()
	}

	// Wait for both goroutines to finish
	go func() {
		wg.Wait()
		close(ch) // close the channel to signal that we're done
	}()

	// Consume the values from the channel and increment a counter
	var counter int
	for value := range ch {
		counter += value
	}

	fmt.Println(counter) // prints 200000
}
