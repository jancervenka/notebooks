ggmap(tx_map, extent = "device") + 

geom_density2d(data = airbnb, aes(x = longitude, y = latitude), size = 0.3) +
  
stat_density2d(data = airbnb, aes(x = longitude, y = latitude, fill = ..level.., alpha = ..level..), size = 0.01, bins = 16, geom = "polygon") +
  
scale_fill_gradient(low = "black", high = "red",name = "Density") + 
  
scale_alpha(range = c(0,0.3), guide = FALSE) +
  
ggtitle("Density Distribution of Airbnb Properties in Texas")
