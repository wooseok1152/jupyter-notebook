# model_14에 배정된 데이터셋을 train, validation, test로 분리
from sklearn.model_selection import train_test_split

x_train_model_14, x_test_model_14, y_train_model_14, y_test_model_14 = train_test_split(x_data_for_model_14, y_data_for_model_14, test_size=0.2, random_state=1)
x_train_model_14, x_val_model_14, y_train_model_14, y_val_model_14 = train_test_split(x_train_model_14, y_train_model_14, test_size=0.25, random_state=1)

# ANN 모델 설계
from tensorflow.keras import models
from tensorflow.keras import layers
from keras.callbacks import EarlyStopping

model_14 = models.Sequential()
model_14.add(layers.Dense(64, activation="relu", input_shape = (41, )))
model_14.add(layers.Dropout(0.6))
model_14.add(layers.Dense(64, activation="relu"))
model_14.add(layers.Dropout(0.6))
model_14.add(layers.Dense(64, activation="relu"))
model_14.add(layers.Dropout(0.6))
model_14.add(layers.Dense(64, activation="relu"))
model_14.add(layers.Dropout(0.6))
model_14.add(layers.Dense(1))

# 조기종료 콜백함수 정의
early_stopping = EarlyStopping(patience = 15) 

# compile 설정
model_14.compile(optimizer="rmsprop", loss = "mse", metrics = ["mae"])

# 해당 model학습
history_model_14 = model_14.fit(x_train_model_14, y_train_model_14, validation_data=(x_val_model_14, y_val_model_14), epochs=300, batch_size= 32, callbacks=[early_stopping])

# 해당 model저장
model_14.save("model_14.h5")

# model_14_result
%matplotlib inline

loss = history_model_14.history["loss"]
mae = history_model_14.history["mae"]

val_loss = history_model_14.history["val_loss"]
val_mae = history_model_14.history["val_mae"]

epoch = list(range(1, len(loss) + 1))

plt.title("Training loss")
plt.plot(epoch, loss, "bo", label = "Training loss")
plt.show()

plt.figure()

plt.title("Validation loss")
plt.plot(epoch, val_loss, "b", label = "Validation loss")

plt.figure()

plt.title("Training mae")
plt.plot(epoch, mae,"bo", label = "Training mae")

plt.figure()

plt.title("Validation mae")
plt.plot(epoch, val_mae, "b", label = "Validation mae")

plt.show()