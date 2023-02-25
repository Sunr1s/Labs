package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(id int, wg *sync.WaitGroup, cond *sync.Cond) {
	defer wg.Done()

	cond.L.Lock()
	defer cond.L.Unlock()

	fmt.Printf("Worker %d waiting for event...\n", id)
	cond.Wait()
	fmt.Printf("Worker %d event received!\n", id)
}

func main() {
	var wg sync.WaitGroup
	var mu sync.Mutex
	cond := sync.NewCond(&mu)

	for i := 0; i < 5; i++ {
		wg.Add(1)
		go worker(i, &wg, cond)
	}

	time.Sleep(time.Second)
	mu.Lock()
	fmt.Println("Sending event...")
	cond.Broadcast()
	mu.Unlock()

	wg.Wait()
}
