package main

import (
	"fmt"
	"log"

	"go.mongodb.org/mongo-driver/bson"
    _ "go.mongodb.org/mongo-driver/mongo"
	_"go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
	fmt.Println("Hello from go")

	fmt.Println("Using db classes")

	c := Candle {
		12.2,
		12.1,
		5.2,
		10.1,
		1000,
		"Testing",
		bson.A{},
	}

	fmt.Println(c)

	mw := Init()

	fmt.Println("Got db: ", mw)

	mw.insertCandle(c)

	err := mw.Cleanup()

	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connection to MongoDB closed.")

	

}