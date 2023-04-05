package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	// Create a channel to receive signals
	signalChannel := make(chan os.Signal, 1)

	// Notify the channel when receiving the following signals: SIGINT, SIGTERM, and SIGHUP
	signal.Notify(signalChannel, syscall.SIGINT, syscall.SIGTERM, syscall.SIGHUP)

	// Start a Goroutine to handle the signals
	go func() {
		for {
			sig := <-signalChannel
			switch sig {
			case syscall.SIGINT:
				fmt.Println("Received SIGINT, cleaning up and exiting...")
				// Perform cleanup actions here
				os.Exit(0)

			case syscall.SIGTERM:
				fmt.Println("Received SIGTERM, shutting down gracefully...")
				// Perform graceful shutdown here
				os.Exit(0)

			case syscall.SIGHUP:
				fmt.Println("Received SIGHUP, reloading configuration...")
				// Reload configuration or perform other necessary actions here
			}
		}
	}()

	// Simulate some work
	fmt.Println("Running... Press Ctrl+C to exit.")
	select {}
}
