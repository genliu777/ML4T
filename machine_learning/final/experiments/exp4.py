from utils.util import plot_data
from machine_learning.final.models import lstm
from machine_learning.final.models import ffnn
from machine_learning.final.models import lin_reg
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

#future gap
stock = 'MSFT'
dates_dic = {
    'MSFT'  : ['2017-01-01', '2018-01-01']
}
future_gap_list = [1, 2, 3, 4, 5]

#LSTM
window = 2
future_gap = 1
time_steps = 1
neurons = [256, 256, 32, 1]
drop_out = 0.2                                   
batch_size = 2048
epochs = 300
validation_split = 0.1
verbose = 1
early_stopping_callback = EarlyStopping(monitor='val_loss', min_delta=0, 
                                        patience=50, verbose=verbose, mode='auto')
callbacks = [early_stopping_callback] 

lstm_future_gap_metrics = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}


for future_gap in future_gap_list:
    start_date = dates_dic[stock][0]
    end_date = dates_dic[stock][1]
    normalized_metrics, _, df = lstm.final_test_lstm(stock, start_date, 
    end_date, window, future_gap, time_steps, neurons, drop_out, batch_size, epochs, validation_split, 
    verbose, callbacks)
    lstm_future_gap_metrics[future_gap] = normalized_metrics
    plot_data(df, 'Future Gap = '+str(future_gap), "Date", "Price", show_plot=False)


#FFNN
neurons = [256, 256, 64, 1]
batch_size = 128
epochs = 200

ffnn_future_gap_metrics = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}

for future_gap in future_gap_list:
    start_date = dates_dic[stock][0]
    end_date = dates_dic[stock][1]
    normalized_metrics, _, df = ffnn.final_test_ffnn(stock, start_date, 
    end_date, window, future_gap, neurons, drop_out, batch_size, epochs, validation_split, 
    verbose, callbacks)
    ffnn_future_gap_metrics[future_gap] = normalized_metrics
    plot_data(df, 'Future Gap = '+str(future_gap), "Date", "Price", show_plot=False)

linreg_future_gap_metrics = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}

for future_gap in future_gap_list:
    start_date = dates_dic[stock][0]
    end_date = dates_dic[stock][1]
    normalized_metrics, _, df = lin_reg.final_test_linreg(stock, start_date, 
    end_date, window, future_gap)
    linreg_future_gap_metrics[future_gap] = normalized_metrics
    plot_data(df, 'Future Gap = '+str(future_gap), "Date", "Price", show_plot=False)

print(lstm_future_gap_metrics)
print(ffnn_future_gap_metrics)
print(linreg_future_gap_metrics)
plt.show()