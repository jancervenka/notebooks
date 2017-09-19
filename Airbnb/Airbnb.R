data <- Airbnb_Texas_Rentals

cities <- names(tail(sort(table(data[, 'city'])), 5))

subdata <- data[data$city %in% cities,][, c("city", "longitude", "latitude")] # comma means all rows

mean_coords <- aggregate(latitude ~ city, subdata, mean)
mean_coords[, 'longitude'] <- aggregate(longitude ~ city, subdata, mean)[, 'longitude']
