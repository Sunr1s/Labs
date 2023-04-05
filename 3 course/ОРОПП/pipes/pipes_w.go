package main

import (
	"fmt"
	"log"
	"os"
	"syscall"
)

func main() {
	pipeName := "/tmp/test_pipe"
	data := "Hello from Go!"

	err := syscall.Mkfifo(pipeName, 0600)
	if err != nil && !os.IsExist(err) {
		log.Fatalf("Error creating named pipe: %v", err)
	}

	pipe, err := os.OpenFile(pipeName, os.O_WRONLY, os.ModeNamedPipe)
	if err != nil {
		log.Fatalf("Error opening named pipe: %v", err)
	}
	defer pipe.Close()

	_, err = pipe.WriteString(data)
	if err != nil {
		log.Fatalf("Error writing to named pipe: %v", err)
	}
	fmt.Println("Data sent:", data)
}

