'''

Writting some of the regression metrics without using libraries.

'''

# Mean Absolute Error (MAE) 
def mae(y_true, y_pred):
    '''
    Parameters
    ----------
    y_true: list of true values
    y_pred: list of predicted values

    '''
    # Creating a variable to store the sum of the absolute errors
    total_error = 0
    # Iterating over the true and predicted values with zip and calculating the absolute error
    for yt, yp in zip(y_true, y_pred):
        total_error += abs(yt - yp)
    # Getting the mean absolute error and returning it
    mae = total_error / len(y_true)
    return mae

# Mean Absolute Percentage Error (MAPE)
def mape(y_true, y_pred, epsilon=1e-20):
    '''
    Parameters
    ----------
    y_true: list of true values
    y_pred: list of predicted values
    epsilon: float small number to avoid division by zero

    '''
    # Creating a variable to store the sum of the absolute errors by the true values or the epsilon
    total_error = 0
    # Iterating over the true and predicted values with zip and calculating the absolute error by yt or epsilon
    for yt, yp in zip(y_true, y_pred):
        total_error += abs((yt - yp) / [abs(yt) if abs(yt) > epsilon else epsilon][0])
    # Getting the mean absolute error and returning it
    mape = total_error / len(y_true)
    return mape

# Mean Squared Error (MSE)
def mse(y_true, y_pred):
    '''
    Parameters
    ----------
    y_true: list of true values
    y_pred: list of predicted values

    '''
    # Creating a variable to store the sum of the squared errors
    total_error = 0
    # Iterating over the true and predicted values with zip and calculating the squared error
    for yt, yp in zip(y_true, y_pred):
        total_error += (yt - yp) ** 2
    # Getting the mean squared error and returning it
    mse = total_error / len(y_true)
    return mse

# Root Mean Squared Error (RMSE)
def rmse(y_true, y_pred):
    '''
    Parameters
    ----------
    y_true: list of true values
    y_pred: list of predicted values

    '''
    # Creating a variable to store the sum of the squared errors
    total_error = 0
    # Iterating over the true and predicted values with zip and calculating the squared error
    for yt, yp in zip(y_true, y_pred):
        total_error += (yt - yp) ** 2
    # Getting the mean squared error and returning it
    rmse = (total_error / len(y_true))**0.5
    return rmse

# R2 Score
def r2(y_true, y_pred):
    '''
    Parameters
    ----------
    y_true: list of true values
    y_pred: list of predicted values

    '''
    # Getting the mean of the true values
    y_mean = sum(y_true) / len(y_true)
    # Creating variables to store the sum of the squared errors by the mean and the predicted values
    mean_error = 0
    predict_error = 0
    # Iterating over the true and predicted values with zip and calculating the squared errors
    for yt, yp in zip(y_true, y_pred):
        mean_error += (yt - y_mean) ** 2
        predict_error += (yt - yp) ** 2
    # Getting the r2 score and returning it
    r2 = 1 - (predict_error / mean_error)
    return r2

# Median Absolute Error (MedAE)
def medae(y_true, y_pred):
    '''
    Parameters
    ----------
    y_true: list of true values
    y_pred: list of predicted values

    '''
    # Opening a list to store the absolute errors
    abs_error = []
    # Iterating over the true and predicted values with zip, calculating the absolute error, and appending it to the list
    for yt, yp in zip(y_true, y_pred):
        abs_error.append(abs(yt - yp))
    # Sorting the list, getting the median, and returning it
    abs_error.sort()
    if len(abs_error) % 2 == 0:
        medae = (abs_error[len(abs_error) // 2] + abs_error[len(abs_error) // 2 - 1]) / 2
    else:
        medae = abs_error[len(abs_error) // 2]
    return medae