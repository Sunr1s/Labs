package main

import (
	"fmt"
	"log"

	"github.com/templexxx/ipc/mq"
)

func main() {
	queueName := "/test_queue"
	message := "Hello from Go!"

	attr := &mq.Attr{
		Maxmsg: 10,
		Msgsize: 1024,
	}

	mq, err := mq.Open(queueName, mq.O_WRONLY|mq.O_CREAT, 0644, attr)
	if err != nil {
		log.Fatalf("Error creating message queue: %v", err)
	}
	defer mq.Close()

	err = mq.Send([]byte(message), 0)
	if err != nil {
		log.Fatalf("Error sending message: %v", err)
	}
	fmt.Println("Message sent:", message)
}
