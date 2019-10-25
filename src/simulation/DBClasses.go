package main

import (
)

// candles with cointained class, indicators

type Candle struct {
	Open float32
	Close float32
	High float32
	Low float32
	Volume int
	Symbol string
	Indicators Indicators
}

type Indicators struct {
  // rs is AvgUp/AvgDown
	AvgUp float32
	AvgDown float32
	MAs map[string]float32
}

func (c *Candle) rsi() float32 {
    return 100.0 - 100.0 / (1 + c.Indicators.AvgUp / c.Indicators.AvgDown)
}

// price levels measured with tests

type PriceLevel struct {
	Price float32
	// probably should point to tests not sure how Mongo/Go handle this
	Tests [] Test
}

type Test struct {
	Length int
	// probably should point to candles not sure how Mongo/Go handle this
	Candles [] Candle
}

// 

type Symbol struct {
	Symbol string
	Trading bool
	Price_levels [] PriceLevel
}

/* Option encapsulates a stock option, with methods to calculate
    its price */
type Option struct {
	Symbol string
	Expiry int
	Strike int
}

/*

*/
