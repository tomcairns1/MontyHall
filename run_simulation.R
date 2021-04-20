library(reticulate)
library(ggplot2)
library(scales)
library(mgsub)

# Choose the number of runs of the simulation
runs <- 10000

# Create a list of the results of the simulations
new_list <- lapply(seq_len(runs), 
                  function(x) py_run_file('monty_hall_game.py')$win)

# Clean the vector and change categorical values
new_list <- unlist(new_list)
new_list <- mgsub(pattern=c(T, F), replacement=c('Win', 'Lose'), new_list)

# Visualize the data
ggplot(data.frame(new_list), aes(x=new_list)) + 
    geom_bar(aes(y=(..count..)/sum(..count..)), fill='steelblue') + 
    scale_y_continuous(labels=scales::percent) +
    ylab('Percentage of simulations') + xlab('Wins')
