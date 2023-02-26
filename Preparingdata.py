x_train=x_train/255.0
x_text=x_test/255.0

x_train[0].shape
#output-(28, 28)

x_train=x_train.reshape(x_train.shape[0],-1)
x_test=x_test.reshape(x_test.shape[0],-1)
print(x_train.shape)

#output(60000, 784)
