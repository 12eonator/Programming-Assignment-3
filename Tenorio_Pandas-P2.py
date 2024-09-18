{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b4fa1b1c-3654-442a-89bc-ab4257e99760",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "30dedefc-3337-49fe-9039-f37ee0fca4a3",
   "metadata": {},
   "source": [
    "# Problem 2\n",
    "Using the dataframe cars in problem 1, extract the following information using subsetting, slicing a indexing operation: a) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars. \n",
    "b  Display the row that contains the ‘Model’ of ‘Mazda R 4X' c)  . How many cylinders (‘cyl’) does the car model ‘Camaro Z28have  d) d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models zMa Ra  X4\r\n",
    "Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ h\n",
    "ve.."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "f22a7462-f79c-4ddf-9f2d-7687512a2255",
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
       "      <th>mpg</th>\n",
       "      <th>disp</th>\n",
       "      <th>drat</th>\n",
       "      <th>qsec</th>\n",
       "      <th>am</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>21.0</td>\n",
       "      <td>160.0</td>\n",
       "      <td>3.90</td>\n",
       "      <td>16.46</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>21.0</td>\n",
       "      <td>160.0</td>\n",
       "      <td>3.90</td>\n",
       "      <td>17.02</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>22.8</td>\n",
       "      <td>108.0</td>\n",
       "      <td>3.85</td>\n",
       "      <td>18.61</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>21.4</td>\n",
       "      <td>258.0</td>\n",
       "      <td>3.08</td>\n",
       "      <td>19.44</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>18.7</td>\n",
       "      <td>360.0</td>\n",
       "      <td>3.15</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    mpg   disp  drat   qsec  am\n",
       "0  21.0  160.0  3.90  16.46   1\n",
       "1  21.0  160.0  3.90  17.02   1\n",
       "2  22.8  108.0  3.85  18.61   1\n",
       "3  21.4  258.0  3.08  19.44   0\n",
       "4  18.7  360.0  3.15  17.02   0"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# A) Displaying the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.\n",
    "cars.iloc[:5, [1,3,5,7,9]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "ecdd0eae-426b-430b-b3d3-c25ec22b46a5",
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
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# B) Displaying the row that contains the 'Model' of 'Mazda RX'\n",
    "cars.loc[cars['Model'] == \"Mazda RX4\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "507edc46-28b7-4795-ac88-0abf0bb23923",
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
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Camaro Z28</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Model  cyl\n",
       "23  Camaro Z28    8"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# C) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?\n",
    "cars.loc[(cars['Model'] == 'Camaro Z28'), ['Model','cyl']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "b7c9eb2d-181a-40ac-941d-7e125d66070a",
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
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "1    Mazda RX4 Wag    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# D) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.\n",
    "cars.loc[(cars['Model'].isin([\"Mazda RX4 Wag\",\"Ford Pantera L\",\"Honda Civic\"])), ['Model','cyl', 'gear'] ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0114d023-2646-412a-9907-9410f82fc7df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
