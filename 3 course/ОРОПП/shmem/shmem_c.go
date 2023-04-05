package main

import (
	"fmt"
	"log"

	"github.com/akutz/memconn"
)

func main() {
	conn, err := memconn.Dial("memu", "shared_mem")
	if err != nil {
		log.Fatalf("Error connecting to server: %v", err)
	}
	defer conn.Close()

	data := "Hello from Go!\n"
	_, err = conn.Write([]byte(data))
	if err != nil {
		log.Fatalf("Error sending data to server: %v", err)
	}

	fmt.Println("Data sent:", data)
}
