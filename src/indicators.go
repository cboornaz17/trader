/*
func main() {
  // closing prices of the last 15 candles
  prices := [24]float32{45.15, 46.26, 46.5, 46.23, 46.08, 46.03, 46.83, 47.69,
                        47.54, 49.25, 49.23, 48.2, 47.57, 47.61, 48.08, 47.21,
                        46.76, 46.68, 46.21, 47.47, 47.98, 40.0, 20.1, 25.1}

  var candles [len(prices)]Candle

  for i := 0; i < len(prices); i++ {
    candles[i] = Candle{Close : prices[i]}
  }

  // this function should be passed all of the prices that you want rsi for
  // and the 14 before
  fullrsi(candles[:])
}

*/

/*
NORMAL RSI
you want the RSI calculated for all of the new candles
check how far back you need rsi calculated, as far back as candle 14
if you have candle 0-43
candle 30 is the last candle with RSI
candle index 0 is the first
candle index 14 is the first with RSI
candle index 15 requires candle 1-15

find latest candle with rsi entry
calculate rsi for all candles after that i...
need i-15... candles
*/

/*
WILDER'S RSI

If we tracked the average upchange and downchange we're in and no loops

use the standard 14 candles for the first RS (on candle index 14)
AvgUt = 1/14 * Ut + 13/14 * AvgUt-1
AvgDt = 1/14 * Dt + 13/14 * AvgDt-1

*/

// need to calculate standard rsi for the 14th index candle
func fullRS(candles []Candle) {
  var avgu float32
  var avgd float32

  var change float32

  // loop through candles
  for i := 1; i <= 14; i++ {
    // change is the price difference with the previous price
    change = candles[i].Close - candles[i-1].Close

    // keep a running total of positive and negative changes, separately
    if change > 0 {
      avgu += change
    } else if change < 0 {
      avgd += -change
    }
  }

  // on the candle that can have its rsi calculated
  candles[i].Indicators.AvgUp = avgu / 14.0
  candles[i].Indicators.AvgDown = avgd / 14.0

  // be careful of the edge case 14 candles of consecutive up or down
  if avgu > 0 & avgd > 0 & len(candles) > 15 {
    // pass remaining candles to the smoothing rsi calculation
    smoothRS(candles[14:len(candles)])
  }
}

// be careful of the edge case 14 candles of consecutive up or down
// rsi can be "backcalculated" from prev AvgUp, prev AvgDown, prev price, current price
func smoothRS(candles []Candle) {
  var change float32
  var price float32

  // initialize loop with previous avgs
  avgu := candles[0].Indicators.AvgUp
  avgd := candles[0].Indicators.AvgDown

  prev_price := candles[0].Close

  for i := 1; i < len(candles); i++ {
    price = candles[i].Close
    change = price - prev_price
    prev_price = price

    // whats the most pythonic way to represent change as change when >0 and as 0 otherwise, etc.
    if change > 0 {
      avgu = (13.0 * avgu + change) / 14.0
      avgd = (13.0 * avgd) / 14.0
    } else if change < 0 {
      avgu = (13.0 * avgu) / 14.0
      avgd = (13.0 * avgd - change) / 14.0
    }

    candles[i].Indicators.AvgUp = avgu
    candles[i].Indicators.AvgDown = avgd
  }
}

/* recursive version of smoothRS
func recurseRS(candles []Candle, i, avgu, avgd) {
  change = candles[i].Close - candles[i-1].Close

  // could do candles[i].Indicators.AvgDown as pointer but idk how to or why

  if change > 0 {
    candles[i].Indicators.AvgUp = (13.0 * avgu + change) / 14.0
    candles[i].Indicators.AvgDown = avgd = (13.0 * avgd) / 14.0
  } else if change < 0 {
    candles[i].Indicators.AvgUp = (13.0 * avgu) / 14.0
    candles[i].Indicators.AvgDown = avgd = (13.0 * avgd - change) / 14.0
  }

  recurseRS(candles, i + 1, candles[i].Indicators.AvgUp, candles[i].Indicators.AvgDown)
}
*/

// iterate to the last desired interval, calculating the SMA (also first EMA)
func fullEMA(candles []Candle, intervals []int) {
  for i := 0; i < max(intervals)
}

// check before this that candles[0] has EMAs calculated for all desired intervals
func backEMA(candles []Candle, intervals []int) {
  var interval int
  var last_sma float32

  last_emas[interval] = candles[0].Indicators.EMAs[interval]

  for i := 1; i < len(candles); i++ {
    for j := 0; j < len(intervals); j++ {
      interval = intervals[j]
      smoothing = 2 / (interval + 1)



      last_ema = candles[i].Close * smoothing + last_ema * (1 - smoothing)

      candles[i].Indicators.EMAs[interval] = last_ema
    }
  }

}
