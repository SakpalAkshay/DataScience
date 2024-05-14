# EDA Terminologies and Usage 

## Univariate Analysis
Univariate analysis focuses on **analyzing a single variable at a time**, examining its **distribution, central tendency, variability, and other descriptive statistics**. It aims to understand the characteristics and properties of that variable without considering relationships with other variables.
### CountPlot
A count plot is a type of data visualization that shows the **frequency** of **observations** in **categorical data**. It's used in univariate analysis to quickly understand the **distribution of categories within a single variable**, helping to identify common or rare categories and their relative frequencies.
### Histogram
A histogram is a graphical representation of the distribution of numerical data. It **divides the data into intervals called bins and displays the frequency of observations within each bin as bars**. In univariate analysis, histograms are used to visualize the distribution of a single variable, providing insights into its central tendency, dispersion, skewness, and presence of outliers.
### DistPlot
A distplot, short for distribution plot, is a type of data visualization that **combines a histogram with a kernel density estimation (KDE) plot**. It displays the distribution of numerical data and provides an **estimate of the probability density function of the variable**. 
### BoxPlot
A box plot, also known as a **box-and-whisker plot**, is a statistical visualization that shows the **distribution of numerical data based on quartiles**. It consists of a box that **represents the interquartile range (IQR), with a line inside denoting the median**. Whiskers extend from the box to **show the range of the data excluding outliers**. 

## Bivariate/Multivariate Analysis
Bivariate analysis examines the relationship between two variables, while multivariate analysis looks at the interactions among multiple variables to understand complex patterns and relationships in data.
### ScatterPlot (Numerical - Numerical)
A scatter plot is used in bivariate and multivariate analysis to visualize the relationship between two numerical variables. Each point on the plot represents a pair of values from the two variables, showing patterns such as correlations, clusters, or trends. Multiple variables can be displayed simultaneously in a multivariate scatter plot, offering deeper insights into complex data relationships.
### BoxPlot (Numerical - Categorical)
A box plot, also known as a box-and-whisker plot, is used in bivariate and multivariate analysis to visualize the distribution of a numerical variable across different categories of a categorical variable. It shows the median, quartiles, and outliers, providing insights into the central tendency, spread, and variability of the numerical data within each category, making it useful for comparing groups or identifying trends based on categories.
### DistPlot (Numerical - Categorical)
A distplot, or distribution plot, is typically used in univariate analysis to visualize the distribution of a single numerical variable. It's not typically used for bivariate or multivariate analysis involving a categorical variable. However, you can create separate distplots for different categories of a categorical variable to compare the distributions of the numerical variable across those categories.
### PairPlot 
A pairplot is used in multivariate analysis to visualize relationships between multiple numerical variables simultaneously. It creates scatter plots for numerical variables and histograms for univariate distributions along the diagonal, while showing bivariate relationships between variables in the off-diagonal plots. It doesn't directly handle categorical variables, but you can use it to explore relationships between numerical variables grouped by categories in your data.
