# cs105-prj-phase3-pho
cs105-prj-phase3-pho created by GitHub Classroom

For information about phases 1 and 2 use the two links below




For my dataset, I am using in game information about League of Legends games. This dataset included information such as gold, xp, level, minionsKilled, and jungleMinionsKilled. I was wondering what the best ways to calculate the level without using xp because the requirements for a level in League of Legends is always the same so the accuracy would be 100% accurate. 

For my analysis process I started by cleaning the data and then ran Linear regression and KNN on each inputs and outputs I decided to use. I write my observations and colclusions in the Jupyter file.

To my suprise however, totalMinionsKilled performed slightly worse than just using both minionsKilled and jungleMinionsKilled. It could mean there is a bigger discrepency in the amount of golf a player gets between jungle minions and regular minions when it should be about the same. The difference is small in the accuracies, but totalMinonsKilled performed slightly worse in both cases tested.
