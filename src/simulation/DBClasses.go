package main

import (
)


type Candle struct {
	Open float32,
	Close float32,
	High float32,
	Low float32,
	Volume int,
	Symbol string,
	Indicators map[string]float32
}

type Test struct {
	Length int,
	Candles [] Candle,
}

type PriceLevel struct {
	Price float32,
	Tests [] Test
}
type Symbol struct {
	Symbol string,
	Trading bool,
	Price_levels [] PriceLevel,
}

/* Option encapsulates a stock option, with methods to calculate 
    its price */
type Option struct {
	Symbol string,
	Expiry int, 
	Strike int
}


