package main

import (
	"fmt"
	"log"

	"go.mongodb.org/mongo-driver/bson"
    _ "go.mongodb.org/mongo-driver/mongo"
	_"go.mongodb.org/mongo-driver/mongo/options"
)

func main() {

	symbol := "Testing"

	// make sample candle
	c := Candle {
		12.2,
		12.1,
		5.2,
		10.1,
		1000,
		symbol,
		Indicators{},
	}
	
	fmt.Println(c)

	// Initialize MongoWrapper object
	mw := Init()

	// Insert candle
	mw.insertCandle(c)

	// Filter to search for candles on
	filter := bson.D{{"Symbol", symbol}} 

	// Get candle
	new_c := mw.getCandle(filter)

	fmt.Println("Got candle", new_c)

	// Close db connection
	err := mw.Cleanup()

	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connection to MongoDB closed.")

	

}
