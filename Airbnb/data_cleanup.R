clean_rate <- function(x) 
{
  return(as.numeric(substr(x, 2, 1000)))
}

f = "C:\Users\Jan\Documents\Programming\Airbnb\Airbnb_Texas_Rentals.csv"
airbnb <- read.csv(f)

airbnb$average_rate_per_night <- lapply(airbnb$average_rate_per_night, clean_rate)

subsample <- rapply(airbnb$average_rate_per_night, c)
subsample <- subsample[subsample < 1000]

hist(subsample, col = "thistle")

