package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	var sharedVariable int

	for i := 0; i < 200000; i++ {
		wg.Add(1)
		go func() {
			sharedVariable++
			wg.Done()
		}()
	}

	wg.Wait()

	fmt.Println(sharedVariable)
}
