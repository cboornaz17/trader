package main

import(. "trader/src/simulation")
import("fmt")

func main() {
  // closing prices of the last 15 candles
  prices := [21]float32{45.15, 46.26, 46.5, 46.23, 46.08, 46.03, 46.83, 47.69,
                        47.54, 49.25, 49.23, 48.2, 47.57, 47.61, 48.08, 47.21,
                        46.76, 46.68, 46.21, 47.47, 47.98}

  var candles [len(prices)]Candle

  for i := 0; i < len(prices); i++ {
    candles[i] = Candle{Close : prices[i]}
    candles[i].Indicators.SMAs = make(map[int]float32)
    candles[i].Indicators.EMAs = make(map[int]float32)
  }



  intervals := []int{5, 10}

  FullIndicators(candles[:], intervals, intervals)
}

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

// this should be passed a candles list with no indicators
func FullIndicators(candles []Candle, smaIntervals []int, emaIntervals []int) {
  gains := float32(0)
  losses := float32(0)

  // loop through candles
  for c := 1; c < len(candles); c++ {
    // rsi calculation control
    if c < 14 {
      // need a function to sum gains and losses
      UpdateAvgGL(candles[c].Close, candles[c-1].Close, &gains, &losses)
    } else if c == 14 {
      candles[c].Indicators.AvgUp = gains / 14.0
      candles[c].Indicators.AvgDown = losses / 14.0
    } else {
      // need a function to calculate the new avgs for rs
      SetAvgGL(&candles[c], &candles[c - 1])
    }

    // sma calculation
    for s := 0; s < len(smaIntervals); s++ {
      // if the iteration is at a point where sma can be made
      // interval is 4, needs 4 entries
      if c + 1 >= smaIntervals[s] {
        // pass in the slice of candles with to be used in the calculations
        // interval is 4, c is 4 need c-interval+1 to c
        SetSMA(candles[(c-smaIntervals[s]+1):c])
      }
    }

    // ema calculation
    for e := 0; e < len(emaIntervals); e++ {
      // if the iteration is at a point where ema can be made
      // c = 4 is 5th candle.. interval 4 requires c = 4
      if c == emaIntervals[e] {
        // pass 0 to c
        if candles[c-1].Indicators.SMAs[emaIntervals[e]] != 0 {
          SetEMA(candles[(c-1):c], emaIntervals[e])
        } else {
          SetEMA(candles[0:c], emaIntervals[e])
        }

      } else if c >= emaIntervals[e] {
        // pass c-1 to c
        SetEMA(candles[(c-1):c], emaIntervals[e])
      }
    }
  }
}

/*
// or a candles list with the minimum sma interval back already with indicators
// ie minimum sma interval is 5, this should be passed a list of candles where the first 4 have all desired indicators

// could also be handled by taking a previous prices list to make this more sensible
func FillIndicators(candles []Candle, emaIntervals []Int, smaIntervals[]Int) {
  var avgu float32
  var avgd float32

  var change float32

  minInterval := 1000

  for s := 0; s < len(smaIntervals); i++ {
    if smaIntervals[s] < minInterval {
      minInterval = smaIntervals[s]
    }
  }

  // will only calculate indicators starting from the lowest sma interval
  for c := minInterval; c < len(candles); c++ {
    SetRSAvgs(&candles[c], &candles[c - 1])

    // at each candle loop through the emaIntervals
    for i := 0; i < len(emaIntervals); i++ {
      SetEMA(candles, emaIntervals)
    }

    // at each candle calculate the
    for s := 0; s < len(smaIntervals); i++ {
      SetSMA(candles, smaIntervals)
    }
  }

  // on the candle that can have its rsi calculated
  candles[i].indicators.avgUp = avgu / 14.0
  candles[i].indicators.avgDown = avgd / 14.0

  // be careful of the edge case 14 candles of consecutive up or down
  if avgu > 0 & avgd > 0 & len(candles) > 15 {
    // pass remaining candles to the smoothing rsi calculation
    smoothRS(candles[14:len(candles)])
  }
}
*/

func UpdateAvgGL(price float32, prevPrice float32, gains *float32, losses *float32) {
  change := price - prevPrice

  // keep a running total of positive and negative changes, separately
  if change > 0 {
    *gains += change
  } else if change < 0 {
    *losses += -change
  }
}

func SetAvgGL(curCandle *Candle, prevCandle *Candle) {
  change := curCandle.Close - prevCandle.Close

  avgu := prevCandle.Indicators.AvgUp
  avgd := prevCandle.Indicators.AvgDown

  // whats the most pythonic way to represent change as change when >0 and as 0 otherwise, etc.
  if change > 0 {
    avgu = (13.0 * avgu + change) / 14.0
    avgd = (13.0 * avgd) / 14.0
  } else if change < 0 {
    avgu = (13.0 * avgu) / 14.0
    avgd = (13.0 * avgd - change) / 14.0
  }

  curCandle.Indicators.AvgUp = avgu
  curCandle.Indicators.AvgDown = avgd
}

func SetSMA(candles []Candle) {
    candles[len(candles) - 1].Indicators.SMAs[len(candles)] = GetSMA(candles)
    fmt.Println(candles[len(candles) - 1])
}

func SetEMA(candles []Candle, interval int) {
  var ema float32
  var baseMA float32

  if len(candles) == 2 {
    //doesn't have to be close
    baseMA = candles[0].Indicators.EMAs[interval]
    if baseMA == 0.0 {
      baseMA = candles[0].Indicators.SMAs[interval]
    }
  } else {
    // interval 5, candle 5 can
    // assert(candles[0:interval-1] == interval - 1)
    baseMA = GetSMA(candles[0:interval-1])
  }
  ema = GetEMA(candles[1], baseMA, interval)
  candles[len(candles)-1].Indicators.EMAs[interval] = ema
}

// meant to be used for one off sma calculations (ie. when ema starts up)
// this function takes a set length of candles and calculates the sma of the last one
func GetSMA(candles []Candle) float32 {
  sum := float32(0)

  for i := 0; i < len(candles); i++ {
    // doesn't have to be close but should be the same as GetEMA
    sum += candles[i].Close
  }
  return sum / float32(len(candles))
}

// price doesn't have to be close
func GetEMA(candle Candle, baseMA float32, interval int) float32 {
  smoothing := 2.0 / (float32(interval) + 1.0)

  return candle.Close * smoothing + baseMA * (1.0 - smoothing)
}
