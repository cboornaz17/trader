package main

import (
	"fmt"

	"log"
	"context"

	bson "go.mongodb.org/mongo-driver/bson"
    "go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Candle struct {
	Open float32;
	Close float32;
	High float32;
	Low float32;
	Volume int;
	Symbol string;
	Indicators bson.A;
}



type Test struct {
	Length int;
	Candles [] Candle;
}

type PriceLevel struct {
	Price float32;
	Tests [] Test;
}
type Symbol struct {
	Symbol string;
	Trading bool;
	Price_levels [] PriceLevel;
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

func (mw MongoWrapper) insertCandle(c Candle) {
	fmt.Println("Inserting candle: ", c)

	db := mw.Db
	collection := db.Collection(c.Symbol)

	insertResult, err := collection.InsertOne(context.TODO(), c)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Inserted a single document: ", insertResult.InsertedID)

}

func (mw MongoWrapper) getCandle(filter bson.D{}) Candle {
	
}


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

func (mw MongoWrapper) Cleanup() error {
	return mw.client.Disconnect(context.TODO())
}

