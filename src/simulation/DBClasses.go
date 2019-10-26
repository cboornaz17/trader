package main

import (
	"fmt"

	"log"
	"context"

	bson "go.mongodb.org/mongo-driver/bson"
    "go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Test struct {
	Length int;
	Candles [] Candle;
}

type Indicators struct {
	// rs is AvgUp/AvgDown
	AvgUp float32
	AvgDown float32
	SMAs map[string]float32
	EMAs map[string]float32
}

// candles with cointained class, indicators
type Candle struct {
	Open float32 			`bson:"Open"`
	Close float32			`bson:"Close"`
	High float32			`bson:"High"`
	Low float32				`bson:"Low"`
	Volume int				`bson:"Volume"`
	Symbol string			`bson:"Symbol"`
	Indicators Indicators 	`bson:"Indicators"`
}


// candle.rsi() returns rsi calculation
func (c *Candle) rsi() float32 {
    return 100.0 - 100.0 / (1 + c.Indicators.AvgUp / c.Indicators.AvgDown)
}

// price levels measured with tests
type PriceLevel struct {
	Price float32;
	// probably should point to tests not sure how Mongo/Go handle this
	Tests [] Test;
}

type Symbol struct {
	Symbol string;
	Price_levels [] PriceLevel;
	Trading bool
	PriceLevels [] PriceLevel
}

/* Option encapsulates a stock option, with methods to calculate
    its price */
type Option struct {
	Symbol string;
	Expiry int; 
	Strike int;
}


type MongoWrapper struct {
	Db *mongo.Database;
	client *mongo.Client;
}

func getData(c mongo.Database) {
	
}

// Adds a candle to mongo 
// uses collection based on symbol
func (mw MongoWrapper) insertCandle(c Candle) {
	collection := mw.Db.Collection(c.Symbol)

	// Insert candle
	insertResult, err := collection.InsertOne(context.TODO(), c)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Inserted a document with id: ", insertResult.InsertedID)
}

// Gets a candle from mongo according to the filter parameter
func (mw MongoWrapper) getCandle(filter bson.D) Candle {
	// Get filter to Candle type
	var filterCandle Candle;
	b, err := bson.Marshal(filter)
	err = bson.Unmarshal(b, &filterCandle)
	if err != nil {
		log.Fatal("Error unmarshalling")
	}

	// Get collection based on filter symbol
	collection := mw.Db.Collection(filterCandle.Symbol)
	
	// Get resulting candle
	var result Candle;	
	err = collection.FindOne(context.Background(), filter).Decode(&result)
	return result
}

/* Disconnects the MongoWrapper from the db */
func (mw MongoWrapper) Cleanup() error {
	return mw.client.Disconnect(context.TODO())
}

/* Creates and returns MongoWrapper object */
func Init() MongoWrapper {
	fmt.Println("Init")

	// Set client options
	clientOptions := options.Client().ApplyURI("mongodb://192.168.99.100:27017")

	// Connect to MongoDB
	client, err := mongo.Connect(context.TODO(), clientOptions)

	if err != nil {
		log.Fatal(err)
	}

	// Check the connection
	err = client.Ping(context.TODO(), nil)

	if err != nil {
		log.Fatal(err)
	}

	db := client.Database("trader")

	mw := MongoWrapper{db, client}

	return mw
}
