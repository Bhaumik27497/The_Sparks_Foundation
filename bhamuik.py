{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **TASK 1 - Prediction using Supervised ML**\n",
    "\n",
    "To Predict the percentage of marks of the students based on the number of hours they studied\n",
    "\n",
    "## Author - Bhaumik shah\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing the required libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_absolute_error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1.5</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>9.2</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>5.5</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.3</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2.7</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Hours  Scores\n",
       "0    2.5      21\n",
       "1    5.1      47\n",
       "2    3.2      27\n",
       "3    8.5      75\n",
       "4    3.5      30\n",
       "5    1.5      20\n",
       "6    9.2      88\n",
       "7    5.5      60\n",
       "8    8.3      81\n",
       "9    2.7      25"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading the Data \n",
    "data = pd.read_csv ('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')\n",
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check if there any null value in the Dataset\n",
    "data.isnull == True"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**There is no null value in the Dataset so, we can now visualize our Data.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set_style('darkgrid')\n",
    "sns.scatterplot(y= data['Scores'], x= data['Hours'])\n",
    "plt.title('Marks Vs Study Hours',size=20)\n",
    "plt.ylabel('Marks Percentage', size=12)\n",
    "plt.xlabel('Hours Studied', size=12)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**From the above scatter plot there looks to be correlation between the 'Marks Percentage' and 'Hours Studied', Lets plot a regression line to confirm the correlation.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYMAAAEaCAYAAADzDTuZAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeWBU9dX4//edPTPJZCEbSdgCBGQnrC7gimhFEEVlES221bq01cdaqFX0V32KrUjV2sqjta1fZBFkEdtCURRRUAqEXQRFtmxs2ZNZ7szc3x+TDAlMMpOQTBI4r39i7ty5c5LInLmf5RxF0zQNIYQQlzRdawcghBCi9UkyEEIIIclACCGEJAMhhBBIMhBCCIEkAyGEEIChtQMQ7deKFSv49a9/HfQxk8lEXFwcAwYM4Cc/+QmDBg2KcHRtR25uLtdffz3XX389f/nLX1olhunTp/Pf//73vONGo5G4uDgGDRrEj3/84zp/p1mzZrFy5UpWrVrFZZdd1qTX/ec//8nAgQPp1KlTk2MXkSHJQFyw4cOHM3z48DrHysrK2L17Nx9//DEbNmzgnXfeYejQoa0UYeuy2+08+uijZGZmtnYo3Hvvvdjt9sD3qqpy5MgRPv74Yz799FPeeOMNRo8e3Syv9dJLL/HXv/6VVatWNcv1RMuSZCAu2PDhw/nZz34W9LFXX32Vv/zlL8ydO5clS5ZEOLK2wW631/v7ibT77ruPjIyM845/+OGH/PKXv+SFF15g3bp1zfJaZ86caZbriMiQOQPRoh566CGMRiM7duzA4XC0djiiHuPGjSM1NZWjR49y+PDh1g5HtAJJBqJFmUwmoqOjAXC73XUe+/LLL5kxYwZDhgxh0KBB3H333axduzboddauXcukSZMYPHgwo0aNYu7cuWzevJlevXqxYsWKwHm9evVi1qxZzJ8/n6FDhzJ06FD+8Y9/BB5fs2YNkydPZvDgwWRnZ3Pffffx1Vdfnfd6e/bs4cEHH+Sqq66if//+jB07lrlz51JRUdHo83Jzc+nVqxcPP/xwneeePHmS2bNnc/XVV9OvXz+uvvpqZs+ezcmTJ+uc96c//YlevXpx6NAh5s2bxzXXXEO/fv245ZZbWLx4cQO//fApikJycjIAJSUlDZ67adMmZsyYQXZ2NgMGDGDixIksXLgQn88XOOe6665j5cqVANx2221cd911zRKnaDkyTCRa1N69eykuLiYtLY3Y2NjA8WXLlvHMM8+QkJDAD37wA6xWK+vXr+cXv/gFjz/+OD/96U8D577zzjv87ne/IykpiQkTJqCqKu+++269iePzzz/no48+YuLEiZw+fZqBAwcCZ4es0tPTmThxIoqisHbtWmbMmMGLL77IhAkTADh8+DAzZsxAp9Nx0003Ybfb2bFjB2+99RZ79uzhnXfeadR5wRw7dowpU6Zw+vRprrjiCm6++WYOHDjAe++9xyeffMLixYvPm3R98sknyc/P58Ybb8RgMLB69Wqee+45rFZrIPam8vl85ObmApCSklLveQsWLOCFF14gJiaGMWPGYLVa+fzzz/ntb3/Ltm3bmDdvHoqicO+997Jy5Uq++eYb7r777jYxXyJC0IRoouXLl2tZWVnaa6+9Vue4z+fTSktLtQ0bNmg33HCDlpWVpS1btizweEFBgdavXz/t5ptv1oqKigLHHQ6Hdvfdd2u9e/fWDhw4EDh3wIAB2g033KCdOnUqcO6+ffu0vn37allZWdry5csDx7OysrSsrCxt/fr1dWLatWuX1qtXL+2ee+7RqqqqAseLioq0MWPGaAMHDtTOnDmjaZqmvfjii1pWVpb25Zdf1rnGAw88oGVlZWkHDx5s1HnHjx/XsrKytIceeihwzr333qtlZWVpS5curfPchQsXallZWdq9994bOPbaa69pWVlZ2rXXXhuIUdM0bfv27VpWVpY2depULZR77rlHy8rK0o4fPx708b///e9aVlaWNnHixMCxmTNnallZWdrXX3+taZqmHTt2TOvTp492zTXXaMeOHQucV1lZGfh5Vq5cWe/zRdsmdwbigr3++uu8/vrrQR+LiYlh1qxZTJo0KXBs9erVuN1ufv7znxMfHx84brFY+PnPf86MGTNYuXIlM2fOZM2aNTidTh588EESExMD5/bp04eJEyeydOnS817TYrFw9dVX1zn2/vvvo2kav/rVr4iKigocj4+P5yc/+QlPP/00a9asYdq0aYHhjpycHEaOHBk4d86cOQAkJCQAhH3euQoLC/nqq68YOnQod955Z53Hpk6dyooVK/jqq6/Izc2tM9l7xx131LlmdnY2drudI0eOBH2dYN555506q4kcDgd79uzhv//9L1arleeee67e565evRqP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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Hours    Scores\n",
      "Hours   1.000000  0.976191\n",
      "Scores  0.976191  1.000000\n"
     ]
    }
   ],
   "source": [
    "sns.regplot(x= data['Hours'], y= data['Scores'])\n",
    "plt.title('Regression Plot',size=20)\n",
    "plt.ylabel('Marks Percentage', size=12)\n",
    "plt.xlabel('Hours Studied', size=12)\n",
    "plt.show()\n",
    "print(data.corr())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**It is confirmed that the variables are positively correlated.**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Training the Model\n",
    "### 1) Splitting the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Defining X and y from the Data\n",
    "X = data.iloc[:, :-1].values  \n",
    "y = data.iloc[:, 1].values\n",
    "\n",
    "# Spliting the Data in two\n",
    "train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2) Fitting the Data into the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------Model Trained---------\n"
     ]
    }
   ],
   "source": [
    "regression = LinearRegression()\n",
    "regression.fit(train_X, train_y)\n",
    "print(\"---------Model Trained---------\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Predicting the Percentage of Marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Predicted Marks</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.5</td>\n",
       "      <td>16.844722</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.2</td>\n",
       "      <td>33.745575</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7.4</td>\n",
       "      <td>75.500624</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2.5</td>\n",
       "      <td>26.786400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.9</td>\n",
       "      <td>60.588106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.8</td>\n",
       "      <td>39.710582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1.9</td>\n",
       "      <td>20.821393</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Hours  Predicted Marks\n",
       "0    1.5        16.844722\n",
       "1    3.2        33.745575\n",
       "2    7.4        75.500624\n",
       "3    2.5        26.786400\n",
       "4    5.9        60.588106\n",
       "5    3.8        39.710582\n",
       "6    1.9        20.821393"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred_y = regression.predict(val_X)\n",
    "prediction = pd.DataFrame({'Hours': [i[0] for i in val_X], 'Predicted Marks': [k for k in pred_y]})\n",
    "prediction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Comparing the Predicted Marks with the Actual Marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual Marks</th>\n",
       "      <th>Predicted Marks</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>16.844722</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27</td>\n",
       "      <td>33.745575</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69</td>\n",
       "      <td>75.500624</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30</td>\n",
       "      <td>26.786400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>60.588106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>35</td>\n",
       "      <td>39.710582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>24</td>\n",
       "      <td>20.821393</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Actual Marks  Predicted Marks\n",
       "0            20        16.844722\n",
       "1            27        33.745575\n",
       "2            69        75.500624\n",
       "3            30        26.786400\n",
       "4            62        60.588106\n",
       "5            35        39.710582\n",
       "6            24        20.821393"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "compare_scores = pd.DataFrame({'Actual Marks': val_y, 'Predicted Marks': pred_y})\n",
    "compare_scores"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visually Comparing the Predicted Marks with the Actual Marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(x=val_X, y=val_y, color='blue')\n",
    "plt.plot(val_X, pred_y, color='Black')\n",
    "plt.title('Actual vs Predicted', size=20)\n",
    "plt.ylabel('Marks Percentage', size=12)\n",
    "plt.xlabel('Hours Studied', size=12)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evaluating the Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error:  4.130879918502486\n"
     ]
    }
   ],
   "source": [
    "# Calculating the accuracy of the model\n",
    "print('Mean absolute error: ',mean_absolute_error(val_y,pred_y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Small value of Mean absolute error states that the chances of error or wrong forecasting through the model are very less.**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What will be the predicted score of a student if he/she studies for 9.25 hrs/ day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Score = 93.893\n"
     ]
    }
   ],
   "source": [
    "hours = [9.25]\n",
    "answer = regression.predict([hours])\n",
    "print(\"Score = {}\".format(round(answer[0],3)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**According to the regression model if a student studies for 9.25 hours a day he/she is likely to score 93.89 marks.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
