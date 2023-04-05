package main

import (
	"bufio"
	"fmt"
	"log"
	"net"

	"github.com/akutz/memconn"
)

func main() {
	ln, err := memconn.Listen("memu", "shared_mem")
	if err != nil {
		log.Fatalf("Error setting up listener: %v", err)
	}
	defer ln.Close()

	fmt.Println("Server listening on shared memory")

	conn, err := ln.Accept()
	if err != nil {
		log.Fatalf("Error accepting connection: %v", err)
	}

	handleConnection(conn)
}

func handleConnection(conn net.Conn) {
	defer conn.Close()

	reader := bufio.NewReader(conn)
	data, err := reader.ReadString('\n')
	if err != nil {
		log.Printf("Error reading data from client: %v", err)
		return
	}

	fmt.Printf("Data received: %s", data)
}
