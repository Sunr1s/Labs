package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	pipeName := "/tmp/test_pipe"

	pipe, err := os.OpenFile(pipeName, os.O_RDONLY, os.ModeNamedPipe)
	if err != nil {
		log.Fatalf("Error opening named pipe: %v", err)
	}
	defer pipe.Close()

	data, err := ioutil.ReadAll(pipe)
	if err != nil {
		log.Fatalf("Error reading from named pipe: %v", err)
	}
	fmt.Println("Data received:", string(data))
}
