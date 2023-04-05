package main

import (
	"fmt"
	"golang.org/x/sys/unix"
	"log"
)

func main() {
	queueName := "/test_queue"

	fd, err := unix.Open(queueName, unix.O_RDONLY, 0)
	if err != nil {
		log.Fatalf("Error opening message queue: %v", err)
	}
	defer unix.Close(fd)

	buf := make([]byte, 1024)
	n, err := unix.Read(fd, buf)
	if err != nil {
		log.Fatalf("Error receiving message: %v", err)
	}
	fmt.Println("Message received:", string(buf[:n]))
}
